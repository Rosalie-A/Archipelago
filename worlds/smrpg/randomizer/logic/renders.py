"""Business logic for custom prize location render methods.

This module contains the extracted business logic from custom render methods
in prizelocations.py, organized by location/area.
"""

from __future__ import annotations

from ast import Return
from typing import TYPE_CHECKING, cast

from randomizer.progression.prizes import (
    ClerkBossFight,
    DirectorBossFight,
    ManagerBossFight,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_FaceNortheast,
    A_FaceNorthwest,
    A_FaceSoutheast,
    A_FaceSouthwest,
    A_Jmp,
    A_Pause,
    A_ResetProperties,
    A_ReturnQueue,
    A_SetBit,
    A_SetSequenceSpeed,
    A_SetSpriteSequence,
    A_ShiftXYPixels,
    A_ShiftZUpPixels,
    A_ShiftZUpSteps,
    A_StartLoopNTimes,
    A_WalkNorthPixels,
    A_WalkSouthPixels,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    NORMAL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_5,
    NPC_6,
    NPC_7,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    ActionQueueAsync,
    ActionQueueSync,
    RemoveObjectFromSpecificLevel,
    Pause,
)

from ..data.variables.action_script_names import (
    A0386_TOWER_SHOOT_BULLET_BILLS,
    A0576_CURTAIN_GAME_OPEN_CURTAIN,
    A0577_CURTAIN_GAME_OPEN_CURTAIN,
    A0962_FACTORY_3RD_BOSS_LEFT_HAMMER,
    A0963_FACTORY_3RD_BOSS_MID_HAMMER,
    A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER,
)
from ..data.variables.event_script_names import (
    E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
    E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
    E0936_PECK_SUBROUTINE_LEFT_STATUE,
    E0937_PECK_SUBROUTINE_MIDDLE_STATUE,
    E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1,
    E3792_FACTORY_FINAL_BOSS_ROOM_LOADER,
    E3794_FACTORY_FINAL_BOSS_FIGHT,
)
from ..data.variables.room_names import (
    R202_BOOSTER_TOWER_ENTRANCE,
    R254_BEAN_VALLEY_SMILAX_AREA,
    R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
)
from ..data.variables.variable_names import TEMP_7043_3
from ..types.physical_objects import BossNPC, SpriteAnimation
from ..types.prize import BossFightHenchman, BossFightPrize, CharacterPrize
from ..types.prizelocation import BossFightLocationNPC
from ..utils.npcs import is_swse_only
from ..utils.snippets.es_castle_statue_room_bonk import script as bonk
from ..utils.snippets.es_castle_statue_room_bonk_mario import script as bonk_mario
from ..utils.snippets.es_mimic_rise import get_mimic_rise_dojo
from ..utils.snippets.create_peck_subroutine import (
    gen_peck_left_subroutine,
    gen_peck_middle_subroutine,
    gen_start_battle,
)
from ..utils.snippets.es_non_smithy_final_boss import (
    es_non_smithy_3792,
    es_non_smithy_3794,
)
from ..types.ally import Ally, SpriteAnimationState

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

def update_ally_animation(seq: A_SetSpriteSequence, ally: Ally, anim: SpriteAnimationState) -> None:
    """Update an ally animation sequence command with the given animation.

    If no animation is provided, replace the command with a face direction
    command instead.
    """
    data = ally._sprites_secondary[anim]
    seq.set_is_mold(data[2])
    seq.set_index(data[1])
    seq.set_sprite_offset(data[0])


# =============================================================================
# Bandits Way
# =============================================================================


