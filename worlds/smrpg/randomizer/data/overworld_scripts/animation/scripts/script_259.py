#A0259_NIMBUS_PINWHEEL_RIGHT
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
	A_JmpIfRandom1of2(["ACTION_259_pause_2"], identifier="ACTION_259_jmp_if_random_above_128_0"),
	A_Pause(60),
	A_Pause(30, identifier="ACTION_259_pause_2"),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetBit(TEMP_7043_6),
	A_Pause(120),
	A_ClearBit(TEMP_7043_6),
	A_ResetProperties(),
	A_Jmp(["ACTION_259_jmp_if_random_above_128_0"])
])
