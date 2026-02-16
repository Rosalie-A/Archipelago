# E3364_KEEP_LOGIC_GAME_LOADER
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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShiftXYPixels(x=250, y=253),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastSteps(5)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(2)
	]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	SetBit(TEMP_7044_7),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	SetVarToConst(TEMP_7026, 2),
	SetVarToConst(TEMP_7028, 3),
	SetVarToConst(TEMP_702A, 4),
	StartLoopNTimes(18),
	JmpIfRandom1of2(["EVENT_3364_jmp_if_random_above_66_20"]),
	JmpIfRandom2of3(['EVENT_3364_swap_vars_16', 'EVENT_3364_swap_vars_18']),
	SwapVars(TEMP_7026, SECONDARY_TEMP_7024),
	Jmp(["EVENT_3364_end_loop_26"]),
	SwapVars(TEMP_7028, SECONDARY_TEMP_7024, identifier="EVENT_3364_swap_vars_16"),
	Jmp(["EVENT_3364_end_loop_26"]),
	SwapVars(TEMP_702A, SECONDARY_TEMP_7024, identifier="EVENT_3364_swap_vars_18"),
	Jmp(["EVENT_3364_end_loop_26"]),
	JmpIfRandom2of3(['EVENT_3364_swap_vars_23', 'EVENT_3364_swap_vars_25'], identifier="EVENT_3364_jmp_if_random_above_66_20"),
	SwapVars(TEMP_7028, TEMP_7026),
	Jmp(["EVENT_3364_end_loop_26"]),
	SwapVars(TEMP_702A, TEMP_7026, identifier="EVENT_3364_swap_vars_23"),
	Jmp(["EVENT_3364_end_loop_26"]),
	SwapVars(TEMP_702A, TEMP_7028, identifier="EVENT_3364_swap_vars_25"),
	EndLoop(identifier="EVENT_3364_end_loop_26"),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	Return()
])
