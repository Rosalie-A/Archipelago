# E3599_MUSHROOM_DERBY_PRIZE_CALCULATOR
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
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TIMER_701C, 0),
	StoreEmptyItemInventorySlotCountTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3599_copy_var_to_var_33"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	Compare7000ToVar(SECONDARY_TEMP_7024),
	JmpIfComparisonResultIsLesser(["EVENT_3599_copy_var_to_var_13"]),
	JmpIfLoadedMemoryIs0(["EVENT_3599_copy_var_to_var_13"]),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	Jmp(["EVENT_3599_copy_var_to_var_15"]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3599_copy_var_to_var_13"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3599_copy_var_to_var_15"),
	SetObjectMemoryToVar(SECONDARY_TEMP_7024),
	AddToInventory(YoshiCookieItem),
	EndLoop(),
	JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_3599_set_var_to_const_48"]),
	CopyVarToVar(from_var=UNKNOWN_70D8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3599_copy_var_to_var_20"),
	AddVarTo7000(TEMP_7026),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CompareVarToConst(PRIMARY_TEMP_7000, 201),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3599_set_var_to_const_36"]),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3599_run_dialog_31"]),
	RunDialog(dialog_id=DI0950_TOO_MANY_COOKIES, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3599_copy_var_to_var_28"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70D8),
	Jmp(["EVENT_3599_set_var_to_const_48"]),
	RunDialog(dialog_id=DI2362_STORE_EXTRA_COOKIES_AFTER_WINNING, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3599_run_dialog_31"),
	Jmp(["EVENT_3599_copy_var_to_var_28"]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3599_copy_var_to_var_33"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	Jmp(["EVENT_3599_copy_var_to_var_20"]),
	SetVarToConst(SECONDARY_TEMP_7024, 200, identifier="EVENT_3599_set_var_to_const_36"),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=UNKNOWN_70D8, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	DecVarFrom7000(TEMP_7026),
	RunDialog(dialog_id=DI2510_WON_COOKIES_IN_EXCESS, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO061_DEEP_UHOH, channel=6),
	Pause(60),
	RunDialog(dialog_id=DI0952_DUPLICATE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(UNKNOWN_70D8, 200),
	SetVarToConst(TEMP_70AE, 0, identifier="EVENT_3599_set_var_to_const_48"),
	SetVarToConst(TEMP_70B8, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	Return()
])
