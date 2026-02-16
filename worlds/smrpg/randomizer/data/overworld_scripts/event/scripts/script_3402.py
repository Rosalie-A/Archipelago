# E3402_COIN_CHEST_MULTI_HIT_3
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
	DisableObjectTrigger(MEM_70A8),
	JmpIfVarEqualsConst(ITEM_ID, 240, ["EVENT_3402_play_sound_3"]),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_3402_play_sound_3"),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	SetVarToConst(PRIMARY_TEMP_7000, 290),
	JmpIfMem704XAt7000BitSet(["EVENT_3402_jmp_if_var_not_equals_const_16"]),
	SetMem704XAt7000Bit(),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 0, ["EVENT_3402_copy_var_to_var_15"], identifier="EVENT_3402_jmp_if_var_equals_const_11"),
	AddConstToVar(PRIMARY_TEMP_7000, 15),
	Dec(COIN_CHEST_MULTIPLIER),
	Jmp(["EVENT_3402_jmp_if_var_equals_const_11"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_COUNTER_3, identifier="EVENT_3402_copy_var_to_var_15"),
	JmpIfVarNotEqualsConst(COIN_COUNTER_3, 1, ["EVENT_3402_set_temp_action_script_21"], identifier="EVENT_3402_jmp_if_var_not_equals_const_16"),
	SetSyncActionScript(MEM_70AA, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	SetVarToConst(PRIMARY_TEMP_7000, 290),
	ClearMem704XAt7000Bit(),
	Jmp(["EVENT_3402_set_7010_to_object_xyz_22"]),
	SetTempSyncActionScript(MEM_70AA, A0008_HIT_TREASURE_CHEST_CONTENTS_REMAINING, identifier="EVENT_3402_set_temp_action_script_21"),
	Set70107015ToObjectXYZ(target=MEM_70AA, identifier="EVENT_3402_set_7010_to_object_xyz_22"),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x00F0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_3402_add_coins_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 160, ["EVENT_3402_dec_32"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3402_dec_38"]),
	Jmp(["EVENT_3402_ret_49"]),
	Dec(COIN_COUNTER_3, identifier="EVENT_3402_dec_32"),
	AddCoins(10),
	PlaySound(sound=SO013_COIN, channel=6),
	CreatePacketAt7010(packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_3402_ret_49"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	Jmp(["EVENT_3402_ret_49"]),
	Dec(COIN_COUNTER_3, identifier="EVENT_3402_dec_38"),
	AddCoins(1),
	PlaySound(sound=SO013_COIN, channel=6),
	CreatePacketAt7010(packet=P018_SMALL_COIN_BEING_COLLECTED, destinations=["EVENT_3402_ret_49"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	Jmp(["EVENT_3402_ret_49"]),
	AddCoins(1, identifier="EVENT_3402_add_coins_44"),
	PlaySound(sound=SO013_COIN, channel=6),
	CreatePacketAt7010(packet=P018_SMALL_COIN_BEING_COLLECTED, destinations=["EVENT_3402_ret_49"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	EnableObjectTrigger(MEM_70AA),
	Return(identifier="EVENT_3402_ret_49")
])
