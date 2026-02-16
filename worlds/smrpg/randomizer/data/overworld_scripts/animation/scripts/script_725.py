#A0725_MINES_LONG_TRACK_ROOM_MINECART
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
	A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_JmpIfObjectInSpecificLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, ["ACTION_725_ret_27"]),
	A_JmpIfObjectNotInSpecificLevel(NPC_0, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, ["ACTION_725_ret_27"]),
	A_SetVarToConst(SECONDARY_TEMP_7024, 900),
	A_JmpIfBitSet(TEMP_7044_7, ["ACTION_725_set_bit_11"], identifier="ACTION_725_jmp_if_bit_set_7"),
	A_Pause(1),
	A_Dec(SECONDARY_TEMP_7024),
	A_JmpIfLoadedMemoryIsNot0(["ACTION_725_jmp_if_bit_set_7"]),
	A_SetBit(TEMP_7044_7, identifier="ACTION_725_set_bit_11"),
	A_RemoveObjectFromSpecificLevel(NPC_0, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
	A_RemoveObjectFromSpecificLevel(NPC_4, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
	A_SetWalkingSpeed(FAST),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_PlaySound(sound=SO048_MINECART_START, channel=4),
	A_WalkToXYCoords(x=2, y=124),
	A_FadeOutSoundToVolume(duration=1, volume=0),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_UnknownCommand(bytearray(b'\xfd\xf2')),
	A_SummonObjectToSpecificLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM),
	A_ReturnQueue(),
	A_ReturnQueue(identifier="ACTION_725_ret_27")
])
