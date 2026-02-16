#A0412_FOREST_MAZE_AREA_BEE
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
	A_SetPriority(3),
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_UnknownCommand(bytearray(b' \x07')),
	A_JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_7"]),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	A_Jmp(["ACTION_412_jmp_if_random_above_128_8"]),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80'), identifier="ACTION_412_embedded_animation_routine_7"),
	A_JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_11"], identifier="ACTION_412_jmp_if_random_above_128_8"),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80")),
	A_Jmp(["ACTION_412_jmp_if_random_above_128_12"]),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80"), identifier="ACTION_412_embedded_animation_routine_11"),
	A_JmpIfRandom1of2(["ACTION_412_embedded_animation_routine_15"], identifier="ACTION_412_jmp_if_random_above_128_12"),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\x00\x00\x00\x04\x80')),
	A_Jmp(["ACTION_412_jmp_if_object_within_range_16"]),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x0c\x00\x01\x00\x00\x00\x04\x80'), identifier="ACTION_412_embedded_animation_routine_15"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=128, tiles=4, destinations=["ACTION_412_bpl_26_27_28_19"], identifier="ACTION_412_jmp_if_object_within_range_16"),
	A_Pause(48),
	A_Jmp(["ACTION_412_jmp_if_object_within_range_16"]),
	A_BPL262728(identifier="ACTION_412_bpl_26_27_28_19"),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x07')),
	A_BPL2627(),
	A_VisibilityOn(),
	A_UnknownCommand(bytearray(b'0\x00\x02')),
	A_UnknownCommand(bytearray(b')\x00')),
	A_Pause(1, identifier="ACTION_412_pause_27"),
	A_Jmp(["ACTION_412_pause_27"])
])
