# E1071_BEGIN_MELODY_BAY_TADPOLES
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
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(NORMAL),
		A_WalkToXYCoords(x=7, y=48),
		A_WalkNortheastPixels(3),
		A_WalkNorthwestPixels(2),
		A_FaceNortheast(),
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetPriority(3),
		A_SetVRAMPriority(PRIORITY_3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_BounceToXYWithHeight(x=4, y=32, height=0)
	]),
	FreezeCamera(),
	JmpIfBitClear(TEMP_7044_2, ["EVENT_1071_set_var_to_const_32"]),
	JmpIfBitSet(TOADOFSKY_REMOVED, ["EVENT_1071_jmp_if_bit_clear_8"]),
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1071_jmp_if_bit_clear_8"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShiftToXYCoords(x=14, y=25),
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestPixels(6),
		A_SequenceLoopingOn()
	]),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_1071_jmp_if_bit_clear_11"], identifier="EVENT_1071_jmp_if_bit_clear_8"),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_1071_jmp_if_bit_clear_14"], identifier="EVENT_1071_jmp_if_bit_clear_11"),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_1071_jmp_if_bit_clear_17"], identifier="EVENT_1071_jmp_if_bit_clear_14"),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_1071_jmp_if_bit_clear_20"], identifier="EVENT_1071_jmp_if_bit_clear_17"),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_1071_jmp_if_bit_clear_23"], identifier="EVENT_1071_jmp_if_bit_clear_20"),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_1071_jmp_if_bit_clear_26"], identifier="EVENT_1071_jmp_if_bit_clear_23"),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_1071_jmp_if_bit_clear_29"], identifier="EVENT_1071_jmp_if_bit_clear_26"),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_1071_set_var_to_const_32"], identifier="EVENT_1071_jmp_if_bit_clear_29"),
	SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	Pause(10),
	SetVarToConst(X_COORD_1, 3, identifier="EVENT_1071_set_var_to_const_32"),
	SetVarToConst(TEMP_70A9, 20),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=43, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_0, A0570_MELODY_BAY_TADPOLE_SWIMS),
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1071_jmp_to_event_45"]),
	JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1071_jmp_if_bit_clear_43"]),
	JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1071_jmp_if_bit_clear_41"]),
	JmpToEvent(E1082_MELODY_BAY_SONG_1_INPUT),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1071_jmp_to_event_45"], identifier="EVENT_1071_jmp_if_bit_clear_41"),
	JmpToEvent(E1083_MELODY_BAY_SONG_2_INPUT),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1071_jmp_to_event_45"], identifier="EVENT_1071_jmp_if_bit_clear_43"),
	JmpToEvent(E1084_MELODY_BAY_SONG_3_INPUT),
	JmpToEvent(E1073_MELODY_BAY_JUMP_ON_TADPOLES, identifier="EVENT_1071_jmp_to_event_45"),
	Return()
])