def render_bandits_way_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation script changes for Bandits Way boss fight."""
    m = prize.smallest_npc()
    bway = m.animations.bandits_way_distracted
    seq_id_replacements = [
        ("bway_aqueue_1", "bway_distracted_1"),
        ("bway_aqueue_2", "bway_distracted_2"),
        ("bway_aqueue_3", "bway_distracted_3"),
        ("bway_aqueue_4", "bway_distracted_4"),
        ("bway_aqueue_5", "bway_distracted_5"),
    ]
    for eid, aid in seq_id_replacements:
        e = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if bway:
            e.set_index(bway.sequence_id)
        else:
            if e.mirror_sprite:
                world.event_scripts.replace_subscript_command_by_identifier(
                    eid, aid, A_FaceSoutheast()
                )
            else:
                world.event_scripts.replace_subscript_command_by_identifier(
                    eid, aid, A_FaceSouthwest()
                )
    recoil = m.animations.recoil
    if recoil:
        a = world.action_scripts.get_command_by_identifier(
            "bandits_way_ascript_recoil", A_SetSpriteSequence
        )
        a.set_index(recoil.sequence_id)


# =============================================================================
# Forest Maze
# =============================================================================


def render_forest_maze_character_empty(world: GameWorld) -> None:
    """Remove character sprite animations when Toad substitute remains in place."""
    deletions = [
        "forest_character_animation_1",
        "forest_character_animation_2",
        "forest_character_animation_3",
        "forest_character_animation_4",
        "forest_character_animation_5",
        "forest_character_animation_6",
        "forest_character_animation_7",
        "forest_character_animation_8",
        "forest_character_animation_9",
        "forest_character_animation_10",
        "forest_character_animation_11",
    ]
    for d in deletions:
        world.action_scripts.delete_command_by_identifier(d)
    e = cast(
        ActionQueueAsync,
        world.event_scripts.get_command_by_identifier("forest_character_animation_14"),
    )
    ss = e.subscript
    cast(
        A_SetSpriteSequence,
        ss.get_command_by_name("forest_character_animation_13")[1],
    ).set_index(6)
    world.event_scripts.delete_subscript_command_by_identifier(
        "forest_character_animation_14", "forest_character_animation_11"
    )
    e.set_subscript(ss.contents)

def render_forest_maze_character(world: GameWorld, prize: CharacterPrize) -> None:
    ally = prize.ally
    a1 = world.action_scripts.get_command_by_identifier("forest_character_animation_1", A_SetSpriteSequence)
    update_ally_animation(a1, ally, SpriteAnimationState.SHAKING_HEAD)
    a3 = world.action_scripts.get_command_by_identifier("forest_character_animation_3", A_SetSpriteSequence)
    update_ally_animation(a3, ally, SpriteAnimationState.SHAKING_HEAD_BACKWARD)
    a5 = world.action_scripts.get_command_by_identifier("forest_character_animation_5", A_SetSpriteSequence)
    update_ally_animation(a5, ally, SpriteAnimationState.LOOKING_DOWN)
    a7 = world.action_scripts.get_command_by_identifier("forest_character_animation_7", A_SetSpriteSequence)
    update_ally_animation(a7, ally, SpriteAnimationState.SHAKING_HEAD_BACKWARD)
    a8 = world.action_scripts.get_command_by_identifier("forest_character_animation_8", A_SetSpriteSequence)
    update_ally_animation(a8, ally, SpriteAnimationState.SLEEPING)
    a9 = world.action_scripts.get_command_by_identifier("forest_character_animation_9", A_SetSpriteSequence)
    update_ally_animation(a9, ally, SpriteAnimationState.SHOCKED_BACKWARDS_SEQUENCE)

    e1 = world.event_scripts.get_subscript_command_by_identifier("forest_character_animation_14", "forest_character_animation_13", A_SetSpriteSequence)
    update_ally_animation(e1, ally, SpriteAnimationState.SOUTH)
    e2 = world.event_scripts.get_subscript_command_by_identifier("forest_character_animation_14", "forest_character_animation_11", A_SetSpriteSequence)
    update_ally_animation(e2, ally, SpriteAnimationState.DEFEND)
    



# =============================================================================
# Booster Tower
# =============================================================================


def render_booster_tower_indoor_boss(
    world: GameWorld,
    prize: BossFightPrize,
    npc_slots: list[BossFightLocationNPC],
    is_vanilla: bool,
) -> None:
    """Apply animation and sprite changes for Booster Tower indoor boss fight."""
    # Adjust the boss sprite behind the Booster Tower door
    entrance = next(
        (s for s in npc_slots if s.room_id == R202_BOOSTER_TOWER_ENTRANCE),
        None,
    )
    assert entrance is not None and entrance.sequence_setter_event_id is not None
    ev = world.event_scripts.get_script_by_id(entrance.sequence_setter_event_id)
    from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
        UsableActionScriptCommand,
    )

    as_contents: list[UsableActionScriptCommand] = []
    m = prize.smallest_npc()
    if m.tower_entrance_horizontal_shift:
        as_contents.append(A_ShiftXYPixels(m.tower_entrance_horizontal_shift, 0))
    if m.eye_height:
        as_contents.append(A_ShiftZUpPixels(m.eye_height))
    if len(as_contents) > 0:
        ev.set_contents(
            [
                ActionQueueAsync(entrance.npc_id, as_contents),
                *ev.contents,
            ]
        )

    # Crown height in the chapel
    ev_crown = world.event_scripts.get_subscript_command_by_identifier(
        "crown_adjust_height_aq", "crown_adjust_height", A_ShiftZUpSteps
    )
    ev_crown.set_steps(m.crown_height)

    # Exit here if vanilla
    if is_vanilla:
        return

    # Chapel laugh animation
    anim = m.animations.chapel_laugh
    seq_id_replacements = [
        ("tower_boss_laughing_aqueue_1", "tower_boss_laughing_seq_1"),
        ("tower_boss_laughing_aqueue_2", "tower_boss_laughing_seq_2"),
        ("tower_boss_laughing_aqueue_3", "tower_boss_laughing_seq_3"),
    ]
    for eid, aid in seq_id_replacements:
        e = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if anim:
            e.set_index(anim.sequence_id)
        elif e.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSoutheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSouthwest()
            )

    # Delete henchman curtain animations
    deletions = [
        ("tower_boss_crying_aq_1", "tower_boss_crying_1"),
        ("tower_henchman_curtain_aqueue_1", "tower_henchman_curtain_1"),
        ("tower_henchman_curtain_aqueue_2", "tower_henchman_curtain_2"),
        ("tower_henchman_curtain_aqueue_3", "tower_henchman_curtain_3"),
        ("tower_henchman_curtain_aqueue_4", "tower_henchman_curtain_4"),
        ("tower_henchman_curtain_aqueue_5", "tower_henchman_curtain_5"),
        ("tower_henchman_curtain_aqueue_6", "tower_henchman_curtain_6"),
        ("tower_henchman_curtain_aqueue_7", "tower_henchman_curtain_7"),
        ("tower_henchman_curtain_aqueue_8", "tower_henchman_curtain_8"),
        ("tower_henchman_curtain_aqueue_9", "tower_henchman_curtain_9"),
        ("tower_henchman_curtain_aqueue_10", "tower_henchman_curtain_10"),
        ("tower_henchman_curtain_aqueue_11", "tower_henchman_curtain_11"),
        ("tower_henchman_curtain_aqueue_12", "tower_henchman_curtain_12"),
        ("tower_henchman_curtain_aqueue_13", "tower_henchman_curtain_13"),
        ("tower_henchman_curtain_aqueue_14", "tower_henchman_curtain_14"),
        ("tower_henchman_curtain_aqueue_15", "tower_henchman_curtain_15"),
        ("tower_henchman_curtain_aqueue_16", "tower_henchman_curtain_16"),
        ("tower_henchman_curtain_aqueue_17", "tower_henchman_curtain_17"),
        ("tower_henchman_curtain_aqueue_18", "tower_henchman_curtain_18"),
        ("tower_henchman_curtain_aqueue_19", "tower_henchman_curtain_19"),
        ("tower_henchman_curtain_aqueue_20", "tower_henchman_curtain_20"),
        ("tower_henchman_curtain_aqueue_21", "tower_henchman_curtain_21"),
        ("tower_henchman_curtain_aqueue_22", "tower_henchman_curtain_22"),
        ("tower_henchman_curtain_aqueue_23", "tower_henchman_curtain_23"),
        ("tower_henchman_curtain_aqueue_24", "tower_henchman_curtain_24"),
        ("tower_henchman_curtain_aqueue_25", "tower_henchman_curtain_25"),
        ("tower_henchman_curtain_aqueue_26", "tower_henchman_curtain_26"),
        ("tower_henchman_curtain_aqueue_27", "tower_henchman_curtain_27"),
        ("tower_henchman_curtain_aqueue_28", "tower_henchman_curtain_28"),
        ("tower_henchman_curtain_aqueue_29", "tower_henchman_curtain_29"),
        ("tower_henchman_curtain_aqueue_30", "tower_henchman_curtain_30"),
        ("tower_henchman_curtain_aqueue_31", "tower_henchman_curtain_31"),
        ("tower_henchman_curtain_aqueue_32", "tower_henchman_curtain_32"),
        ("tower_henchman_curtain_aqueue_33", "tower_henchman_curtain_33"),
        ("tower_henchman_curtain_aqueue_34", "tower_henchman_curtain_34"),
        ("tower_henchman_curtain_aqueue_35", "tower_henchman_curtain_35"),
        ("tower_henchman_curtain_aqueue_36", "tower_henchman_curtain_36"),
        ("tower_henchman_curtain_aqueue_37", "tower_henchman_curtain_37"),
        ("tower_henchman_curtain_aqueue_38", "tower_henchman_curtain_38"),
        ("tower_henchman_curtain_aqueue_39", "tower_henchman_curtain_39"),
        ("tower_henchman_curtain_aqueue_39", "tower_henchman_curtain_40"),
    ]
    for eid, aid in deletions:
        world.event_scripts.delete_subscript_command_by_identifier(eid, aid)

    # T-pose replacements
    tpose_replacements = [("chapel_tpose_queue_1", "chapel_tpose_1")]
    for eid, aid in tpose_replacements:
        a = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if m.animations.tpose_mold_id is not None:
            a.set_index(m.animations.tpose_mold_id)
        elif a.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceNortheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceNorthwest()
            )

    # Stare up replacements
    stare_up_replacements = [
        ("chapel_stare_up_queue_1", "chapel_stare_up_1"),
        ("chapel_stare_up_queue_2", "chapel_stare_up_2"),
        ("chapel_stare_up_queue_3", "chapel_stare_up_3"),
        ("chapel_stare_up_queue_4", "chapel_stare_up_4"),
    ]
    for eid, aid in stare_up_replacements:
        a = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if m.animations.look_at_ceiling_mold_id is not None:
            a.set_index(m.animations.look_at_ceiling_mold_id)
        elif a.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSoutheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSouthwest()
            )

    # Tower toss animation
    if m.animations.tower_toss is not None:
        tower_toss = m.animations.tower_toss
        from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
            Pause,
        )
        from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
            NPC_6,
        )

        pause_length = (
            tower_toss.contact_frame
            if tower_toss.contact_frame is not None
            else tower_toss.total_duration or 0
        )
        cast(
            Pause,
            world.event_scripts.get_command_by_identifier("tower_toss_contact_frame"),
        ).set_length(pause_length + 30)
        world.event_scripts.replace_command_by_identifier(
            "tower_toss_aqueue",
            ActionQueueSync(
                target=NPC_6,
                subscript=[
                    A_FaceSouthwest(),
                    A_Pause(30),
                    A_SetSpriteSequence(index=tower_toss.sequence_id, is_sequence=True),
                ],
                identifier="tower_toss_aqueue",
            ),
        )

    # Door height adjustment
    door_height = 15 - m.eye_height
    if door_height < 0:
        world.event_scripts.get_script_by_id(
            E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER
        ).insert_before_nth_command(
            0, ActionQueueAsync(NPC_1, [A_WalkSouthPixels(door_height * -1)])
        )
    elif door_height > 0:
        world.event_scripts.get_script_by_id(
            E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER
        ).insert_before_nth_command(
            0, ActionQueueAsync(NPC_1, [A_WalkNorthPixels(door_height)])
        )


def render_booster_tower_henchman_scripts(
    world: GameWorld,
    prize: BossFightPrize,
    henchmen_count: int,
) -> None:
    """Apply henchman-related script changes for Booster Tower."""
    # Remove special snifit sprites that other henchmen don't have
    if henchmen_count >= 3:
        world.action_scripts.replace_script(
            A0576_CURTAIN_GAME_OPEN_CURTAIN,
            ActionScript([A_FaceNorthwest(), A_Pause(12), A_ReturnQueue()]),
        )
        world.action_scripts.replace_script(
            A0577_CURTAIN_GAME_OPEN_CURTAIN,
            ActionScript(
                [
                    A_FaceNorthwest(),
                    A_Pause(17),
                    A_ResetProperties(),
                    A_FaceNorthwest(),
                    A_ReturnQueue(),
                ]
            ),
        )

        # Hill sprite replacements
        hill_ids = [
            "hill_sprite_set_1",
            "hill_sprite_set_2",
            "hill_sprite_set_3",
            "hill_sprite_set_4",
            "hill_sprite_set_5",
        ]
        for h in hill_ids:
            world.action_scripts.replace_command_by_identifier(h, A_FaceNorthwest())

        # Third henchman tower bullet animation
        if prize.character_henchmen is not None and len(prize.character_henchmen) >= 3:
            third_henchman = prize.character_henchmen[2]
            third_henchman_animations = third_henchman.model()._animations
            b = third_henchman_animations.tower_bullet
            if b is not None and b.total_duration is not None:
                pelim_pause = 0
                contact_frame = b.contact_frame
                if contact_frame is None:
                    contact_frame = b.total_duration // 2
                if contact_frame < 56:
                    pelim_pause = 56 - contact_frame
                interval_after_shot = min(40, b.total_duration - contact_frame)
                final_interval = max(0, 96 - b.total_duration - pelim_pause)

                world.action_scripts.replace_script(
                    A0386_TOWER_SHOOT_BULLET_BILLS,
                    script=ActionScript(
                        [
                            A_FaceSoutheast(),
                            A_Pause(18),
                            A_FaceSouthwest(),
                            A_Pause(18),
                            *(
                                [
                                    A_Pause(
                                        pelim_pause,
                                        identifier="ACTION_386_set_sprite_sequence_4",
                                    ),
                                    A_SetSpriteSequence(
                                        index=b.sequence_id,
                                        is_sequence=True,
                                        looping=False,
                                    ),
                                ]
                                if pelim_pause > 0
                                else [
                                    A_SetSpriteSequence(
                                        index=b.sequence_id,
                                        is_sequence=True,
                                        looping=False,
                                        identifier="ACTION_386_set_sprite_sequence_4",
                                    )
                                ]
                            ),
                            A_Pause(contact_frame),
                            A_SetBit(TEMP_7043_3),
                            *(
                                [A_Pause(interval_after_shot)]
                                if interval_after_shot > 0
                                else []
                            ),
                            A_SetSpriteSequence(
                                index=0,
                                is_sequence=True,
                                looping=True,
                            ),
                            A_Pause(final_interval),
                            A_Jmp(["ACTION_386_set_sprite_sequence_4"]),
                        ]
                    ),
                )
            else:
                pelim_pause = 0
                if b is not None and b.total_duration is not None:
                    pelim_pause = 56 - (b.total_duration / 2)

                world.action_scripts.replace_script(
                    A0386_TOWER_SHOOT_BULLET_BILLS,
                    script=ActionScript(
                        [
                            A_FaceSoutheast(),
                            A_Pause(18),
                            A_FaceSouthwest(),
                            A_Pause(18),
                            A_Pause(
                                56,
                                identifier="ACTION_386_set_sprite_sequence_4",
                            ),
                            A_SetBit(TEMP_7043_3),
                            A_Pause(40),
                            A_Jmp(["ACTION_386_set_sprite_sequence_4"]),
                        ]
                    ),
                )


# =============================================================================
# Marrymore
# =============================================================================


def render_marrymore_boss_henchmen(
    world: GameWorld,
    henchmen: list[BossFightHenchman],
) -> None:
    """Apply henchman animation changes for Marrymore boss fight."""
    if len(henchmen) >= 1:
        first_henchman = henchmen[0]
        henchman_animations = first_henchman.model()._animations
        if henchman_animations.kitchen_prep is not None:
            cmd = world.action_scripts.get_command_by_identifier(
                "kitchen_chef_seq_1", A_SetSpriteSequence
            )
            cmd.set_index(henchman_animations.kitchen_prep.sequence_id)
        else:
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_1")

    if len(henchmen) >= 2:
        second_henchman = henchmen[1]
        henchman_animations = second_henchman.model()._animations
        if henchman_animations.kitchen_prep is not None:
            for cmd_id in ["kitchen_chef_seq_2", "kitchen_chef_seq_3"]:
                cmd = world.action_scripts.get_command_by_identifier(
                    cmd_id, A_SetSpriteSequence
                )
                cmd.set_index(henchman_animations.kitchen_prep.sequence_id)
        else:
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_2")
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_3")


def render_marrymore_character_empty(world: GameWorld) -> None:
    """Remove character sprite animations when Toad substitute remains in chapel."""
    deletions: list[tuple[str, list[str]]] = [
        (
            "chapel_character_queue_1",
            ["chapel_character_animation_1", "chapel_character_animation_2"],
        ),
        ("chapel_character_queue_2", ["chapel_character_animation_3"]),
        ("chapel_character_queue_3", []),
        (
            "chapel_character_queue_4",
            ["chapel_character_animation_4", "chapel_character_animation_5"],
        ),
        ("chapel_character_queue_5", ["chapel_character_animation_6"]),
        ("chapel_character_queue_6", ["chapel_character_animation_7"]),
        (
            "chapel_character_queue_7",
            ["chapel_character_animation_8", "chapel_character_animation_9"],
        ),
        (
            "chapel_character_queue_8",
            ["chapel_character_animation_10", "chapel_character_animation_11"],
        ),
        ("chapel_character_queue_9", ["chapel_character_animation_12"]),
        (
            "EVENT_3499_action_queue_42",
            ["chapel_character_animation_13", "chapel_character_animation_14"],
        ),
        (
            "EVENT_3499_action_queue_45",
            ["chapel_character_animation_15", "chapel_character_animation_16"],
        ),
        ("chapel_character_queue_10", ["chapel_character_animation_17"]),
        (
            "chapel_character_queue_11",
            ["chapel_character_animation_18", "chapel_character_animation_19"],
        ),
        (
            "chapel_character_queue_12",
            ["chapel_character_animation_20", "chapel_character_animation_21"],
        ),
    ]
    for queue, actions in deletions:
        if len(actions) == 0:
            world.event_scripts.delete_command_by_identifier(queue)
        else:
            e = cast(
                ActionQueueAsync,
                world.event_scripts.get_command_by_identifier(queue),
            )
            ss = e.subscript
            for action in actions:
                idx = ss.get_index_of_identifier(action)
                ss.delete_at_index(idx)
            e.set_subscript(ss.contents)
            
def render_marrymore_character(world: GameWorld, prize: CharacterPrize) -> None:
    ally = prize.ally

    a1 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_1", "chapel_character_animation_1", A_SetSpriteSequence)
    update_ally_animation(a1, ally, SpriteAnimationState.SHOCKED_LOOP)
    a2 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_1", "chapel_character_animation_2", A_SetSpriteSequence)
    update_ally_animation(a2, ally, SpriteAnimationState.FLOORED)
    a3 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_2", "chapel_character_animation_3", A_SetSpriteSequence)
    update_ally_animation(a3, ally, SpriteAnimationState.HURT)
    a4 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_3", "chapel_character_queue_3_", A_SetSpriteSequence)
    update_ally_animation(a4, ally, SpriteAnimationState.LOOKING_DOWN_STATIC)
    a5 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_4", "chapel_character_animation_4", A_SetSpriteSequence)
    update_ally_animation(a5, ally, SpriteAnimationState.SHAKING_HEAD)
    a6 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_4", "chapel_character_animation_5", A_SetSpriteSequence)
    update_ally_animation(a6, ally, SpriteAnimationState.LOOKING_DOWN_STATIC)
    a7 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_5", "chapel_character_animation_6", A_SetSpriteSequence)
    update_ally_animation(a7, ally, SpriteAnimationState.CRYING)
    a8 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_6", "chapel_character_animation_7", A_SetSpriteSequence)
    update_ally_animation(a8, ally, SpriteAnimationState.SHOCKED_LOOP)
    a9 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_7", "chapel_character_animation_9", A_SetSpriteSequence)
    update_ally_animation(a9, ally, SpriteAnimationState.LOOKING_DOWN_STATIC)
    a10 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_7", "chapel_character_animation_8", A_SetSpriteSequence)
    update_ally_animation(a10, ally, SpriteAnimationState.CRYING)
    a11 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_8", "chapel_character_animation_10", A_SetSpriteSequence)
    update_ally_animation(a11, ally, SpriteAnimationState.SHOCKED_LOOP)
    a12 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_8", "chapel_character_animation_11", A_SetSpriteSequence)
    update_ally_animation(a12, ally, SpriteAnimationState.CRYING_BACKWARDS)
    a13 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_9", "chapel_character_animation_12", A_SetSpriteSequence)
    update_ally_animation(a13, ally, SpriteAnimationState.SHOCKED_LOOP)
    a14 = world.event_scripts.get_subscript_command_by_identifier("EVENT_3499_action_queue_42", "chapel_character_animation_13", A_SetSpriteSequence)
    update_ally_animation(a14, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a15 = world.event_scripts.get_subscript_command_by_identifier("EVENT_3499_action_queue_42", "chapel_character_animation_14", A_SetSpriteSequence)
    update_ally_animation(a15, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a16 = world.event_scripts.get_subscript_command_by_identifier("EVENT_3499_action_queue_45", "chapel_character_animation_15", A_SetSpriteSequence)
    update_ally_animation(a16, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a17 = world.event_scripts.get_subscript_command_by_identifier("EVENT_3499_action_queue_45", "chapel_character_animation_16", A_SetSpriteSequence)
    update_ally_animation(a17, ally, SpriteAnimationState.SHOCKED_LOOP)
    a18 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_10", "chapel_character_animation_17", A_SetSpriteSequence)
    update_ally_animation(a18, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a19 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_11", "chapel_character_animation_18", A_SetSpriteSequence)
    update_ally_animation(a19, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a20 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_11", "chapel_character_animation_19", A_SetSpriteSequence)
    update_ally_animation(a20, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a21 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_12", "chapel_character_animation_20", A_SetSpriteSequence)
    update_ally_animation(a21, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS)
    a22 = world.event_scripts.get_subscript_command_by_identifier("chapel_character_queue_12", "chapel_character_animation_21", A_SetSpriteSequence)
    update_ally_animation(a22, ally, SpriteAnimationState.SHOCKED_LOOP)
    


# =============================================================================
# Seaside / Ship
# =============================================================================


def render_seaside_beach_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Seaside Beach boss fight."""
    m = prize.smallest_npc()

    # large boss sprite
    world.event_scripts.delete_subscript_command_by_identifier(
        "seaside_boss_reveal_sequence", "seaside_boss_reveal_sequence_1"
    )


