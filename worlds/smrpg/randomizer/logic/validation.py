"""Settings validation for the randomizer.

This module provides validation functions to check that settings combinations
are valid before the randomization process begins. Invalid combinations should
be caught early to provide clear error messages to the user.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types.settings import Settings


class SettingsValidationError(Exception):
    """Raised when settings have an invalid combination."""
    pass


def validate_settings(settings: Settings) -> None:
    """Validate that settings combinations are valid.

    This should be called before shuffle_items to catch invalid settings early.

    Args:
        settings: The settings object to validate

    Raises:
        SettingsValidationError: If settings have an invalid combination
    """
    _validate_character_requirements(settings)
    _validate_star_piece_requirements(settings)
    _validate_exp_sources(settings)


def _validate_character_requirements(settings: Settings) -> None:
    """Validate character-related settings are compatible.

    Checks:
    - Characters required by gating settings are not disabled
    - Characters explicitly set as starting characters are not disabled
    - Total required unique characters does not exceed max characters
    """
    from ..types.flags import (
        ShuffleCharacters,
        AvailableCharacters,
        MaxCharacters,
        StartingCharacters,
        BanditsWayGate, BanditsWayGating,
        KeroSewersGate, KeroSewersGating,
        PipeVaultGate, PipeVaultGating,
        Moleville1Gate, Moleville1Gating,
        BoosterTowerGate, BoosterTowerGating,
        SeaGate, SeaGating,
    )

    # Only validate if character shuffle is enabled
    if not settings.isflag_enabled(ShuffleCharacters):
        return

    # Collect characters required by gating settings
    gating_required_characters: set[str] = set()
    gating_checks: list[tuple[type, object, str]] = [
        (BanditsWayGate, BanditsWayGating.MALLOW, "Mallow"),
        (KeroSewersGate, KeroSewersGating.MALLOW, "Mallow"),
        (PipeVaultGate, PipeVaultGating.GENO, "Geno"),
        (Moleville1Gate, Moleville1Gating.GENO, "Geno"),
        (BoosterTowerGate, BoosterTowerGating.MARIO, "Mario"),
        (BoosterTowerGate, BoosterTowerGating.MALLOW, "Mallow"),
        (BoosterTowerGate, BoosterTowerGating.GENO, "Geno"),
        (BoosterTowerGate, BoosterTowerGating.BOWSER, "Bowser"),
        (BoosterTowerGate, BoosterTowerGating.TOADSTOOL, "Toadstool"),
        (SeaGate, SeaGating.TOADSTOOL, "Toadstool"),
    ]
    for flag_class, gating_value, char_name in gating_checks:
        if settings.is_flag_value(flag_class, gating_value):
            gating_required_characters.add(char_name)

    # Collect explicitly set starting characters (non-random)
    starting_chars_flag = settings.get_flag(StartingCharacters)
    explicitly_set_starting_chars: set[str] = set()
    for option in starting_chars_flag.enabled:
        value = option.value
        # Check if this is a "Random_X" string value - skip, those aren't explicit
        if isinstance(value, str):
            continue
        # This is an actual ally instance
        ally_name = value.name
        if ally_name:
            explicitly_set_starting_chars.add(ally_name)

    # Get available characters and max count
    available_chars_flag = settings.get_flag(AvailableCharacters)
    disabled_char_names = {m.value.name for m in available_chars_flag.disabled}
    max_char_count = settings.get_flag(MaxCharacters).value

    # Combine gating-required and explicitly set starting characters
    all_required_characters = gating_required_characters | explicitly_set_starting_chars

    # Check for disabled required characters
    disabled_required = all_required_characters & disabled_char_names
    if disabled_required:
        raise SettingsValidationError(
            f"Settings require characters that are disabled: "
            f"{', '.join(sorted(disabled_required))}. "
            f"Either change the gating/starting settings or enable these characters."
        )

    # Check for max characters constraint
    if len(all_required_characters) > max_char_count:
        raise SettingsValidationError(
            f"Settings require {len(all_required_characters)} unique characters "
            f"({', '.join(sorted(all_required_characters))}), "
            f"but 'Total playable allies' is set to {max_char_count}. "
            f"Either reduce character requirements or increase 'Total playable allies'."
        )


def _validate_star_piece_requirements(settings: Settings) -> None:
    """Validate star piece-related settings are compatible.

    Checks:
    - StarPiecesRequired does not exceed TotalStarPieces
    - TotalStarPieces is at least 4 if SeaGate is STAR_4
    - TotalStarPieces is at least 5 if LandsEndGate is STAR_5
    - TotalStarPieces is at least 6 if BowsersKeepGate or FactoryGate is STAR_6
    """
    from ..types.flags import (
        ShuffleStarPieces,
        TotalStarPieces,
        StarPiecesRequired,
        SeaGate, SeaGating,
        LandsEndGate, LandsEndGating,
        BowsersKeepGate, BowsersKeepGating,
        FactoryGate, FactoryGating,
    )

    # Get star piece settings
    total_stars = settings.get_flag(TotalStarPieces).value
    required_stars = settings.get_flag(StarPiecesRequired).value

    # Check that required doesn't exceed total
    if required_stars > total_stars:
        raise SettingsValidationError(
            f"'Star Pieces required to access the final Factory boss' ({required_stars}) "
            f"cannot be higher than 'Total Star Pieces available' ({total_stars})."
        )

    # Only check gating requirements if star piece shuffle is enabled
    if not settings.isflag_enabled(ShuffleStarPieces):
        return

    # Check minimum star pieces based on gating settings
    min_required = 0
    min_reason = ""

    if settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        if min_required < 4:
            min_required = 4
            min_reason = "'Sea & Sunken Ship access' is set to 'Collect 4 Star Pieces'"

    if settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        if min_required < 5:
            min_required = 5
            min_reason = "'Land's End access' is set to 'Collect 5 Star Pieces'"

    if settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        if min_required < 6:
            min_required = 6
            min_reason = "'Bowser's Keep access' is set to 'Collect 6 Star Pieces'"

    if settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        if min_required < 6:
            min_required = 6
            min_reason = "'Factory access' is set to 'Collect 6 Star Pieces'"

    if total_stars < min_required:
        raise SettingsValidationError(
            f"'Total Star Pieces available' ({total_stars}) must be at least {min_required} "
            f"because {min_reason}."
        )


def _validate_exp_sources(settings: Settings) -> None:
    """Validate that at least one EXP source is available.

    Checks that all of the following are not true simultaneously:
    - Remove EXP from regular enemy encounters is enabled
    - Remove EXP from boss encounters is enabled
    - EXP Star Behaviour is set to NONE
    """
    from ..types.flags import (
        ExperienceNoRegular,
        ExperienceNoBosses,
        EXPChallenge,
        EXPChallengeOptions,
    )

    no_regular_exp = settings.isflag_enabled(ExperienceNoRegular)
    no_boss_exp = settings.isflag_enabled(ExperienceNoBosses)
    no_star_exp = settings.is_flag_value(EXPChallenge, EXPChallengeOptions.NONE)

    if no_regular_exp and no_boss_exp and no_star_exp:
        raise SettingsValidationError(
            "Invalid settings combination: all EXP sources are disabled. "
            "You cannot have 'Remove EXP from regular enemy encounters', "
            "'Remove EXP from boss encounters', and 'EXP Star Behaviour' set to 'None' "
            "all at the same time. The player needs at least one source of EXP."
        )
