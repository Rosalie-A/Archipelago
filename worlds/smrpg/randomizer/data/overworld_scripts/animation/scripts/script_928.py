#A0928_MINES_TREASURE_HUNTER
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
	A_JmpIfBitSet(MINECART_CLEARED, ["ACTION_928_visibility_off_17"], identifier="ACTION_928_jmp_if_bit_set_0"),
	A_SetWalkingSpeed(SLOW),
	A_JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	A_WalkNorthwestSteps(2),
	A_JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	A_WalkNorthwestSteps(2),
	A_JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	A_WalkSoutheastSteps(2),
	A_JmpToSubroutine(["ACTION_928_face_northeast_11"]),
	A_WalkSoutheastSteps(2),
	A_Jmp(["ACTION_928_jmp_if_bit_set_0"]),
	A_FaceNortheast(identifier="ACTION_928_face_northeast_11"),
	A_JumpToHeight(height=32, silent=True),
	A_Pause(12),
	A_JumpToHeight(height=32, silent=True),
	A_Pause(12),
	A_ReturnQueue(),
	A_VisibilityOff(identifier="ACTION_928_visibility_off_17"),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
