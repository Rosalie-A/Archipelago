# E1084_MELODY_BAY_SONG_3_INPUT
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
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_0"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_5"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_0"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_0"], identifier="EVENT_1084_jmp_if_bit_clear_5"),
	SetSyncActionScript(NPC_0, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=7, y=41, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_1, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 21),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_18"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_23"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_18"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_18"], identifier="EVENT_1084_jmp_if_bit_clear_23"),
	SetSyncActionScript(NPC_1, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7026),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=8, y=39, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_2, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 22),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_36"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_41"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_36"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_36"], identifier="EVENT_1084_jmp_if_bit_clear_41"),
	SetSyncActionScript(NPC_2, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7028),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=9, y=37, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_3, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 23),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_54"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_59"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_54"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_54"], identifier="EVENT_1084_jmp_if_bit_clear_59"),
	SetSyncActionScript(NPC_3, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702A),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=10, y=35, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_4, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 24),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_72"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_77"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_72"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_72"], identifier="EVENT_1084_jmp_if_bit_clear_77"),
	SetSyncActionScript(NPC_4, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702C),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=11, y=33, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_5, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 25),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_90"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_95"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_90"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_90"], identifier="EVENT_1084_jmp_if_bit_clear_95"),
	SetSyncActionScript(NPC_5, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702E),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=12, y=31, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_6, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 26),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_108"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_113"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_108"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_108"], identifier="EVENT_1084_jmp_if_bit_clear_113"),
	SetSyncActionScript(NPC_6, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7030),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=13, y=29, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_7, A0570_MELODY_BAY_TADPOLE_SWIMS),
	SetVarToConst(TEMP_70A9, 27),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_126"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_131"]),
	Jmp(["EVENT_1084_set_7000_to_tapped_button_126"]),
	JmpIfBitClear(TEMP_7044_3, ["EVENT_1084_set_7000_to_tapped_button_126"], identifier="EVENT_1084_jmp_if_bit_clear_131"),
	SetSyncActionScript(NPC_7, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	PauseActionScript(MARIO),
	CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7032),
	CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
	Pause(10),
	SetVarToConst(Y_COORD_1, 3),
	CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
	DecVarFrom7000(X_COORD_1),
	JmpToSubroutine(["EVENT_1084_jmp_if_var_equals_const_147"]),
	Jmp(["EVENT_1074_set_bit_0"]),
	Return(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1084_pause_action_script_160"], identifier="EVENT_1084_jmp_if_var_equals_const_147"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1084_pause_action_script_163"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1084_pause_action_script_166"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1084_pause_action_script_169"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1084_pause_action_script_172"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1084_pause_action_script_175"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1084_pause_action_script_178"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65535, ["EVENT_1084_pause_action_script_181"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65534, ["EVENT_1084_pause_action_script_184"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65533, ["EVENT_1084_pause_action_script_187"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65532, ["EVENT_1084_pause_action_script_190"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65531, ["EVENT_1084_pause_action_script_193"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65530, ["EVENT_1084_pause_action_script_196"]),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_160"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=64, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\x00\xff')),
		A_Pause(16),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_163"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=64, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x01\x80\xfe')),
		A_Pause(16),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_166"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x00\xab\xfe')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_169"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$V\xffV\xfe')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_172"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\xab\xfe\x00\xfe')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_175"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\xfe@\xfe')),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_178"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xfe\x00\xfe')),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_181"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\xab\xff')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_184"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\xaa\x02\x00\x00')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_187"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$U\x03U\x00')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_190"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x04\xaa\x00')),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_193"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\x03\xc0\x00')),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_196"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x04\x00\x01')),
		A_Pause(32),
		A_BPL262728()
	]),
	Return()
])
