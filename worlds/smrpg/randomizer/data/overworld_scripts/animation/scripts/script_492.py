#A0492_MUSHROOM_WAY_BOSS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=6, destinations=["ACTION_492_set_bit_3"], identifier="ACTION_492_jmp_if_object_within_range_0"),
	A_Pause(1),
	A_Jmp(["ACTION_492_jmp_if_object_within_range_0"]),
	A_SetBit(TEMP_7044_6, identifier="ACTION_492_set_bit_3"),
	A_ReturnQueue()
])
