# E2820_ASYNC_NO_ANIMATION_ITEM
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
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["river_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["river_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
    Jmp(["river_choose_article"]),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="river_key_item_sound"),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_2820_run_dialog_16"], identifier="river_choose_article"),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_2820_run_dialog_16"]),
	RunDialog(dialog_id=DI0066_GOT_A_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI0064_GOT_AN_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, identifier="EVENT_2820_run_dialog_16"),
	AddToInventory(ITEM_ID),
	Return()
])
