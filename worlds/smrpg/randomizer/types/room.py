"""Room type extension with extra sprite actions support."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
from smrpgpatchbuilder.datatypes.levels.classes import Room as RoomBase
from .ally import SpriteAnimationState

# Backwards compatibility alias - deprecated, use SpriteAnimationState directly
ExtraSpriteActions = SpriteAnimationState


class Room(RoomBase):
    """Extended Room class with extra_sprite_actions and adjacent_rooms support."""

    extra_sprite_actions: list[SpriteAnimationState]
    adjacent_rooms: list[int]  # List of adjacent room indices for EXP star buffer propagation

    def __init__(
        self,
        *args,
        extra_sprite_actions: list[SpriteAnimationState] | None = None,
        adjacent_rooms: list[int] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.extra_sprite_actions = extra_sprite_actions or []
        self.adjacent_rooms = adjacent_rooms or []

    def update_partition_by_protagonist(self, world: GameWorld) -> None:
        if self.partition is None:
            return
        if self.partition.ally_sprite_buffer_size == 0:
            return

        m = world.overworld_character.character_model
        ally = world.overworld_character.ally

        # Base animation sequences to always check
        vram_values = [
            m.min_vram_from_sequence(world, a[0], a[1])
            for a in [
                (0, 0),
                (1, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (3, 1),
                (4, 1),
                (5, 1),
                (6, 1),
                (7, 1),
                (8, 1),
                (9, 1),
            ]
        ]

        # Check extra sprite actions required by this room
        for state in self.extra_sprite_actions:
            if state not in ally._sprites_primary:
                continue
            tup = ally._sprites_primary[state]
            # Validate the sprite reference before using it
            sprite = world.get_sprite(m.base.sprite_id + tup[1])
            props = sprite.animation.properties
            if tup[2]:  # is_mold
                if tup[0] < len(props.molds):
                    vram_values.append(m.min_vram_from_mold(world, tup[0], tup[1]))
            else:
                if tup[0] < len(props.sequences):
                    vram_values.append(m.min_vram_from_sequence(world, tup[0], tup[1]))

        min_vram = max(vram_values) 
        self.partition.set_ally_sprite_buffer_size(max(min_vram, self.partition.ally_sprite_buffer_size))


    def update_partition_by_prize(self) -> None:
        """Update the room's partition based on its prize type."""
        pass
