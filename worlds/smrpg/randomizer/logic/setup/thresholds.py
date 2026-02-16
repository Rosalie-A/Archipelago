"""Threshold adjustments for minigames and sidequests."""
from __future__ import annotations
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpIfVarEqualsConst,
    CompareVarToConst,
    JmpIfBitClear,
)

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_threshold_settings(world: GameWorld) -> None:
    """Apply all threshold settings for minigames and sidequests.

    This configures thresholds for:
    - Marrymore suite prizes (1-6)
    - Super Jump rewards (30 and 100)
    - Knife Guy prize
    - Grate Guy prize
    - Bowser door requirements
    - Star pieces required for boss access
    """
    from ...types.flags import (
        SuitePrize1Threshold, SuitePrize2Threshold, SuitePrize3Threshold,
        SuitePrize4Threshold, SuitePrize5Threshold, SuitePrize6Threshold,
        SuperJump1Threshold, SuperJump2Threshold,
        KnifeGuyPrizeThreshold, KnifeGuyFixedPrizeThreshold,
        GrateGuyPrizeThreshold, BowserDoorRequirements,
        StarPiecesRequired, FixKnifeGuy,
    )
    from ...data.variables.variable_names import KNIFE_GUY_SECOND_PRIZE_AWARDED
    from ...data.variables.event_script_names import E0949_FROGFUCIUS_HINT_TREASURE_CHESTS

    # Suite prize thresholds
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_1"),
    ).set_value(world.settings.get_flag(SuitePrize1Threshold).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_2"),
    ).set_value(world.settings.get_flag(SuitePrize2Threshold).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_3"),
    ).set_value(world.settings.get_flag(SuitePrize3Threshold).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_4"),
    ).set_value(world.settings.get_flag(SuitePrize4Threshold).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_5"),
    ).set_value(world.settings.get_flag(SuitePrize5Threshold).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("suite_threshold_6"),
    ).set_value(world.settings.get_flag(SuitePrize6Threshold).value)

    # Super Jump thresholds
    cast(
        CompareVarToConst,
        world.event_scripts.get_command_by_identifier("sj_threshold_1"),
    ).set_value(world.settings.get_flag(SuperJump1Threshold).value)
    cast(
        CompareVarToConst,
        world.event_scripts.get_command_by_identifier("sj_threshold_2"),
    ).set_value(world.settings.get_flag(SuperJump2Threshold).value)

    # Knife Guy threshold
    cast(
        CompareVarToConst,
        world.event_scripts.get_command_by_identifier(
            "tower_knife_guy_sidequest_completed"
        ),
    ).set_value(world.settings.get_flag(KnifeGuyPrizeThreshold).value)

    # Grate Guy threshold
    cast(
        CompareVarToConst,
        world.event_scripts.get_command_by_identifier(
            "casino_grate_guy_sidequest_completed"
        ),
    ).set_value(world.settings.get_flag(GrateGuyPrizeThreshold).value)

    # Bowser door requirements
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("check_doors_complete"),
    ).set_value(world.settings.get_flag(BowserDoorRequirements).value)

    # Star pieces required for boss access
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("enable_boss_access_1"),
    ).set_value(world.settings.get_flag(StarPiecesRequired).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("enable_boss_access_2"),
    ).set_value(world.settings.get_flag(StarPiecesRequired).value)
    cast(
        JmpIfVarEqualsConst,
        world.event_scripts.get_command_by_identifier("enable_boss_access_3"),
    ).set_value(world.settings.get_flag(StarPiecesRequired).value)

    # Fixed Knife Guy second prize
    if world.settings.isflag_enabled(FixKnifeGuy):
        cast(
            CompareVarToConst,
            world.event_scripts.get_command_by_identifier(
                "tower_knife_guy_fixed_sidequest_completed"
            ),
        ).set_value(world.settings.get_flag(KnifeGuyFixedPrizeThreshold).value)
        world.event_scripts.get_script_by_id(
            E0949_FROGFUCIUS_HINT_TREASURE_CHESTS
        ).insert_after_identifier(
            "EVENT_949_knifeguy_insert",
            JmpIfBitClear(
                KNIFE_GUY_SECOND_PRIZE_AWARDED, ["EVENT_991_run_dialog_18"]
            ),
        )
