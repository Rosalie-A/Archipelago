# E0165_FREESTANDING_GRANT_ITEM_BAG
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
	DisableObjectTrigger(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["freestand_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["freestand_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
    Jmp(["freestand_choose_article"]),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="freestand_key_item_sound"),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_165_run_dialog_17"], identifier="freestand_choose_article"),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_165_run_dialog_17"], identifier="EVENT_165_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_165_run_dialog_17"], identifier="EVENT_165_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_165_run_dialog_17"], identifier="EVENT_165_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_165_run_dialog_17"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_165_run_dialog_17"]),
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI1178_FOUND_AN_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_165_run_dialog_17"),
	AddToInventory(ITEM_ID),
	Return()
])
