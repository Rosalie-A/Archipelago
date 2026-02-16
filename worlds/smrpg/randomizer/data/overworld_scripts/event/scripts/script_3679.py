# E3679_NIMBUS_CASTLE_EGG_ROOM_LOADER
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
	JmpIfObjectNotInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_3679_action_queue_2"]),
	ApplySolidityModToLevel(permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=0),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=20, y=49, z=10, direction=EAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	], identifier="EVENT_3679_action_queue_2"),
	RememberLastObject(),
	SetSyncActionScript(NPC_1, A0978_RANDOMLY_FACE_SOUTHWEST),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3679_fade_in_from_black_async_6"]),
	FadeInFromBlack(sync=False, identifier="EVENT_3679_fade_in_from_black_async_6"),
	Return()
])
