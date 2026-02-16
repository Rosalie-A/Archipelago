# E2228_KEEP_DARK_ROOM_LOADER
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
	JmpIfObjectNotInSpecificLevel(NPC_2, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM, ["EVENT_2228_db_2"]),
	SetSyncActionScript(NPC_2, A1010_KEEP_DARK_ROOM_INIT_GOOMBA),
	UnknownCommand(bytearray(b'\xfd\x8f\x02'), identifier="EVENT_2228_db_2"),
	PrioritySet(mainscreen=[LAYER_L3], subscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], colour_math=[BACKGROUND, HALF_INTENSITY]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSoutheastPixels(4),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkSoutheastPixels(1),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkSoutheastPixels(1),
		A_FaceSouthwest()
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_2228_fade_in_from_black_async_14"]),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7043_2),
	FadeInFromBlack(sync=False, identifier="EVENT_2228_fade_in_from_black_async_14"),
	Return()
])
