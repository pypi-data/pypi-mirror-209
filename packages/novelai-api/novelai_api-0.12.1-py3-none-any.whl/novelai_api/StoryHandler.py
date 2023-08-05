import re
from copy import deepcopy
from json import dumps, loads
from time import time
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union, TypeVar

from novelai_api import NovelAIAPI
from novelai_api.BanList import BanList
from novelai_api.BiasGroup import BiasGroup
from novelai_api.GlobalSettings import GlobalSettings
from novelai_api.Idstore import Idstore
from novelai_api.Keystore import Keystore
from novelai_api.Preset import Model, Preset
from novelai_api.Tokenizer import Tokenizer
from novelai_api.utils import b64_to_tokens, decrypt_user_data, encrypt_user_data

_SENTINEL = object()
T = TypeVar("T")

DictUtil = Dict[str, Union[str, int, bool]]
DictUtilT = Dict[str, Union[str, int, bool, T]]


def _get_time() -> int:
    """
    Get the current time, as formatted for createdAt and lastUpdatedAt

    :return: Current time with millisecond precision
    """

    return int(time() * 1000)


def _get_short_time() -> int:
    """
    Because some lastUpdatedAt only are precise to the second

    :return: Current time with second precision
    """

    return int(time())


def _set_nested_item(item: Dict[str, Any], val: Any, path: str):
    path = path.split(".")

    for key in path[:-1]:
        item = item[key]

    item[path[-1]] = val