def render_ship_password_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Password boss fight."""
    world.action_scripts.delete_command_by_identifier("password_boss_vanilla_1")
    world.action_scripts.delete_command_by_identifier("password_boss_vanilla_2")
    m = prize.smallest_npc()
    if m.animations.ship_beckon is not None:
        c = world.action_scripts.get_command_by_identifier(
            "password_boss_reveal_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_beckon.sequence_id)
    else:
        world.action_scripts.delete_command_by_identifier(
            "password_boss_reveal_sequence"
        )


def render_ship_final_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Final boss fight."""
    m = prize.smallest_npc()
    # boss room on revisit
    if m.animations.ship_chair is not None:
        c = world.action_scripts.get_command_by_identifier(
            "ship_boss_idle_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_chair.sequence_id)
    else:
        world.action_scripts.replace_command_by_identifier(
            "ship_boss_idle_sequence", A_FaceSouthwest()
        )
        world.action_scripts.delete_command_by_identifier(
            "ship_boss_idle_sequence_loop"
        )

    # ending credits
    if m.animations.tpose_mold_id is not None:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_SetSpriteSequence(index=m.animations.tpose_mold_id, is_mold=True),
        )
    else:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_FaceNorthwest(),
        )

    # Delete event script commands for unfilled character henchman slots
    assigned_count = (
        len(prize.character_henchmen) if prize.character_henchmen is not None else 0
    )
    if assigned_count > 0 and assigned_count < 2:
        # Slot 0 unfilled
        if assigned_count < 1:
            for d in [
                "ship_henchman_1_beach_1",
                "ship_henchman_1_beach_2",
                "ship_henchman_1_beach_3",
            ]:
                world.event_scripts.delete_command_by_identifier(d)
        # Slot 1 unfilled
        if assigned_count < 2:
            world.event_scripts.delete_command_by_identifier("ship_henchman_2_beach_1")


