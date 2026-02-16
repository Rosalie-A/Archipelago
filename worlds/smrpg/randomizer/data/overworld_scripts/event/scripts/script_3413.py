# E3413_MINES_SHYGUY_COLLIDE_WITH_BOXES
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
	Pause(1, identifier="EVENT_3413_pause_0"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3413_action_queue_5"]),
	Jmp(["EVENT_3413_pause_0"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_TransferToObjectXY(NPC_0),
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(height=80, silent=True),
		A_WalkSouthSteps(2),
		A_JumpToHeight(height=32, silent=True),
		A_WalkSouthPixels(3),
		A_JumpToHeight(height=8, silent=True),
		A_WalkSouthPixels(1),
		A_Pause(20),
		A_SetSolidityBits(cant_jump_through=True)
	], identifier="EVENT_3413_action_queue_5"),
	ClearBit(TEMP_7043_0),
	Return(identifier="EVENT_3413_ret_7")
])
