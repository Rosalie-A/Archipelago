#A0890_NIMBUS_DIZZY_SHY_GUY
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_890_pause_23"]),
	A_Pause(1, identifier="ACTION_890_pause_2"),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_890_pause_5"]),
	A_Jmp(["ACTION_890_pause_2"]),
	A_Pause(90, identifier="ACTION_890_pause_5"),
	A_FaceSouthwest(),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_JmpIfRandom1of2(["ACTION_890_set_animation_speed_11"], identifier="ACTION_890_jmp_if_random_above_128_8"),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_890_walk_1_step_south_12"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_890_set_animation_speed_11"),
	A_Walk1StepSouth(identifier="ACTION_890_walk_1_step_south_12"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(8),
	A_JmpIfRandom1of2(["ACTION_890_set_animation_speed_18"]),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_890_walk_1_step_west_19"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_890_set_animation_speed_18"),
	A_Walk1StepWest(identifier="ACTION_890_walk_1_step_west_19"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(8),
	A_Jmp(["ACTION_890_jmp_if_random_above_128_8"]),
	A_Pause(1, identifier="ACTION_890_pause_23"),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_890_pause_26"]),
	A_Jmp(["ACTION_890_pause_23"]),
	A_Pause(90, identifier="ACTION_890_pause_26"),
	A_FaceSouthwest(),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_JmpIfRandom1of2(["ACTION_890_set_animation_speed_32"], identifier="ACTION_890_jmp_if_random_above_128_29"),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_890_walk_1_step_south_33"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_890_set_animation_speed_32"),
	A_Walk1StepSouth(identifier="ACTION_890_walk_1_step_south_33"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(8),
	A_JmpIfRandom1of2(["ACTION_890_set_animation_speed_39"]),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_890_walk_1_step_west_40"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_890_set_animation_speed_39"),
	A_Walk1StepWest(identifier="ACTION_890_walk_1_step_west_40"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(8),
	A_Jmp(["ACTION_890_jmp_if_random_above_128_29"])
])