# =============================================================================
# Dojo
# =============================================================================


def render_dojo_first_fight(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Dojo first fight."""
    m = prize.smallest_npc()
    # Check if prize is a mimic-type boss
    from ..progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier("dojo_boss_1_initiate_aq"),
        ).set_subscript(get_mimic_rise_dojo())
    elif m.animations.dojo_challenge is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "dojo_boss_1_initiate_aq",
            "dojo_boss_1_initiate",
            A_SetSpriteSequence,
        ).set_index(m.animations.dojo_challenge.sequence_id)
        if m.animations.dojo_challenge.contact_frame is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                "dojo_boss_1_initiate_aq", "dojo_boss_1_pause", A_Pause
            ).set_length(m.animations.dojo_challenge.contact_frame)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "dojo_boss_1_initiate_aq", "dojo_boss_1_initiate"
        )
    world.event_scripts.replace_subscript_command_by_identifier(
        "EVENT_2067_action_queue_0", "jagger_looks_around", A_FaceNorthwest()
    )


def render_dojo_fight(
    world: GameWorld,
    prize: BossFightPrize,
    initiate_aq_id: str,
    initiate_id: str,
    pause_id: str,
) -> None:
    """Apply animation changes for a generic Dojo fight."""
    m = prize.smallest_npc()
    from ..progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier(initiate_aq_id),
        ).set_subscript(get_mimic_rise_dojo())
    elif m.animations.dojo_challenge is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            initiate_aq_id,
            initiate_id,
            A_SetSpriteSequence,
        ).set_index(m.animations.dojo_challenge.sequence_id)
        if m.animations.dojo_challenge.contact_frame is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id, pause_id, A_Pause
            ).set_length(m.animations.dojo_challenge.contact_frame)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            initiate_aq_id, initiate_id
        )


# =============================================================================
# Bean Valley
# =============================================================================


def render_bean_valley_planter_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply NPC position changes for Bean Valley Planter boss fight."""
    room = world.rooms._rooms[R254_BEAN_VALLEY_SMILAX_AREA]
    assert room is not None
    thrax = room.get_npc_by_target_id(NPC_0)
    thrax.set_visible(False)
    boss = room.get_npc_by_target_id(NPC_1)
    boss.set_x(thrax.x)
    boss.set_y(thrax.y)
    boss.set_z(thrax.z)

    world.event_scripts.get_script_by_id(
        E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
    ).insert_before_nth_command(
        0, RemoveObjectFromSpecificLevel(NPC_0, R254_BEAN_VALLEY_SMILAX_AREA)
    )


# =============================================================================
# Nimbus Castle / Statue Room
# =============================================================================


def render_statue_room_boss(
    world: GameWorld,
    prize: BossFightPrize,
    keep_minigame_sprites: bool,
) -> None:
    """Apply animation changes for Statue Room boss fight."""
    # wedding ending
    world.event_scripts.delete_subscript_command_by_identifier(
        "wedding_ending_aq", "wedding_ending_shift"
    )
    if keep_minigame_sprites:
        return

    # statue game
    # Use VRAM-constrained selection (max 6144 for statue room)
    mo = prize.get_npc_for_slot(world, 6144)
    m = mo()
    if m.animations.statue_peck is None:
        world.event_scripts.get_script_by_id(
            E0936_PECK_SUBROUTINE_LEFT_STATUE
        ).set_contents(bonk.contents)
        world.event_scripts.get_script_by_id(
            E0937_PECK_SUBROUTINE_MIDDLE_STATUE
        ).set_contents(bonk_mario.contents)
        cast(
            ActionQueueSync,
            world.event_scripts.get_command_by_identifier("dodo_starts_battle"),
        ).set_subscript(
            [
                A_FaceSouthwest(),
                A_Pause(160),
            ]
        )
    else:
        world.event_scripts.get_script_by_id(
            E0936_PECK_SUBROUTINE_LEFT_STATUE
        ).set_contents(gen_peck_left_subroutine(m.animations.statue_peck).contents)
        world.event_scripts.get_script_by_id(
            E0937_PECK_SUBROUTINE_MIDDLE_STATUE
        ).set_contents(
            gen_peck_middle_subroutine(m.animations.statue_peck).contents
        )
        cast(
            ActionQueueSync,
            world.event_scripts.get_command_by_identifier("dodo_starts_battle"),
        ).set_subscript(
            gen_start_battle(
                world.get_sprite(m.base.sprite_id), m.animations.statue_peck
            )
        )

    if m.animations.look_at_ceiling_mold_id is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_introduced_aq",
            "statue_keeper_introduced_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.look_at_ceiling_mold_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_introduced_aq", "statue_keeper_introduced_1"
        )

    if m.animations.statue_flustered is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_flustered_aq",
            "statue_keeper_flustered_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.statue_flustered.sequence_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_flustered_aq", "statue_keeper_flustered_1"
        )

    spr = world.sprites.sprites[m.base.sprite_id]
    assert spr is not None
    has_walking_sequence = len(spr.animation.properties.sequences[0].frames) >= 2
    has_back_walking_sequence = len(spr.animation.properties.sequences) > 1 and len(
        spr.animation.properties.sequences[1].frames
    ) >= 2 and not is_swse_only(spr)

    # walking from statue to statue
    for aq, id in [("EVENT_3640_action_queue_271", "dodo_extra_sprite_1")]:
        if has_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq,
                id,
                A_SetSpriteSequence(
                    index=2,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                ),
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("EVENT_3640_action_queue_273", "dodo_extra_sprite_2")]:
        if has_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq,
                id,
                A_SetSpriteSequence(
                    index=1,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                ),
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("EVENT_3640_action_queue_304", "dodo_left_forward")]:
        if has_back_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq, id, A_SetSpriteSequence(index=4, is_mold=True)
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("EVENT_3640_action_queue_306", "dodo_right_forward")]:
        if has_back_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq, id, A_SetSpriteSequence(index=5, is_mold=True)
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    # head-shake
    for aq, id in [
        ("dodo_shake_head_aq", "dodo_shake_head_1"),
        ("dodo_shake_head_aq", "dodo_shake_head_2"),
    ]:
        world.event_scripts.replace_subscript_command_by_identifier(
            aq,
            id,
            A_SetSpriteSequence(index=0, is_mold=True, mirror_sprite=True),
        )

    # finished deletions
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq", "dodo_finished_1"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq_2", "dodo_finished_2"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq_3", "dodo_finished_3"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_possibly_unused_aq", "dodo_possibly_unused"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "final_statue_peck_aq", "dodo_fakeout_1"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "final_statue_peck_aq", "dodo_fakeout_2"
    )


