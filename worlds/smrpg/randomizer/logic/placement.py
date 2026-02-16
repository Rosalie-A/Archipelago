"""Core placement algorithms for randomizer."""
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import random
from copy import copy

from ..types.prizelocation import FrogDiscipleLocation, StarPieceLocation
from ..types.logic import Inventory
from ..types.prize import StarPiecePrize, CharacterPrize

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from ..types.prizelocation import PrizeLocation
    from ..types.prize import Prize


class PlacementException(Exception):
    """Raised when placement fails with unplaced items."""
    def __init__(self, unplaced_count: int, unplaced_items: list):
        self.unplaced_count = unplaced_count
        self.unplaced_items = unplaced_items
        super().__init__(f"No progress made in placement; {unplaced_count} items could not be placed: {unplaced_items}")


def collect_accessible_items(world: GameWorld) -> Inventory:
    progress = True
    accessible_items = Inventory()
    checked = []
    while progress:
        progress = False
        accessible_locations = [
            l for l in world.locations.values()
            if l.can_access(accessible_items, world)
        ]
        for loc in accessible_locations:
            if loc in checked:
                continue
            if loc.has_item:
                accessible_items.append(loc.prize)
                checked.append(loc)
                progress = True
    return accessible_items



def place(
    world: GameWorld,
    to_place: list[Prize],
    can_overflow: bool = False,
    on_placed: Callable[[Prize, PrizeLocation], None] | None = None,
    force_frog_disciple: bool = False
):
    pending = copy(to_place)
    iteration = 0
    while pending:
        iteration += 1
        length_at_start = len(pending)

        # Check if there's a character in the pending list
        character_items = [item for item in pending if isinstance(item, CharacterPrize)]

        # If there's a character, try to place it first
        if character_items:
            character = character_items[0]
            player_has = collect_accessible_items(world)
            accessible_locations = [
                l for l in world.locations.values()
                if l.can_access(player_has, world)
                and l.can_accept(character, player_has, world)
                and not l.has_item
            ]
            if force_frog_disciple:
                frog_locations = [
                    l for l in accessible_locations
                    if isinstance(l, FrogDiscipleLocation)
                ]
                if len(frog_locations) > 0:
                    accessible_locations = frog_locations

            # If the character can be placed, place it
            if len(accessible_locations) > 0:
                random.shuffle(accessible_locations)
                accessible_locations[0].set_prize(character)
                pending.remove(character)
                if on_placed:
                    on_placed(character, accessible_locations[0])
                continue  # Go back to the start of the loop
            # If character can't be placed yet, fall through to place other items

        # Standard placement algorithm for all items (including character if it couldn't be placed)
        random.shuffle(pending)
        placed_this_iteration = False
        for _, item in enumerate(pending):
            player_has = collect_accessible_items(world)
            #print(f"  Inventory: {[type(i).__name__ for i in player_has]}")
            accessible_locations = [
                l for l in world.locations.values()
                if l.can_access(player_has, world)
                and l.can_accept(item, player_has, world)
                and not l.has_item
            ]
            if force_frog_disciple:
                frog_locations = [
                    l for l in accessible_locations
                    if isinstance(l, FrogDiscipleLocation)
                ]
                if len(frog_locations) > 0:
                    accessible_locations = frog_locations
            if isinstance(item, StarPiecePrize):
                star_locations = [
                    l for l in accessible_locations
                    if isinstance(l, StarPieceLocation)
                ]
                reduce = random.randint(0, 10)
                if reduce < 4:
                    accessible_locations = star_locations
            if len(accessible_locations) == 0:
                # Move onto the next item to see if it can be placed
                continue
            placed_this_iteration = True
            random.shuffle(accessible_locations)
            accessible_locations[0].set_prize(item)
            pending.remove(item)
            if on_placed:
                on_placed(item, accessible_locations[0])
            break
            # Start again from the beginning of the now-shortened pending list

        if len(pending) == 0:
            break
        if len(pending) == length_at_start:
            if not can_overflow:
                raise PlacementException(len(pending), [type(p).__name__ for p in pending])
            else:
                break
            
