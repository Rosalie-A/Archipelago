# E1107_TADPOLE_BRIDGE_JUMPING
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
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=12, y=51, height=0),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(1)
	], identifier="EVENT_1107_action_queue_0"),
	Jmp(["EVENT_1107_set_7000_to_object_coord_10"]),
	Set7000ToTappedButton(identifier="EVENT_1107_set_7000_to_tapped_button_2"),
	Pause(1),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1107_set_7000_to_pressed_button_6"]),
	Jmp(["EVENT_1107_set_7000_to_tapped_button_2"]),
	Set7000ToPressedButton(identifier="EVENT_1107_set_7000_to_pressed_button_6"),
	JmpIf7000AnyBitsSet(bits=[0, 3], destinations=["EVENT_1107_set_7000_to_object_coord_10"]),
	JmpIf7000AnyBitsSet(bits=[1, 2], destinations=["EVENT_1107_action_queue_14"]),
	Jmp(["EVENT_1107_action_queue_18"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True, identifier="EVENT_1107_set_7000_to_object_coord_10"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_1107_enable_controls_until_return_20"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(1),
		A_ReturnQueue()
	]),
	Jmp(["EVENT_1107_set_7000_to_tapped_button_2"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_ShadowOff(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkSouthwestSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_FaceSouthwest(),
		A_Pause(1),
		A_ShadowOn(),
		A_ReturnQueue()
	], identifier="EVENT_1107_action_queue_14"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_1105_action_queue_41"]),
	Jmp(["EVENT_1107_set_7000_to_tapped_button_2"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_JumpToHeight(80),
		A_Pause(24),
		A_ShadowOn()
	], identifier="EVENT_1107_action_queue_18"),
	Jmp(["EVENT_1107_set_7000_to_tapped_button_2"]),
	EnableControlsUntilReturn([], identifier="EVENT_1107_enable_controls_until_return_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(128),
		A_WalkNortheastSteps(3),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceNortheast(),
		A_WalkNortheastPixels(22),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ClearBit(TEMP_7043_1),
	Return()
])
