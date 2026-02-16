# E1295_TOWER_CHECKERBOARD_ROOM_LOADER
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
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8)
	]),
	FadeInFromBlack(sync=False),
	Return()
])
