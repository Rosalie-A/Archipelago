# E1564_LANDS_END_CANNON_CONTD
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
    JmpIfBitSet(LANDS_END_GATED, ["EVENT_1564_return_0"]),
	SetBit(TEMP_7044_4),
	Set7016701BToObjectXYZ(target=MEM_70A8, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_WalkTo70167018(),
		A_FaceSouth(),
		A_FloatingOn(),
		A_Pause(6)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(2),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthPixels(12)
	]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
		A_ShiftZDownPixels(4),
		A_VisibilityOff(),
		A_ShiftZDownPixels(12)
	]),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1564_set_action_script_10"]),
	SetSyncActionScript(MEM_70A8, A0782_LANDS_END_CANNON_WHILE_PLAYER_OCCUPIED),
	Jmp(["EVENT_1564_pause_11"]),
	SetSyncActionScript(MEM_70A8, A0783_LANDS_END_CANNON_WHILE_PLAYER_OCCUPIED, identifier="EVENT_1564_set_action_script_10"),
	Pause(1, identifier="EVENT_1564_pause_11"),
	Pause(1, identifier="EVENT_1564_pause_12"),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_1564_pause_12"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	VarShiftLeft(PRIMARY_TEMP_7000, 8),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x00FF),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1564_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1564_action_queue_32"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1564_action_queue_35"]),
	ClearBit(TEMP_7044_4),
	StopSound(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast7C(),
		A_FloatingOff(),
		A_JumpToHeight(height=192, silent=True),
		A_SetVarToConst(TEMP_7034, 61166),
		A_CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=MARIO, destinations=["EVENT_1564_action_queue_26_SUBSCRIPT_set_animation_speed_5"]),
		A_SetWalkingSpeed(NORMAL, identifier="EVENT_1564_action_queue_26_SUBSCRIPT_set_animation_speed_5"),
		A_Pause(2),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_FloatingOn(),
		A_VisibilityOn()
	]),
	MoveScriptToBackgroundThread2(),
	Jmp(["EVENT_1564_action_queue_44"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast7C(),
		A_SetWalkingSpeed(NORMAL),
		A_FloatingOff(),
		A_JumpToHeight(height=192, silent=True)
	], identifier="EVENT_1564_action_queue_29"),
	SetVarToConst(TEMP_7030, 1),
	Jmp(["EVENT_1564_clear_bit_37"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast7C(),
		A_SetWalkingSpeed(FAST),
		A_FloatingOff(),
		A_JumpToHeight(height=192, silent=True)
	], identifier="EVENT_1564_action_queue_32"),
	SetVarToConst(TEMP_7030, 2),
	Jmp(["EVENT_1564_clear_bit_37"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast7C(),
		A_SetWalkingSpeed(VERY_FAST),
		A_FloatingOff(),
		A_JumpToHeight(height=192, silent=True)
	], identifier="EVENT_1564_action_queue_35"),
	SetVarToConst(TEMP_7030, 4),
	ClearBit(TEMP_7044_4, identifier="EVENT_1564_clear_bit_37"),
	StopSound(),
	SetVarToConst(TEMP_7034, 61166),
	CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=MARIO, destinations=["EVENT_1564_pause_41"]),
	Pause(2, identifier="EVENT_1564_pause_41"),
	MoveScriptToBackgroundThread2(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_FloatingOn(),
		A_CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_700C, identifier="EVENT_1564_action_queue_43_SUBSCRIPT_copy_var_to_var_2"),
		A_WalkFDirection16Pixels(),
		A_VisibilityOn(),
		A_JmpIfMarioInAir(["EVENT_1564_action_queue_43_SUBSCRIPT_copy_var_to_var_2"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_1564_action_queue_44"),
	ClearBit(TEMP_7043_0),
	MoveScriptToMainThread(),
	Return(identifier="EVENT_1564_return_0")
])
