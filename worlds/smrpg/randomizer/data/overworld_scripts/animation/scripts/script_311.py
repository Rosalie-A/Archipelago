#A0311_SHIP_TROOPA_PUZZLE_TROOPA
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
	A_SetPriority(3, identifier="ACTION_311_set_priority_0"),
	A_SetWalkingSpeed(SLOW),
	A_SetVarToConst(TEMP_70AE, 0),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_ShadowOff(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 15, ["ACTION_311_set_700C_to_object_coord_12"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 111, ["ACTION_311_set_700C_to_object_coord_12"]),
	A_SetVarToConst(TEMP_70AE, 1),
	A_Jmp(["ACTION_311_face_mario_30"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_12"),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 15, ["ACTION_311_set_700C_to_object_coord_18"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 113, ["ACTION_311_set_700C_to_object_coord_18"]),
	A_SetVarToConst(TEMP_70AE, 2),
	A_Jmp(["ACTION_311_face_mario_30"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_18"),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_700C_to_object_coord_24"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 111, ["ACTION_311_set_700C_to_object_coord_24"]),
	A_SetVarToConst(TEMP_70AE, 3),
	A_Jmp(["ACTION_311_face_mario_30"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True, bit_7=True, identifier="ACTION_311_set_700C_to_object_coord_24"),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_priority_0"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 113, ["ACTION_311_set_priority_0"]),
	A_SetVarToConst(TEMP_70AE, 4),
	A_Jmp(["ACTION_311_face_mario_30"]),
	A_FaceMario(identifier="ACTION_311_face_mario_30"),
	A_Walk1StepFDirection(),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_311_set_priority_0"]),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 112, ["ACTION_311_set_priority_0"]),
	A_Jmp(["ACTION_311_set_priority_0"])
])
