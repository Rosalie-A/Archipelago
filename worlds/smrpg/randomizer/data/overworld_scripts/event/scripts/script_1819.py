# E1819_SHY_AWAY_EARLY_LANDS_END
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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1819_ret_13"]),
	SetBit(TEMP_7043_0),
	Pause(1, identifier="EVENT_1819_pause_2"),
	JmpIfMarioInAir(["EVENT_1819_pause_2"]),
	JmpIfBitSet(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_1819_ret_13"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 48),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1819_ret_13"]),
	ResetCoords(NPC_3),
	SetAsyncActionScript(NPC_3, A0160_SEQUENCE_LOOPING_ON),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=28, y=37),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI1277_DEAD_END_SHY_AWAY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_3, A0714_LANDS_END_SLOW_RANDOM_MOVING_ENEMIES),
	Return(identifier="EVENT_1819_ret_13")
])
