# E2147_KEEP_ORIGINAL_THRONE_ROOM_LOADER
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
	ApplySolidityModToLevel(permanent=True, room_id=R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM, mod_id=0),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_2147_fade_in_from_black_async_13"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=2, y=66, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=2, y=67, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_0, A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS),
	SetSyncActionScript(NPC_1, A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS),
	FadeInFromBlack(sync=False, identifier="EVENT_2147_fade_in_from_black_async_13"),
	Return()
])
