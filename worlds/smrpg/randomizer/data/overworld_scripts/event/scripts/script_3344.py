# E3344_VOLCANO_FINAL_TRAMPOLINE_ROOM_LOADER
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
	JmpIfBitSet(VOLCANO_TRAMPOLINE_ROOM_ANIMATION_COMPLETED, ["EVENT_3344_jmp_to_event_13"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_VisibilityOff(),
		A_Walk1StepNortheast()
	]),
	RunEventAsSubroutine(E0844_VOLCANO_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftXYPixels(x=252, y=254),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_JumpToHeight(108),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(8),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3344_action_queue_4_SUBSCRIPT_pause_9"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3344_action_queue_4_SUBSCRIPT_pause_9"]),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FloatingOff(),
		A_SetBit(TEMP_7043_0),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(8),
		A_JumpToHeight(256),
		A_Pause(10),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftXYPixels(x=252, y=254),
		A_Pause(30),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_JumpToHeight(108),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(8),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3344_action_queue_5_SUBSCRIPT_pause_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3344_action_queue_5_SUBSCRIPT_pause_10"]),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FloatingOff(),
		A_SetBit(TEMP_7043_0),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(8),
		A_JumpToHeight(256),
		A_Pause(10),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="axem_henchman_1_aq"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftXYPixels(x=252, y=254),
		A_Pause(60),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_JumpToHeight(108),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(8),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3344_action_queue_6_SUBSCRIPT_pause_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3344_action_queue_6_SUBSCRIPT_pause_10"]),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FloatingOff(),
		A_SetBit(TEMP_7043_0),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(8),
		A_JumpToHeight(256),
		A_Pause(10),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="axem_henchman_2_aq"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftXYPixels(x=252, y=254),
		A_Pause(90),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_JumpToHeight(108),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(8),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3344_action_queue_7_SUBSCRIPT_pause_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3344_action_queue_7_SUBSCRIPT_pause_10"]),
		A_SetBit(TEMP_7043_0),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FloatingOff(),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(8),
		A_JumpToHeight(256),
		A_Pause(10),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="axem_henchman_3_aq"),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftXYPixels(x=252, y=254),
		A_Pause(120),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_JumpToHeight(108),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(8),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3344_action_queue_8_SUBSCRIPT_pause_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3344_action_queue_8_SUBSCRIPT_pause_10"]),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FloatingOff(),
		A_SetBit(TEMP_7043_0),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(8),
		A_JumpToHeight(256),
		A_Pause(10),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="axem_henchman_4_aq"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_StartLoopNTimes(4, identifier="axem_trampoline_loop"),
		A_Pause(1, identifier="EVENT_3344_action_queue_9_SUBSCRIPT_pause_1"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3344_action_queue_9_SUBSCRIPT_pause_1"]),
		A_SetSequenceSpeed(FASTEST),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(4),
		A_ClearBit(TEMP_7043_0),
		A_EndLoop()
	], identifier="axem_trampoline_aqueue"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_VisibilityOn(),
		A_Walk1StepSouthwest()
	]),
	SetBit(VOLCANO_TRAMPOLINE_ROOM_ANIMATION_COMPLETED),
	Return(),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3344_jmp_to_event_13")
])