class NovelAIStory:
    TEXT_GENERATION_SETTINGS_VERSION = 2
    DEFAULT_MODEL = Model.Euterpe
    DEFAULT_CONTEXT_CONFIG = {
        "prefix":               "",
        "suffix":               "\n",
        "tokenBudget":          2048,
        "reservedTokens":       512,
        "budgetPriority":       0,
        "trimDirection":        "trimTop",
        "insertionType":        "newline",
        "maximumTrimType":      "sentence",
        "insertionPosition":    -1,
        "allowInsertionInside": True
    }
    DEFAULT_CONTEXT_ENTRY = {
        "text": "",
        "contextConfig": DEFAULT_CONTEXT_CONFIG
    }

    api: NovelAIAPI
    keystore: Keystore

    key: bytes
    story: Dict[str, Any]
    storycontent: Dict[str, Any]
    tree: List[int]

    global_settings: GlobalSettings
    banlists: List[BanList]
    biases: List[BiasGroup]
    model: Model
    preset: Preset
    prefix: str
    context_size: int


    memory: Dict[str, Union[str, Dict[str, Union[str, int]]]]
    an: Dict[str, Union[str, Dict[str, Union[str, int]]]]
    lorebook: DictUtilT[Union[DictUtil, List[DictUtil]]]
    ec: List[DictUtil]

    def _handle_banlist(self, data: Dict[str, Any]):
        if "bannedSequenceGroups" not in data:
            data["bannedSequenceGroups"] = []

        ban_seq = data["bannedSequenceGroups"]
        self.banlists = [BanList(*seq["sequences"], enabled=seq["enabled"]) for seq in ban_seq]

    def _handle_biasgroups(self, data: Dict[str, Any]):
        if "phraseBiasGroup" not in data:
            data["phraseBiasGroups"] = []

        self.biases = []
        for bias in data["phraseBiasGroups"]:
            self.biases.append(BiasGroup.from_data(bias))

    def _handle_preset(self, data: Dict[str, Any]):
        settings = data["settings"]

        if "textGenerationSettingsVersion" not in settings:
            settings["textGenerationSettingsVersion"] = self.TEXT_GENERATION_SETTINGS_VERSION

        if "prefix" not in settings:
            settings["prefix"] = "vanilla"
        self.prefix = settings["prefix"]

        if "model" not in settings:
            settings["model"] = self.DEFAULT_MODEL.value
        self.model = Model(settings["model"])

        if "preset" not in settings:
            settings["preset"] = ""

        parameters = settings["parameters"]

        if "bad_words_ids" in parameters:
            self.banlists.append(BanList(*parameters["bad_words_ids"]))
            del parameters["bad_words_ids"]

        if "logit_bias_groups" in parameters:
            for bias in parameters["logit_bias_groups"]:
                self.biases.append(BiasGroup.from_data(bias))
            del parameters["logit_bias_groups"]

        self.preset = Preset.from_preset_data(settings)
        self.preset.name = settings["preset"]
        self.preset.model = self.model

    def __init__(
        self,
        api: NovelAIAPI,
        keystore: Keystore,
        meta: str,
        global_settings: GlobalSettings,
        story: Dict[str, Any],
        storycontent: Dict[str, Any],
    ):
        self.api = api
        self.key = keystore[meta]
        self.story = story
        self.storycontent = storycontent
        self.tree = []

        data = storycontent["data"]

        self.global_settings = global_settings.copy()

        print(dumps(data, indent=4))
        self._handle_banlist(data)
        self._handle_biasgroups(data)
        self._handle_preset(data)

        # FIXME: variable context size ? From global settings ?
        self.context_size = 2048

        # TODO: trimResponses
        # TODO: banBrackets
        # TODO: dynamicPenaltyRange

        self.memory, self.an = storycontent.get("context", (self.DEFAULT_CONTEXT_ENTRY, self.DEFAULT_CONTEXT_ENTRY))
        self.ec = storycontent.get("ephemeralContext", [])
        self.story_config = storycontent.get("storyContextConfig", self.DEFAULT_CONTEXT_CONFIG)
        self.lorebook = storycontent.get("lorebook", {})

    def __str__(self) -> str:
        story_fragments = self.storycontent["data"]["story"]["fragments"]

        story_content = "".join(fragment["data"] for fragment in story_fragments)

        # FIXME: handle edit

        return story_content

    @staticmethod
    def resolve_context_entries(
        model: Model,
        entries: List[DictUtilT[DictUtil]],
        context_size: int
    ) -> Tuple[List[int], List[BiasGroup]]:
        """
        Resolve the context entries and trim them if needed.

        :param model: The model for tokenization
        :param entries: The context entries (memory, an, lorebook)
        :param context_size: The context size

        :return: A tuple containing the context tokens and the triggered biases
        """

        """ Memory and AN :
        {
            "text":          "",
            "contextConfig": {
                "prefix":            "",
                "suffix":            "\n",
                "tokenBudget":       2048,
                "reservedTokens":    0,
                "budgetPriority":    800,
                "trimDirection":     "trimBottom",
                "insertionType":     "newline",
                "maximumTrimType":   "sentence",
                "insertionPosition": 0
            }
        },
        """

        """ Lorebook :
        {
            "text":                "",
            "contextConfig":       {
                "prefix":            "",
                "suffix":            "\n",
                "tokenBudget":       2048,
                "reservedTokens":    0,
                "budgetPriority":    800,
                "trimDirection":     "trimBottom",
                "insertionType":     "newline",
                "maximumTrimType":   "sentence",
                "insertionPosition": -1
            },
            "keys":                [],
            "searchRange":         1000,
            "enabled":             True,
            "forceActivation":     False,
            "keyRelative":         False,
            "nonStoryActivatable": False,
            "category":            "",
            "loreBiasGroups":      [
                {
                    "phrases":              [],
                    "ensureSequenceFinish": False,
                    "generateOnce":         True,
                    "bias":                 0,
                    "enabled":              True,
                    "whenInactive":         False
                }
            ]
        },
        """

        """ Story :
        {
            "text": "",
            "contextConfig": {
                "prefix": "",
                "suffix": "",
                "tokenBudget": 2048,
                "reservedTokens": 512,
                "budgetPriority": 0,
                "trimDirection": "trimTop",
                "insertionType": "newline",
                "maximumTrimType": "sentence",
                "insertionPosition": -1,
                "allowInsertionInside": true
            }
        }
        """

        # get biases from lorebook entries
        biases = [
            BiasGroup.from_data(e) for entry in entries for e in entry["loreBiasGroups"] if "loreBiasGroups" in entry
        ]

        newline = Tokenizer.encode(model, "\n")[0]
        sentence = Tokenizer.encode(model, ".")[0]
        space = Tokenizer.encode(model, " ")[0]

        tokenized_entries = [
            Tokenizer.encode(model, f"{entry['contextConfig'].get('prefix', '')}"
                                    f"{entry['text']}"
                                    f"{entry['contextConfig'].get('suffix', '')}"
            ) for entry in entries
        ]

        # number of tokens left. Negative if we need to trim
        projected = context_size - sum(len(entry) for entry in tokenized_entries)

        # no need to trim if we have enough context
        if 0 <= projected:
            return [token for entry in tokenized_entries for token in entry], biases

        for entry in entries:
            context_config = entry["contextConfig"]

            # trimDirection => "trimBottom", "trimTop", or null (no trim)
            trim_direction: Union[str, None] = context_config.get("trimDirection", None)
            # insertionType => "newline", "sentence", "space", or null (newline)
            insertion_type = context_config.get("insertionType", "newline")
            # maximumTrimType => "newline", "sentence", "space, or null (newline)
            maximum_trim_type = context_config.get("maximumTrimType", "newline")
            # insertionPosition => number of newlines from the top of the context, negative from the bottom
            insertion_position = context_config.get("insertionPosition", 0)

            # we try to trim newline, then sentence, then space, up to the maximum trim type
            trim_types = [newline, sentence, space]
            for trim_type in trim_types[:trim_types.index(maximum_trim_type) + 1]:
                pass

                # TODO: trim
                # if the trimmed entry is under 30% of the target size, the trim failed, we need to trim more


        return [], biases

    def build_context_get_lorebook_entries(self, story: str) -> List[DictUtilT[DictUtil]]:
        """
        Get the active lorebook entries

        :return: The lorebook entries
        """

        lorebook_entries: List[DictUtilT[DictUtil]] = self.lorebook["entries"]
        # filter out disabled entries
        lorebook_entries = [entry for entry in lorebook_entries if entry["enabled"]]

        lorebook_entries_forced = [entry for entry in lorebook_entries if entry["forceActivation"]]
        lorebook_entries = [entry for entry in lorebook_entries if not entry["forceActivation"]]

        if self.lorebook.get("settings", {}).get("orderByKeyLocations", True):
            # separate entries that are forced (TODO: check if it's before or after the search range)
            # get position of entries from the bottom of context (keys are regex)
            entry_match_positions = [
                tuple(re.match(key, story[-entry["searchRange"]:], re.MULTILINE) for key in entry["keys"])
                for entry in lorebook_entries
            ]
            entry_positions = [
                max(match.end() for match in matches if match is not None) if any(matches) else None
                for matches in entry_match_positions
            ]

            # filter out entries that are not in the story (no match) and sort them by position
            lorebook_entry_positions = {
                pos: entry for entry, pos in zip(lorebook_entries, entry_positions) if pos is not None
            }

            lorebook_entries = [
                *lorebook_entries_forced,
                *(v for k, v in  sorted(lorebook_entry_positions.items(), key=lambda e: e[0]))
            ]
        else:
            # filter out entries that are not in the story
            lorebook_entries = [
                *lorebook_entries_forced,
                *(entry for entry in lorebook_entries
                if any(re.search(key, story[-entry["searchRange"]:], re.MULTILINE) for key in entry["keys"]))
            ]

        return lorebook_entries

    @staticmethod
    def build_context_sort_entries(*entries: DictUtilT[DictUtil]) -> List[DictUtilT[DictUtil]]:
        """
        Sort the lorebook entries

        :param entries: The lorebook entries

        :return: The sorted lorebook entries
        """

        return list(sorted(entries, key=lambda e: e["contextConfig"].get("insertionPosition", 0)))

    def build_context(
        self,
        model: Model,
        module: bool,
        complete_until_sentence: bool
    ) -> Tuple[List[int], List[BiasGroup]]:
        """
        Build the context for the story

        :param model: The model used for tokenization
        :param module: True if a module is used for generation, reserves 20 tokens
        :param complete_until_sentence: True if GlobalSettings.complete_until_sentence is enabled, reserves 20 tokens

        :return: the tokenized context, and the bias list from lorebook entries
        """

        # TODO: optimize for large stories ? Would return tokenized form of story entries up to max context size
        # edit is a pain for input in token form, so we use it's string representation instead (for the moment)
        story_content = str(self)

        # TODO: add option to remove superfluous spaces at the end

        context_size = self.context_size - 20 * module - 20 * complete_until_sentence

        story = {"text": story_content, "contextConfig": self.story_config}
        memory: DictUtilT[DictUtil] = self.memory
        an: DictUtilT[DictUtil] = self.an
        ec: List[DictUtilT[DictUtil]] = self.ec
        lorebook_entries = self.build_context_get_lorebook_entries(story_content)
        # TODO: handle cascading Lorebook entries

        entries = self.build_context_sort_entries(story, memory, an, *lorebook_entries, *ec)
        tokens, biases = self.resolve_context_entries(model, entries, context_size)

        # Internal assert, should never happen
        assert len(tokens) <= self.context_size

        return tokens, biases

    def create_datablock(self, fragment: Dict[str, str], end_offset: int):
        story = self.storycontent["data"]["story"]
        blocks = story["datablocks"]
        fragments = story["fragments"]

        cur_index = story["currentBlock"]
        cur_block = blocks[cur_index]

        story["step"] += 1

        frag_index = len(fragments)
        fragments.append(fragment)

        start = cur_block["endIndex"] + len(cur_block["dataFragment"]["data"])

        block = {
            "nextBlock": [],
            "prevBlock": cur_index,
            "origin": fragment["origin"],
            "startIndex": start,
            "endIndex": start + end_offset,
            "dataFragment": fragment,
            "fragmentIndex": frag_index,
            "removedFragments": [],
            "chain": False,
        }
        new_index = len(blocks)
        blocks.append(block)

        cur_block["nextBlock"].append(new_index)

        story["currentBlock"] = new_index
        self.tree.append(new_index)

    async def generate(self):
        prompt, biases = self.build_context()
        # FIXME: find why the output is garbage
        rsp = await self.api.high_level.generate(
            prompt,
            self.model,
            self.preset,
            self.global_settings,
            self.banlists,
            [*self.biases, *biases],
            self.prefix,
        )

        output = Tokenizer.decode(self.model, b64_to_tokens(rsp["output"]))
        fragment = {"data": output, "origin": "ai"}

        self.create_datablock(fragment, 0)

        return self

    async def edit(self, start: int, end: int, replace: str):
        # FIXME: redo edit implementation

        fragment = {"data": replace, "origin": "edit"}

        self.create_datablock(fragment, end - start)

    async def undo(self):
        story = self.storycontent["data"]["story"]

        cur_index = story["currentBlock"]
        blocks = story["datablocks"]

        cur_block = blocks[cur_index]
        story["currentBlock"] = cur_block["prevBlock"]

    async def redo(self):
        story = self.storycontent["data"]["story"]

        cur_index = story["currentBlock"]
        blocks = story["datablocks"]

        cur_block = blocks[cur_index]
        story["currentBlock"] = cur_block["nextBlock"][-1]

    async def save(self, upload: bool = False) -> bool:
        encrypted_story = encrypt_user_data(deepcopy(self.story), self.keystore)
        encrypted_storycontent = encrypt_user_data(deepcopy(self.storycontent), self.keystore)

        success = True

        # TODO: keep local copy if upload ?
        if upload:
            success = success and await self.api.high_level.upload_user_content(encrypted_storycontent)
            success = success and await self.api.high_level.upload_user_content(encrypted_story)

        return success

    async def choose(self, index: int):
        story = self.storycontent["data"]["story"]

        cur_index = story["currentBlock"]
        blocks = story["datablocks"]

        cur_block = blocks[cur_index]
        next_blocks = cur_block["nextBlock"]
        if not (0 <= index < len(next_blocks)):
            raise ValueError(f"Expected index between 0 and {len(next_blocks)}, but got {index}")

        story["currentBlock"] = next_blocks[index]

    async def flatten(self):
        story = self.storycontent["data"]["story"]

        blocks = story["datablocks"]
        new_datablocks = [blocks[i] for i in self.tree]
        self.tree = [i for i in range(len(new_datablocks))]
        story["datablocks"] = new_datablocks

    async def delete(self):
        pass

    async def get_current_tree(self) -> List[Dict[str, Any]]:
        story = self.storycontent["data"]["story"]

        blocks = story["datablocks"]
        return [blocks[i] for i in self.tree]


