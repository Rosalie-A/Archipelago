#A0597_MIDAS_FISH
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
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_ShadowOff(),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b'\xc8\x00')),
	A_AddConstToVar(X_COORD_2, 62976),
	A_AddConstToVar(Y_COORD_2, 1280),
	A_SetVarToConst(Z_COORD_2, 0),
	A_UnknownCommand(bytearray(b'\x99')),
	A_VisibilityOn(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_WalkNortheastSteps(4),
	A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	A_Pause(1),
	A_ResetProperties(),
	A_FixedFCoordOn(),
	A_SetWalkingSpeed(FASTEST),
	A_SetSequenceSpeed(FAST),
	A_AddZCoord1Step(),
	A_SetWalkingSpeed(VERY_FAST),
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(2),
	A_StartLoopNTimes(1),
	A_ShiftZDownPixels(2),
	A_ShiftZUpPixels(2),
	A_EndLoop(),
	A_SetWalkingSpeed(FASTEST),
	A_WalkNortheastPixels(4),
	A_ShiftZDownPixels(12),
	A_DecZCoord1Step(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
