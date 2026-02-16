#A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD
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
	A_SetWalkingSpeed(SLOW),
	A_WalkNorthwestSteps(2),
	A_FixedFCoordOn(),
	A_JmpIfRandom2of3(['ACTION_717_pause_6', 'ACTION_717_pause_9'], identifier="ACTION_717_jmp_if_random_above_66_3"),
	A_Pause(30),
	A_Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	A_Pause(30, identifier="ACTION_717_pause_6"),
	A_WalkNortheastSteps(2),
	A_Jmp(["ACTION_717_jmp_if_random_above_128_12"]),
	A_Pause(30, identifier="ACTION_717_pause_9"),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_717_jmp_if_random_above_128_17"]),
	A_JmpIfRandom1of2(["ACTION_717_pause_14"], identifier="ACTION_717_jmp_if_random_above_128_12"),
	A_Pause(30),
	A_Pause(30, identifier="ACTION_717_pause_14"),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	A_JmpIfRandom1of2(["ACTION_717_pause_19"], identifier="ACTION_717_jmp_if_random_above_128_17"),
	A_Pause(30),
	A_Pause(30, identifier="ACTION_717_pause_19"),
	A_WalkNortheastSteps(2),
	A_Jmp(["ACTION_717_jmp_if_random_above_66_3"])
])
