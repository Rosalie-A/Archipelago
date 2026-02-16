# E3778_BALL_SOLITAIRE_SET_PUZZLE
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
	SetVarToConst(ROSE_WAY_703E, 16),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShiftXYPixels(x=250, y=253),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(9)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, looping=False),
		A_Pause(38)
	]),
	RunEventAsSubroutine(E3884_BALL_SOLITAIRE_SET_PUZZLE_CONFIGURATION_VALUE),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_8"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[1], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_10"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_8"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_12"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_10"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[3], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_14"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_12"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[4], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_16"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_14"),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[5], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_18"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_16"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[6], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_20"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_18"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_22"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_20"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[8], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_24"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_22"),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[9], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_26"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_24"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[10], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_28"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_26"),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[11], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_30"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_28"),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[12], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_32"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_30"),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[13], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_34"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_32"),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[14], destinations=["EVENT_3778_jmp_if_7000_any_bits_set_36"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_34"),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	JmpIf7000AnyBitsSet(bits=[15], destinations=["EVENT_3778_action_queue_38"], identifier="EVENT_3778_jmp_if_7000_any_bits_set_36"),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_Dec(ROSE_WAY_703E),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthwestSteps(9)
	], identifier="EVENT_3778_action_queue_38"),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	Return()
])
