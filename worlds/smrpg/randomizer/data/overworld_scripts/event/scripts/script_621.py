# E0621_MARRYMORE_INN_ELDERLY_GUEST
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_621_jmp_if_bit_set_85"]),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_621_jmp_if_bit_set_91"]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=6, y=62),
		A_FaceNorthwest()
	]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_var_to_const_9"]),
	SetVarToConst(TEMP_70A9, 27),
	Jmp(["EVENT_621_action_queue_10"]),
	SetVarToConst(TEMP_70A9, 26, identifier="EVENT_621_set_var_to_const_9"),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(2)
	], identifier="EVENT_621_action_queue_10"),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_WalkSoutheastSteps(2),
		A_WalkNortheastSteps(2)
	]),
	Pause(30),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R006_MARRYMORE_INN_2F, face_direction=NORTHEAST, x=15, y=52, z=1, z_add_half_unit=True),
	FadeInFromBlack(sync=True),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_var_to_const_24"]),
	SetVarToConst(TEMP_70A9, 22),
	Jmp(["EVENT_621_pause_25"]),
	SetVarToConst(TEMP_70A9, 21, identifier="EVENT_621_set_var_to_const_24"),
	Pause(1, identifier="EVENT_621_pause_25"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(4),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_TransferToXYZF(x=15, y=52, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(2)
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_WalkNorthwestSteps(4)
	]),
	Pause(50),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R011_MARRYMORE_INN_3F, face_direction=NORTHEAST, x=12, y=73, z=1, z_add_half_unit=True),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_var_to_const_38"]),
	SetVarToConst(TEMP_70A9, 25),
	Jmp(["EVENT_621_pause_39"]),
	SetVarToConst(TEMP_70A9, 24, identifier="EVENT_621_set_var_to_const_38"),
	Pause(1, identifier="EVENT_621_pause_39"),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastSteps(3),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(30),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(30),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNortheast(),
		A_TransferToXYZF(x=12, y=73, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastSteps(2)
	]),
	Pause(52),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=1),
	Pause(70),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=NORTHEAST, x=3, y=21, z=0),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	SetBit(TEMP_7044_5),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_var_to_const_56"]),
	SetVarToConst(TEMP_70A9, 22),
	Jmp(["EVENT_621_fade_in_from_black_sync_57"]),
	SetVarToConst(TEMP_70A9, 21, identifier="EVENT_621_set_var_to_const_56"),
	FadeInFromBlack(sync=True, identifier="EVENT_621_fade_in_from_black_sync_57"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_TransferToXYZF(x=3, y=22, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2)
	]),
	RememberLastObject(),
	FreezeCamera(),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNorthwestSteps(3),
		A_FaceSouth()
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(20),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkEastSteps(7)
	]),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_Pause(30),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkWestSteps(5),
		A_WalkSouthwestSteps(2),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(12)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetBit(GUEST_DROPPED_OFF),
	UnfreezeCamera(),
	Return(),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_621_run_dialog_89"], identifier="EVENT_621_jmp_if_bit_set_85"),
	SetBit(TEMP_7044_2),
	RunEventAsSubroutine(E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1, identifier="event_621_big_tip_claimed"),
	Return(),
	RunDialog(dialog_id=DI1016_THANKS_A_LOT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_621_run_dialog_89"),
	Return(),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_621_run_dialog_95"], identifier="EVENT_621_jmp_if_bit_set_91"),
	SetBit(TEMP_7044_1),
    JmpIfBitSet(MARRYMORE_MAJOR_TIP_GIVEN, ["event_621_big_tip_claimed"]),
    SetBit(MARRYMORE_MAJOR_TIP_GIVEN),
	RunEventAsSubroutine(E0626_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_FLOWERBOX),
	Return(),
	RunDialog(dialog_id=DI2048_HOTEL_GUEST_LEAVING, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_621_run_dialog_95"),
	Return()
])
