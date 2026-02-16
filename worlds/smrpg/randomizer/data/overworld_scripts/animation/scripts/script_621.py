#A0621_SEQ_10_STORE_BUTTON_INPUT_AND_MAKE_SOUND
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
	A_VisibilityOn(),
	A_SetSpriteSequence(index=10, looping=False),
	A_Pause(48),
	A_PlaySound(sound=SO052_DEEP_BOUNCE, channel=4),
	A_Set700CToPressedButton(),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AA),
	A_CreatePacketAtObjectCoords(packet=P021_FLASHING_SMALL_EXPLOSION, target_npc=MEM_70AA, destinations=["ACTION_621_pause_7"]),
	A_Pause(128, identifier="ACTION_621_pause_7"),
	A_ResetProperties(),
	A_SetBit(TEMP_7043_0),
	A_Pause(1),
	A_VisibilityOff(),
	A_ReturnQueue()
])
