# E3814_MUSHROOM_KINGDOM_LIBERATED_LOADER
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
	ClearBit(TEMP_7042_7),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_3814_remove_from_current_level_4"]),
	FadeInFromBlack(sync=False),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_3814_remove_from_current_level_4"),
	SummonObjectToCurrentLevel(NPC_1),
	SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferXYZFPixels(x=6, y=250, z=0, direction=EAST)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R022_MUSHROOM_KINGDOM_CASTLE_GUEST_ROOM, mod_id=0),
	FadeInFromBlack(sync=False),
	Return()
])
