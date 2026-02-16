#A0570_MELODY_BAY_TADPOLE_SWIMS
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
	A_SetVarToConst(Y_COORD_1, 6),
	A_SetPriority(3),
	A_SetSequenceSpeed(FAST),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
	A_Pause(10),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_570_set_sprite_sequence_6"),
	A_StartLoopNTimes(5),
	A_SetBit(TEMP_7044_3),
	A_Pause(20),
	A_ClearBit(TEMP_7044_3),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSoutheastPixels(10),
	A_SetWalkingSpeed(FAST),
	A_WalkSoutheastPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSoutheastPixels(2),
	A_Dec(Y_COORD_1),
	A_EndLoop(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_StartLoopNTimes(5),
	A_SetBit(TEMP_7044_3),
	A_Pause(20),
	A_ClearBit(TEMP_7044_3),
	A_SetWalkingSpeed(FASTEST),
	A_WalkNorthwestPixels(10),
	A_SetWalkingSpeed(FAST),
	A_WalkNorthwestPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_WalkNorthwestPixels(2),
	A_Inc(Y_COORD_1),
	A_EndLoop(),
	A_Jmp(["ACTION_570_set_sprite_sequence_6"])
])
