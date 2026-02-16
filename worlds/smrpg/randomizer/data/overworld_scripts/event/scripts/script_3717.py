# E3717_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_FAN_GUST_PATH
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
	JmpIfObjectNotInSpecificLevel(NPC_3, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, ["EVENT_3584_ret_0"]),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_3584_ret_0"]),
	FreezeAllNPCsUntilReturn(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=15, y=112),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(2),
		A_StartLoopNTimes(3),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_EndLoop(),
		A_WalkNorthwestPixels(2)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_3717_action_queue_6_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3717_action_queue_6_SUBSCRIPT_pause_1"]),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=13, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=14, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=15, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	UnfreezeAllNPCs(),
	ClearBit(TEMP_7043_6),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	ClearBit(TEMP_7043_6),
	Return()
])
