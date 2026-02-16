#A0402_FOREST_TRUNK_AREA_UNDERGROUND_AMANITA
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
	A_SetSequenceSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_JmpIfRandom1of2(["ACTION_402_set_var_to_random_5"], identifier="ACTION_402_jmp_if_random_above_128_2"),
	A_TurnRandomDirection(),
	A_Pause(8),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 2, identifier="ACTION_402_set_var_to_random_5"),
	A_Inc(PRIMARY_TEMP_700C),
	A_WalkF20Steps(),
	A_Jmp(["ACTION_402_jmp_if_random_above_128_2"])
])
