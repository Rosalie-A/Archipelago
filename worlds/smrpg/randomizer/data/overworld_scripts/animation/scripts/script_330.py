#A0330_MARRYMORE_HEAD_CHEF
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
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_330_set_animation_speed_0"),
	A_SetSequenceSpeed(FAST),
	A_WalkSoutheastSteps(3),
	A_FaceSouthwest(),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="kitchen_chef_seq_1"),
	A_Pause(20),
	A_ResetProperties(),
	A_WalkNorthwestSteps(3),
	A_Pause(60),
	A_JmpIfRandom1of2(["ACTION_330_set_animation_speed_0"]),
	A_WalkSouthwestSteps(2, identifier="ACTION_330_shift_southwest_steps_10"),
	A_FaceNorthwest(),
	A_Pause(30),
	A_WalkNortheastSteps(2),
	A_FaceNorthwest(),
	A_Pause(60),
	A_JmpIfRandom1of2(["ACTION_330_shift_southwest_steps_10"]),
	A_Jmp(["ACTION_330_set_animation_speed_0"])
])
