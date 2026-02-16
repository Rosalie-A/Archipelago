# E3334_VOLCANO_ENTER_SHOP_AREA
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
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0]),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 387, ["EVENT_3334_action_queue_6"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_WalkToXYCoords(x=14, y=102),
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	]),
	EnterArea(room_id=R353_VOLCANO_AREA_18_HINO_MART, face_direction=NORTHEAST, x=1, y=61, z=0, show_banner=True, run_entrance_event=True),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_WalkToXYCoords(x=3, y=17),
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	], identifier="EVENT_3334_action_queue_6"),
	EnterArea(room_id=R353_VOLCANO_AREA_18_HINO_MART, face_direction=NORTHEAST, x=6, y=71, z=0, show_banner=True, run_entrance_event=True),
	Return()
])
