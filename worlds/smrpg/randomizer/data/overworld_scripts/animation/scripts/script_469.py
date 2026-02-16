#A0469_BANDITS_WAY_5_LOADER_BOSS
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
	A_SetSolidityBits(cant_walk_through=True),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(NORMAL),
	A_StartLoopNTimes(119, identifier="ACTION_469_start_loop_n_times_3"),
	A_Pause(1),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_469_unknown_jmp_3C_7"]),
	A_Jmp(["ACTION_469_end_loop_8"]),
	A_UnknownJmp3C(0x00, 0x20, ["ACTION_469_set_bit_11"], identifier="ACTION_469_unknown_jmp_3C_7"),
	A_EndLoop(identifier="ACTION_469_end_loop_8"),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_469_start_loop_n_times_3"]),
	A_SetBit(TEMP_7044_4, identifier="ACTION_469_set_bit_11"),
	A_ReturnQueue()
])
