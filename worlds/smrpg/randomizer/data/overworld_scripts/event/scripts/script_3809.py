# E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE
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
	EnableControlsUntilReturn([]),
	ApplyTileModToLevel(use_alternate=True, room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, mod_id=0),
	SetBit(TEMP_704C_0),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=NORTHEAST, x=9, y=100, z=0, run_entrance_event=True),
	SetBit(CHAPEL_ITEM_RETRIEVAL_STARTED),
	FreezeCamera(),
	RunEventAsSubroutine(E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER),
	ActionQueueSync(target=NPC_7, subscript=[
		A_VisibilityOn(),
		A_TransferXYZFPixels(x=252, y=248, z=0, direction=EAST),
		A_Pause(12),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(13),
		A_WalkNortheastPixels(8),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(3),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_tpose_1"),
		A_SetWalkingSpeed(FASTEST),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(3),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(1)
	], identifier="chapel_tpose_queue_1"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_VisibilityOn(),
		A_TransferXYZFPixels(x=8, y=4, z=6, direction=EAST),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_1"),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_Pause(96),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_JumpToHeight(height=112, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(12),
		A_SetSpriteSequence(index=1, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, identifier="chapel_character_animation_2")
	], identifier="chapel_character_queue_1"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1])
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(3),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_JumpToHeight(height=128, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(5),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(24),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(16),
		A_WalkNortheastPixels(16),
		A_WalkSouthwestPixels(16),
		A_WalkNortheastPixels(12),
		A_WalkSouthwestPixels(8),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_TransferToObjectXY(NPC_8),
		A_TransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=144, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xf6\x80\xfd')),
		A_Pause(60),
		A_BPL262728(),
		A_TransferToXYZF(x=11, y=86, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(34),
		A_TransferToObjectXY(NPC_8),
		A_TransferXYZFPixels(x=0, y=8, z=12, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=136, silent=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(4)
	]),
	FadeInFromBlack(sync=True),
	Pause(28),
	ReturnFD(),
	Pause(20),
	ReturnFD(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(48),
		A_TransferToObjectXY(NPC_8),
		A_TransferXYZFPixels(x=0, y=12, z=14, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=152, silent=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestSteps(5),
		A_VisibilityOn()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, identifier="chapel_character_animation_3")
	], identifier="chapel_character_queue_2"),
	Pause(20),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, identifier="chapel_character_queue_3_")
	], identifier="chapel_character_queue_3"),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, identifier="chapel_character_animation_4"),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, identifier="chapel_character_animation_5"),
		A_FaceSouthwest()
	], identifier="chapel_character_queue_4"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True, identifier="chapel_character_animation_6")
	], identifier="chapel_character_queue_5"),
	Pause(30),
	UnfreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_WalkNortheastSteps(13),
		A_Pause(20),
		A_WalkNortheastSteps(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(44),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_7"),
		A_SetWalkingSpeed(FAST),
		A_ShadowOn(),
		A_AddZCoord1Step(),
		A_Pause(20),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(1)
	], identifier="chapel_character_queue_6"),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepEast(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(10),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x04\x00\xff')),
		A_JumpToHeight(height=104, silent=True),
		A_Pause(10),
		A_FloatingOn(),
		A_Pause(14),
		A_BPL262728(),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, identifier="chapel_character_animation_9"),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True, identifier="chapel_character_animation_8")
	], identifier="chapel_character_queue_7"),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="chapel_stare_up_1"),
		A_Pause(8),
		A_ResetProperties()
	], identifier="chapel_stare_up_queue_1"),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(10)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_stare_up_2"),
		A_Pause(120),
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(10),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	], identifier="chapel_stare_up_queue_2"),
	Pause(40),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, identifier="chapel_stare_up_3"),
		A_Pause(8),
		A_ResetProperties()
	], identifier="chapel_stare_up_queue_3"),
	Pause(60),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSouthwest()
	]),
	Pause(60),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Walk1StepNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSoutheastPixels(10),
		A_Pause(30),
		A_WalkNorthwestPixels(14),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(50),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_10"),
		A_SetWalkingSpeed(SLOW),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Walk1StepNorthwest(),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_11")
	], identifier="chapel_character_queue_8"),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(30),
		A_FaceSouthwest(),
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_FaceSouthwest(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(140),
		A_VisibilityOff(),
		A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="tower_boss_laughing_seq_3")
	], identifier="tower_boss_laughing_aqueue_3"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkToXYCoords(x=20, y=75),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(15),
		A_WalkNorthwestSteps(3),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(10),
		A_WalkToXYCoords(x=20, y=75),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(9),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(16),
		A_WalkToXYCoords(x=20, y=75),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_SetBit(TEMP_7043_0),
		A_Pause(30),
		A_ClearBit(TEMP_7043_0),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	Pause(50),
	SetSyncActionScript(SCREEN_FOCUS, A0214_SANCTUARY_CAMERA),
	Pause(60),
	StopAllBackgroundEvents(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	Pause(1, identifier="EVENT_3809_pause_104"),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_pause_104"]),
	SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(8),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RemoveObjectFromCurrentLevel(NPC_4),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	Pause(20),
	Pause(1, identifier="EVENT_3809_pause_113"),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_pause_113"]),
	SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
	Pause(10),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RemoveObjectFromCurrentLevel(NPC_3),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToObjectXYZ(NPC_7),
		A_ShiftZUpSteps(2, identifier="crown_adjust_height"),
		A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True)
	], identifier="crown_adjust_height_aq"),
	Pause(30),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
	SetBit(TEMP_7049_2),
	Pause(1, identifier="EVENT_3809_pause_125"),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_pause_125"]),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_0),
	SetSyncActionScript(NPC_1, A0373_SANCTUARY_HENCHMAN, identifier="EVENT_3809_set_action_script_133"),
	SetSyncActionScript(NPC_0, A0372_SANCTUARY_HENCHMAN),
	SetSyncActionScript(NPC_2, A0374_SANCTUARY_HENCHMAN),
	SlowDownMusicTempoBy(duration=0, change=12),
	SetVarToConst(TEMP_70AE, 8),
	SetVarToConst(TEMP_70AF, 0),
	SetVarToConst(FACTORY_FALL_1, 0),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	ClearBit(SANCTUARY_LOCKED),
	SetVarToConst(TIMER_701C, 300),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0647_MARRYMORE_SANCTUARY_CANDLE_1, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	Return()
])
