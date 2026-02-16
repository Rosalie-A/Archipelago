# E0338_MUSHROOM_KINGDOM_SHOPKEEPER
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
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True),
	CompareVarToConst(Z_COORD_1, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_338_run_dialog_7"]),
	CompareVarToConst(Y_COORD_1, 19),
	JmpIfComparisonResultIsLesser(["EVENT_338_run_dialog_7"]),
	JmpIfLoadedMemoryIs0(["EVENT_338_compare_var_to_const_9"]),
	Jmp(["EVENT_338_jmp_to_event_11"]),
	RunDialog(dialog_id=DI0609_SHOPKEEPER_YELLS_AT_YOU_BEHIND_COUNTER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_338_run_dialog_7"),
	Return(),
	CompareVarToConst(X_COORD_1, 14, identifier="EVENT_338_compare_var_to_const_9"),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_338_run_dialog_7"]),
	JmpToEvent(E0290_MUSHROOM_KINGDOM_SHOP_LOGIC, identifier="EVENT_338_jmp_to_event_11")
])
