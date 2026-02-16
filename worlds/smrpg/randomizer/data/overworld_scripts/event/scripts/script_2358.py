# E2358_TOWER_THWOMP_SEESAW_ROOM_LOADER_CONTD
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
	Pause(1, identifier="EVENT_2358_pause_0"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2358_clear_bit_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2358_set_7000_to_object_coord_5"]),
	Jmp(["EVENT_2358_pause_0"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True, identifier="EVENT_2358_set_7000_to_object_coord_5"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 18, ["EVENT_2358_set_7000_to_object_coord_9"]),
	ClearBit(TEMP_7043_1),
	Return(),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True, identifier="EVENT_2358_set_7000_to_object_coord_9"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_2358_pause_0"]),
	ClearBit(TEMP_7043_1, identifier="EVENT_2358_clear_bit_11"),
	Return()
])
