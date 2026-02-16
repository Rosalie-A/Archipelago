#A0694_BOOSTER_PASS_SPINY
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
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_FloatingOff(),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_Pause(32),
	A_SetSequenceSpeed(SLOW),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\xc0\x00\xc0\xff')),
	A_UnknownCommand(bytearray(b'%\x00\x08\x80\xff')),
	A_Pause(32),
	A_BPL262728(),
	A_SetSequenceSpeed(NORMAL),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(96),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
	A_SetSequenceSpeed(SLOW),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$@\xff@\x00')),
	A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
	A_Pause(32),
	A_BPL262728(),
	A_FaceSouthwest(),
	A_ResetProperties(),
	A_SetSequenceSpeed(NORMAL),
	A_SequenceLoopingOn(),
	A_Pause(32),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_694_set_700C_to_object_coord_31"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_694_set_700C_to_object_coord_38"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_694_set_700C_to_object_coord_45"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_694_set_700C_to_object_coord_52"]),
	A_ReturnQueue(),
	A_Set700CToObjectCoord(target_npc=NPC_0, coord=COORD_Z, pixel=True, bit_7=True, identifier="ACTION_694_set_700C_to_object_coord_31"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_694_clear_bit_35"]),
	A_WalkToXYCoords(x=7, y=115),
	A_FaceSouthwest(),
	A_ClearBit(TEMP_7043_0, identifier="ACTION_694_clear_bit_35"),
	A_TransferToXYZF(x=7, y=115, z=4, direction=EAST),
	A_ReturnQueue(),
	A_Set700CToObjectCoord(target_npc=NPC_1, coord=COORD_Z, pixel=True, bit_7=True, identifier="ACTION_694_set_700C_to_object_coord_38"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_694_clear_bit_42"]),
	A_WalkToXYCoords(x=8, y=107),
	A_FaceSouthwest(),
	A_ClearBit(TEMP_7043_1, identifier="ACTION_694_clear_bit_42"),
	A_TransferToXYZF(x=8, y=107, z=4, direction=EAST),
	A_ReturnQueue(),
	A_Set700CToObjectCoord(target_npc=NPC_2, coord=COORD_Z, pixel=True, bit_7=True, identifier="ACTION_694_set_700C_to_object_coord_45"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_694_clear_bit_49"]),
	A_WalkToXYCoords(x=12, y=107),
	A_FaceSouthwest(),
	A_ClearBit(TEMP_7043_2, identifier="ACTION_694_clear_bit_49"),
	A_TransferToXYZF(x=12, y=107, z=4, direction=EAST),
	A_ReturnQueue(),
	A_Set700CToObjectCoord(target_npc=NPC_3, coord=COORD_Z, pixel=True, bit_7=True, identifier="ACTION_694_set_700C_to_object_coord_52"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 8, ["ACTION_694_clear_bit_56"]),
	A_WalkToXYCoords(x=11, y=95),
	A_FaceSouthwest(),
	A_ClearBit(TEMP_7043_3, identifier="ACTION_694_clear_bit_56"),
	A_TransferToXYZF(x=11, y=95, z=8, direction=EAST),
	A_ReturnQueue()
])
