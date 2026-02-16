#A0849_BEAN_VALLEY_BEANSTALK_BRICK
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
	A_Pause(2, identifier="ACTION_849_pause_0"),
	A_ShiftZDownPixels(1),
	A_Pause(4),
	A_ShiftZDownPixels(1),
	A_Pause(13),
	A_ShiftZUpPixels(1),
	A_Pause(4),
	A_ShiftZUpPixels(1),
	A_Pause(2),
	A_ShiftZUpPixels(1),
	A_Pause(4),
	A_ShiftZUpPixels(1),
	A_Pause(13),
	A_ShiftZDownPixels(1),
	A_Pause(4),
	A_ShiftZDownPixels(1),
	A_JmpIfBitSet(TEMP_708C_4, ["ACTION_849_ret_18"]),
	A_Jmp(["ACTION_849_pause_0"]),
	A_ReturnQueue(identifier="ACTION_849_ret_18")
])
