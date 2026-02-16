# E0469_YOSTER_ISLE_BACKGROUND
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
	EnableControls([LEFT, RIGHT, DOWN, UP]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST)
	]),
	UnfreezeCamera(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP], identifier="EVENT_469_enable_controls_until_return_4"),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_TransferToObjectXY(MARIO)
	]),
	SetSyncActionScript(NPC_9, A0505_SLOW_SEQUENCE_LOOP),
	Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_7"),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_469_set_7000_to_pressed_button_83"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_469_set_7000_to_pressed_button_87"]),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_469_set_7000_to_pressed_button_91"]),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_469_set_7000_to_pressed_button_95"]),
	JmpIf7000AnyBitsSet(bits=[0, 3], destinations=["EVENT_469_set_action_script_61"]),
	JmpIf7000AnyBitsSet(bits=[0, 2], destinations=["EVENT_469_set_action_script_67"]),
	JmpIf7000AnyBitsSet(bits=[1, 2], destinations=["EVENT_469_set_action_script_64"]),
	JmpIf7000AnyBitsSet(bits=[1, 3], destinations=["EVENT_469_set_action_script_58"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_469_action_queue_20"]),
	JmpIf7000AnyBitsSet(bits=[6], destinations=["EVENT_469_enable_controls_until_return_99"]),
	Pause(1),
	Jmp(["EVENT_469_enable_controls_until_return_4"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_703E)
	], identifier="EVENT_469_action_queue_20"),
	Set7016701BToObjectXYZ(target=MARIO, bit_7=True),
	CopyVarToVar(from_var=Z_COORD_2, to_var=PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_469_enable_controls_until_return_4"]),
	UnknownCommand(bytearray(b'\xfd\xca')),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_469_action_queue_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 512, ["EVENT_469_action_queue_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 531, ["EVENT_469_action_queue_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 256, ["EVENT_469_action_queue_30"]),
	Jmp(["EVENT_469_enable_controls_until_return_4"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkTo70167018()
	], identifier="EVENT_469_action_queue_30"),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 4),
	Mem7000AndConst(0x0007),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	EnableControlsUntilReturn([]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_469_set_action_script_48"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_469_set_action_script_48"]),
	SetSyncActionScript(NPC_9, A0289_MARIO_DISMOUNT_YOSHI),
	SetSyncActionScript(MARIO, A0288_MARIO_DISMOUNT_YOSHI),
	UnsyncActionScript(MARIO),
	Pause(1, identifier="EVENT_469_pause_41"),
	JmpIfMarioInAir(["EVENT_469_pause_41"]),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=6),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return(),
	SetSyncActionScript(NPC_9, A0498_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_469_set_action_script_48"),
	SetSyncActionScript(MARIO, A0497_MUSHROOM_DERBY_UNKNOWN),
	UnsyncActionScript(MARIO),
	Pause(1, identifier="EVENT_469_pause_51"),
	JmpIfMarioInAir(["EVENT_469_pause_51"]),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=6),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return(),
	SetSyncActionScript(NPC_9, A0211_GREEN_YOSHI, identifier="EVENT_469_set_action_script_58"),
	SetAsyncActionScript(MARIO, A0230_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0212_GREEN_YOSHI, identifier="EVENT_469_set_action_script_61"),
	SetAsyncActionScript(MARIO, A0231_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0213_GREEN_YOSHI, identifier="EVENT_469_set_action_script_64"),
	SetAsyncActionScript(MARIO, A0232_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0217_GREEN_YOSHI, identifier="EVENT_469_set_action_script_67"),
	SetAsyncActionScript(MARIO, A0233_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0218_GREEN_YOSHI, identifier="EVENT_469_set_action_script_70"),
	SetAsyncActionScript(MARIO, A0234_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0219_GREEN_YOSHI, identifier="EVENT_469_set_action_script_73"),
	SetAsyncActionScript(MARIO, A0235_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetBit(TEMP_7044_7, identifier="EVENT_469_set_bit_76"),
	SetSyncActionScript(NPC_9, A0220_GREEN_YOSHI),
	SetAsyncActionScript(MARIO, A0236_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	SetSyncActionScript(NPC_9, A0221_GREEN_YOSHI, identifier="EVENT_469_set_action_script_80"),
	SetAsyncActionScript(MARIO, A0237_RIDE_YOSHI),
	Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
	Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_83"),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_469_set_action_script_58"]),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_469_set_action_script_61"]),
	Jmp(["EVENT_469_set_action_script_70"]),
	Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_87"),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_469_set_action_script_64"]),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_469_set_action_script_67"]),
	Jmp(["EVENT_469_set_action_script_73"]),
	Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_91"),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_469_set_action_script_58"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_469_set_action_script_64"]),
	Jmp(["EVENT_469_set_bit_76"]),
	Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_95"),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_469_set_action_script_61"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_469_set_action_script_67"]),
	Jmp(["EVENT_469_set_action_script_80"]),
	EnableControlsUntilReturn([], identifier="EVENT_469_enable_controls_until_return_99"),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(108)
	]),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
		A_Set700CToObjectCoord(target_npc=NPC_9, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032),
		A_JmpIf700CAnyBitsSet(bits=[0], destinations=["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_jmp_if_var_equals_const_5"]),
		A_Jmp(["EVENT_469_pause_102"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_11"], identifier="EVENT_469_start_embedded_action_script_101_SUBSCRIPT_jmp_if_var_equals_const_5"),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_17"]),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=False, mirror_sprite=True),
		A_Jmp(["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_pause_19"]),
		A_SetSequenceSpeed(FAST, identifier="EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_11"),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=False),
		A_Jmp(["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_pause_19"]),
		A_SetSequenceSpeed(FAST, identifier="EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_14"),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=False),
		A_Jmp(["EVENT_469_start_embedded_action_script_101_SUBSCRIPT_pause_19"]),
		A_SetSequenceSpeed(FAST, identifier="EVENT_469_start_embedded_action_script_101_SUBSCRIPT_set_animation_speed_17"),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=False, mirror_sprite=True),
		A_Pause(34, identifier="EVENT_469_start_embedded_action_script_101_SUBSCRIPT_pause_19"),
		A_ResetProperties()
	]),
	Pause(1, identifier="EVENT_469_pause_102"),
	JmpIfMarioInAir(["EVENT_469_pause_102"]),
	RememberLastObject(),
	Jmp(["EVENT_469_enable_controls_until_return_4"])
])
