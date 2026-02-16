# E2418_FOREST_UNDERGROUND_1_LOADER
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_2418_jmp_if_bit_set_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 236, ["EVENT_2418_action_queue_4"]),
	Jmp(["EVENT_2418_jmp_if_bit_clear_56"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShadowOn(),
		A_SetAllSpeeds(FASTEST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthPixels(12),
		A_WalkSouthwestPixels(5)
	], identifier="EVENT_2418_action_queue_4"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	SetSyncActionScript(NPC_8, A0947_FOREST_1ST_UNDERGROUND_RAT),
	Jmp(["EVENT_2418_jmp_if_bit_clear_56"]),
	JmpIfBitSet(DIRECTIONAL_7046_7, ["EVENT_2418_summon_to_current_level_28"], identifier="EVENT_2418_jmp_if_bit_set_8"),
	JmpIfBitSet(DIRECTIONAL_7046_5, ["EVENT_2418_remove_from_current_level_40"]),
	JmpIfBitSet(DIRECTIONAL_7046_6, ["EVENT_2418_remove_from_current_level_46"]),
	ApplySolidityModToLevel(permanent=True, room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, mod_id=1),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_10),
	JmpIfRandom1of2(["EVENT_2418_jmp_if_random_above_128_19"]),
	RemoveObjectFromCurrentLevel(NPC_5),
	JmpIfRandom1of2(["EVENT_2418_jmp_if_random_above_128_21"], identifier="EVENT_2418_jmp_if_random_above_128_19"),
	RemoveObjectFromCurrentLevel(NPC_6),
	JmpIfRandom1of2(["EVENT_2418_jmp_if_random_above_128_23"], identifier="EVENT_2418_jmp_if_random_above_128_21"),
	RemoveObjectFromCurrentLevel(NPC_7),
	JmpIfRandom1of2(["EVENT_2418_jmp_if_random_above_128_25"], identifier="EVENT_2418_jmp_if_random_above_128_23"),
	RemoveObjectFromCurrentLevel(NPC_8),
	JmpIfRandom1of2(["EVENT_2418_jmp_27"], identifier="EVENT_2418_jmp_if_random_above_128_25"),
	RemoveObjectFromCurrentLevel(NPC_9),
	Jmp(["EVENT_2418_jmp_if_bit_clear_56"], identifier="EVENT_2418_jmp_27"),
	SummonObjectToCurrentLevel(NPC_2, identifier="EVENT_2418_summon_to_current_level_28"),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	JmpIfObjectNotInSpecificLevel(NPC_10, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["EVENT_2418_jmp_if_bit_clear_56"]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ShadowOn(),
		A_SetAllSpeeds(FASTEST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthPixels(12),
		A_WalkSouthwestPixels(5)
	]),
	SetSyncActionScript(NPC_10, A0947_FOREST_1ST_UNDERGROUND_RAT),
	Jmp(["EVENT_2418_jmp_if_bit_clear_56"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_2418_remove_from_current_level_40"),
	RemoveObjectFromCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_10),
	Jmp(["EVENT_2418_jmp_if_bit_clear_56"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_2418_remove_from_current_level_46"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	JmpIfBitClear(DIRECTIONAL_7047_1, ["EVENT_2418_fade_in_from_black_async_89"], identifier="EVENT_2418_jmp_if_bit_clear_56"),
	PlaySound(sound=SO019_LONG_FALL, channel=6, identifier="EVENT_2418_play_sound_57"),
	ClearBit(DIRECTIONAL_7047_1),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FloatingOff(),
		A_ShiftZUpSteps(16),
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=False),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_2418_action_queue_63_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_2418_action_queue_63_SUBSCRIPT_pause_2"])
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 233, ["EVENT_2418_set_7000_to_object_coord_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 235, ["EVENT_2418_action_queue_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 236, ["EVENT_2418_action_queue_74"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_2418_action_queue_76"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	]),
	Jmp(["EVENT_2418_action_queue_83"]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	], identifier="EVENT_2418_action_queue_72"),
	Jmp(["EVENT_2418_action_queue_83"]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	], identifier="EVENT_2418_action_queue_74"),
	Jmp(["EVENT_2418_action_queue_83"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	], identifier="EVENT_2418_action_queue_76"),
	Jmp(["EVENT_2418_action_queue_83"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True, identifier="EVENT_2418_set_7000_to_object_coord_78"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2418_action_queue_82"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	]),
	Jmp(["EVENT_2418_action_queue_83"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, looping=False)
	], identifier="EVENT_2418_action_queue_82"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(8)
	], identifier="EVENT_2418_action_queue_83"),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray(b'\xfd\x9c\n')),
		A_Walk1StepSouth()
	]),
	Pause(48),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_2418_fade_in_from_black_async_89"),
	Return()
])
