#A0638_ROSE_TOWN_ARROW
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
	A_Pause(59),
	A_VisibilityOn(),
	A_TransferToXYZF(x=11, y=49, z=0, direction=SOUTHEAST),
	A_ShiftXYPixels(x=8, y=253),
	A_SetBit(TEMP_7044_3, identifier="ACTION_638_set_bit_4"),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\x00\x00r\xff')),
	A_SetWalkingSpeed(NORMAL),
	A_Walk1StepNortheast(),
	A_WalkNortheastPixels(12),
	A_BPL262728(),
	A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
	A_StartLoopNTimes(2),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_EndLoop(),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_VisibilityOff(),
	A_TransferToXYZF(x=22, y=78, z=0, direction=EAST),
	A_ClearBit(TEMP_7044_3),
	A_ReturnQueue()
])
