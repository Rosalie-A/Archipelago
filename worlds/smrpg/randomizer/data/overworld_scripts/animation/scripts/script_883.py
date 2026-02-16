#A0883_INC_PALETTE_ROW_FAKE_BIRD_STATUE
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
	A_IncPaletteRowBy(1),
	A_Pause(1, identifier="ACTION_883_pause_1"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=2, destinations=["ACTION_883_pause_4"]),
	A_Jmp(["ACTION_883_pause_1"]),
	A_Pause(30, identifier="ACTION_883_pause_4"),
	A_SequenceLoopingOn(),
	A_IncPaletteRowBy(15, 15),
	A_Jmp(["ACTION_881_set_solidity_bits_0"])
])
