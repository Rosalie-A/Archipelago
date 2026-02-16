# E0455_RESUMMON_PIPE_VAULT_ENEMIES
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
	ClearBit(TEMP_707C_0),
	SummonObjectToSpecificLevel(NPC_0, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_3, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_3, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_1, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_2, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_3, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_0, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_1, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_2, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_0, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
	SummonObjectToSpecificLevel(NPC_1, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
	SummonObjectToSpecificLevel(NPC_12, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS),
	SummonObjectToSpecificLevel(NPC_13, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_455_set_var_to_const_40"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 20),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkEastPixels(11),
		A_WalkNortheastPixels(4),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
    SummonObjectToSpecificLevel(NPC_0, R055_PIPE_VAULT_ENTRANCE),
	SummonObjectToSpecificLevel(NPC_1, R055_PIPE_VAULT_ENTRANCE),
	JmpIfBitSet(PIPE_VAULT_GATED, ["EVENT_455_fade_in_from_black_async_29"]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromSpecificLevel(NPC_1, R055_PIPE_VAULT_ENTRANCE),
	RemoveObjectFromSpecificLevel(NPC_0, R055_PIPE_VAULT_ENTRANCE),
	FadeInFromBlack(sync=False, identifier="EVENT_455_fade_in_from_black_async_29"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_455_ret_34"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_455_ret_34"]),
	RunEventAsSubroutine(E3900_PIPE_VAULT_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_455_ret_34"),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_455_run_event_as_subroutine_35"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_455_ret_39"]),
	RunEventAsSubroutine(E3901_YOSTER_ISLE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_455_ret_39"),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 52, identifier="EVENT_455_set_var_to_const_40"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_455_run_event_as_subroutine_35"]),
	FadeInFromBlack(sync=False),
	Return()
])
