# E3506_BOOSTER_HILL_GET_FLOWER
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
	JmpIfBitClear(TEMP_7044_1, ["EVENT_3506_disable_trigger_2"]),
	Return(),
	DisableObjectTrigger(NPC_8, identifier="EVENT_3506_disable_trigger_2"),
	StopBackgroundEvent(TIMER_701C),
	EnableControlsUntilReturn([]),

    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["summon_flower_1_"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["summon_flower_2_"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["summon_flower_3_"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["summon_flower_4_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["summon_flower_5_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["summon_flower_6_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["summon_flower_7_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["summon_flower_8_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["summon_flower_9_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["summon_flower_10_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["summon_flower_11_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["summon_flower_12_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["summon_flower_13_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["summon_flower_14_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["summon_flower_15_"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["summon_flower_16_"]),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P038_BOOSTER_HILL_PRIZE_0, MARIO, ["summon_flower_1__"], identifier="summon_flower_1_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_1__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P039_BOOSTER_HILL_PRIZE_1, MARIO, ["summon_flower_2__"], identifier="summon_flower_2_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_2__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P041_BOOSTER_HILL_PRIZE_2, MARIO, ["summon_flower_3__"], identifier="summon_flower_3_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_3__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P042_BOOSTER_HILL_PRIZE_3, MARIO, ["summon_flower_4__"], identifier="summon_flower_4_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_4__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P044_BOOSTER_HILL_PRIZE_4, MARIO, ["summon_flower_5__"], identifier="summon_flower_5_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_5__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P046_BOOSTER_HILL_PRIZE_5, MARIO, ["summon_flower_6__"],  identifier="summon_flower_6_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_6__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P057_BOOSTER_HILL_PRIZE_6, MARIO, ["summon_flower_7__"],  identifier="summon_flower_7_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_7__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P058_BOOSTER_HILL_PRIZE_7, MARIO, ["summon_flower_8__"],  identifier="summon_flower_8_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_8__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P059_BOOSTER_HILL_PRIZE_8, MARIO, ["summon_flower_9__"],  identifier="summon_flower_9_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_9__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P060_BOOSTER_HILL_PRIZE_9, MARIO, ["summon_flower_10__"],  identifier="summon_flower_10_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_10__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P061_BOOSTER_HILL_PRIZE_10, MARIO, ["summon_flower_11__"],  identifier="summon_flower_11_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_11__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P062_BOOSTER_HILL_PRIZE_11, MARIO, ["summon_flower_12__"],  identifier="summon_flower_12_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_12__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P063_BOOSTER_HILL_PRIZE_12, MARIO, ["summon_flower_13__"],  identifier="summon_flower_13_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_13__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P065_BOOSTER_HILL_PRIZE_13, MARIO, ["summon_flower_14__"],  identifier="summon_flower_14_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_14__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P066_BOOSTER_HILL_PRIZE_14, MARIO, ["summon_flower_15__"],  identifier="summon_flower_15_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_15__"),
    Jmp(["increment_70B1_final_2"]),
    CreatePacketAtObjectCoords(P068_BOOSTER_HILL_PRIZE_15, MARIO, ["summon_flower_16__"],  identifier="summon_flower_16_"),
    RunEventAsSubroutine(E0213_BOOSTER_HILL_PRIZE_CONTAINER_EVENT, identifier="summon_flower_16__"),
    
	Inc(BOOSTER_HILL_FLOWER_COUNTER, identifier="increment_70B1_final_2"),
	Pause(8),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_18"),
		A_WalkNorthPixels(4),
		A_WalkWestPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_19"),
		A_WalkWestPixels(8)
	], identifier="chapel_character_queue_11"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FixedFCoordOff(),
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, identifier="chapel_character_animation_20"),
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="chapel_character_animation_21"),
		A_WalkSouthPixels(8)
	], identifier="chapel_character_queue_12"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceNorthwest(),
		A_FixedFCoordOn()
	]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3506_action_queue_16"]),
	SetSyncActionScript(NPC_7, A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_FloatingOff(),
		A_SetAllSpeeds(FAST),
		A_JumpToHeight(height=112, silent=True),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_FloatingOn(),
		A_StartLoopNTimes(15),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(1),
		A_Dec(SECONDARY_TEMP_7024),
		A_EndLoop(),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_3506_action_queue_16"),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_3506_set_bit_19"]),
	SetTempSyncActionScript(NPC_7, A0718_BOOSTER_HILL_BOSS_MOVE_FORWARD),
	SetBit(TEMP_7043_7, identifier="EVENT_3506_set_bit_19"),
	EnableControlsUntilReturn([B]),
	ResumeBackgroundEvent(TIMER_701C),
	EnableObjectTrigger(NPC_8),
	Return()
])
