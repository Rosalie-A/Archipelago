#A0879_MONSTRO_GOOMBETTE
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
	A_Pause(3, identifier="ACTION_879_pause_0"),
	A_JmpIfRandom1of2(["ACTION_879_pause_0"]),
	A_Set700CToObjectCoord(target_npc=NPC_1, coord=COORD_F),
	A_FaceEast7C(),
	A_Pause(1),
	A_Jmp(["ACTION_879_pause_0"])
])
