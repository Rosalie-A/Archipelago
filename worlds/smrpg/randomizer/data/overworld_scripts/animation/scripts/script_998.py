#A0998_KEEP_ORIGINAL_THRONE_ROOM_GOOMBA
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
	A_FaceSoutheast(),
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_Pause(1, identifier="ACTION_998_pause_3"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_998_clear_solidity_bits_6"]),
	A_Jmp(["ACTION_998_pause_3"]),
	A_ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_998_clear_solidity_bits_6"),
	A_SequenceLoopingOn(),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(FAST),
	A_JumpToHeight(height=96, silent=True),
	A_WalkSoutheastSteps(2),
	A_SequenceLoopingOff(),
	A_Pause(30),
	A_Jmp(["ACTION_997_sequence_playback_on_0"])
])
