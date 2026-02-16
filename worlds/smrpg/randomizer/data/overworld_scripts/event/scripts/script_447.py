# E0447_GOOMBA_THUMPIN_SPAWNS
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
	JmpIfBitClear(TEMP_7044_0, ["EVENT_447_set_var_to_random_6"], identifier="EVENT_447_jmp_if_bit_clear_0"),
	JmpIfBitClear(TEMP_7044_1, ["EVENT_447_set_var_to_random_6"]),
	JmpIfBitClear(TEMP_7044_2, ["EVENT_447_set_var_to_random_6"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_447_set_var_to_random_6"]),
	Pause(1),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetVarToRandom(PRIMARY_TEMP_7000, 4, identifier="EVENT_447_set_var_to_random_6"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_447_jmp_if_bit_set_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_447_jmp_if_bit_set_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_447_jmp_if_bit_set_73"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_447_jmp_if_bit_clear_0"]),
	ClearBit(TEMP_7043_1),
	SetVarToRandom(PRIMARY_TEMP_7000, 23),
	CompareVarToConst(PRIMARY_TEMP_7000, 21),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_20"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_23"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_26"]),
	Jmp(["EVENT_447_jmp_if_random_above_66_48"]),
	SetSyncActionScript(NPC_5, A0416_GOOMBA_THUMPIN_LEFT_PIPE, identifier="EVENT_447_set_action_script_20"),
	SetBit(TEMP_7044_0),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_10, A0416_GOOMBA_THUMPIN_LEFT_PIPE, identifier="EVENT_447_set_action_script_23"),
	SetBit(TEMP_7044_0),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_1, A0416_GOOMBA_THUMPIN_LEFT_PIPE, identifier="EVENT_447_set_action_script_26"),
	SetBit(TEMP_7044_0),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_447_jmp_if_bit_clear_0"], identifier="EVENT_447_jmp_if_bit_set_29"),
	ClearBit(TEMP_7043_2),
	SetVarToRandom(PRIMARY_TEMP_7000, 23),
	CompareVarToConst(PRIMARY_TEMP_7000, 21),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_39"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_42"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_45"]),
	Jmp(["EVENT_447_jmp_if_random_above_66_48"]),
	SetSyncActionScript(NPC_6, A0417_GOOMBA_THUMPIN_TOP_PIPE, identifier="EVENT_447_set_action_script_39"),
	SetBit(TEMP_7044_1),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_11, A0417_GOOMBA_THUMPIN_TOP_PIPE, identifier="EVENT_447_set_action_script_42"),
	SetBit(TEMP_7044_1),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_2, A0417_GOOMBA_THUMPIN_TOP_PIPE, identifier="EVENT_447_set_action_script_45"),
	SetBit(TEMP_7044_1),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	JmpIfRandom2of3(['EVENT_447_jmp_if_bit_clear_0', 'EVENT_447_jmp_if_random_above_128_51'], identifier="EVENT_447_jmp_if_random_above_66_48"),
	Pause(71),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	JmpIfRandom1of2(["EVENT_447_jmp_if_bit_clear_0"], identifier="EVENT_447_jmp_if_random_above_128_51"),
	Pause(99),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_447_jmp_if_bit_clear_0"], identifier="EVENT_447_jmp_if_bit_set_54"),
	ClearBit(TEMP_7043_3),
	SetVarToRandom(PRIMARY_TEMP_7000, 23),
	CompareVarToConst(PRIMARY_TEMP_7000, 21),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_64"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_67"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_70"]),
	Jmp(["EVENT_447_jmp_if_random_above_66_48"]),
	SetSyncActionScript(NPC_7, A0418_GOOMBA_THUMPIN_RIGHT_PIPE, identifier="EVENT_447_set_action_script_64"),
	SetBit(TEMP_7044_2),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_12, A0418_GOOMBA_THUMPIN_RIGHT_PIPE, identifier="EVENT_447_set_action_script_67"),
	SetBit(TEMP_7044_2),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_3, A0418_GOOMBA_THUMPIN_RIGHT_PIPE, identifier="EVENT_447_set_action_script_70"),
	SetBit(TEMP_7044_2),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_447_jmp_if_bit_clear_0"], identifier="EVENT_447_jmp_if_bit_set_73"),
	ClearBit(TEMP_7043_4),
	SetVarToRandom(PRIMARY_TEMP_7000, 23),
	CompareVarToConst(PRIMARY_TEMP_7000, 21),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_83"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_86"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_447_set_action_script_89"]),
	Jmp(["EVENT_447_jmp_if_random_above_66_48"]),
	SetSyncActionScript(NPC_8, A0419_GOOMBA_THUMPIN_BOTTOM_PIPE, identifier="EVENT_447_set_action_script_83"),
	SetBit(TEMP_7044_3),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_13, A0419_GOOMBA_THUMPIN_BOTTOM_PIPE, identifier="EVENT_447_set_action_script_86"),
	SetBit(TEMP_7044_3),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS),
	SetSyncActionScript(NPC_4, A0419_GOOMBA_THUMPIN_BOTTOM_PIPE, identifier="EVENT_447_set_action_script_89"),
	SetBit(TEMP_7044_3),
	JmpToEvent(E0447_GOOMBA_THUMPIN_SPAWNS)
])
