#A0304_OUTER_SEA_WHIRLPOOL
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
	A_Mem700CAndConst(0x0006),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_304_pause_8"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_304_pause_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_304_pause_10"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_304_jmp_to_subroutine_11"]),
	A_Pause(80, identifier="ACTION_304_pause_8"),
	A_Pause(80, identifier="ACTION_304_pause_9"),
	A_Pause(80, identifier="ACTION_304_pause_10"),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"], identifier="ACTION_304_jmp_to_subroutine_11"),
	A_TransferXYZFSteps(x=2, y=4, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	A_TransferXYZFSteps(x=253, y=254, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	A_TransferXYZFSteps(x=1, y=254, z=20, direction=NORTHEAST),
	A_Pause(40),
	A_Jmp(["ACTION_304_jmp_to_subroutine_11"]),
	A_VisibilityOn(identifier="ACTION_304_visibility_on_21"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x08\x00\x00\x10\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x00\x00\x00\x01\x04\x00\x00\x10\x80")),
	A_ShiftZUpSteps(6),
	A_BPL262728(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
