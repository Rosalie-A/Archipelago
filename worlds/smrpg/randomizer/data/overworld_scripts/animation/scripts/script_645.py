#A0645_MIDAS_2ND_TUNNELS_JAWFUL
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
	A_SetPriority(3),
	A_JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_645_clear_bit_13"]),
	A_Pause(1, identifier="ACTION_645_pause_2"),
	A_JmpIfBitClear(TEMP_7043_2, ["ACTION_645_pause_2"]),
	A_Pause(1, identifier="ACTION_645_pause_4"),
	A_JmpIfBitSet(TEMP_7043_2, ["ACTION_645_pause_4"]),
	A_Pause(109),
	A_StartLoopNTimes(1),
	A_Pause(32),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(32),
	A_EndLoop(),
	A_ReturnQueue(),
	A_ClearBit(MIDAS_RIVER_TUNNEL_1_BIT, identifier="ACTION_645_clear_bit_13"),
	A_Pause(168),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(64),
	A_JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_2, ["ACTION_645_pause_22"]),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(35),
	A_SetBit(MIDAS_RIVER_TUNNEL_1_BIT),
	A_ReturnQueue(),
	A_Pause(15, identifier="ACTION_645_pause_22"),
	A_SetSpriteSequence(index=3, looping=False),
	A_Pause(36),
	A_SetSequenceSpeed(SLOW),
	A_SetSpriteSequence(index=2, looping=False),
	A_Pause(50),
	A_FaceSoutheast(),
	A_Pause(40),
	A_SetSpriteSequence(index=4, looping=False, mirror_sprite=True),
	A_ReturnQueue()
])
