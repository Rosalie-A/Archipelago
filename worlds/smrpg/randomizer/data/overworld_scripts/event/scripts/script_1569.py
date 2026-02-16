# E1569_MIDAS_RIVER_BARREL_SUBROUTINE
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
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_1569_set_var_to_const_5"]),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1569_set_var_to_const_5"]),
	Return(),
	SetVarToConst(TEMP_702C, 160, identifier="EVENT_1569_set_var_to_const_5"),
	Pause(1, identifier="EVENT_1569_pause_6"),
	Dec(TEMP_702C),
	JmpIfVarNotEqualsConst(TEMP_702C, 0, ["EVENT_1569_pause_6"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1569_set_var_to_const_13"]),
	SetSyncActionScript(NPC_0, A0597_MIDAS_FISH),
	SetSyncActionScript(NPC_11, A0167_SPAWN_AT_7016_701A_CALCULATED),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1569_ret_20"]),
	SetVarToConst(TEMP_702C, 80, identifier="EVENT_1569_set_var_to_const_13"),
	Pause(1, identifier="EVENT_1569_pause_14"),
	Dec(TEMP_702C),
	JmpIfVarNotEqualsConst(TEMP_702C, 0, ["EVENT_1569_pause_14"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1569_ret_20"]),
	SetSyncActionScript(NPC_0, A0597_MIDAS_FISH),
	SetSyncActionScript(NPC_11, A0167_SPAWN_AT_7016_701A_CALCULATED),
	Return(identifier="EVENT_1569_ret_20")
])
