# E3333_VOLCANO_GENERIC_LOADER_2
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 50, identifier="EVENT_3333_set_var_to_const_0"),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Set7000ToCurrentLevel(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 361, ["EVENT_3333_jmp_if_var_not_equals_short_5"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetPriority(2),
		A_SetPriority(3)
	]),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 358, ["EVENT_3333_jmp_if_var_equals_const_7"], identifier="EVENT_3333_jmp_if_var_not_equals_short_5"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetPriority(2),
		A_SetPriority(3)
	]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 354, ["EVENT_3333_run_background_event_11"], identifier="EVENT_3333_jmp_if_var_equals_const_7"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_FaceEast7C(),
		A_Pause(1)
	]),
	RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
	Return(),
	RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True, identifier="EVENT_3333_run_background_event_11"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3333_ret_16"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3333_ret_16"]),
	RunEventAsSubroutine(E3913_VOLCANO_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3333_ret_16")
])
