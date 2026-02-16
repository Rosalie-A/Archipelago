# E1680_TEMPLE_PIPE_TO_FORTUNE_RESULT_ROOM
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
	SetVarToConst(X_COORD_2, 5194),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	SetVarToConst(TEMP_70AC, 0),
	ClearBit(BELOME_HEAD_1),
	ClearBit(BELOME_HEAD_2),
	ClearBit(BELOME_HEAD_3),
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1680_enter_area_8"]),
	SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
	EnterArea(room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, face_direction=SOUTH, x=4, y=83, z=9, identifier="EVENT_1680_enter_area_8"),
	JmpIfBitClear(HAS_A_PRIZE_FORTUNE, ["EVENT_1680_action_queue_12"]),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	], identifier="EVENT_1680_action_queue_12"),
	JmpToEvent(E1770_TEMPLE_FORTUNE_RESULTS_ROOM_LOADER)
])
