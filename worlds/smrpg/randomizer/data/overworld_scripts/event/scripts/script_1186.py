# E1186_HENCHMAN_BATTLE_PACK_SELECTOR
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_1186_start_battle_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_1186_start_battle_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 37, ["EVENT_1186_start_battle_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 43, ["EVENT_1186_start_battle_24"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_1186_start_battle_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 194, ["EVENT_1186_start_battle_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 273, ["EVENT_1186_set_var_to_const_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 277, ["EVENT_1186_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 283, ["EVENT_1186_set_var_to_const_36"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 325, ["EVENT_1186_start_battle_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 327, ["EVENT_1186_start_battle_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 332, ["EVENT_1186_start_battle_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 405, ["EVENT_1186_start_battle_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 469, ["EVENT_1186_start_battle_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 480, ["EVENT_1186_start_battle_49"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 481, ["EVENT_1186_start_battle_51"]),
	Return(),
	StartBattleAtBattlefield(PACK068_SHIP_HENCHMAN_1, BF04_SUNKEN_SHIP, identifier="EVENT_1186_start_battle_18"),
	Return(),
	StartBattleAtBattlefield(PACK069_SHIP_HENCHMAN_2, BF04_SUNKEN_SHIP, identifier="EVENT_1186_start_battle_20"),
	Return(),
	StartBattleAtBattlefield(PACK142_MINES_HENCHMAN_MIDDLE, BF12_BOOSTER_TOWER, identifier="EVENT_1186_start_battle_22"),
	Return(),
	StartBattleAtBattlefield(PACK142_MINES_HENCHMAN_MIDDLE, BF12_BOOSTER_TOWER, identifier="EVENT_1186_start_battle_24"),
	Return(),
	StartBattleAtBattlefield(PACK011_KINGDOM_HENCHMEN_2, BF28_MUSHROOM_KINGDOM, identifier="EVENT_1186_start_battle_26"),
	Return(),
	StartBattleAtBattlefield(PACK142_MINES_HENCHMAN_MIDDLE, BF12_BOOSTER_TOWER, identifier="EVENT_1186_start_battle_28"),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 141, identifier="EVENT_1186_set_var_to_const_30"),
	StartBattleWithPackAt700E(),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 141, identifier="EVENT_1186_set_var_to_const_33"),
	StartBattleWithPackAt700E(),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 141, identifier="EVENT_1186_set_var_to_const_36"),
	StartBattleWithPackAt700E(),
	Return(),
	StartBattleAtBattlefield(PACK010_KINGDOM_HENCHMEN_1, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_1186_start_battle_39"),
	Return(),
	StartBattleAtBattlefield(PACK011_KINGDOM_HENCHMEN_2, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_1186_start_battle_41"),
	Return(),
	StartBattleAtBattlefield(PACK011_KINGDOM_HENCHMEN_2, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_1186_start_battle_43"),
	Return(),
	StartBattleAtBattlefield(PACK032_TOWER_PASS_HENCHMAN, BF10_MOUNTAINS, identifier="EVENT_1186_start_battle_45"),
	Return(),
	StartBattleAtBattlefield(PACK150_FACTORY_BOSS_RUSH_HENCHMAN, BF48_FACTORY_GROUNDS, identifier="EVENT_1186_start_battle_47"),
	Return(),
	StartBattleAtBattlefield(PACK011_KINGDOM_HENCHMEN_2, BF11_MUSHROOM_KINGDOM_HOUSE, identifier="EVENT_1186_start_battle_49"),
	Return(),
	StartBattleAtBattlefield(PACK011_KINGDOM_HENCHMEN_2, BF11_MUSHROOM_KINGDOM_HOUSE, identifier="EVENT_1186_start_battle_51"),
	Return()
])
