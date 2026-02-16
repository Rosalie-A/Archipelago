# E2531_STAR_HILL_2ND_ROOM_WISH_BOTTOM_RIGHT
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
	JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_2531_run_dialog_5"]),
	RunDialog(dialog_id=DI3327_CONVERTED_WISH, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Return(),
	RunDialog(dialog_id=DI3116_WISH_10, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2531_run_dialog_5"),
	PlaySound(sound=SO000_SILENCE, channel=6),
	JmpIfBitSet(MALLOWS_PARENTS_WISH_READ, ["EVENT_2531_ret_38"]),
	SetBit(MALLOWS_PARENTS_WISH_READ),
	FadeOutMusicFDA3(),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_21),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(108),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8)
	]),
	RunDialog(dialog_id=DI3123_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	PlayMusicAtDefaultVolume(M0021_SADSONG),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	Pause(48),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(48),
	RunDialog(dialog_id=DI3126_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_StartLoopNTimes(8),
		A_WalkNorthPixels(1),
		A_Pause(2),
		A_WalkSouthPixels(1),
		A_Pause(16),
		A_EndLoop()
	]),
	UnsyncDialog(),
	Pause(96),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3124_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(32),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3125_MALLOW_WISH_CUTSCENE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_21, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_21),
	FadeOutMusicFDA3(),
	Pause(16),
	PlayMusicAtDefaultVolume(M0034_STARHILL),
	Return(identifier="EVENT_2531_ret_38")
])