# =============================================================================
# Volcano
# =============================================================================


def render_volcano_exit_boss(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply henchman slot event script changes for Volcano Exit boss fight."""

    def slot_has_henchman(slot_index: int) -> bool:
        return (
            prize.character_henchmen is not None
            and len(prize.character_henchmen) > slot_index
        )

    loops = 0

    # Slot 0
    if not slot_has_henchman(0):
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_2")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_3")
    else:
        loops += 1

    # Slot 1
    if not slot_has_henchman(1):
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq_2")
    else:
        loops += 1

    # Slot 2
    if not slot_has_henchman(2):
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq_2")
    else:
        loops += 1

    # Slot 3
    if not slot_has_henchman(3):
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq_2")
    else:
        loops += 1

    if loops == 0:
        world.event_scripts.delete_command_by_identifier("axem_trampoline_aqueue")
    else:
        # Get the loop command and set its count (don't delete it)
        world.event_scripts.get_subscript_command_by_identifier(
            "axem_trampoline_aqueue",
            "axem_trampoline_loop",
            A_StartLoopNTimes,
        ).set_count(loops)


# =============================================================================
# Inner Factory
# =============================================================================


def render_inner_factory_second_fight(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply look-up animation changes for Inner Factory Second Fight."""
    if isinstance(prize, (ClerkBossFight, ManagerBossFight, DirectorBossFight)):
        return
    m = prize.smallest_npc()
    look_up_replacements = [
        ("factory_2nd_boss_look_up_aq_1", "factory_2nd_boss_look_up_1"),
        ("factory_2nd_boss_look_up_aq_2", "factory_2nd_boss_look_up_2"),
        ("factory_2nd_boss_look_up_aq_3", "factory_2nd_boss_look_up_3"),
    ]
    for eid, aid in look_up_replacements:
        if m.animations.look_at_ceiling_mold_id is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                eid, aid, A_SetSpriteSequence
            ).set_index(m.animations.look_at_ceiling_mold_id)
        else:
            world.event_scripts.delete_subscript_command_by_identifier(eid, aid)


