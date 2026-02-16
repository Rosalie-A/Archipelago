# E3362_KEEP_BUTTON_GAME_PRESS_BUTTON
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
	DisableObjectTrigger(MEM_70A8),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=ROSE_WAY_703C),
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3362_copy_var_to_var_18"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3362_copy_var_to_var_22"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3362_copy_var_to_var_26"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3362_copy_var_to_var_30"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 25, ["EVENT_3362_copy_var_to_var_34"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 26, ["EVENT_3362_copy_var_to_var_38"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 27, ["EVENT_3362_copy_var_to_var_42"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 28, ["EVENT_3362_copy_var_to_var_46"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3362_copy_var_to_var_50"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 30, ["EVENT_3362_copy_var_to_var_54"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3362_copy_var_to_var_58"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 32, ["EVENT_3362_copy_var_to_var_62"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 33, ["EVENT_3362_copy_var_to_var_66"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 34, ["EVENT_3362_copy_var_to_var_70"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 35, ["EVENT_3362_copy_var_to_var_74"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 36, ["EVENT_3362_copy_var_to_var_78"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_18"),
	Mem7000XorConst(0x0013),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_22"),
	Mem7000XorConst(0x0027),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_26"),
	Mem7000XorConst(0x004E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_30"),
	Mem7000XorConst(0x008C),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_34"),
	Mem7000XorConst(0x0131),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_38"),
	Mem7000XorConst(0x0272),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_42"),
	Mem7000XorConst(0x04E4),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_46"),
	Mem7000XorConst(0x08C8),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_50"),
	Mem7000XorConst(0x1310),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_54"),
	Mem7000XorConst(0x2720),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_58"),
	Mem7000XorConst(0x4E40),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_62"),
	Mem7000XorConst(0x8C80),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_66"),
	Mem7000XorConst(0x3100),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_70"),
	Mem7000XorConst(0x7200),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_74"),
	Mem7000XorConst(0xE400),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3362_copy_var_to_var_78"),
	Mem7000XorConst(0xC800),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	Jmp(["EVENT_3362_set_var_to_const_82"]),
	SetVarToConst(TEMP_70A9, 21, identifier="EVENT_3362_set_var_to_const_82"),
	StartLoopNTimes(15),
	SetSyncActionScript(MEM_70A9, A0281_KEEP_TOPPER_GAME_SET_BUTTON_OR_BALL_STATE),
	Inc(TEMP_70A9),
	EndLoop(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftZDownPixels(8),
		A_JumpToHeight(height=0, silent=True),
		A_ResetProperties(),
		A_Pause(1)
	]),
	JmpIfVarNotEqualsConst(ROSE_WAY_703E, 65535, ["EVENT_3362_ret_101"]),
	Pause(8),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOn()
	]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
	Pause(16),
	PlayMusicAtDefaultVolume(M0009_VICTORY),
	SetBit(TEMP_7044_7),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, mod_id=0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	Return(identifier="EVENT_3362_ret_101")
])
