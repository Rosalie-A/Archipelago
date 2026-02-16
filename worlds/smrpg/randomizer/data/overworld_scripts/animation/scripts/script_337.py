#A0337_VARIOUS_SHIP_OBJECTS
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
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 172, ["ACTION_337_set_palette_row_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 177, ["ACTION_337_set_palette_row_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 163, ["ACTION_337_set_palette_row_24"]),
	A_IncPaletteRowBy(1),
	A_UnknownCommand(bytearray(b'\xfd\x9c\x05'), identifier="ACTION_337_db_6"),
	A_UnknownCommand(bytearray(b' \x04')),
	A_UnknownCommand(bytearray(b'%\xc0\x03\x80\xff')),
	A_Pause(8),
	A_UnknownCommand(bytearray(b'%@\x00\x80\xff')),
	A_Pause(8),
	A_BPL262728(),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 172, ["ACTION_337_set_palette_row_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 177, ["ACTION_337_set_palette_row_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 163, ["ACTION_337_set_palette_row_26"]),
	A_IncPaletteRowBy(15, 15),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="ACTION_337_object_memory_clear_bit_18"),
	A_ReturnQueue(),
	A_SetPaletteRow(row=2, identifier="ACTION_337_set_palette_row_20"),
	A_Jmp(["ACTION_337_db_6"]),
	A_SetPaletteRow(row=1, identifier="ACTION_337_set_palette_row_22"),
	A_Jmp(["ACTION_337_object_memory_clear_bit_18"]),
	A_SetPaletteRow(row=3, identifier="ACTION_337_set_palette_row_24"),
	A_Jmp(["ACTION_337_db_6"]),
	A_SetPaletteRow(row=2, identifier="ACTION_337_set_palette_row_26"),
	A_Jmp(["ACTION_337_object_memory_clear_bit_18"])
])
