# E3388_SHIP_BOSS_ROOM_PERISCOPE
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
	JmpIfBitSet(JOHNNY_POSITION, ["EVENT_3388_ret_25"]),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTH, x=7, y=82, z=0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_VisibilityOff()
	]),
	RunEventAsSubroutine(E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED),
	JmpIfComparisonResultIsLesser(["EVENT_3388_action_queue_14"]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_VisibilityOn()
	]),
	Jmp(["EVENT_3388_remove_from_current_level_15"]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_VisibilityOff()
	], identifier="EVENT_3388_action_queue_14"),
	RemoveObjectFromCurrentLevel(MARIO, identifier="EVENT_3388_remove_from_current_level_15"),
	CircleMaskShrinkToObject(target=MARIO, width=96, speed=8, static=True),
	Pause(180),
	Pause(180),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=8, static=True),
	EnterArea(room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, face_direction=NORTHEAST, x=24, y=110, z=0),
	RunEventAsSubroutine(E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(4)
	]),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_3388_ret_25")
])
