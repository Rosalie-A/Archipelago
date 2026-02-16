# E3311_SHIP_SHOP
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_3311_jmp_if_bit_set_3"]),
	Jmp(["EVENT_3311_run_event_as_subroutine_12"]),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3311_run_dialog_11"], identifier="EVENT_3311_jmp_if_bit_set_3"),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3311_run_dialog_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3311_run_dialog_11"]),
	RunDialog(dialog_id=DI1691_SHAMAN_PASSWORD_PROGRESS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3311_run_event_as_subroutine_12"]),
	RunDialog(dialog_id=DI1686_SHAMAN_PASSWORD_WRONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3311_run_dialog_9"),
	Jmp(["EVENT_3311_run_event_as_subroutine_12"]),
	RunDialog(dialog_id=DI1687_SHAMAN_PASSWORD_RIGHT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3311_run_dialog_11"),
	RunEventAsSubroutine(E3297_SEA_SHOP, identifier="EVENT_3311_run_event_as_subroutine_12"),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_3311_ret_15"]),
	RunDialog(dialog_id=DI1690_SEA_SHOPKEEPER_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(identifier="EVENT_3311_ret_15")
])
