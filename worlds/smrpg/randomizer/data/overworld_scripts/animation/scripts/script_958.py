#A0958_CRANE_FOR_FINAL_FACTORY_BOSS_DEFAULT
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
	A_SetPriority(3),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_WalkEastPixels(12, identifier="ACTION_958_shift_east_pixels_3"),
	A_SetWalkingSpeed(SLOW),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_ShiftZDownSteps(4),
	A_ShiftZDownPixels(3),
	A_Pause(32),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	A_Pause(11),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_Pause(8),
	A_SetBit(TEMP_7044_0),
	A_ShiftZUpSteps(3),
	A_WalkToXYCoords(x=3, y=88),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSoutheastPixels(8),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZDownSteps(3),
	A_Pause(10),
	A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	A_Pause(10),
	A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	A_Pause(16),
	A_ShiftZUpSteps(4),
	A_ShiftZUpPixels(3),
	A_WalkToXYCoords(x=1, y=72),
	A_Jmp(["ACTION_958_shift_east_pixels_3"])
])
