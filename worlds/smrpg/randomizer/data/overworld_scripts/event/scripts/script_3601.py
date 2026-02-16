# E3601_MUSHROOM_DERBY_YOSHI_AUTOPLAY
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
	SetVarToConst(ROSE_WAY_703E, 3),
	SetSyncActionScript(MARIO, A0288_MARIO_DISMOUNT_YOSHI),
	SetSyncActionScript(NPC_9, A0289_MARIO_DISMOUNT_YOSHI),
	UnsyncActionScript(MARIO),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI0944_YOSHI_ILL_TRY_MY_BEST, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	FreezeCamera(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(1),
		A_WalkToXYCoords(x=13, y=84),
		A_FaceNorthwest()
	]),
	RunBackgroundEvent(event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC, return_on_level_exit=True, run_as_second_script=True),
	Pause(1, identifier="EVENT_3601_pause_18"),
	JmpIfAudioMemoryEquals(3, ["EVENT_3601_pause_18"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(SCREEN_FOCUS, A0801_MUSHROOM_DERBY_UNKNOWN),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_ResetProperties(),
		A_WalkNortheastSteps(5),
		A_FaceWest()
	]),
	Pause(1),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 17),
	JmpIfComparisonResultIsLesser(["EVENT_3601_set_action_script_29"]),
	SetAsyncActionScript(MARIO, A0798_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_3601_set_action_script_29"),
	SetSyncActionScript(SCREEN_FOCUS, A0801_MUSHROOM_DERBY_UNKNOWN),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(5),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceWest()
	]),
	Pause(1, identifier="EVENT_3601_pause_32"),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 12),
	JmpIfComparisonResultIsLesser(["EVENT_3601_set_action_script_37"]),
	Jmp(["EVENT_3601_pause_32"]),
	SetAsyncActionScript(MARIO, A0798_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_3601_set_action_script_37"),
	SetSyncActionScript(SCREEN_FOCUS, A0801_MUSHROOM_DERBY_UNKNOWN),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(4),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceWest()
	]),
	Pause(1),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 8),
	JmpIfComparisonResultIsLesser(["EVENT_3601_set_action_script_44"]),
	SetAsyncActionScript(MARIO, A0802_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_3601_set_action_script_44"),
	Pause(1, identifier="EVENT_3601_pause_45"),
	JmpIfVarEqualsConst(Z_COORD_1, 0, ["EVENT_3601_clear_bit_48"]),
	Jmp(["EVENT_3601_pause_45"]),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_7085_4, identifier="EVENT_3601_clear_bit_48"),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3600_jmp_if_bit_clear_13"]),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_3600_jmp_if_bit_clear_13"]),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_jmp_if_bit_clear_13"]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SetAllSpeeds(NORMAL)
	]),
	UnsyncActionScript(NPC_9),
	StartAsyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(MARIO, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_9, A0677_MUSHROOM_DERBY_UNKNOWN),
	Jmp(["EVENT_3600_action_queue_21"])
])
