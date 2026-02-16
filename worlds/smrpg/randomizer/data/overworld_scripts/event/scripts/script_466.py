# E0466_MUSHROOM_DERBY_BUSINESS_LOGIC_EXTENSION
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
	SetSyncActionScript(NPC_10, A0794_MUSHROOM_DERBY_UNKNOWN),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_466_set_action_script_4"]),
	SetSyncActionScript(NPC_9, A0431_YOSHI_RACE_ANIMATION),
	Jmp(["EVENT_466_jmp_if_bit_clear_5"]),
	SetSyncActionScript(NPC_9, A0797_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_466_set_action_script_4"),
	JmpIfBitClear(YOSTER_ISLE_LIBERATED_2, ["EVENT_466_set_action_script_14"], identifier="EVENT_466_jmp_if_bit_clear_5"),
	SetSyncActionScript(NPC_3, A0795_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_2, A0796_MUSHROOM_DERBY_UNKNOWN),
	PauseActionScript(NPC_5),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=16, y=64, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SetPriority(3),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(NPC_5, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN),
	Jmp(["EVENT_466_jmp_if_bit_set_18"]),
	SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN, identifier="EVENT_466_set_action_script_14"),
	SetSyncActionScript(NPC_2, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_1, A0677_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_3, A0677_MUSHROOM_DERBY_UNKNOWN),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_256_ret_0"], identifier="EVENT_466_jmp_if_bit_set_18"),
	SetSyncActionScript(MARIO, A0500_MUSHROOM_DERBY_UNKNOWN),
	ClearBit(TEMP_7043_0, identifier="EVENT_466_clear_bit_20"),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	Pause(1, identifier="EVENT_466_pause_25"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_466_inc_31"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_466_set_var_to_const_35"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_466_set_var_to_const_42"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_466_pause_39"]),
	Jmp(["EVENT_466_pause_25"]),
	Inc(TEMP_70AE, identifier="EVENT_466_inc_31"),
	SetSyncActionScript(MARIO, A0499_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_9, A0430_YOSHI_FINISH_RACE),
	Jmp(["EVENT_466_clear_bit_20"]),
	SetVarToConst(TEMP_7032, 0, identifier="EVENT_466_set_var_to_const_35"),
	SetSyncActionScript(MARIO, A0502_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_9, A0428_YOSHI_FINISH_RACE),
	Jmp(["EVENT_466_pause_39"]),
	Pause(1, identifier="EVENT_466_pause_39"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_466_clear_bit_20"]),
	Jmp(["EVENT_466_pause_39"]),
	SetVarToConst(TEMP_7032, 0, identifier="EVENT_466_set_var_to_const_42"),
	SetSyncActionScript(MARIO, A0501_MUSHROOM_DERBY_UNKNOWN),
	SetSyncActionScript(NPC_9, A0430_YOSHI_FINISH_RACE),
	Jmp(["EVENT_466_pause_39"])
])
