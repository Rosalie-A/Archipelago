#A0555_BOOSTER_PASS_TOSSED_SPINY
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
	A_VisibilityOff(),
	A_SetBit(TEMP_7043_7),
	A_SequenceLoopingOn(),
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b'\xc8\x98')),
	A_UnknownCommand(bytearray(b'\x9a')),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_JumpToHeight(48),
	A_Walk1StepNorthwest(),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_Pause(1),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(45),
	A_ClearBit(TEMP_7043_7),
	A_Jmp(["ACTION_404_face_mario_3"])
])
