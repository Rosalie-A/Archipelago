# E3496_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT_BACKGROUND
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
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
	Pause(1, identifier="EVENT_3496_pause_2"),
	JmpIfBitClear(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3496_pause_2"]),
	Pause(3),
	PauseActionScript(SCREEN_FOCUS),
	PauseActionScript(MARIO),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_JmpIfVarEqualsConst(TEMP_7034, 0, ["EVENT_3496_action_queue_8"]),
		A_PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO065_THWOMP_STOMP, channel=4),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=144, silent=True)
	], identifier="EVENT_3496_action_queue_8"),
	SetVarToConst(PRIMARY_TEMP_700C, 0),
	StartLoopNTimes(7),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3496_pause_15"]),
	CreatePacketAtObjectCoords(packet=P017_SMALL_MINIGAME_COIN, target_npc=MARIO, destinations=["EVENT_3496_pause_15"]),
	Dec(TEMP_702A),
	Pause(1, identifier="EVENT_3496_pause_15"),
	Inc(PRIMARY_TEMP_700C),
	EndLoop(),
	Pause(1, identifier="EVENT_3496_pause_18"),
	JmpIfMarioInAir(["EVENT_3496_pause_18"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=3, looping=False),
		A_Pause(4),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ResumeActionScript(SCREEN_FOCUS),
	ResumeActionScript(MARIO),
	ClearBit(MIDAS_RIVER_TUNNEL_1_BIT),
	SetBit(MIDAS_RIVER_TUNNEL_2_BIT_2),
	Return()
])
