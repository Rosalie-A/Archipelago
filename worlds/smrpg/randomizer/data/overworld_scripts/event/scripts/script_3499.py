# E3499_BOOSTER_HILL_1ST_PASS_LOADER
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
	SetVarToConst(TEMP_7032, 0),
	RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7034, 16),
	SetVarToConst(TEMP_7026, 1),
	SetVarToConst(BOOSTER_HILL_FLOWER_COUNTER, 0),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=11, y=67, z=0, direction=EAST)
	]),
	ActionQueueSync(target=LAYER_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(18)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x01\x00\x01\x00\x00\x00 \x80')),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_12"),
		A_ShiftZUpPixels(9),
		A_WalkSoutheastPixels(8)
	], identifier="chapel_character_queue_9"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthwestSteps(11)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(11),
		A_SetSequenceSpeed(NORMAL)
	]),
	SetSyncActionScript(NPC_8, A0715_FOREVER_PAUSE_LOOP),
	JmpToSubroutine(["EVENT_3499_action_queue_42"]),
	JmpToSubroutine(["EVENT_3499_action_queue_45"]),
	Pause(20),
	JmpToSubroutine(["EVENT_3499_action_queue_42"]),
	JmpToSubroutine(["EVENT_3499_action_queue_45"]),
	JmpToSubroutine(["EVENT_3499_action_queue_42"]),
	JmpToSubroutine(["EVENT_3499_action_queue_45"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(8),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL)
	]),
    RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3499_no_star"]),
	RunEventAsSubroutine(E3842_BOOSTER_HILL_STAR_PIECE_SIGNAL),
	JmpToSubroutine(["EVENT_3499_action_queue_42"], identifier="EVENT_3499_no_star"),
	JmpToSubroutine(["EVENT_3499_action_queue_45"]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(40),
		A_SetSequenceSpeed(NORMAL)
	]),
	JmpToSubroutine(["EVENT_3499_action_queue_42"]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequenceLoopingOn()
	]),
	SetVarToConst(TEMP_70AE, 3),
	JmpToSubroutine(["EVENT_3499_action_queue_45"]),
	SetSyncActionScript(NPC_3, A0707_BOOSTER_HILL_HENCHMAN),
	SetSyncActionScript(NPC_4, A0707_BOOSTER_HILL_HENCHMAN),
	SetSyncActionScript(NPC_5, A0707_BOOSTER_HILL_HENCHMAN),
	Pause(60),
	RunBackgroundEvent(event_id=E3500_BOOSTER_HILL_1ST_PASS_SNIFIT_JUMPS, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E3503_BOOSTER_HILL_BARREL_SUMMONER, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
	SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
	SetSyncActionScript(LAYER_3, A0705_BOOSTER_HILL_LAYER_3),
	PlayMusicAtDefaultVolume(M0038_BOOSTERHILL),
	RunEventAtReturn(E3502_BOOSTER_HILL_END),
	Return(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_13"),
		A_WalkNorthPixels(4),
		A_WalkWestPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_14"),
		A_WalkWestPixels(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	], identifier="EVENT_3499_action_queue_42"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceSoutheast()
	]),
	Return(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_15"),
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_16"),
		A_WalkSouthPixels(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	], identifier="EVENT_3499_action_queue_45"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceNorthwest()
	]),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=5, y=54, z=0, direction=EAST),
		A_SetPriority(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FASTER),
		A_WalkSouthwestPixels(36),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_VisibilityOn(),
		A_JumpToHeight(24, identifier="EVENT_3499_action_queue_48_SUBSCRIPT_jump_to_height_9"),
		A_Walk1StepSoutheast(),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
		A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
		A_JmpIfComparisonResultIsLesser(["EVENT_3499_action_queue_48_SUBSCRIPT_jump_to_height_9"])
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(50),
		A_JumpToHeight(112)
	]),
	Return()
])
