#A0315_SHIP_TRAMPOLINE_PUZZLE_BUTTON
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
	A_ShadowOff(identifier="ACTION_315_shadow_off_0"),
	A_SetPriority(3),
	A_Pause(1),
	A_JmpIfBitClear(TEMP_7043_3, ["ACTION_315_shadow_off_0"]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
	A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
	A_ReturnQueue()
])
