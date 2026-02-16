# E1106_TADPOLE_BRIDGE_SUMMON
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1106_ret_56"]),
	SetBit(TEMP_7043_1),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_BounceToXYWithHeight(x=22, y=32, height=4),
		A_Pause(1),
		A_FaceSouthwest(),
		A_Pause(1),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=12, y=47),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=15, y=49),
		A_WalkNortheastPixels(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=14, y=43),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=17, y=45),
		A_WalkNortheastPixels(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=16, y=39),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=19, y=41),
		A_WalkNortheastPixels(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=18, y=35),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=21, y=37),
		A_WalkNortheastPixels(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	SetSyncActionScript(NPC_7, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_6, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_5, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_4, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_3, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_2, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_1, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_0, A0091_BRIDGE_TADPOLE),
	Pause(5),
	Set7000ToTappedButton(identifier="EVENT_1106_set_7000_to_tapped_button_28"),
	Pause(1),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1106_set_7000_to_pressed_button_33"]),
	JmpIf7000AnyBitsSet(bits=[0, 3], destinations=["EVENT_1106_action_queue_36"]),
	Jmp(["EVENT_1106_set_7000_to_tapped_button_28"]),
	Set7000ToPressedButton(identifier="EVENT_1106_set_7000_to_pressed_button_33"),
	JmpIf7000AnyBitsSet(bits=[1, 2], destinations=["EVENT_1106_action_queue_57"]),
	Jmp(["EVENT_1106_set_7000_to_tapped_button_28"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceNortheast(),
		A_WalkNortheastPixels(22),
		A_ReturnQueue()
	], identifier="EVENT_1106_action_queue_36"),
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
	Return(identifier="EVENT_1106_ret_56"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(96),
		A_WalkSouthwestSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestSteps(1),
		A_Pause(1),
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_1106_action_queue_57"),
	Jmp(["EVENT_1107_set_7000_to_tapped_button_2"])
])
