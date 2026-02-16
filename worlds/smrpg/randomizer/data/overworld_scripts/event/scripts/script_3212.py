# E3212_SHIP_3D_MAZE_FORFEIT_LISTENER
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
	PauseActionScript(NPC_2, identifier="EVENT_3212_pause_action_script_0"),
	RemoveObjectFromCurrentLevel(NPC_2),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Pause(1),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[4], destinations=["EVENT_3212_pause_action_script_0"]),
	EnableControlsUntilReturn([]),
	SetSyncActionScript(NPC_2, A0351_OERLIKONS_AND_3D_MAZE),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_SetVRAMPriority(PRIORITY_3)
	]),
	Pause(1, identifier="EVENT_3212_pause_10"),
	JmpIfMarioInAir(["EVENT_3212_pause_10"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	VarShiftLeft(UNKNOWN_7006, 1),
	CloseDialog(),
	RunDialog(dialog_id=DI1658_3D_MAZE_GIVE_UP_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3212_pause_action_script_19"]),
	RunDialog(dialog_id=DI1657_3D_MAZE_OVERLAY, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	Jmp(["EVENT_3212_pause_action_script_0"]),
	PauseActionScript(NPC_2, identifier="EVENT_3212_pause_action_script_19"),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueSync(target=MARIO, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	EnterArea(room_id=R168_SUNKEN_SHIP_PUZZLE_ROOM_3, face_direction=NORTHWEST, x=31, y=116, z=0, run_entrance_event=True),
	Return()
])
