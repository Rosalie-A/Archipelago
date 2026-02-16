#A0380_MARRYMORE_LIBERATED_EXTERIOR_APPROACH_CHAPEL
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_380_set_animation_speed_0"),
	A_SetSequenceSpeed(NORMAL),
	A_WalkNortheastSteps(3),
	A_SetSequenceSpeed(SLOW),
	A_Pause(120),
	A_SetSequenceSpeed(NORMAL),
	A_WalkSouthwestSteps(3),
	A_SetSequenceSpeed(SLOW),
	A_FaceNortheast(),
	A_Pause(180),
	A_Jmp(["ACTION_380_set_animation_speed_0"])
])
