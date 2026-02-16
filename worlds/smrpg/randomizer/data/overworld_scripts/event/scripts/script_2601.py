# E2601_FACTORY_4TH_ROOM_LOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkSouthPixels(4),
		A_WalkWestPixels(4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkEastPixels(12),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkWestPixels(8),
		A_WalkSouthPixels(1),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["EVENT_2601_remove_from_level_13"]),
	RunEventAsSubroutine(E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED),
	JmpIfComparisonResultIsLesser(["EVENT_2601_fade_in_from_black_async_16"]),
	SummonObjectToSpecificLevel(NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	SummonObjectToCurrentLevel(NPC_14),
	Jmp(["EVENT_2601_run_event_as_subroutine_15"]),
	RemoveObjectFromSpecificLevel(NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, identifier="EVENT_2601_remove_from_level_13"),
	RemoveObjectFromCurrentLevel(NPC_14),
	RunEventAsSubroutine(E0858_INNER_FACTORY_4TH_ROOM_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_2601_run_event_as_subroutine_15"),
	FadeInFromBlack(sync=False, identifier="EVENT_2601_fade_in_from_black_async_16"),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT, ["EVENT_2601_ret_20"]),
	SetVarToConst(PRIMARY_TEMP_7000, 523),
	RunEventAsSubroutine(E1245_INNER_FACTORY_5_BOSS_UNLOCKS),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(identifier="EVENT_2601_ret_20")
])
