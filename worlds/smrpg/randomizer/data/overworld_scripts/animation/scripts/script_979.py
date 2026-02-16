#A0979_NIMBUS_CASTLE_CAGED_BIRD
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
	A_ShadowOn(),
	A_SetPriority(3),
	A_SetWalkingSpeed(SLOW),
	A_TransferXYZFPixels(x=251, y=254, z=5, direction=EAST),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="ACTION_979_set_sprite_sequence_4"),
	A_Pause(10),
	A_ShiftZUpPixels(8),
	A_ShiftZDownPixels(8),
	A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	A_JmpIfRandom1of2(["ACTION_979_pause_11"]),
	A_Pause(60),
	A_Pause(60, identifier="ACTION_979_pause_11"),
	A_JmpIfRandom1of2(["ACTION_980_pause_4"]),
	A_Jmp(["ACTION_979_set_sprite_sequence_4"])
])
