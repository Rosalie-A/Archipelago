# E0435_PIPE_VAULT_ROOM_1_LOADER
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
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_435_action_queue_3"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=10, y=10, z=2, direction=EAST),
		A_FaceSouthwest()
	]),
	Jmp(["EVENT_435_jmp_if_object_not_in_level_4"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=22, z=2, direction=EAST),
		A_FaceNortheast()
	], identifier="EVENT_435_action_queue_3"),
	JmpIfObjectNotInSpecificLevel(NPC_1, R123_PIPE_VAULT_AREA_01, ["EVENT_435_jmp_if_object_not_in_level_6"], identifier="EVENT_435_jmp_if_object_not_in_level_4"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R123_PIPE_VAULT_AREA_01, ["EVENT_435_jmp_if_object_not_in_level_8"], identifier="EVENT_435_jmp_if_object_not_in_level_6"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectNotInSpecificLevel(NPC_3, R123_PIPE_VAULT_AREA_01, ["EVENT_435_jmp_if_object_not_in_level_10"], identifier="EVENT_435_jmp_if_object_not_in_level_8"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectNotInSpecificLevel(NPC_4, R123_PIPE_VAULT_AREA_01, ["EVENT_435_run_background_event_12"], identifier="EVENT_435_jmp_if_object_not_in_level_10"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True, identifier="EVENT_435_run_background_event_12"),
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_256_ret_0"]),
	FadeInFromBlack(sync=False),
	Return()
])
