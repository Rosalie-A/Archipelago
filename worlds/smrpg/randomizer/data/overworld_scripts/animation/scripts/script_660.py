#A0660_VARIOUS_YELLOW_PLATFORMS_WITHOUT_XY_MOVEMENT
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
	A_Set700CToCurrentLevel(identifier="ACTION_660_set_700C_to_current_level_0"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 378, ["ACTION_660_shadow_on_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 381, ["ACTION_660_shadow_on_9"]),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpSteps(2),
	A_Pause(30),
	A_ShiftZDownSteps(2),
	A_Pause(30),
	A_Jmp(["ACTION_660_set_700C_to_current_level_0"]),
	A_ShadowOn(identifier="ACTION_660_shadow_on_9"),
	A_SetAllSpeeds(SLOW),
	A_SequenceLoopingOn(),
	A_ShiftZUpSteps(3),
	A_JmpIfRandom1of2(["ACTION_660_shift_z_up_steps_15"]),
	A_JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
	A_ShiftZUpSteps(3, identifier="ACTION_660_shift_z_up_steps_15"),
	A_JmpIfRandom1of2(["ACTION_660_shift_z_down_steps_18"]),
	A_JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
	A_ShiftZDownSteps(3, identifier="ACTION_660_shift_z_down_steps_18"),
	A_JmpIfRandom1of2(["ACTION_660_shift_z_down_steps_21"]),
	A_JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
	A_ShiftZDownSteps(3, identifier="ACTION_660_shift_z_down_steps_21"),
	A_JmpIfRandom1of2(["ACTION_660_shadow_on_9"]),
	A_JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
	A_Jmp(["ACTION_660_shadow_on_9"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, identifier="ACTION_660_set_700C_to_object_coord_25"),
	A_Pause(30),
	A_TurnRandomDirection(),
	A_Pause(30),
	A_TurnRandomDirection(),
	A_Pause(30),
	A_FaceEast7C(),
	A_ReturnQueue()
])
