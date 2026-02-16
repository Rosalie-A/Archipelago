#A0306_WHIRLPOOL
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
	A_SetSequenceSpeed(VERY_SLOW),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_306_jmp_to_subroutine_5"]),
	A_Pause(80),
	A_JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_306_jmp_to_subroutine_5"),
	A_TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	A_Pause(40),
	A_Jmp(["ACTION_306_jmp_to_subroutine_5"]),
	A_VisibilityOn(identifier="ACTION_306_visibility_on_9"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\xf0\xff\x00\x10\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x00\x04\x00\x01\xf8\xff\x00\x10\x80")),
	A_ShiftZDownSteps(5),
	A_BPL262728(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
