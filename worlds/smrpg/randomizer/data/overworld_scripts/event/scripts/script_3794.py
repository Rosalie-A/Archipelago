# E3794_FACTORY_FINAL_BOSS_FIGHT
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
	SetSyncActionScript(NPC_9, A0991_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_4, A0240_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_8, A0990_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_5, A0241_SMITHY_COMPONENT),
	SetBit(TEMP_7044_0),
	RunBackgroundEvent(event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_3794_action_queue_6_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_6_SUBSCRIPT_pause_2"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouth()
	]),
	RememberLastObject(),
	Pause(10),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_5),
	UnsyncActionScript(NPC_8),
	Pause(1, identifier="EVENT_3794_pause_14"),
	JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_14"]),
	ClearBit(TEMP_704C_0),
	StopAllBackgroundEvents(),
	SetBit(TEMP_7043_2),
	SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
	JmpToSubroutine(["EVENT_3794_set_bit_69"]),
	Pause(10),
	JmpToSubroutine(["EVENT_3794_set_bit_74"]),
	SetBit(TEMP_7043_5),
	SetBit(TEMP_7043_1),
	RunBackgroundEvent(event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True),
	Pause(90),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_30_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_30_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_30_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_30_SUBSCRIPT_pause_4"])
	]),
	Pause(30),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_5),
	UnsyncActionScript(NPC_8),
	Pause(1, identifier="EVENT_3794_pause_36"),
	JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_36"]),
	ClearBit(TEMP_704C_0),
	StopAllBackgroundEvents(),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
	JmpToSubroutine(["EVENT_3794_set_bit_69"]),
	Pause(10),
	JmpToSubroutine(["EVENT_3794_set_bit_74"]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True)
	]),
	JmpToSubroutine(["EVENT_3794_set_bit_69"]),
	Pause(10),
	JmpToSubroutine(["EVENT_3794_set_bit_74"]),
	Pause(30),
	UnfreezeCamera(),
	SetBit(TEMP_7043_5),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(20),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_JumpToHeight(152),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(2),
		A_FloatingOff(),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	PauseActionScript(NPC_8),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(4),
		A_WalkSouthwestPixels(6)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(4)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(1),
		A_WalkNorthPixels(2),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(55),
	InitiateBattleMask(),
	EnterArea(room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, face_direction=NORTHEAST, x=4, y=51, z=0, run_entrance_event=True),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_69"),
	UnsyncActionScript(NPC_8),
	ClearBit(TEMP_7043_1),
	SetSyncActionScript(NPC_8, A0242_SMITHY_COMPONENT),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_74"),
	ClearBit(TEMP_7043_3),
	UnsyncActionScript(NPC_8),
	ClearBit(TEMP_7043_1),
	SetSyncActionScript(NPC_8, A0987_SMITHY_COMPONENT),
	Return()
])
