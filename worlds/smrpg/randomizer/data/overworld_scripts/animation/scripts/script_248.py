#A0248_ENDING_CUTSCENE_EFFECT
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
	A_UnknownCommand(bytearray(b' \x03')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x18\x00\x7f\xff\x00\xee\xff\x80\xfe\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xe4\x00\\\xff\x00\xee\xff\x80\xfe\x80")),
	A_SetWalkingSpeed(VERY_SLOW),
	A_AddZCoord1Step(),
	A_Pause(392),
	A_BPL262728(),
	A_ReturnQueue()
])
