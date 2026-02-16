# E1739_REFOCUS_CAMERA
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
	Set7016701BToObjectXYZ(target=MEM_70AB, bit_7=True),
	AddConstToVar(X_COORD_2, 65532),
	CompareVarToConst(X_COORD_2, 32768),
	JmpIfComparisonResultIsLesser(["EVENT_1739_add_const_to_var_5"]),
	SetVarToConst(X_COORD_2, 0),
	AddConstToVar(Y_COORD_2, 65520, identifier="EVENT_1739_add_const_to_var_5"),
	CopyVarToVar(from_var=Z_COORD_2, to_var=PRIMARY_TEMP_7000),
	Mem7000XorConst(0xFFFF),
	Inc(PRIMARY_TEMP_7000),
	AddVarTo7000(Y_COORD_2),
	CompareVarToConst(PRIMARY_TEMP_7000, 32768),
	JmpIfComparisonResultIsLesser(["EVENT_1739_copy_var_to_var_13"]),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2, identifier="EVENT_1739_copy_var_to_var_13"),
	SetVarToConst(Z_COORD_2, 0),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_JmpIfBitSet(SKY_BRIDGE_PAN, ["EVENT_1739_action_queue_15_SUBSCRIPT_set_animation_speed_4"]),
		A_JmpIfBitSet(UNKNOWN_PAN, ["EVENT_1739_action_queue_15_SUBSCRIPT_set_animation_speed_6"]),
		A_SetWalkingSpeed(FASTEST),
		A_Jmp(["EVENT_1739_action_queue_15_SUBSCRIPT_db_7"]),
		A_SetWalkingSpeed(FASTEST, identifier="EVENT_1739_action_queue_15_SUBSCRIPT_set_animation_speed_4"),
		A_Jmp(["EVENT_1739_action_queue_15_SUBSCRIPT_db_7"]),
		A_SetWalkingSpeed(FASTEST, identifier="EVENT_1739_action_queue_15_SUBSCRIPT_set_animation_speed_6"),
		A_UnknownCommand(bytearray(b'\x98'), identifier="EVENT_1739_action_queue_15_SUBSCRIPT_db_7"),
		A_SetWalkingSpeed(FASTEST)
	]),
	Return()
])
