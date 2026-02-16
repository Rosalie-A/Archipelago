# E0160_NPC_QUEST_GRANT_ITEM
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["npc_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["npc_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
    Jmp(["npc_choose_article"]),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="npc_key_item_sound"),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_160_run_dialog_16"], identifier="npc_choose_article"),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_160_run_dialog_16"], identifier="EVENT_160_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_160_run_dialog_16"], identifier="EVENT_160_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_160_run_dialog_16"], identifier="EVENT_160_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_160_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_160_run_dialog_16"]),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI0065_GOT_AN_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False, identifier="EVENT_160_run_dialog_16"),
	AddToInventory(ITEM_ID),
	Return()
])
