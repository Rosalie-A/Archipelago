# E2456_AWAKEN_SLEEPING_WIGGLER
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	JmpIfBitClear(DIRECTIONAL_7046_7, ["EVENT_2456_ret_23"]),
	JmpIfBitSet(WIGGLER_IS_AWAKE, ["EVENT_2456_ret_23"]),
	ClearBit(DIRECTIONAL_7046_7),
	ClearBit(DIRECTIONAL_7046_5),
	ClearBit(DIRECTIONAL_7046_6),
	SetBit(WIGGLER_IS_AWAKE),
	SetBit(DIRECTIONAL_7047_0),
	SetBit(DIRECTIONAL_7047_4),
	FreezeCamera(),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromSpecificLevel(NPC_10, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=0, y=59),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetSyncActionScript(MARIO, A0485_PLAYER_SHOCKED_WHEN_WIGGLER_WAKES_UP),
	SetSyncActionScript(SCREEN_FOCUS, A0392_SLEEPING_WIGGLER_CAMERA),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(8),
		A_StartLoopNTimes(6),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthPixels(5),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(8),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthPixels(5),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(8),
		A_EndLoop(),
		A_SetSpriteSequence(index=26, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(8),
		A_SetSpriteSequence(index=27, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetBit(TEMP_7043_0),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(8),
		A_SetSpriteSequence(index=29, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(3),
		A_WalkNorthwestPixels(6),
		A_SetSpriteSequence(index=30, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_Pause(3),
		A_SetSpriteSequence(index=31, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO021_RUMBLING, channel=6)
	]),
	Pause(8),
	FadeOutToBlack(sync=False, duration=24),
	RemoveObjectFromSpecificLevel(NPC_1, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS),
	ApplySolidityModToLevel(permanent=True, room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R234_FOREST_MAZE_SECRET, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, mod_id=0),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=4, y=74, z=0, run_entrance_event=True),
	Return(identifier="EVENT_2456_ret_23")
])
