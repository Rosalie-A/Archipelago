# E2555_BEAN_VALLEY_BOSS_ROOM_LOADER
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
	ClearBit(DIRECTIONAL_7047_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	JmpIfBitSet(BEAN_VALLEY_BOSS_DEFEATED, ["EVENT_2555_action_queue_9"]),
	RunBackgroundEvent(event_id=E2557_BEAN_VALLEY_WATERS_BOSS, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	Return(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_TransferToXYZF(x=26, y=60, z=0, direction=EAST),
		A_WalkNorthwestPixels(5),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2555_action_queue_9"),
	FadeInFromBlack(sync=False),
	Return()
])
