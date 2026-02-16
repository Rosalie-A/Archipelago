# E1846_SAFE_DONUT_LIFT_JUMP
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1846_clear_bit_30"], identifier="EVENT_1846_jmp_if_bit_set_0"),
	EnableControls([B]),
	MoveScriptToBackgroundThread2(),
	SetBit(TEMP_7043_1),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
		A_UnknownCommand(bytearray(b'\xc8\x91')),
		A_SetWalkingSpeed(FAST),
		A_FloatingOff(),
		A_WalkTo70167018(),
		A_FloatingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	]),
	Set7000ToTappedButton(identifier="EVENT_1846_set_7000_to_tapped_button_7"),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1846_action_queue_21"]),
	JmpIfMarioInAir(["EVENT_1846_clear_bit_30"]),
	Set7000ToPressedButton(),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
	JmpIf7000AnyBitsSet(bits=[1, 3], destinations=["EVENT_1846_action_queue_17"]),
	CopyVarToVar(from_var=X_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AnyBitsSet(bits=[0, 2], destinations=["EVENT_1846_action_queue_19"]),
	Pause(1, identifier="EVENT_1846_pause_15"),
	Jmp(["EVENT_1846_set_7000_to_tapped_button_7"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	], identifier="EVENT_1846_action_queue_17"),
	Jmp(["EVENT_1846_pause_15"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	], identifier="EVENT_1846_action_queue_19"),
	Jmp(["EVENT_1846_pause_15"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(108)
	], identifier="EVENT_1846_action_queue_21"),
	StartLoopNTimes(11),
	Pause(1),
	Set7000ToPressedButton(),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
	JmpIf7000AnyBitsSet(bits=[1, 3], destinations=["EVENT_1846_copy_var_to_var_33"]),
	CopyVarToVar(from_var=X_COORD_1, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AnyBitsSet(bits=[0, 2], destinations=["EVENT_1846_action_queue_39"]),
	EndLoop(),
	ClearBit(TEMP_7043_1, identifier="EVENT_1846_clear_bit_30"),
	MoveScriptToMainThread(),
	Return(),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1846_copy_var_to_var_33"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_1846_action_queue_37"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	Jmp(["EVENT_1846_clear_bit_30"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthwestSteps(3),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_1846_action_queue_37"),
	Jmp(["EVENT_1846_clear_bit_30"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_1846_action_queue_39"),
	Jmp(["EVENT_1846_clear_bit_30"])
])
