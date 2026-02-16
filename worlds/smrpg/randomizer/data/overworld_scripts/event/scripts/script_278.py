# E0278_UNKNOWN
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
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_278_action_queue_0_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(MEM_70A9, ["EVENT_278_action_queue_0_SUBSCRIPT_pause_3"]),
		A_CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_700C),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_278_ret_1"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Return(identifier="EVENT_278_ret_1")
])
