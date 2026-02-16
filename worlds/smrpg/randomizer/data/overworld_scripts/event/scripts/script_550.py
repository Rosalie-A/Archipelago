# E0550_ROSE_TOWN_OCCUPIED_ARROW_CONTROL_3
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
	JmpIfBitSet(UNKNOWN_ROSE_TOWN_7060_0, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_256_ret_0"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	CompareVarToConst(TEMP_7026, 3),
	JmpIfComparisonResultIsLesser(["EVENT_550_set_bit_8"]),
	CompareVarToConst(TEMP_7026, 6),
	JmpIfComparisonResultIsLesser(["EVENT_256_ret_0"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_0, identifier="EVENT_550_set_bit_8"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_SetSolidityBits(cant_walk_through=True),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	]),
	SetSyncActionScript(NPC_7, A0638_ROSE_TOWN_ARROW),
	Return()
])
