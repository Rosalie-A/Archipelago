# E0215_HILL_ITEM
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
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["hill_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["hill_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
    Jmp(["hill_choose_article"]),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="hill_key_item_sound"),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_215_run_dialog_16"], identifier="hill_choose_article"),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_215_run_dialog_16"], identifier="EVENT_215_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_215_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_215_run_dialog_16"]),
	RunDialog(dialog_id=DI0536_BOOSTER_HILL_ITEM, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI0535_BOOSTER_HILL_ITEM_VOWEL, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_215_run_dialog_16"),
	AddToInventory(ITEM_ID),
	Return()
])
