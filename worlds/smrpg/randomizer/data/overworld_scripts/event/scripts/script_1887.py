# E1887_WHIRLPOOL_SHOGUN_5
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AF),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_1887_jmp_if_bit_set_4"]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1745_freeze_all_npcs_until_return_43', 'EVENT_1887_jmp_if_bit_set_4']),
	JmpIfBitSet(SHOGUN_5_CLEARED, ["EVENT_1887_jmp_to_subroutine_9"], identifier="EVENT_1887_jmp_if_bit_set_4"),
	RunEventAsSubroutine(E1745_WHIRLPOOL_SHOGUN),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_1887_ret_8"]),
	SetBit(SHOGUN_5_CLEARED),
	Return(identifier="EVENT_1887_ret_8"),
	JmpToSubroutine(["EVENT_1745_freeze_all_npcs_until_return_60"], identifier="EVENT_1887_jmp_to_subroutine_9"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(90),
		A_SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	Return()
])
