# E2618_FACTORY_2ND_BOSS
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
	JmpIfBitSet(INNER_FACTORY_ROOM_2_COMPLETED, ["EVENT_2618_ret_58"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=3, y=17)
	]),
	SetSyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(16),
		A_ShiftToXYCoords(x=11, y=49)
	]),
	UnsyncDialog(),
	SetSyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, identifier="factory_2nd_boss_look_up_1"),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast()
	], identifier="factory_2nd_boss_look_up_aq_1"),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="factory_2nd_boss_look_up_2"),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	], identifier="factory_2nd_boss_look_up_aq_2"),
	ActionQueueSync(target=NPC_12, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkNortheastPixels(6),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FASTER),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkSoutheastSteps(3),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4)
	]),
	SetSyncActionScript(NPC_12, A0401_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(NPC_13, A0401_SEQUENCE_LOOPING_OFF),
	SetAsyncActionScript(NPC_14, A0401_SEQUENCE_LOOPING_OFF),
	Pause(32),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=5, y=23)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, identifier="factory_2nd_boss_look_up_3"),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="factory_2nd_boss_look_up_aq_3"),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(2)
	]),
	Pause(24),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2618_restore_all_hp_45"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2618_restore_all_hp_45"),
	RestoreAllFP(),
	SetBit(INNER_FACTORY_ROOM_2_COMPLETED),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromCurrentLevel(NPC_14),
	RemoveObjectFromCurrentLevel(NPC_15),
	RemoveObjectFromSpecificLevel(NPC_12, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_13, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_14, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_15, R471_FACTORY_GROUNDS_AREA_02),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E1242_INNER_FACTORY_2_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2618_ret_58")
])
