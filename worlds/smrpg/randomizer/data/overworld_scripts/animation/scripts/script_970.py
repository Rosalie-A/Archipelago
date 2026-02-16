#A0970_ENDING_CREDITS_CASTLE_TERRAPINS
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
	A_SetWalkingSpeed(FASTEST),
	A_Walk1StepNorthwest(),
	A_WalkNorthwestPixels(4),
	A_FaceNortheast(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_970_start_loop_n_times_15"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_970_start_loop_n_times_23"]),
	A_StartLoopNTimes(9),
	A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
	A_Pause(34),
	A_EndLoop(),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(80),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue(),
	A_StartLoopNTimes(10, identifier="ACTION_970_start_loop_n_times_15"),
	A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
	A_Pause(34),
	A_EndLoop(),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(64),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue(),
	A_StartLoopNTimes(11, identifier="ACTION_970_start_loop_n_times_23"),
	A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
	A_Pause(34),
	A_EndLoop(),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(48),
	A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue()
])
