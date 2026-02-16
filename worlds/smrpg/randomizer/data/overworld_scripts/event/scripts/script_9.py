# E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP
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
	SetVarToRandom(PRIMARY_TEMP_7000, 46),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_9_set_var_to_const_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_9_set_var_to_const_50"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_9_set_var_to_const_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_9_set_var_to_const_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_9_set_var_to_const_56"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_9_set_var_to_const_58"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_9_set_var_to_const_60"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_9_set_var_to_const_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_9_set_var_to_const_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_9_set_var_to_const_66"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_9_set_var_to_const_68"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["EVENT_9_set_var_to_const_70"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_9_set_var_to_const_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_9_set_var_to_const_74"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["EVENT_9_set_var_to_const_76"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_9_set_var_to_const_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_9_set_var_to_const_80"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_9_set_var_to_const_82"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 18, ["EVENT_9_set_var_to_const_84"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 19, ["EVENT_9_set_var_to_const_86"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_9_set_var_to_const_88"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_9_set_var_to_const_90"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_9_set_var_to_const_92"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_9_set_var_to_const_94"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_9_set_var_to_const_96"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_9_set_var_to_const_98"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 26, ["EVENT_9_set_var_to_const_100"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_9_set_var_to_const_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_9_set_var_to_const_104"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 29, ["EVENT_9_set_var_to_const_106"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 30, ["EVENT_9_set_var_to_const_108"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 31, ["EVENT_9_set_var_to_const_110"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 32, ["EVENT_9_set_var_to_const_112"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_9_set_var_to_const_114"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 34, ["EVENT_9_set_var_to_const_116"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 35, ["EVENT_9_set_var_to_const_118"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 36, ["EVENT_9_set_var_to_const_120"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 37, ["EVENT_9_set_var_to_const_122"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 38, ["EVENT_9_set_var_to_const_124"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 39, ["EVENT_9_set_var_to_const_126"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 40, ["EVENT_9_set_var_to_const_128"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_9_set_var_to_const_130"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 42, ["EVENT_9_set_var_to_const_132"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 43, ["EVENT_9_set_var_to_const_134"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 44, ["EVENT_9_set_var_to_const_136"]),
	SetVarToConst(ITEM_ID, PantsItem),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireCapeItem, identifier="EVENT_9_set_var_to_const_48"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, NauticaDressItem, identifier="EVENT_9_set_var_to_const_50"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SailorPantsItem, identifier="EVENT_9_set_var_to_const_52"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SailorShirtItem, identifier="EVENT_9_set_var_to_const_54"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SpikedLinkItem, identifier="EVENT_9_set_var_to_const_56"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SpikedLinkItem, identifier="EVENT_9_set_var_to_const_58"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, JumpShoesItem, identifier="EVENT_9_set_var_to_const_60"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CymbalsItem, identifier="EVENT_9_set_var_to_const_62"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, PunchGloveItem, identifier="EVENT_9_set_var_to_const_64"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FuzzyCapeItem, identifier="EVENT_9_set_var_to_const_66"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HappyPantsItem, identifier="EVENT_9_set_var_to_const_68"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HappyShirtItem, identifier="EVENT_9_set_var_to_const_70"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HealShellItem, identifier="EVENT_9_set_var_to_const_72"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, PolkaDressItem, identifier="EVENT_9_set_var_to_const_74"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HandGunItem, identifier="EVENT_9_set_var_to_const_76"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HurlyGlovesItem, identifier="EVENT_9_set_var_to_const_78"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, BtubRingItem, identifier="EVENT_9_set_var_to_const_80"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, RareScarfItem, identifier="EVENT_9_set_var_to_const_82"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ScroogeRingItem, identifier="EVENT_9_set_var_to_const_84"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MegaShirtItem, identifier="EVENT_9_set_var_to_const_86"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, TrueformPinItem, identifier="EVENT_9_set_var_to_const_88"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireShellItem, identifier="EVENT_9_set_var_to_const_90"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MegaPantsItem, identifier="EVENT_9_set_var_to_const_92"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SailorCapeItem, identifier="EVENT_9_set_var_to_const_94"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FroggieStickItem, identifier="EVENT_9_set_var_to_const_96"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, NokNokShellItem, identifier="EVENT_9_set_var_to_const_98"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ChompItem, identifier="EVENT_9_set_var_to_const_100"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CoinTrickItem, identifier="EVENT_9_set_var_to_const_102"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FearlessPinItem, identifier="EVENT_9_set_var_to_const_104"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FeatherItem, identifier="EVENT_9_set_var_to_const_106"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FingerShotItem, identifier="EVENT_9_set_var_to_const_108"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ThickShirtItem, identifier="EVENT_9_set_var_to_const_110"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ChompShellItem, identifier="EVENT_9_set_var_to_const_112"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, CourageShellItem, identifier="EVENT_9_set_var_to_const_114"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HappyCapeItem, identifier="EVENT_9_set_var_to_const_116"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ThickPantsItem, identifier="EVENT_9_set_var_to_const_118"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, WakeUpPinItem, identifier="EVENT_9_set_var_to_const_120"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SignalRingItem, identifier="EVENT_9_set_var_to_const_122"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ZoomShoesItem, identifier="EVENT_9_set_var_to_const_124"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, AntidotePinItem, identifier="EVENT_9_set_var_to_const_126"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HammerItem, identifier="EVENT_9_set_var_to_const_128"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ShirtItem, identifier="EVENT_9_set_var_to_const_130"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LuckyHammerItem, identifier="EVENT_9_set_var_to_const_132"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HappyShellItem, identifier="EVENT_9_set_var_to_const_134"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MegaCapeItem, identifier="EVENT_9_set_var_to_const_136"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
