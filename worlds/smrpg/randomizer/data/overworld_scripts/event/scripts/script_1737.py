# E1737_SKY_BRIDGE_DONUT_LIFT
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
	JmpIfMarioOnAnObjectOrNot(['EVENT_1737_jmp_if_bit_set_4', 'EVENT_1737_ret_3']),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_1737_ret_3"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_JumpToHeight(153),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(20),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_WalkSoutheastPixels(50),
		A_SetWalkingSpeed(FAST)
	]),
	Return(identifier="EVENT_1737_ret_3"),
	JmpIfBitSet(SKY_BRIDGE_COURSE_CHOICE, ["EVENT_1846_jmp_if_bit_set_0"], identifier="EVENT_1737_jmp_if_bit_set_4"),
	Return()
])
