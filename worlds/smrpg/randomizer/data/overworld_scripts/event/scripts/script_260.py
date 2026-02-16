# E0260_UNKNOWN
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
	ActionQueueAsync(target=MEM_70AA, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x12\x00')),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_260_action_queue_0_SUBSCRIPT_face_southeast_6"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_260_action_queue_0_SUBSCRIPT_face_southwest_8"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["EVENT_260_action_queue_0_SUBSCRIPT_face_northwest_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["EVENT_260_action_queue_0_SUBSCRIPT_face_northeast_12"]),
		A_FaceSoutheast(identifier="EVENT_260_action_queue_0_SUBSCRIPT_face_southeast_6"),
		A_Jmp(["EVENT_260_ret_1"]),
		A_FaceSouthwest(identifier="EVENT_260_action_queue_0_SUBSCRIPT_face_southwest_8"),
		A_Jmp(["EVENT_260_ret_1"]),
		A_FaceNorthwest(identifier="EVENT_260_action_queue_0_SUBSCRIPT_face_northwest_10"),
		A_Jmp(["EVENT_260_ret_1"]),
		A_FaceNortheast(identifier="EVENT_260_action_queue_0_SUBSCRIPT_face_northeast_12")
	]),
	Return(identifier="EVENT_260_ret_1")
])
