# E3793_FACTORY_SMELTER_ANIMATION
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
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	ClearBit(TEMP_7044_4),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_3793_pause_13"]),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_5),
	UnsyncActionScript(NPC_8),
	Pause(10),
	SetSyncActionScript(NPC_4, A0240_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_9, A0991_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_5, A0241_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_8, A0990_SMITHY_COMPONENT),
	Pause(1, identifier="EVENT_3793_pause_13"),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3793_clear_bit_16"]),
	Jmp(["EVENT_3793_pause_13"]),
	ClearBit(TEMP_7044_0, identifier="EVENT_3793_clear_bit_16"),
	ClearBit(TEMP_7044_6),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_704C_0),
	SetVarToConst(X_COORD_1, 4),
	SetVarToConst(Y_COORD_1, 19),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P050_WATER_BLAST_SFX, destinations=["EVENT_3793_clear_bit_28"]),
	Pause(1, identifier="EVENT_3793_pause_25"),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3793_clear_bit_28"]),
	Jmp(["EVENT_3793_pause_25"]),
	ClearBit(TEMP_7044_0, identifier="EVENT_3793_clear_bit_28"),
	ClearBit(TEMP_7044_6),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_704C_0),
	SetVarToConst(X_COORD_1, 4),
	SetVarToConst(Y_COORD_1, 19),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P051_DRILL_BIT, destinations=["EVENT_3793_set_bit_40"]),
	Pause(1, identifier="EVENT_3793_pause_37"),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_3793_set_bit_40"]),
	Jmp(["EVENT_3793_pause_37"]),
	SetBit(TEMP_704C_0, identifier="EVENT_3793_set_bit_40"),
	Pause(1),
	ClearBit(TEMP_704C_0),
	Pause(29),
	JmpToEvent(E3793_FACTORY_SMELTER_ANIMATION)
])
