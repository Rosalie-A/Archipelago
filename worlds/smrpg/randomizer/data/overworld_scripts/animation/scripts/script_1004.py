#A1004_KEEP_1ST_BOSS_SUMMON_ANIMATION
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
	A_FaceSouthwest(),
	A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(4),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOn(),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=False, identifier="keep_battle_room_summon"),
	A_ReturnQueue()
])
