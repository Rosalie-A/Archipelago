# E3806_ENDING_CREDITS_RACE_NPCS
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
	FreezeCamera(),
	RunEventAsSubroutine(E1193_ENDING_CREDITS_YOSTER_SHUFFLED_NPC_ANIMATION_LOADER),
	RunBackgroundEvent(event_id=E3808_ENDING_CREDITS_RACE_AUDIENCE, return_on_level_exit=True),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast(),
		A_Pause(30),
		A_FaceNortheast(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=False, mirror_sprite=True),
		A_Pause(68),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_WalkSouthwestSteps(5),
		A_WalkSouthwestPixels(12),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(61),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(12),
		A_ShiftZDownPixels(12),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(4),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(159),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_VisibilityOff(),
		A_TransferToObjectXY(NPC_10),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(4),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthPixels(8),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthPixels(2),
		A_WalkSouthPixels(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(4),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouth(),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouth(),
		A_WalkSouthPixels(2),
		A_Walk1StepSouthwest(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(300),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(300),
		A_FaceSouthwest()
	]),
	StarMaskExpandFromScreenCenter(),
	RememberLastObject(),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(5),
		A_WalkNortheastSteps(1),
		A_WalkNortheastPixels(12),
		A_FaceSoutheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(4),
		A_WalkSouthwestPixels(4),
		A_WalkNorthwestSteps(4),
		A_WalkNorthwestPixels(4),
		A_FaceNortheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(5),
		A_WalkSouthwestPixels(6),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(12),
		A_SequenceLoopingOff()
	]),
	SetSyncActionScript(NPC_10, A0239_ENDING_CREDITS_CROCO),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SequenceLoopingOff()
	]),
	SetSyncActionScript(NPC_7, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_2, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_3, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_4, A0677_MUSHROOM_DERBY_UNKNOWN),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(4),
		A_Pause(134),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNortheastSteps(12)
	]),
	SetSyncActionScript(NPC_5, A0208_RAZ_ENDING),
	SetSyncActionScript(NPC_6, A0209_RAINI_ENDING),
	Pause(425),
	PauseScriptUntilEffectDone(),
	StarMaskShrinkToScreenCenter(),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E3800_ENDING_CREDITS_INDIGO_STAR)
])
