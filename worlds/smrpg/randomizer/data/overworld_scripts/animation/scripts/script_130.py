#A0130_HENCHMAN_TERRORIZING_EAST_GUARD
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
	A_SetPriority(3, identifier="ACTION_130_set_priority_0"),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	A_ClearBit(TEMP_7044_3),
	A_SetBit(TEMP_7044_4),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_ClearBit(TEMP_7044_4),
	A_SetBit(TEMP_7044_3),
	A_Jmp(["ACTION_130_set_priority_0"])
])
