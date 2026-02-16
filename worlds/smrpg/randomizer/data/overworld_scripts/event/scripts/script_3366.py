# E3366_KEEP_LOGIC_GAME_BOO
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3366_ret_8"]),
	RunDialog(dialog_id=DI1925_EMPTY_AUTO_TERMINATE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI1921_BOO, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfVarEqualsConst(TEMP_70AF, 1, ["EVENT_3369_copy_var_to_var_32"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_3369_run_dialog_12"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 2, ["EVENT_3369_run_dialog_10"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 3, ["EVENT_3369_run_dialog_8"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_3369_run_dialog_30"]),
	Return(identifier="EVENT_3366_ret_8")
])