def render_inner_factory_third_fight_slot(
    world: GameWorld,
    henchman: BossFightHenchman,
    slot_index: int,
) -> None:
    """Apply factory pierce animation for a single henchman slot."""
    anim = henchman.model()._animations.factory_pierce

    slot_configs = [
        (
            A0962_FACTORY_3RD_BOSS_LEFT_HAMMER,
            "factory_3rd_boss_left_hammer_attack",
            "factory_3rd_boss_left_hammer_attack_pause_32",
        ),
        (
            A0963_FACTORY_3RD_BOSS_MID_HAMMER,
            "factory_3rd_boss_mid_hammer_attack",
            "factory_3rd_boss_mid_hammer_attack_pause_32",
        ),
        (
            A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER,
            "factory_3rd_boss_right_hammer_attack",
            "factory_3rd_boss_right_hammer_attack_pause_32",
        ),
    ]

    if slot_index >= len(slot_configs):
        return

    script_id, attack_id, pause_id = slot_configs[slot_index]

    if (
        anim is not None
        and anim.total_duration is not None
        and anim.contact_frame is not None
    ):
        prepause = 32 - anim.total_duration
        world.action_scripts.get_command_by_identifier(
            attack_id, A_SetSpriteSequence
        ).set_index(anim.sequence_id)
        world.action_scripts.get_command_by_identifier(pause_id, A_Pause).set_length(
            anim.contact_frame
        )
        if anim.speed is not NORMAL:
            world.action_scripts.scripts[script_id].insert_before_identifier(
                attack_id, A_SetSequenceSpeed(anim.speed)
            )
        world.action_scripts.scripts[script_id].insert_before_identifier(
            attack_id, A_Pause(prepause)
        )


