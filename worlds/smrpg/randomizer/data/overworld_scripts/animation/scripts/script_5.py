#A0005_SHIP_SHOP_SHAMAN
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
	A_TurnRandomDirection(identifier="ACTION_5_turn_random_direction_0"),
	A_Walk1StepFDirection(identifier="ACTION_5_walk_1_step_f_direction_1"),
	A_Pause(30, identifier="ACTION_5_pause_2"),
	A_JmpIfRandom1of2(["ACTION_5_pause_2"]),
	A_JmpIfRandom1of2(["ACTION_5_walk_1_step_f_direction_1"]),
	A_JmpIfRandom2of3(['ACTION_5_set_animation_speed_8', 'ACTION_5_set_animation_speed_10']),
	A_SetWalkingSpeed(SLOW),
	A_Jmp(["ACTION_5_turn_random_direction_0"]),
	A_SetWalkingSpeed(VERY_SLOW, identifier="ACTION_5_set_animation_speed_8"),
	A_Jmp(["ACTION_5_turn_random_direction_0"]),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_5_set_animation_speed_10"),
	A_Jmp(["ACTION_5_turn_random_direction_0"])
])
