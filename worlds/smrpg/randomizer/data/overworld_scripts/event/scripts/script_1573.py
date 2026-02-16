# E1573_MIDAS_RIVER_BARREL_SUBROUTINE
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
	SetVarToConst(Z_COORD_2, 0),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_1573_copy_var_to_var_4"]),
	AddConstToVar(X_COORD_2, 1),
	AddConstToVar(Y_COORD_2, 2),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1573_copy_var_to_var_4"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	ResetCoords(MEM_70A8),
	SetSyncActionScript(MEM_70A8, A0595_MIDAS_BARREL_SLOW_ANIMATION),
	AddConstToVar(PRIMARY_TEMP_7000, 8),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	SetSyncActionScript(MEM_70A8, A0170_MIDAS_BARRELS_WATER_SPLASH),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	ResetCoords(MEM_70A8),
	ResetCoords(MARIO),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1573_set_action_script_19"]),
	SetSyncActionScript(MEM_70A8, A0596_MIDAS_BARREL_LEFT_LANE_TO_RIGHT),
	SetSyncActionScript(MARIO, A0596_MIDAS_BARREL_LEFT_LANE_TO_RIGHT),
	Jmp(["EVENT_1573_pause_21"]),
	SetSyncActionScript(MEM_70A8, A0594_MIDAS_BARREL_RIGHT_LANE_TO_LEFT, identifier="EVENT_1573_set_action_script_19"),
	SetSyncActionScript(MARIO, A0594_MIDAS_BARREL_RIGHT_LANE_TO_LEFT),
	Pause(5, identifier="EVENT_1573_pause_21"),
	SetBit(TEMP_7044_3),
	Return()
])
