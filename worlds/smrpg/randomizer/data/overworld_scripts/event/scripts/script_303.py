# E0303_MUSHROOM_KINGDOM_JUMPING_KID
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
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_303_start_embedded_action_script_1_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_303_start_embedded_action_script_1_SUBSCRIPT_pause_2"])
	]),
	RunDialog(dialog_id=DI0541_JUMPING_KID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_303_run_event_as_subroutine_11"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
	RunDialog(dialog_id=DI0545_YEAH, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Return(),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_303_run_event_as_subroutine_11"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_FaceMario(),
		A_Set700CToObjectCoord(target_npc=NPC_0, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 4),
		A_Mem700CAndConst(0x0007),
		A_FixedFCoordOff(),
		A_FaceEast7C()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_303_action_queue_15_SUBSCRIPT_pause_1"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_303_action_queue_15_SUBSCRIPT_pause_1"])
	]),
	SetSyncActionScript(NPC_0, A0015_DO_NOTHING),
	RunDialog(dialog_id=DI0546_THANKS_A_BUNCH, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Return()
])
