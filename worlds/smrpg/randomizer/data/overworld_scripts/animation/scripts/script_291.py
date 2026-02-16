#A0291_MINES_FINAL_BOSS_ROOM_HENCHMAN
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_291_set_animation_speed_0"),
	A_SetSequenceSpeed(FAST),
	A_SetPriority(2),
	A_WalkNorthwestSteps(2),
	A_JmpIfRandom2of3(['ACTION_291_set_priority_6', 'ACTION_291_set_priority_6']),
	A_JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	A_SetPriority(3, identifier="ACTION_291_set_priority_6"),
	A_WalkNortheastSteps(2),
	A_JmpIfRandom2of3(['ACTION_291_set_priority_10', 'ACTION_291_set_priority_10']),
	A_JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	A_SetPriority(3, identifier="ACTION_291_set_priority_10"),
	A_WalkSoutheastSteps(2),
	A_JmpIfRandom2of3(['ACTION_291_set_priority_14', 'ACTION_291_set_priority_14']),
	A_JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	A_SetPriority(2, identifier="ACTION_291_set_priority_14"),
	A_WalkSouthwestSteps(2),
	A_JmpIfRandom2of3(['ACTION_291_set_animation_speed_0', 'ACTION_291_set_animation_speed_0']),
	A_JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	A_Jmp(["ACTION_291_set_animation_speed_0"])
])
