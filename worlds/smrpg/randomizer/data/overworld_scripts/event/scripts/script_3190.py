# E3190_ACTIVATE_POST_MINES_BOSS_FIRST_MINECART_SESSION_CONTINUED
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
	StopAllBackgroundEvents(identifier="EVENT_3190_stop_all_background_events_0"),
	ClearBit(TOADOFSKY_REMOVED),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
		A_WalkToXYCoords(x=11, y=61),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FaceSoutheast(),
		A_FloatingOn()
	]),
	SetAsyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkToXYCoords(x=12, y=61),
		A_FaceNorthwest()
	]),
	SetVarToConst(TEMP_70AE, 21),
	SetTempAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(54),
		A_Pause(20),
		A_JumpToHeight(54),
		A_Pause(30)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_Pause(1, identifier="EVENT_3190_action_queue_10_SUBSCRIPT_pause_5"),
		A_JmpIfBitClear(TEMP_7044_6, ["EVENT_3190_action_queue_10_SUBSCRIPT_pause_5"]),
		A_SetWalkingSpeed(FAST),
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff(),
		A_WalkSoutheastPixels(3),
		A_WalkSouthPixels(6),
		A_WalkSouthwestPixels(12),
		A_WalkWestPixels(8),
		A_ShiftZUpPixels(20),
		A_Pause(16),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_ShadowOn(),
		A_BounceToXYWithHeight(x=12, y=62, height=2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(0),
		A_ShiftZDownPixels(3),
		A_FixedFCoordOff(),
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_FloatingOff(),
		A_Pause(1, identifier="EVENT_3190_action_queue_10_SUBSCRIPT_pause_26"),
		A_JmpIfBitClear(TEMP_7044_5, ["EVENT_3190_action_queue_10_SUBSCRIPT_pause_26"]),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_SetVRAMPriority(PRIORITY_3)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_WalkToXYCoords(x=12, y=61),
		A_Pause(20),
		A_FaceNortheast(),
		A_Pause(20),
		A_SetBit(TEMP_7044_6),
		A_FaceEast(),
		A_Pause(6),
		A_FaceSoutheast(),
		A_Pause(6),
		A_FaceSouth(),
		A_Pause(8),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(16),
		A_FaceNortheast(),
		A_Walk1StepNortheast(),
		A_SetBit(TEMP_7044_2),
		A_Pause(1, identifier="EVENT_3190_action_queue_11_SUBSCRIPT_pause_22"),
		A_JmpIfBitClear(TEMP_7044_1, ["EVENT_3190_action_queue_11_SUBSCRIPT_pause_22"]),
		A_FaceSouthwest(),
		A_Walk1StepSouthwest(),
		A_Pause(16),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_JumpToHeight(108),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(9),
		A_ShadowOn(),
		A_Pause(8),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_FloatingOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True),
		A_SetBit(TEMP_7044_5)
	]),
	Pause(1, identifier="EVENT_3190_pause_12"),
	JmpIfBitClear(TEMP_7044_2, ["EVENT_3190_pause_12"]),
	SetBit(TEMP_7044_1),
	Pause(1, identifier="EVENT_3190_pause_15"),
	RunEventAsSubroutine(E1200_INNER_MINES_BOSS_UNLOCKS),
    RunEventAsSubroutine(E1227_MOLEVILLE_CHARACTER),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsLesser(["EVENT_3190_j_24"]),
	SetBit(SWITCH_MENU_UNLOCKED),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_3190_pause_15"], identifier="EVENT_3190_j_24"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(8),
		A_UnknownCommand(bytearray(b' \x03')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_PlaySound(sound=SO048_MINECART_START, channel=4),
		A_Pause(200)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_UnknownCommand(bytearray(b' \x07')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x10\x00\x00\x01\x00\x00\x00\x04\x80')),
		A_Pause(200),
		A_SetBit(TEMP_7043_0)
	]),
	Pause(1, identifier="EVENT_3190_pause_20"),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3190_pause_20"]),
	CloseDialog(),
	FadeOutToBlack(sync=False),
	RemoveObjectFromSpecificLevel(NPC_1, R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM),
	Set7000ToMinecartTimer(),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
	JmpIfBitClear(SKIP_MANDATORY_MINECART, ["EVENT_3190_run_moleville_mountain_sequence_29"]),
	JmpIfBitClear(OPTIONAL_MINECART_CLEARED, ["EVENT_3190_enter_area_30"]),
    JmpIfBitClear(MINECART_CLEARED, ["EVENT_3190_set_mines_cleared"], identifier="skip_moleville_minecart_sequence"),
	RunMolevilleMountainSequence(identifier="EVENT_3190_run_moleville_mountain_sequence_29"),
	SetBit(MINECART_CLEARED, identifier="EVENT_3190_set_mines_cleared"),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0, identifier="EVENT_3190_enter_area_30"),
	RunEventAsSubroutine(E1394_FOUR_DIGIT_COIN_VALUE_HANDLER),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1648_MINECART_ENDING)
])
