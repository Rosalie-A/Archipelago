#A0969_ENDING_CREDITS_CASTLE_DIRECTOR
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
	A_Walk1StepNortheast(),
	A_StartLoopNTimes(5),
	A_SetSpriteSequence(index=4, sprite_offset=2, looping=False),
	A_Pause(46),
	A_EndLoop(),
	A_SetSpriteSequence(index=13, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	A_Pause(32),
	A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(56),
	A_ResetProperties(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSouthwestSteps(2),
	A_WalkSouthwestPixels(8),
	A_Walk1StepNorthwest(),
	A_Pause(64),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_ReturnQueue()
])
