# E3411_SHIP_PASSWORD_CORRECTNESS_CHECK
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
	JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_3411_jmp_if_var_not_equals_const_2"]),
	Inc(TEMP_70AC),
	JmpIfVarNotEqualsConst(TEMP_7026, 2, ["EVENT_3411_jmp_if_var_not_equals_const_4"], identifier="EVENT_3411_jmp_if_var_not_equals_const_2"),
	Inc(TEMP_70AC),
	JmpIfVarNotEqualsConst(TEMP_7028, 0, ["EVENT_3411_jmp_if_var_not_equals_const_6"], identifier="EVENT_3411_jmp_if_var_not_equals_const_4"),
	Inc(TEMP_70AC),
	JmpIfVarNotEqualsConst(TEMP_702A, 2, ["EVENT_3411_jmp_if_var_not_equals_const_8"], identifier="EVENT_3411_jmp_if_var_not_equals_const_6"),
	Inc(TEMP_70AC),
	JmpIfVarNotEqualsConst(TEMP_702C, 3, ["EVENT_3411_jmp_if_var_not_equals_const_10"], identifier="EVENT_3411_jmp_if_var_not_equals_const_8"),
	Inc(TEMP_70AC),
	JmpIfVarNotEqualsConst(TEMP_702E, 0, ["EVENT_3411_ret_12"], identifier="EVENT_3411_jmp_if_var_not_equals_const_10"),
	Inc(TEMP_70AC),
	Return(identifier="EVENT_3411_ret_12")
])
