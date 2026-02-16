"""Character randomization logic."""
from __future__ import annotations
import random
from typing import TYPE_CHECKING

from ..utils import mutate_normal

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def randomize_character_stats(world: GameWorld) -> None:
    """Randomize character stats, level-up bonuses, and stat growths."""
    from smrpgpatchbuilder.datatypes.allies.ally import LevelUp

    LEVEL_STATS = [
        "hp_plus",
        "attack_plus",
        "defense_plus",
        "mg_attack_plus",
        "mg_defense_plus",
    ]
    BONUS_STATS = [
        "hp_plus_bonus",
        "attack_plus_bonus",
        "defense_plus_bonus",
        "mg_attack_plus_bonus",
        "mg_defense_plus_bonus",
    ]

    # Randomize XP requirements for each level
    randomize_levelup_xps(world)

    # Collect all bonuses from all allies for inter-shuffling (first 19 levels)
    all_bonuses: list[LevelUp] = []
    for ally in world.allies._allies:
        all_bonuses.extend(ally.levels[:19])

    # Inter-shuffle level up stat bonuses between all characters
    for attrs in (
        ("hp_plus_bonus",),
        ("attack_plus_bonus", "defense_plus_bonus"),
        ("mg_attack_plus_bonus", "mg_defense_plus_bonus"),
    ):
        shuffled = all_bonuses[:]
        random.shuffle(shuffled)

        for attr in attrs:
            swaps = [getattr(s, attr) for s in shuffled]
            for bonus, bval in zip(all_bonuses, swaps):
                setattr(bonus, attr, bval)

        # For any bonuses that are zero, pick a random non-zero one
        non_zeros = [
            b for b in all_bonuses if all(getattr(b, attr) for attr in attrs)
        ]
        for bonus in all_bonuses:
            for attr in attrs:
                while getattr(bonus, attr) == 0 and non_zeros:
                    setattr(bonus, attr, getattr(random.choice(non_zeros), attr))

    # Randomize each ally's stats
    for ally in world.allies._allies:
        # Mutate starting level and speed
        ally.starting_level = mutate_normal(
            ally.starting_level, minimum=1, maximum=30
        )
        ally.starting_speed = mutate_normal(
            ally.starting_speed, minimum=1, maximum=255
        )

        # Randomize level up stat bonuses
        for level_up in ally.levels:
            for attr in BONUS_STATS:
                value = getattr(level_up, attr)
                # Make each bonus at least 1
                new_value = max(mutate_normal(value, maximum=15), 1)
                setattr(level_up, attr, new_value)

        # Randomize level up stat growths for each stat
        for attr in LEVEL_STATS:
            # For growths, work with levels 2-20 (first 19 entries)
            for i, level_up in enumerate(ally.levels[:19]):
                value = getattr(level_up, attr)
                new_value = max(mutate_normal(value, maximum=15), 1)
                setattr(level_up, attr, new_value)

            # Beyond level 20, give smaller increases (1-2)
            for level_up in ally.levels[19:]:
                setattr(level_up, attr, random.choices([1, 2], weights=[2, 1])[0])


def randomize_levelup_xps(world: GameWorld) -> None:
    """Randomize the XP requirements for each level by shuffling the gaps."""
    # Get current XP values from first ally (they share the same XP table)
    if not world.allies._allies:
        return

    ally = world.allies._allies[0]
    if not ally.levels:
        return

    # Build gaps between levels
    gaps = []
    prev_xp = 0
    for level_up in ally.levels:
        gap = level_up.exp_needed - prev_xp
        gaps.append(mutate_normal(gap, minimum=1, maximum=9999))
        prev_xp = level_up.exp_needed

    gaps.sort()

    # Make sure we total 9999 at level 30
    total = sum(gaps)
    if total != 9999:
        diff = 9999 - total
        piece = diff / sum(range(1, len(gaps) + 1))
        for i in range(len(gaps)):
            gaps[i] += round(piece * (i + 1))

    # Check total again for rounding
    total = sum(gaps)
    if total != 9999:
        diff = 9999 - total
        gaps[-1] += diff
        gaps.sort()

    # Apply new XP values to all allies
    for ally in world.allies._allies:
        prev = 0
        for i, level_up in enumerate(ally.levels):
            if i < len(gaps):
                new_val = prev + gaps[i]
                level_up.exp_needed = new_val
                prev = new_val


def randomize_character_spell_stats(world: GameWorld) -> None:
    """Randomize character spell stats (FP cost, power, hit rate)."""
    from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
    from ...data.spells.spells import (
        GenoBoostSpell,
        TherapySpell,
        GroupHugSpell,
        HPRainSpell,
        PsychopathSpell,
        SleepyTimeSpell,
        MuteSpell,
    )

    # Spells that should not have their power randomized
    NO_POWER_SHUFFLE = (GenoBoostSpell, SleepyTimeSpell, MuteSpell, PsychopathSpell)

    # Spells that should not have their hit rate randomized
    NO_HIT_RATE_SHUFFLE = (
        GenoBoostSpell,
        TherapySpell,
        GroupHugSpell,
        HPRainSpell,
        PsychopathSpell,
    )

    for spell in world.spells.spells:
        if not isinstance(spell, CharacterSpell):
            continue

        # Randomize FP cost (1-31, capped by set_fp assertion)
        new_fp = mutate_normal(int(spell.fp), minimum=1, maximum=31)
        spell.set_fp(new_fp)

        # Randomize power (except for certain spells)
        if not isinstance(spell, NO_POWER_SHUFFLE):
            new_power = mutate_normal(
                int(spell.power), minimum=0, maximum=255
            )
            spell.set_power(int(max(0, min(255, new_power))))

        # Randomize hit rate (except for certain spells)
        if not isinstance(spell, NO_HIT_RATE_SHUFFLE):
            # Cap hit rate at 99 for instant KO spells so protection items work
            max_hit_rate = 99 if spell.check_ohko else 100
            new_hit_rate = mutate_normal(
                int(spell.hit_rate), minimum=1, maximum=max_hit_rate
            )
            spell.set_hit_rate(new_hit_rate)
