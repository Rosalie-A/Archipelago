# E0277_UNKNOWN
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
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7032),
	JmpIf7000AnyBitsSet(bits=[0], destinations=["EVENT_277_jmp_if_var_equals_const_4"]),
	Jmp(["EVENT_277_action_queue_8"]),
	JmpIfVarEqualsConst(TEMP_7032, 1, ["EVENT_277_action_queue_14"], identifier="EVENT_277_jmp_if_var_equals_const_4"),
	JmpIfVarEqualsConst(TEMP_7032, 3, ["EVENT_277_action_queue_16"]),
	JmpIfVarEqualsConst(TEMP_7032, 5, ["EVENT_277_action_queue_18"]),
	JmpIfVarEqualsConst(TEMP_7032, 7, ["EVENT_277_action_queue_20"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x00\x10')),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=PRIMARY_TEMP_7000)
	], identifier="EVENT_277_action_queue_8"),
	Mem7000AndConst(0x00C0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_277_action_queue_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_277_action_queue_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_277_action_queue_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_277_action_queue_20"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_EndLoop()
	], identifier="EVENT_277_action_queue_14"),
	Jmp(["EVENT_277_action_queue_21"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True),
		A_Pause(5),
		A_EndLoop()
	], identifier="EVENT_277_action_queue_16"),
	Jmp(["EVENT_277_action_queue_21"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True),
		A_Pause(5),
		A_EndLoop()
	], identifier="EVENT_277_action_queue_18"),
	Jmp(["EVENT_277_action_queue_21"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_EndLoop()
	], identifier="EVENT_277_action_queue_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	], identifier="EVENT_277_action_queue_21"),
	ClearBit(TEMP_7044_7),
	Return()
])
