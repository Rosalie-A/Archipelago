# E0022_BETTER_TIP_GRANTER
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
	SetVarToRandom(PRIMARY_TEMP_7000, 100),
	CompareVarToConst(PRIMARY_TEMP_7000, 66),
	JmpIfComparisonResultIsLesser(["tier_low"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 91),
	JmpIfComparisonResultIsLesser(["tier_high"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 3),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["highest_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["highest_1"]),
	SetVarToConst(ITEM_ID, RockCandyItem),
	Return(),
	SetVarToConst(ITEM_ID, RedEssenceItem, identifier="highest_0"),
	Return(),
	SetVarToConst(ITEM_ID, KerokeroColaItem, identifier="highest_1"),
	Return(),
    SetVarToRandom(PRIMARY_TEMP_7000, 19, identifier="tier_low"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["low_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["low_1"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["low_2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["low_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["low_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["low_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["low_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["low_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["low_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["low_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["low_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["low_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["low_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["low_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["low_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["low_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["low_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["low_17"]),
	SetVarToConst(ITEM_ID, PickMeUpItem),
	Return(),
	SetVarToConst(ITEM_ID, MushroomItem, identifier="low_0"),
	Return(),
	SetVarToConst(ITEM_ID, HoneySyrupItem, identifier="low_1"),
	Return(),
	SetVarToConst(ITEM_ID, AbleJuiceItem, identifier="low_2"),
	Return(),
	SetVarToConst(ITEM_ID, BracerItem, identifier="low_3"),
	Return(),
	SetVarToConst(ITEM_ID, EnergizerItem, identifier="low_4"),
	Return(),
	SetVarToConst(ITEM_ID, YoshiCookieItem, identifier="low_5"),
	Return(),
	SetVarToConst(ITEM_ID, PureWaterItem, identifier="low_6"),
	Return(),
	SetVarToConst(ITEM_ID, SleepyBombItem, identifier="low_7"),
	Return(),
	SetVarToConst(ITEM_ID, BadMushroomItem, identifier="low_8"),
	Return(),
	SetVarToConst(ITEM_ID, FlowerTabItem, identifier="low_9"),
	Return(),
	SetVarToConst(ITEM_ID, FroggieDrinkItem, identifier="low_10"),
	Return(),
	SetVarToConst(ITEM_ID, MukuCookieItem, identifier="low_11"),
	Return(),
	SetVarToConst(ITEM_ID, FreshenUpItem, identifier="low_12"),
	Return(),
	SetVarToConst(ITEM_ID, FrightBombItem, identifier="low_13"),
	Return(),
	SetVarToConst(ITEM_ID, WiltShroomItem, identifier="low_14"),
	Return(),
	SetVarToConst(ITEM_ID, RottenMushItem, identifier="low_15"),
	Return(),
	SetVarToConst(ITEM_ID, MoldyMushItem, identifier="low_16"),
	Return(),
	SetVarToConst(ITEM_ID, MushroomItem2, identifier="low_17"),
	Return(),
    SetVarToRandom(PRIMARY_TEMP_7000, 12, identifier="tier_high"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["high_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["high_1"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["high_2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["high_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["high_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["high_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["high_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["high_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["high_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["high_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["high_10"]),
	SetVarToConst(ITEM_ID, PowerBlastItem),
	Return(),
	SetVarToConst(ITEM_ID, MidMushroomItem, identifier="high_0"),
	Return(),
	SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="high_1"),
	Return(),
	SetVarToConst(ITEM_ID, MapleSyrupItem, identifier="high_2"),
	Return(),
	SetVarToConst(ITEM_ID, RoyalSyrupItem, identifier="high_3"),
	Return(),
	SetVarToConst(ITEM_ID, YoshiAdeItem, identifier="high_4"),
	Return(),
	SetVarToConst(ITEM_ID, FireBombItem, identifier="high_5"),
	Return(),
	SetVarToConst(ITEM_ID, IceBombItem, identifier="high_6"),
	Return(),
	SetVarToConst(ITEM_ID, YoshiCandyItem, identifier="high_7"),
	Return(),
	SetVarToConst(ITEM_ID, ElixirItem, identifier="high_8"),
	Return(),
	SetVarToConst(ITEM_ID, MegalixirItem, identifier="high_9"),
	Return(),
	SetVarToConst(ITEM_ID, CrystallineItem, identifier="high_10"),
	Return(),
])
