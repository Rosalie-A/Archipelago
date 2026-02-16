#A0250_DRILL_BIT
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
	A_VisibilityOff(),
	A_FaceSoutheast(),
	A_TransferToXYZF(x=4, y=19, z=0, direction=EAST),
	A_TransferXYZFPixels(x=12, y=12, z=0, direction=EAST),
	A_ShadowOff(),
	A_VisibilityOn(),
	A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(6),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(6),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(6),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(6),
	A_ResetProperties(),
	A_SetSequenceSpeed(FAST),
	A_SequencePlaybackOn(),
	A_WalkSoutheastSteps(5),
	A_SequencePlaybackOff(),
	A_AddZCoord1Step(),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpSteps(2),
	A_SetWalkingSpeed(VERY_FAST),
	A_SetBit(TEMP_7044_4),
	A_ShiftZUpSteps(2),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpSteps(4),
	A_ShadowOn(),
	A_SetWalkingSpeed(NORMAL),
	A_TransferToXYZF(x=3, y=48, z=0, direction=EAST),
	A_SetBit(TEMP_7044_4),
	A_ReturnQueue()
])
