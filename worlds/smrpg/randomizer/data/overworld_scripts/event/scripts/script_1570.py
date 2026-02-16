# E1570_MIDAS_RIVER_FISH
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
	SetBit(TEMP_7044_2),
	DisableObjectTrigger(NPC_0),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_JumpToHeight(48),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepWest(),
		A_VisibilityOff()
	]),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	PauseActionScript(MEM_70A8),
	PauseActionScript(MARIO),
	PauseActionScript(SCREEN_FOCUS),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_FloatingOff(),
		A_JumpToHeight(height=72, silent=True),
		A_CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_700C),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_1570_action_queue_10_SUBSCRIPT_play_sound_8"]),
		A_PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
		A_Pause(8),
		A_Jmp(["EVENT_1570_action_queue_11"]),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4, identifier="EVENT_1570_action_queue_10_SUBSCRIPT_play_sound_8"),
		A_Pause(8)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(FAST)
	], identifier="EVENT_1570_action_queue_11"),
	SetVarToConst(PRIMARY_TEMP_700C, 5),
	StartLoopNTimes(4),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1570_pause_18"]),
	CreatePacketAtObjectCoords(packet=P017_SMALL_MINIGAME_COIN, target_npc=MARIO, destinations=["EVENT_1570_pause_18"]),
	Dec(TEMP_702A),
	Pause(1, identifier="EVENT_1570_pause_18"),
	Inc(PRIMARY_TEMP_700C),
	EndLoop(),
	Pause(3),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ResumeActionScript(MEM_70A8),
	ResumeActionScript(MARIO),
	ResumeActionScript(SCREEN_FOCUS),
	ClearBit(TEMP_7044_2),
	Return()
])
