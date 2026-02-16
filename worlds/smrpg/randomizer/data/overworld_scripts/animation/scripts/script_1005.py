#A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY
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
	A_JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["ACTION_1005_ret_30"]),
	A_Pause(25),
	A_ResetProperties(),
	A_Pause(10),
	A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	A_StartLoopNTimes(2),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_StartLoopNTimes(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(4),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(6),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ReturnQueue(identifier="ACTION_1005_ret_30")
])