def render_inner_factory_fourth_fight(world: GameWorld) -> None:
    """Hide NPCs 0-6 in Gun Yolk's room for non-vanilla boss."""
    room = world.rooms._rooms[R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    assert room is not None
    for npc_id in [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
        obj = room.get_npc_by_target_id(npc_id)
        if obj is not None:
            obj.set_visible(False)


def render_final_boss_fight(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply animation changes for Final Boss fight."""

    e3792 = world.event_scripts.get_script_by_id(E3792_FACTORY_FINAL_BOSS_ROOM_LOADER)
    e3794 = world.event_scripts.get_script_by_id(E3794_FACTORY_FINAL_BOSS_FIGHT)
    e3792.set_contents(es_non_smithy_3792.contents)
    e3794.set_contents(es_non_smithy_3794.contents)

    anim = prize.largest_npc().animations.endgame_challenge
    if anim is not None:
        if anim.total_duration is not None and anim.total_duration > 55:
            cast(
                Pause, world.event_scripts.get_command_by_identifier("final_boss_pause")
            ).set_length(anim.total_duration)
            cast(
                ActionQueueSync,
                world.event_scripts.get_command_by_identifier("final_boss_mario_rise"),
            ).subscript.insert_before_nth_command(0, A_Pause(anim.total_duration - 55))
        world.event_scripts.get_script_by_id(
            E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1
        ).insert_before_nth_command(
            0,
            ActionQueueSync(
                NPC_0,
                [
                    A_SetSpriteSequence(
                        index=anim.sequence_id,
                        is_sequence=True,
                    )
                ],
            ),
        )
