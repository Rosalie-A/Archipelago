#A0261_NIMBUS_FINAL_HALLWAY_BOSS
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
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_FaceNortheast(),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepNortheast(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST),
	A_WalkNortheastSteps(6),
	A_SetBit(TEMP_7043_0),
	A_Pause(20),
	A_Walk1StepNortheast(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
