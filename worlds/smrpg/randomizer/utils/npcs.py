"""Utils for NPCs"""

from __future__ import annotations
from math import ceil
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite
from smrpgpatchbuilder.datatypes.levels.classes import NPC, VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import SOUTHWEST
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject, Direction
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import ActionQueueSync
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import A_SetSpriteSequence, A_Pause

from ..types.physical_objects import BossNPC, SpriteAnimationCollection

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def min_vram(number_of_tiles: int):
    """Get the expected min vram size from the given number of tiles."""
    return ceil(max(0, number_of_tiles - 4) / 4)


def is_swse_only(sprite: CompleteSprite):
    sequences = sprite.animation.properties.sequences
    if len(sequences) < 2:
        return False
    south = sequences[0]
    north = sequences[1]
    if len(north.frames) != len(south.frames):
        return False
    for comp1, comp2 in zip(south.frames, north.frames):
        if comp1.mold_id != comp2.mold_id:
            return False
    return True


def set_npc_direction_if_swse_only(
    world: GameWorld,
    room_id: int,
    npc_id: AreaObject,
    npc_base: NPC,
    direction: Direction = SOUTHWEST,
) -> None:
    """Set an NPC's direction to SOUTHWEST if its sprite only has SW/SE directions.

    This is useful when swapping NPCs with sprites that only support south-facing
    directions, ensuring they don't display incorrectly when facing north.

    Args:
        world: The game world.
        room_id: The room ID where the NPC is located.
        npc_id: The NPC's target ID within the room.
        npc_base: The NPC base model to check for direction constraints.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None
    obj = room.get_npc_by_target_id(npc_id)
    if obj is not None:
        sprite = world.sprites.sprites[npc_base.sprite_id]
        if npc_base.directions == VramStore.DIR2_SWSE or is_swse_only(sprite):
            obj.set_direction(direction)


def set_mines_punch_command(world: GameWorld, boss: BossNPC):
    contact_frame = 1  # Default to 1 (minimum valid pause duration)
    if boss.animations is None or boss.animations.mines_punch is None:
        world.event_scripts.delete_command_by_identifier("inner_mines_boss_shove_animation")
    else:
        collection = boss.animations.mines_punch
        contact_frame = max(1, collection.contact_frame or 1)  # Ensure at least 1
        sequence_id = collection.sequence_id
        sprite_id = boss.base.sprite_id
        sprite = world.sprites.sprites[sprite_id]
        num_sequences = len(sprite.animation.properties.sequences)
        assert sequence_id < num_sequences, (
            f"Mines punch animation error: {boss.__class__.__name__} references "
            f"sequence {sequence_id} but sprite {sprite_id} only has {num_sequences} sequences"
        )
        sequence = sprite.animation.properties.sequences[sequence_id]
        boss_pause_length = sequence.total_duration
        try:
            
            final_mold = sequence.frames[-1].mold_id
        except IndexError:
            raise Exception(
                f"Mines punch animation error: {boss.__class__.__name__} references "
                f"sequence {sequence_id} has {len(sequence.frames)} frames"
            )
        boss_animation = ActionQueueSync(target=NPC_0, subscript=[
            A_SetSpriteSequence(index=sequence_id, is_sequence=True, looping=False),
            A_Pause(boss_pause_length),
            A_SetSpriteSequence(index=final_mold, is_mold=True, is_sequence=True, looping=True)
        ])
        world.event_scripts.replace_command_by_identifier("inner_mines_boss_shove_animation", boss_animation)
    world.event_scripts.replace_subscript_command_by_identifier(
        "inner_mines_mario_shoved_backward",
        "inner_mines_mario_shoved_backward_duration",
        A_Pause(contact_frame)
    )
        