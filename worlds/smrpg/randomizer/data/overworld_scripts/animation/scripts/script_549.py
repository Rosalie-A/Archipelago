#A0549_KEEP_CROSSING_TERRA_COTTAS_BASE
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
	A_Dec(GAME_OVER_COUNTER_MAYBE, identifier="ACTION_549_dec_0"),
	A_ResetProperties(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_Pause(16),
	A_SetSolidityBits(cant_pass_walls=True, identifier="ACTION_549_set_solidity_bits_5"),
	A_JmpIfRandom2of3(['ACTION_549_face_mario_10', 'ACTION_549_face_mario_10']),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_549_set_solidity_bits_5"]),
	A_FaceMario(identifier="ACTION_549_face_mario_10"),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_549_set_solidity_bits_5"])
])
