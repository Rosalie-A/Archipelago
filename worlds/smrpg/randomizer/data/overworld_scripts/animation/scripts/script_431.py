#A0431_YOSHI_RACE_ANIMATION
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
	A_SetSequenceSpeed(NORMAL, identifier="ACTION_431_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_ResetProperties(),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	A_Pause(1, identifier="ACTION_431_pause_4"),
	A_Jmp(["ACTION_431_pause_4"])
])
