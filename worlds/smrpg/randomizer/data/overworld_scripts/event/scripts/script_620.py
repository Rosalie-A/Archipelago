# E0620_REAL_BELLHOP_BLOCKS_EXIT_2
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
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_620_jmp_if_bit_set_5"]),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_620_jmp_if_bit_set_5"]),
	Return(),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_256_ret_0"], identifier="EVENT_620_jmp_if_bit_set_5"),
	SetBit(TEMP_7043_4),
	ClearBit(TEMP_7043_3),
	Set7000ToObjectCoord(target_npc=NPC_5, coord=COORD_Y, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_256_ret_0"]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest()
	]),
	Return()
])
