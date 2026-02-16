#A0943_BLUE_FIRE_TRAIL
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 395, ["ACTION_943_set_sprite_sequence_23"]),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_943_set_sprite_sequence_4"]),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="ACTION_943_set_sprite_sequence_4"),
	A_JmpIfRandom1of2(["ACTION_943_shift_xy_pixels_9"]),
	A_JmpIfRandom1of2(["ACTION_943_jmp_if_random_above_128_11"]),
	A_ShiftXYPixels(x=252, y=2),
	A_Jmp(["ACTION_943_pause_15"]),
	A_ShiftXYPixels(x=4, y=2, identifier="ACTION_943_shift_xy_pixels_9"),
	A_Jmp(["ACTION_943_pause_15"]),
	A_JmpIfRandom1of2(["ACTION_943_shift_xy_pixels_14"], identifier="ACTION_943_jmp_if_random_above_128_11"),
	A_ShiftXYPixels(x=4, y=254),
	A_Jmp(["ACTION_943_pause_15"]),
	A_ShiftXYPixels(x=252, y=254, identifier="ACTION_943_shift_xy_pixels_14"),
	A_Pause(6, identifier="ACTION_943_pause_15"),
	A_JmpIfBitSet(TEMP_7044_4, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=MARIO, destinations=["ACTION_943_pause_18"]),
	A_Pause(6, identifier="ACTION_943_pause_18"),
	A_JmpIfBitSet(TEMP_7044_4, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=MARIO, destinations=["ACTION_943_visibility_off_21"]),
	A_VisibilityOff(identifier="ACTION_943_visibility_off_21"),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, identifier="ACTION_943_set_sprite_sequence_23"),
	A_Inc(TEMP_70AE),
	A_JmpIfVarEqualsConst(TEMP_70AE, 1, ["ACTION_943_pause_28"]),
	A_JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_943_pause_36"]),
	A_JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_943_set_var_to_const_44"]),
	A_Pause(6, identifier="ACTION_943_pause_28"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_2, destinations=["ACTION_943_pause_31"]),
	A_Pause(6, identifier="ACTION_943_pause_31"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_2, destinations=["ACTION_943_visibility_off_34"]),
	A_VisibilityOff(identifier="ACTION_943_visibility_off_34"),
	A_ReturnQueue(),
	A_Pause(6, identifier="ACTION_943_pause_36"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_3, destinations=["ACTION_943_pause_39"]),
	A_Pause(6, identifier="ACTION_943_pause_39"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_3, destinations=["ACTION_943_visibility_off_42"]),
	A_VisibilityOff(identifier="ACTION_943_visibility_off_42"),
	A_ReturnQueue(),
	A_SetVarToConst(TEMP_70AE, 0, identifier="ACTION_943_set_var_to_const_44"),
	A_Pause(6),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_4, destinations=["ACTION_943_pause_48"]),
	A_Pause(6, identifier="ACTION_943_pause_48"),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_4, destinations=["ACTION_943_visibility_off_51"]),
	A_VisibilityOff(identifier="ACTION_943_visibility_off_51"),
	A_ReturnQueue()
])
