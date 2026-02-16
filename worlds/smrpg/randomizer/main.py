from copy import deepcopy
from typing import Callable

from .types.gameworld import GameWorld, Settings
from .types.patch import Patch
from .data.allies.allies import ally_collection
from .data.battle_animation._02.export import bank as bank02
from .data.battle_animation._35.export import bank as bank35
from .data.battle_animation._3A.export import bank as bank3A
from .data.battle_dialogs.battle_dialogs import collection as battle_dialog_collection
from .data.dialogs.dialogs import data as dialog_collection
from .data.enemies.enemies import ENEMIES
from .data.enemy_attacks.attacks import collection as enemy_attack_collection
from .data.items.items import ITEMS
from .data.monster_ai.monster_scripts import monster_scripts
from .data.overworld_scripts.event.events import events
from .data.overworld_scripts.animation.actionqueues import actions
from .data.packets.packets import ALL_PACKETS
from .data.packs.pack_collection import pack_collection
from .data.rooms.rooms import room_collection
from .data.shops.shops import shop_collection
from .data.spells.spells import ALL_SPELLS
from .data.sprites.sprites import sprites
from .data.world_map_locations.world_map_locations import world_map_location_collection
from .data.palettes.event_palettes import ALL_EVENT_PALETTES
from .data.palettes.sprite_palettes import ALL_SPRITE_PALETTES

# Current version number
VERSION = '9.0.0'

def create(
    seed: int | str,
    settings: Settings,
    progress_callback: Callable[[str, int], None] | None = None,
    debug_bps_patches: bool = False,
) -> GameWorld:
    """Create a patch for the given seed.

    Deep copies all mutable collections so modifications during randomization
    don't affect subsequent seed generations.

    Args:
        seed: The randomizer seed value.
        settings: The randomizer settings/flags.
        progress_callback: Optional callback for progress updates. Called with
            (message: str, percent: int) during generation.
        debug_bps_patches: If True, generate separate BPS patches for each render
            stage (only works in debug/development environment).
    """
    return GameWorld(
        seed,
        VERSION,
        settings,
        deepcopy(ally_collection),
        {
            0x02: deepcopy(bank02),
            0x35: deepcopy(bank35),
            0x3A: deepcopy(bank3A),
        },
        deepcopy(battle_dialog_collection),
        deepcopy(dialog_collection),
        deepcopy(ENEMIES),
        deepcopy(enemy_attack_collection),
        deepcopy(ITEMS),
        deepcopy(monster_scripts),
        deepcopy(events),
        deepcopy(actions),
        deepcopy(ALL_PACKETS),
        deepcopy(pack_collection),
        deepcopy(room_collection),
        deepcopy(shop_collection),
        deepcopy(ALL_SPELLS),
        deepcopy(sprites),
        deepcopy(world_map_location_collection),
        deepcopy(ALL_EVENT_PALETTES),
        deepcopy(ALL_SPRITE_PALETTES),
        progress_callback=progress_callback,
        debug_bps_patches=debug_bps_patches,
    )

