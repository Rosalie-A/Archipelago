# E1633_MOLEVILLE_INN
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
	JmpIfBitSet(MOLEVILLE_TOADOFSKY_HINT, ["EVENT_1633_set_var_to_const_4"]),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1633_set_var_to_const_4"]),
	RunDialog(dialog_id=DI1091_MOLEVILLE_INN_TOADOFSKY_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(MOLEVILLE_TOADOFSKY_HINT),
	SetVarToConst(SECONDARY_TEMP_7024, 10, identifier="EVENT_1633_set_var_to_const_4"),
	SetVarToConst(PRIMARY_TEMP_7000, 1088),
	SetVarToConst(TEMP_70AE, 20),
	JmpToSubroutine(["EVENT_1633_clear_bit_12"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1633_set_bit_10"]),
	Return(),
	SetBit(MOLEVILLE_INN, identifier="EVENT_1633_set_bit_10"),
	JmpToEvent(E0280_SLEEP_IN_NIMBUS_INN),
	ClearBit(TEMP_7043_0, identifier="EVENT_1633_clear_bit_12"),
	RunDialog(dialog_id=PRIMARY_TEMP_7000, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	SwapVars(TEMP_7026, PRIMARY_TEMP_7000),
	StoreCoinCountTo7000(),
	Compare7000ToVar(SECONDARY_TEMP_7024),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1633_swap_vars_23"]),
	SwapVars(TEMP_7026, PRIMARY_TEMP_7000),
	Inc(PRIMARY_TEMP_7000),
	Inc(PRIMARY_TEMP_7000),
	AppendDialogAt7000ToCurrentDialog(closable=True, sync=False),
	Return(),
	SwapVars(TEMP_7026, PRIMARY_TEMP_7000, identifier="EVENT_1633_swap_vars_23"),
	Inc(PRIMARY_TEMP_7000),
	AppendDialogAt7000ToCurrentDialog(closable=True, sync=False),
	JmpIfDialogOptionBSelected(["EVENT_1633_pause_33"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetBit(TEMP_7043_0),
	Return(),
	Pause(10, identifier="EVENT_1633_pause_33"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
