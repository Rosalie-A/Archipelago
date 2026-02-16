#A0116_MK_THRONE_ANTECHAMBER_HENCHMAN
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
	A_JmpIfRandom2of3(['ACTION_116_jmp_to_subroutine_4', 'ACTION_116_jmp_to_subroutine_7'], identifier="ACTION_116_jmp_if_random_above_66_0"),
	A_JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	A_JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	A_Jmp(["ACTION_116_jmp_if_random_above_66_0"]),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"], identifier="ACTION_116_jmp_to_subroutine_4"),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	A_Jmp(["ACTION_116_jmp_if_random_above_66_0"]),
	A_JmpToSubroutine(["ACTION_105_set_animation_speed_0"], identifier="ACTION_116_jmp_to_subroutine_7"),
	A_JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	A_Jmp(["ACTION_116_jmp_if_random_above_66_0"])
])
