"""Non-Smithy final boss room EventScript snippets.

These scripts are used when the final boss is not Smithy.
- es_non_smithy_3792: Room setup script
- es_non_smithy_3794: Battle initiation script
"""

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    ActionQueueAsync,
    ActionQueueSync,
    ClearBit,
    EnterArea,
    FadeInFromBlack,
    FreezeCamera,
    InitiateBattleMask,
    Pause,
    PrioritySet,
    Return,
    RunEventAsSubroutine,
    RunEventAtReturn,
    SetBit,
    UnfreezeCamera,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_JmpIfMarioInAir,
    A_JumpToHeight,
    A_Pause,
    A_ResetProperties,
    A_SetSequenceSpeed,
    A_SetSpriteSequence,
    A_TransferToXYZF,
    A_VisibilityOff,
    A_Walk1StepNortheast,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
    NORMAL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    LAYER_3,
    MARIO,
    SCREEN_FOCUS,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import NORTHEAST, SOUTHEAST
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import (
    LAYER_L1,
    LAYER_L2,
    NPC_SPRITES,
)

from ...data.variables.event_script_names import (
    E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
    E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1,
    E0945_FINAL_BOSS_ANIMATION_SUBROUTINE_2,
    E0946_FINAL_BOSS_ANIMATION_SUBROUTINE_3,
    E3794_FACTORY_FINAL_BOSS_FIGHT,
)
from ...data.variables.room_names import R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE
from ...data.variables.variable_names import TEMP_7043_1, TEMP_7043_5


# Script for E3792 - Room setup for non-Smithy final boss
es_non_smithy_3792 = EventScript([
    SetBit(TEMP_7043_1, identifier="EVENT_3792_set_bit_0"),
    SetBit(TEMP_7043_5, identifier="EVENT_3792_set_bit_1"),
    ActionQueueSync(
        target=MARIO,
        subscript=[
            A_TransferToXYZF(
                x=3,
                y=23,
                z=0,
                direction=SOUTHEAST,
                identifier="EVENT_3792_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_0",
            ),
        ],
        identifier="EVENT_3792_action_queue_sync_5",
    ),
    FreezeCamera(identifier="EVENT_3792_freeze_camera_6"),
    ClearBit(TEMP_7043_1, identifier="EVENT_3792_clear_bit_29"),
    ClearBit(TEMP_7043_5, identifier="EVENT_3792_clear_bit_30"),
    RunEventAsSubroutine(
        E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
        identifier="EVENT_3792_sequence_setter_2",
    ),
    ActionQueueAsync(
        target=LAYER_3,
        subscript=[
            A_VisibilityOff(identifier="EVENT_3792_action_queue_sync_5_SUBSCRIPT_visibility_off"),
        ],
        identifier="EVENT_3792_red_thing",
    ),
    PrioritySet(
        mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
        subscreen=[],
        colour_math=[],
        identifier="EVENT_3792_red_thing_2",
    ),
    FadeInFromBlack(sync=False, identifier="EVENT_3792_fade_in_from_black_async_31"),
    RunEventAtReturn(
        E3794_FACTORY_FINAL_BOSS_FIGHT,
        identifier="EVENT_3792_run_event_at_return_32",
    ),
    Return(identifier="EVENT_3792_ret_33"),
])


# Script for E3794 - Battle initiation for non-Smithy final boss
es_non_smithy_3794 = EventScript([
    ActionQueueAsync(
        target=MARIO,
        subscript=[
            A_Pause(1, identifier="EVENT_3794_loop_pause_42"),
            A_JmpIfMarioInAir(
                ["EVENT_3794_loop_pause_42"],
                identifier="EVENT_3794_pause_42_",
            ),
            A_SetSpriteSequence(
                index=6,
                is_sequence=True,
                identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_1",
            ),
            A_Pause(10, identifier="EVENT_3794_loop_pause_42_b"),
            A_SetSequenceSpeed(
                FAST,
                identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_animation_speed_0",
            ),
            A_SetSpriteSequence(
                index=2,
                is_sequence=True,
                identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_1_b",
            ),
            A_Pause(30, identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_pause_2"),
            A_ResetProperties(
                identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_reset_properties_3"
            ),
            A_SetSequenceSpeed(
                NORMAL,
                identifier="EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_animation_speed_4",
            ),
        ],
        identifier="EVENT_3794_action_queue_sync_38",
    ),
    Pause(60, identifier="EVENT_3794_pause_42"),
    ActionQueueAsync(
        target=MARIO,
        subscript=[
            A_JumpToHeight(
                80,
                identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_jump_to_height_0",
            ),
            A_Pause(1, identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1"),
            A_JmpIfMarioInAir(
                ["EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1"],
                identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_jmp_if_mario_in_air_2",
            ),
            A_JumpToHeight(
                80,
                identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_jump_to_height_3",
            ),
            A_Pause(1, identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4"),
            A_JmpIfMarioInAir(
                ["EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4"],
                identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_jmp_if_mario_in_air_5",
            ),
        ],
        identifier="EVENT_3794_action_queue_async_51",
    ),
    Pause(30, identifier="EVENT_3794_pause_69"),
    ActionQueueAsync(
        target=MARIO,
        subscript=[
            A_SetSpriteSequence(
                index=6,
                is_sequence=True,
                identifier="EVENT_3794_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_4",
            ),
        ],
        identifier="EVENT_3794_action_queue_async_122",
    ),
    UnfreezeCamera(identifier="EVENT_3794_unfreeze_camera_128"),
    SetBit(TEMP_7043_5, identifier="EVENT_3794_set_bit_129"),
    ActionQueueSync(
        target=SCREEN_FOCUS,
        subscript=[
            A_Pause(20, identifier="EVENT_3794_action_queue_sync_132_SUBSCRIPT_pause_0"),
            A_SetSequenceSpeed(
                NORMAL,
                identifier="EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_animation_speed_1",
            ),
            A_Walk1StepNortheast(
                identifier="EVENT_3794_action_queue_sync_132_SUBSCRIPT_walk_1_step_northeast_2"
            ),
        ],
        identifier="EVENT_3794_action_queue_sync_132",
    ),
    RunEventAsSubroutine(
        E0946_FINAL_BOSS_ANIMATION_SUBROUTINE_3,
        identifier="EVENT_3794_animate_mario",
    ),
    RunEventAsSubroutine(
        E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1,
        identifier="EVENT_3794_animate_boss",
    ),
    RunEventAsSubroutine(
        E0945_FINAL_BOSS_ANIMATION_SUBROUTINE_2,
        identifier="EVENT_3794_wait",
    ),
    InitiateBattleMask(identifier="EVENT_3794_initiate_battle_mask_141"),
    EnterArea(
        room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
        face_direction=NORTHEAST,
        x=4,
        y=51,
        z=0,
        run_entrance_event=True,
        identifier="EVENT_3794_enter_area_142",
    ),
    Return(identifier="EVENT_3794_ret_143"),
])
