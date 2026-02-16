# E2145_KEEP_DONUT_BRIDGE_ROOM_LOADER
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
	ApplyTileModToLevel(use_alternate=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=33),
	ApplyTileModToLevel(use_alternate=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=34),
	ApplyTileModToLevel(use_alternate=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=35),
	ApplyTileModToLevel(use_alternate=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=36),
	ApplySolidityModToLevel(permanent=True, room_id=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=0),
	RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(14),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(14),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(14),
		A_WalkSoutheastPixels(8)
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_2145_fade_in_from_black_async_14"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=16, y=42, z=10, direction=EAST),
		A_FaceSouthwest(),
		A_Pause(1)
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_2145_fade_in_from_black_async_14"),
	Return()
])
