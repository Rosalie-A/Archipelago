# E3502_BOOSTER_HILL_END
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
	EnableControlsUntilReturn([B]),
	MoveScriptToBackgroundThread2(),
	Pause(1, identifier="EVENT_3502_pause_2"),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3502_move_script_to_main_thread_32"], identifier="EVENT_3502_jmp_if_bit_set_3"),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_3502_jmp_if_var_equals_const_24"]),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_3502_jmp_if_var_equals_const_24"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_3502_jmp_if_var_equals_const_28"]),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_3502_jmp_if_var_equals_const_28"]),
	Pause(1, identifier="EVENT_3502_pause_9"),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3502_move_script_to_main_thread_32"], identifier="EVENT_3502_jmp_if_bit_set_10"),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_3502_pause_2"]),
	CompareVarToConst(SECONDARY_TEMP_7024, 0),
	JmpIfLoadedMemoryIs0(["EVENT_3502_clear_bit_22"]),
	JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3502_action_queue_20"]),
	Dec(TEMP_7026),
	JmpIfVarNotEqualsConst(TEMP_7026, 0, ["EVENT_3502_pause_2"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastPixels(1),
		A_Dec(SECONDARY_TEMP_7024),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetVarToConst(TEMP_7026, 1),
	Jmp(["EVENT_3502_jmp_if_bit_set_3"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNorthwestPixels(1),
		A_Inc(SECONDARY_TEMP_7024),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_3502_action_queue_20"),
	Jmp(["EVENT_3502_jmp_if_bit_set_3"]),
	ClearBit(TEMP_7043_5, identifier="EVENT_3502_clear_bit_22"),
	Jmp(["EVENT_3502_pause_2"]),
	JmpIfVarEqualsConst(TEMP_7034, 40, ["EVENT_3502_pause_9"], identifier="EVENT_3502_jmp_if_var_equals_const_24"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(2)
	]),
	Inc(TEMP_7034),
	Jmp(["EVENT_3502_jmp_if_bit_set_10"]),
	JmpIfVarEqualsConst(TEMP_7034, 0, ["EVENT_3502_pause_9"], identifier="EVENT_3502_jmp_if_var_equals_const_28"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(2)
	]),
	Dec(TEMP_7034),
	Jmp(["EVENT_3502_jmp_if_bit_set_10"]),
	MoveScriptToMainThread(identifier="EVENT_3502_move_script_to_main_thread_32"),
	FreezeAllNPCsUntilReturn(),
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	SetSyncActionScript(LAYER_1, A0161_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(LAYER_2, A0161_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(NPC_0, A0161_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(NPC_1, A0161_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(NPC_2, A0161_SEQUENCE_LOOPING_OFF),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ResumeActionScript(NPC_5),
	StartSyncEmbeddedActionScript(target=LAYER_1, prefix=0xF1, subscript=[
		A_WalkNorthwestSteps(15)
	]),
	FadeOutMusicToVolume(duration=5, volume=0),
	UnknownCommand(bytearray(b'\xfdE')),
	EnableControlsUntilReturn([]),
	JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_3502_apply_tile_mod_74"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R054_BOOSTER_HILL_DUMMY, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R054_BOOSTER_HILL_DUMMY, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R054_BOOSTER_HILL_DUMMY, mod_id=32),
	StopEmbeddedActionScript(LAYER_1),
	ResetCoords(NPC_7),
	SetAsyncActionScript(NPC_7, A0160_SEQUENCE_LOOPING_ON),
    
	RunEventAsSubroutine(E1329_HILL_UNLOCKS),

	CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3502_run_dialog_61"]),
	RunDialog(dialog_id=DI1189_FLOWER_SCORE_ON_HILL, above_object=TOADSTOOL, closable=True, sync=True, multiline=False, use_background=False),
	Jmp(["EVENT_3502_action_queue_62"]),
	RunDialog(dialog_id=DI1193_NO_FLOWER_HILL, above_object=TOADSTOOL, closable=True, sync=True, multiline=False, use_background=False, identifier="EVENT_3502_run_dialog_61"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FixedFCoordOff(),
		A_SetAllSpeeds(FAST),
		A_Pause(4),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff()
	], identifier="EVENT_3502_action_queue_62"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_17"),
		A_WalkNorthPixels(4),
		A_Pause(64),
		A_VisibilityOff()
	], identifier="chapel_character_queue_10"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(FAST),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_BounceToXYWithHeight(x=5, y=54, height=0)
	]),
	PlayMusicAtCurrentVolume(M0037_BOOSTERHILL_START),
	FadeOutMusicToVolume(duration=3, volume=127),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FASTER),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(50),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_WalkNortheastSteps(2),
		A_Pause(10),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceWest(),
		A_Pause(8),
		A_WalkSouthwestSteps(5)
	]),
	UnfreezeCamera(),
	UnsyncDialog(),
	SetBit(BOOSTER_HILL_CLEARED),
	Jmp(["EVENT_3502_hill_ends"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R014_BOOSTER_HILL, mod_id=34, identifier="EVENT_3502_apply_tile_mod_74"),
	ApplyTileModToLevel(use_alternate=True, room_id=R014_BOOSTER_HILL, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R014_BOOSTER_HILL, mod_id=32),
	StopEmbeddedActionScript(LAYER_1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(FAST),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_BounceToXYWithHeight(x=5, y=54, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FASTER),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(120),
		A_ResetProperties(),
		A_WalkSouthwestSteps(5)
	]),
	UnfreezeCamera(),
	SetBit(MAP_BOOSTER_HILL),
	CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3502_run_dialog_61_2"]),
	RunDialog(dialog_id=DI1189_FLOWER_SCORE_ON_HILL, above_object=TOADSTOOL, closable=True, sync=True, multiline=False, use_background=False),
	Jmp(["EVENT_3502_hill_ends"]),
	RunDialog(dialog_id=DI1193_NO_FLOWER_HILL, above_object=TOADSTOOL, closable=True, sync=True, multiline=False, use_background=False, identifier="EVENT_3502_run_dialog_61_2"),
    
	JmpIfVarEqualsConst(TEMP_7032, 0, ["EVENT_3400_hill"], identifier="EVENT_3502_hill_ends"),
	
	CopyVarToVar(from_var=STAR_PIECE_COUNTER, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(TEMP_7032),
    Dec(PRIMARY_TEMP_7000),
    CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=STAR_PIECE_COUNTER),
    
    JmpToEvent(E3092_STAR_PIECE_GRANT),
	

])
