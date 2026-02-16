#A0319_SHIP_CANNONBALL_PUZZLE_CANNONBALL
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
	A_VisibilityOff(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
	A_SetPaletteRow(row=4),
	A_Pause(24),
	A_CreatePacketAtObjectCoords(packet=P024_REGULAR_SOUND_EXPLOSION, target_npc=DUMMY_0X07, destinations=["ACTION_319_visibility_on_5"]),
	A_VisibilityOn(identifier="ACTION_319_visibility_on_5"),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(4),
	A_ShadowOff(),
	A_Walk1StepSoutheast(),
	A_EndLoop(),
	A_PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
