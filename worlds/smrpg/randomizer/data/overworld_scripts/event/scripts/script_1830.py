# E1830_KEEP_HANDLE_ROOM_RELOAD_AFTER_LAVA_FALL
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
	EnableControlsUntilReturn([]),
	Pause(1),
	FreezeAllNPCsUntilReturn(),
	Pause(1),
	SetSyncActionScript(MARIO, A0775_PLAYER_FALLS_IN_KEEP_LAVA),
	SetSyncActionScript(NPC_0, A0775_PLAYER_FALLS_IN_KEEP_LAVA),
	Pause(1, identifier="EVENT_1830_pause_6"),
	JmpIfMarioInAir(["EVENT_1830_pause_6"]),
	PauseActionScript(MARIO),
	ResetCoords(MARIO),
	StoreCoinCountTo7000(identifier="EVENT_1830_store_coin_amount_7000_10"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1830_stop_embedded_action_script_23"]),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_700C, 5),
	StartLoopNTimes(7),
	StoreCoinCountTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1830_pause_20"]),
	CreatePacketAtObjectCoords(packet=P017_SMALL_MINIGAME_COIN, target_npc=MARIO, destinations=["EVENT_1830_pause_20"]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Dec7000FromCoins(),
	Pause(1, identifier="EVENT_1830_pause_20"),
	Inc(PRIMARY_TEMP_700C),
	EndLoop(),
	StopEmbeddedActionScript(MARIO, identifier="EVENT_1830_stop_embedded_action_script_23"),
	Dec(KEEP_DOOR_LIVES),
	JmpIfVarEqualsConst(KEEP_DOOR_LIVES, 0, ["EVENT_1864_slow_down_music_6"]),
	FadeOutToBlack(sync=False, duration=40),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 321, ["EVENT_1830_enter_area_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_1830_enter_area_52"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_1830_copy_var_to_var_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_1830_enter_area_54"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_1830_enter_area_62"]),
	EnterArea(room_id=R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, face_direction=NORTHEAST, x=22, y=123, z=0),
	JmpToEvent(E1836_KEEP_DONKEY_ROOM_LOADER),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1830_copy_var_to_var_35"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_X, pixel=True, bit_7=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_Y, pixel=True, bit_7=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7030),
	EnterArea(room_id=R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS, face_direction=NORTHEAST, x=6, y=47, z=1),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1825_KEEP_ROTATING_ROOM_LOADER),
	EnterArea(room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, face_direction=NORTHEAST, x=4, y=62, z=7, identifier="EVENT_1830_enter_area_44"),
	JmpToSubroutine(["EVENT_1830_pause_70"]),
	SetBit(UNKNOWN_PAN),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(UNKNOWN_PAN),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1824_KEEP_SET_PLATFORM_PROPERTIES),
	EnterArea(room_id=R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, face_direction=NORTHEAST, x=2, y=57, z=0, identifier="EVENT_1830_enter_area_52"),
	JmpToEvent(E1835_KEEP_CANNONBALL_ROOM_LOADER),
	EnterArea(room_id=R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, face_direction=NORTHEAST, x=8, y=115, z=2, identifier="EVENT_1830_enter_area_54"),
	JmpToSubroutine(["EVENT_1830_pause_70"]),
	SetBit(UNKNOWN_PAN),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(UNKNOWN_PAN),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER),
	EnterArea(room_id=R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, face_direction=NORTHEAST, x=10, y=122, z=5, identifier="EVENT_1830_enter_area_62"),
	JmpToSubroutine(["EVENT_1830_pause_70"]),
	SetBit(UNKNOWN_PAN),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(UNKNOWN_PAN),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER),
	Pause(4, identifier="EVENT_1830_pause_70"),
	FreezeAllNPCsUntilReturn(),
	JmpIfBitSet(TEMP_7095_4, ["EVENT_1830_pause_75"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SwapVars(X_COORD_2, ROSE_WAY_7038),
		A_SwapVars(Y_COORD_2, ROSE_WAY_703A),
		A_SwapVars(Z_COORD_2, ROSE_WAY_703C),
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	Jmp(["EVENT_1830_ret_81"]),
	Pause(1, identifier="EVENT_1830_pause_75"),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	Set7016701BToObjectXYZ(target=MEM_70A8),
	AddConstToVar(Z_COORD_2, 320),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\x99')),
		A_Pause(1, identifier="EVENT_1830_action_queue_80_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_1830_action_queue_80_SUBSCRIPT_pause_1"])
	]),
	Return(identifier="EVENT_1830_ret_81")
])
