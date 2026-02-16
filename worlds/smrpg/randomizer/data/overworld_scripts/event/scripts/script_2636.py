# E2636_CASINO_GUARD
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
	SetVarToConst(ITEM_ID, BrightCardItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2636_jmp_if_bit_set_13"]),
	JmpIfBitSet(DIRECTIONAL_7046_1, ["EVENT_2636_run_dialog_11"]),
	RunDialog(dialog_id=DI3300_BOUNCER_ALLOW, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2636_ret_10"]),
	SetBit(TEMP_7043_0),
	ApplySolidityModToLevel(permanent=True, room_id=R104_GRATE_GUYS_CASINO_FRONT_DOOR, mod_id=0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	Return(identifier="EVENT_2636_ret_10"),
	RunDialog(dialog_id=DI3301_BOUNCER_LEAVE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2636_run_dialog_11"),
	Return(),
	JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_2636_run_dialog_16"], identifier="EVENT_2636_jmp_if_bit_set_13"),
	RunDialog(dialog_id=DI3298_BOUNCER_REJECT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3299_BOUNCER_REJECT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2636_run_dialog_16"),
	Return()
])
