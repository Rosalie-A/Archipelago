# E3089_GRANT_ITEM_FROM_CHEST
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
    JmpIfVarEqualsConst(ITEM_ID, TempleKeyItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RareFrogCoinItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, WalletItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CricketPieItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey1Item, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CastleKey2Item, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BambinoBombItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, TenorCardItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SopranoCardItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrystalShardItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RoomKeyItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShedKeyItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, SeedItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FertilizerItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, DryBonesFlagItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GreaperFlagItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BigBooFlagItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, FireworksItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShinyStoneItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CarboCookieItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BrightCardItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, ShoesItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, BroochItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, RingItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, CrownItem, ["chest_key_item_sound"]),
    JmpIfVarEqualsConst(ITEM_ID, GoldPaintItem, ["chest_key_item_sound"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
    Jmp(["chest_choose_article"]),
    PlaySound(sound=SO085_FLOWER, channel=6, identifier="chest_key_item_sound"),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_3089_run_dialog_16"], identifier="chest_choose_article"),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_3089_run_dialog_16"], identifier="EVENT_3089_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_3089_run_dialog_16"], identifier="EVENT_3089_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_3089_run_dialog_16"], identifier="EVENT_3089_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_3089_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_3089_run_dialog_16"]),
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI1178_FOUND_AN_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_3089_run_dialog_16"),
	AddToInventory(ITEM_ID),
	Return()
])
