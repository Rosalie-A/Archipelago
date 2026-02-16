# E2224_KEEP_FINAL_BOSS_ROOM_LOADER
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
	JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["EVENT_2224_action_queue_7"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8),
		A_WalkNorthwestPixels(4),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SequenceLoopingOn(),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(19),
		A_WalkNorthPixels(3),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SequenceLoopingOn(),
		A_SetPriority(3),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(23),
		A_WalkSoutheastPixels(12),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SequenceLoopingOn(),
		A_SetPriority(3),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	RunEventAsSubroutine(E0853_KEEP_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSoutheastPixels(8)
	], identifier="EVENT_2224_action_queue_7"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM, mod_id=0),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	PrioritySet(mainscreen=[LAYER_L1, NPC_SPRITES], subscreen=[], colour_math=[]),
	FadeInFromBlack(sync=False),
	Return()
])
