# E2529_STAR_HILL_1ST_ROOM_WISH_TOP_LEFT
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
	PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
	RunDialog(dialog_id=DI3115_WISH_9, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO000_SILENCE, channel=6),
	JmpIfBitSet(MALLOWS_WISH_READ, ["EVENT_2529_ret_25"]),
	SetBit(MALLOWS_WISH_READ),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_15),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(4),
		A_FaceSouthwest()
	]),
	FreezeCamera(),
	Pause(8),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_StartLoopNTimes(3),
		A_WalkSouthwestPixels(2),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Pause(8),
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_EndLoop(),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3120_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_15),
	Pause(16),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3121_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_Pause(16),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4),
		A_Pause(8),
		A_SetPriority(0),
		A_Pause(24),
		A_SetPriority(3),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3122_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_Walk1StepSouthwest(),
		A_Pause(4),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_15),
	UnfreezeCamera(),
	Return(identifier="EVENT_2529_ret_25")
])
