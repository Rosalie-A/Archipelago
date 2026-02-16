# E1828_KEEP_MARIO_FALLS_IN_LAVA
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
	Pause(1, identifier="EVENT_1828_pause_0"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1828_db_10"]),
	JmpIfMarioInAir(["EVENT_1828_pause_0"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703C),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_7038),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	Jmp(["EVENT_1828_pause_0"]),
	UnknownCommand(bytearray(b'\xfdD'), identifier="EVENT_1828_db_10"),
	UnknownCommand(bytearray(b'\xfdG')),
	RunEventAtReturn(E1830_KEEP_HANDLE_ROOM_RELOAD_AFTER_LAVA_FALL),
	Return()
])
