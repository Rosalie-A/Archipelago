#A0844_VALLEY_5_PIPE_SHY_AWAY
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
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_ShadowOn(),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(4),
	A_WalkSoutheastPixels(8),
	A_ShadowOff(),
	A_JmpIfObjectNotInSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_not_in_level_16"]),
	A_WalkToXYCoords(x=9, y=29),
	A_WalkEastPixels(10),
	A_Pause(32),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(112),
	A_SetBit(TEMP_7043_4),
	A_Pause(32),
	A_ResetProperties(),
	A_JmpIfObjectNotInSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_not_in_level_24"], identifier="ACTION_844_jmp_if_object_not_in_level_16"),
	A_WalkToXYCoords(x=8, y=25),
	A_Pause(32),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(112),
	A_SetBit(TEMP_7043_0),
	A_Pause(32),
	A_ResetProperties(),
	A_JmpIfObjectNotInSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_not_in_level_32"], identifier="ACTION_844_jmp_if_object_not_in_level_24"),
	A_WalkToXYCoords(x=6, y=29),
	A_Pause(32),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(112),
	A_SetBit(TEMP_7043_1),
	A_Pause(32),
	A_ResetProperties(),
	A_JmpIfObjectNotInSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_jmp_if_object_not_in_level_40"], identifier="ACTION_844_jmp_if_object_not_in_level_32"),
	A_WalkToXYCoords(x=8, y=34),
	A_Pause(32),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(112),
	A_SetBit(TEMP_7043_3),
	A_Pause(32),
	A_ResetProperties(),
	A_JmpIfObjectNotInSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["ACTION_844_walk_to_xy_coords_48"], identifier="ACTION_844_jmp_if_object_not_in_level_40"),
	A_WalkToXYCoords(x=10, y=35),
	A_Pause(32),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(112),
	A_SetBit(TEMP_7043_5),
	A_Pause(32),
	A_ResetProperties(),
	A_WalkToXYCoords(x=7, y=28, identifier="ACTION_844_walk_to_xy_coords_48"),
	A_WalkSouthwestSteps(4),
	A_WalkSouthwestPixels(12),
	A_ShadowOn(),
	A_WalkSouthwestSteps(14),
	A_VisibilityOff(),
	A_ReturnQueue()
])
