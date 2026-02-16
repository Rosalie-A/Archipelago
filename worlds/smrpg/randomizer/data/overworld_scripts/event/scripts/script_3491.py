# E3491_MIDAS_RIVER_TOP_TUNNEL_ANIMATION_AND_EXIT
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
	FadeInFromBlack(sync=True),
	FreezeCamera(),
	SetSyncActionScript(MARIO, A0598_MIDAS_RIVER_TOP_TUNNEL_PLAYER_OUTER),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkEastSteps(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpToSubroutine(["EVENT_3491_action_queue_16"]),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=8, y=31, z=0),
	FadeOutMusicToVolume(duration=1, volume=56),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=12, y=29),
		A_SetVarToConst(X_COORD_2, 6528),
		A_SetVarToConst(Y_COORD_2, 3712),
		A_TransferTo70167018()
	]),
	JmpToSubroutine(["EVENT_3480_action_queue_40"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(8),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x80\x02\xf4\xff')),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_WalkNorthwestSteps(7),
		A_Walk1StepSouthwest(),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
	Jmp(["EVENT_3489_enable_controls_3"]),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True)
	], identifier="EVENT_3491_action_queue_16"),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_17"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_17"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_23"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_23"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_29"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_29"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_35"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_35"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=11, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_41"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_41"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_47"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_47"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_53"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_53"]),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_59"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_59"]),
	EndLoop(),
	Jmp(["EVENT_3491_action_queue_16"]),
	FadeOutToBlack(sync=False, duration=32, identifier="EVENT_3491_fade_out_to_black_async_duration_65"),
	Return()
])
