# E3166_ACTIVE_MINECART_MARIO_COLLISION_CHECK_PROPERTIES
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
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True, identifier="EVENT_3166_set_7010_to_object_xyz_0"),
	JmpIfVarNotEqualsConst(X_COORD_1, 22, ["EVENT_3166_action_queue_6"]),
	JmpIfVarNotEqualsConst(Y_COORD_1, 74, ["EVENT_3166_action_queue_6"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_ShadowOn()
	]),
	Pause(1),
	Jmp(["EVENT_3166_set_7010_to_object_xyz_0"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_ShadowOff()
	], identifier="EVENT_3166_action_queue_6"),
	Pause(1),
	Jmp(["EVENT_3166_set_7010_to_object_xyz_0"])
])