class NovelAIStoryStorage:
    """
    General storage for the NovelAIStory objects. Instances of this class should be loaded or created from here.
    """

    _story_instances: Dict[str, NovelAIStory]

    api: NovelAIAPI
    keystore: Keystore
    idstore: Idstore

    global_settings: GlobalSettings

    def __init__(self, api: NovelAIAPI, keystore: Keystore, global_settings: Optional[GlobalSettings] = None):
        self.api = api
        self.keystore = keystore
        self.idstore = Idstore()

        self.global_settings = global_settings or GlobalSettings()

        self._story_instances = {}

    def __iter__(self) -> Iterator[NovelAIStory]:
        return self._story_instances.values().__iter__()

    def __getitem__(self, story_id: str) -> NovelAIStory:
        return self._story_instances[story_id]

    def __len__(self) -> int:
        return len(self._story_instances)

    def load(self, story: Dict[str, Any], storycontent: Dict[str, Any]) -> NovelAIStory:
        """
        Load a story proxy from a story and storycontent object
        """
        story_meta = story["meta"]
        story_id = story["data"]["remoteStoryId"]

        assert (
            story_meta == storycontent["meta"]
        ), f"Expected meta {story_meta} for storycontent, but got meta {storycontent['meta']}"
        assert story_id == storycontent["id"], f"Missmached id: expected {story_id}, but got {storycontent['id']}"

        story = NovelAIStory(self.api, self.keystore, story_meta, self.global_settings, story, storycontent)

        # FIXME: ignore or overwrite if id exists ?
        self._story_instances[story_id] = story

        return story

    def loads(self, stories: Dict[str, Dict[str, Any]], storycontents: Dict[str, Dict[str, Any]]) -> List[NovelAIStory]:
        mapping = {}
        for story in stories:
            if story.get("decrypted"):
                mapping[story["data"]["remoteStoryId"]] = story

        loaded = []
        for storycontent in storycontents:
            if storycontent.get("decrypted"):
                story_id = storycontent["id"]

                if story_id not in mapping:
                    self.api.logger.warning(f"Storycontent {story_id} has no associated story")
                else:
                    proxy = self.load(mapping[story_id], storycontent)
                    del mapping[story_id]

                    loaded.append(proxy)

        for story_id in mapping.keys():
            self.api.logger.warning(f"Story {story_id} has no associated storycontent")

        return loaded

    async def load_from_remote(self) -> List[NovelAIStory]:
        stories = await self.api.high_level.download_user_stories()
        storycontents = await self.api.high_level.download_user_story_contents()

        decrypt_user_data(stories, self.keystore)
        decrypt_user_data(storycontents, self.keystore)

        return self.loads(stories, storycontents)

    def create(self) -> NovelAIStory:
        meta = self.keystore.create()
        current_time = _get_time()
        current_time_short = _get_short_time()

        with open("templates/template_empty_story.txt") as f:
            story = loads(f.read())

        # local overwrites
        id_story = self.idstore.create()
        for path, val in (
            ("id", id_story),
            ("meta", meta),
            ("data.id", meta),
            ("data.remoteStoryId", id_story),
            ("data.createdAt", current_time),
            ("data.lastUpdatedAt", current_time),
            ("lastUpdatedAt", current_time_short),
        ):
            _set_nested_item(story, val, path)

        with open("templates/template_empty_storycontent.txt") as f:
            storycontent = loads(f.read())

        # local overwrites
        id_storycontent = self.idstore.create()
        id_lore_default = ""  # FIXME: get id

        for path, val in (
            ("id", id_storycontent),
            ("meta", meta),
            ("lastUpdatedAt", current_time_short),
            ("data.contextDefaults.loreDefaults.id", id_lore_default),
            ("data.contextDefaults.loreDefaults.lastUpdatedAt", current_time),
        ):
            _set_nested_item(storycontent, val, path)

        proxy = self.load(story, storycontent)

        return proxy

    def select(self, story_id: str) -> Optional[NovelAIStory]:
        """
        Select a story proxy from the previously created/loaded ones

        :param story_id: Id of the selected story

        :return: Story or None if the story does't exist in the handler
        """

        if story_id not in self._story_instances:
            return None

        return self._story_instances[story_id]

    def unload(self, story_id: str):
        """
        Unload a previously created/loaded story, free'ing the NovelAI_StoryProxy object
        """

        if story_id in self._story_instances:
            del self._story_instances[story_id]
