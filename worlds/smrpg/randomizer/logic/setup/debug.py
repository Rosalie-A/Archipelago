"""Debug mode setup functions."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_debug_start_items(world: GameWorld) -> None:
    """Insert starting items into event script 3840 if debug mode is enabled.

    Reads items.start from debug/config.yml and adds AddToInventory commands
    for each item to E3840_STARTER_DEBUG_ITEMS, which runs at game start.
    """
    if not world.settings.debug_mode:
        return

    from randomizer.debug import load_debug_config, get_item_class
    from randomizer.data.variables.event_script_names import E3840_STARTER_DEBUG_ITEMS
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
        AddToInventory, Return
    )

    config = load_debug_config()
    start_items = config.get("items", {}).get("start", [])
    if not start_items:
        return

    commands = []
    for item_name in start_items:
        item_cls = get_item_class(item_name)
        if item_cls is not None:
            commands.append(AddToInventory(item_cls))

    commands.append(Return())

    script = world.event_scripts.get_script_by_id(E3840_STARTER_DEBUG_ITEMS)
    script.set_contents(commands)


def apply_debug_max_stats(world: GameWorld) -> None:
    """Max out all character starting stats if debug mode is enabled."""
    if not world.settings.debug_mode:
        return

    # Max out starting stats for all allies
    for ally in world.allies._allies:
        ally.starting_max_hp = 999
        ally.starting_current_hp = 999
        ally.starting_attack = 255
        ally.starting_defense = 255
        ally.starting_mg_attack = 255
        ally.starting_mg_defense = 255
        ally.starting_speed = 255
        ally.starting_level = 30
        ally.starting_experience = 9999

        # Learn all spells that were shuffled to this ally
        # Collect spells from level-ups and add to starting_magic
        all_spells = list(ally.starting_magic)  # Start with existing starting spells
        for level_up in ally.levels:
            if level_up.spell_learned is not None:
                if level_up.spell_learned not in all_spells:
                    all_spells.append(level_up.spell_learned)
        ally.starting_magic = all_spells
