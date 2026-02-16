# E2402_8BIT_BACKGROUND
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
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Pause(1, identifier="EVENT_2402_pause_1"),
	ClearBit(TEMP_7043_0),
	JmpIfMarioInAir(["EVENT_2402_set_bit_43"]),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[6], destinations=["EVENT_2402_action_queue_8"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL)
	]),
	Jmp(["EVENT_2402_set_7000_to_pressed_button_9"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST)
	], identifier="EVENT_2402_action_queue_8"),
	Set7000ToPressedButton(identifier="EVENT_2402_set_7000_to_pressed_button_9"),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_2402_jmp_if_bit_set_33"]),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_2402_jmp_if_bit_set_38"]),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_2402_jmp_if_bit_set_38"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_2402_jmp_if_bit_set_33"]),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2402_clear_bit_31"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2402_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2402_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2402_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2402_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2402_action_queue_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2402_action_queue_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2402_action_queue_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2402_action_queue_27"]),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2402_action_queue_27"),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2402_action_queue_29"),
	Jmp(["EVENT_2402_pause_1"]),
	ClearBit(TEMP_7043_0, identifier="EVENT_2402_clear_bit_31"),
	Jmp(["EVENT_2402_pause_1"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2402_pause_1"], identifier="EVENT_2402_jmp_if_bit_set_33"),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Jmp(["EVENT_2402_pause_1"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_2402_pause_1"], identifier="EVENT_2402_jmp_if_bit_set_38"),
	ClearBit(TEMP_7043_1),
	SetBit(TEMP_7043_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Jmp(["EVENT_2402_pause_1"]),
	SetBit(TEMP_7043_0, identifier="EVENT_2402_set_bit_43"),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_2402_action_queue_67"]),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_2402_action_queue_65"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_2402_action_queue_65"]),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_2402_action_queue_67"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2402_action_queue_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2402_action_queue_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2402_action_queue_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2402_action_queue_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2402_action_queue_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2402_action_queue_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2402_action_queue_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2402_action_queue_63"]),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	], identifier="EVENT_2402_action_queue_61"),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2402_action_queue_63"),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	], identifier="EVENT_2402_action_queue_65"),
	Jmp(["EVENT_2402_pause_1"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2402_action_queue_67"),
	Jmp(["EVENT_2402_pause_1"])
])
