#A0331_MARRYMORE_2ND_CHEF
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
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_331_set_animation_speed_0"),
	A_SetSequenceSpeed(FAST),
	A_WalkSouthwestSteps(2),
	A_WalkNorthwestSteps(2),
	A_Pause(30),
	A_WalkSoutheastSteps(2),
	A_WalkNortheastSteps(2),
	A_FaceSoutheast(),
	A_Pause(30),
	A_JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="kitchen_chef_seq_2"),
	A_Pause(20),
	A_ResetProperties(),
	A_JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
	A_WalkNorthwestSteps(2, identifier="ACTION_331_shift_northwest_steps_14"),
	A_Pause(60),
	A_WalkSoutheastSteps(2),
	A_Pause(60),
	A_JmpIfRandom1of2(["ACTION_331_shift_northwest_steps_14"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="kitchen_chef_seq_3"),
	A_Pause(20),
	A_ResetProperties(),
	A_Jmp(["ACTION_331_set_animation_speed_0"])
])
