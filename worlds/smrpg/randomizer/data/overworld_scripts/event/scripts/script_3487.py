# E3487_MIDAS_RIVER_FROG_COIN
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
	SetSyncActionScript(MEM_70A8, A0719_MIDAS_RIVER_FROG_COIN),
	AddFrogCoins(1),
	Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_Y, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 12288),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_16"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 8704),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_14"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 5120),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_12"]),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_4),
	Return(),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_5, identifier="EVENT_3487_set_bit_12"),
	Return(),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_6, identifier="EVENT_3487_set_bit_14"),
	Return(),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_7, identifier="EVENT_3487_set_bit_16"),
	Return()
])
