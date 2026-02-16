# E2340_TOWER_SEESAW_CHEST_ROOM_LOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkSouthwestPixels(5)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownPixels(4),
		A_WalkSouthPixels(6),
		A_WalkNortheastPixels(8)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(9)
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	RunEventAsSubroutine(E0881_BOOSTER_PASS_SEESAW_CHEST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_2340_set_bit_8"]),
	FadeInFromBlack(sync=False),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_2340_set_bit_8"),
	RunBackgroundEvent(event_id=E2343_TOWER_SEESAW_ROOM_SET_ORIGIN, return_on_level_exit=True, bit_6=True),
	RunBackgroundEvent(event_id=E2358_TOWER_THWOMP_SEESAW_ROOM_LOADER_CONTD, return_on_level_exit=True, run_as_second_script=True),
	FadeInFromBlack(sync=False),
	Return()
])
