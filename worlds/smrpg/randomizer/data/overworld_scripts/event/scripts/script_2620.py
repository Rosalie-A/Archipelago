# E2620_FACTORY_3RD_ROOM_BACKGROUND_NPCS_BONK_CONVEYOR
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	Pause(1, identifier="EVENT_2620_pause_0"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2620_clear_bit_5"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_2620_clear_bit_12"]),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_2620_clear_bit_19"]),
	Jmp(["EVENT_2620_pause_0"], identifier="EVENT_2620_jmp_4"),
	ClearBit(TEMP_7043_3, identifier="EVENT_2620_clear_bit_5"),
	SetVarToConst(X_COORD_1, 8),
	SetVarToConst(Y_COORD_1, 96),
	SetVarToConst(Z_COORD_1, 12),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]),
	Jmp(["EVENT_2620_pause_0"]),
	ClearBit(TEMP_7043_4, identifier="EVENT_2620_clear_bit_12"),
	SetVarToConst(X_COORD_1, 10),
	SetVarToConst(Y_COORD_1, 101),
	SetVarToConst(Z_COORD_1, 12),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]),
	Jmp(["EVENT_2620_pause_0"]),
	ClearBit(TEMP_7043_5, identifier="EVENT_2620_clear_bit_19"),
	SetVarToConst(X_COORD_1, 13),
	SetVarToConst(Y_COORD_1, 107),
	SetVarToConst(Z_COORD_1, 12),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]),
	Jmp(["EVENT_2620_pause_0"])
])
