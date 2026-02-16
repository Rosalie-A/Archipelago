#A0965_FACTORY_3RD_BOSS_CONVEYOR_NPC_BASE
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
	A_ShadowOn(identifier="ACTION_965_shadow_on_0"),
	A_SetWalkingSpeed(SLOW),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkToXYCoords(x=7, y=94),
	A_WalkSoutheastPixels(9),
	A_SetBit(TEMP_7043_0),
	A_WalkToXYCoords(x=9, y=99),
	A_WalkSoutheastPixels(9),
	A_SetBit(TEMP_7043_1),
	A_WalkToXYCoords(x=12, y=105),
	A_WalkSoutheastPixels(9),
	A_SetBit(TEMP_7043_2),
	A_Walk1StepSoutheast(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_WalkToXYCoords(x=16, y=113),
	A_ShiftToXYCoords(x=14, y=52),
	A_WalkSoutheastSteps(3),
	A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_ShiftToXYCoords(x=6, y=92),
	A_Jmp(["ACTION_965_shadow_on_0"])
])
