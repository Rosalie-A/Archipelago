"""Minigame settings and configuration."""
from __future__ import annotations
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    SetVarToConst,
    SetVarToRandom,
    JmpToEvent,
)

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_minigame_settings(world: GameWorld) -> None:
    """Apply minigame-related settings.

    This configures:
    - Quiz shuffle
    - Ball solitaire puzzle shuffle
    - Magic buttons puzzle shuffle
    - Minecart skip
    - Tadpole pond song shuffle
    - Sunken ship password shuffle
    - Bowser door shuffle
    - Better tips (improved random rewards)
    """
    from ...types.flags import (
        QuizShuffle, QuizIncludeNonSmrpg,
        BallSolitaireShuffle, MagicButtonShuffle,
        SkipMinecart, RandomTadpolePondSong, RandomSunkenShipPassword,
        BowserDoorShuffle, BetterTips,
    )
    from ...data.minigames.quiz_questions import (
        get_quiz_questions,
        option_1_correct,
        option_2_correct,
        option_3_correct,
    )
    from ...data.minigames.puzzle_games import (
        BallSolitaireGame,
        MagicButtonsGame,
        randomize_ball_solitaire,
        randomize_magic_buttons,
    )
    from ...data.minigames.bowser_doors import randomize_bowser_doors
    from ..shufflers.minigames import randomize_tadpole_pond, randomize_password
    from ...data.variables.event_script_names import (
        E0021_FOREST_MAZE_MUSHROOM_GRANT,
        E0022_BETTER_TIP_GRANTER,
        E0023_MUSHROOM_SELECTION,
        E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1,
        E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER,
        E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE,
    )

    # Quiz shuffle
    if world.settings.isflag_enabled(QuizShuffle):
        include_non_smrpg = world.settings.isflag_enabled(QuizIncludeNonSmrpg)
        questions = get_quiz_questions(include_non_smrpg)
        for text, d_id in zip(
            questions, option_1_correct + option_2_correct + option_3_correct
        ):
            world.update_dialog(d_id, text.get_string(d_id))

    # Ball solitaire puzzle shuffle
    if world.settings.isflag_enabled(BallSolitaireShuffle):
        ball_solitaire = BallSolitaireGame()
        randomize_ball_solitaire(ball_solitaire)
        cast(
            SetVarToConst,
            world.event_scripts.get_command_by_identifier(
                "ball_solitaire_puzzle_value"
            ),
        ).set_value_and_address(value=ball_solitaire.get_puzzle_value())

    # Magic buttons puzzle shuffle
    if world.settings.isflag_enabled(MagicButtonShuffle):
        magic_buttons = MagicButtonsGame()
        randomize_magic_buttons(magic_buttons)
        cast(
            SetVarToConst,
            world.event_scripts.get_command_by_identifier(
                "magic_buttons_puzzle_value"
            ),
        ).set_value_and_address(value=magic_buttons.get_puzzle_value())

    # Minecart skip (if NOT enabled, delete the skip command)
    if not world.settings.isflag_enabled(SkipMinecart):
        world.event_scripts.delete_command_by_identifier(
            "skip_moleville_minecart_sequence"
        )

    # Tadpole pond song shuffle
    if world.settings.isflag_enabled(RandomTadpolePondSong):
        randomize_tadpole_pond(world)

    # Sunken ship password shuffle
    if world.settings.isflag_enabled(RandomSunkenShipPassword):
        randomize_password(world)

    # Bowser door shuffle
    if world.settings.isflag_enabled(BowserDoorShuffle):
        randomize_bowser_doors(world)

    # Better tips (improved random rewards)
    if world.settings.isflag_enabled(BetterTips):
        cast(
            SetVarToRandom,
            world.event_scripts.get_command_by_identifier("mushroom_boy_odds"),
        ).set_value(5000)
        world.event_scripts.get_script_by_id(
            E0021_FOREST_MAZE_MUSHROOM_GRANT
        ).set_contents([JmpToEvent(E0023_MUSHROOM_SELECTION)])
        world.event_scripts.get_script_by_id(
            E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1
        ).set_contents([JmpToEvent(E0022_BETTER_TIP_GRANTER)])
        world.event_scripts.get_script_by_id(
            E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER
        ).set_contents([JmpToEvent(E0022_BETTER_TIP_GRANTER)])
        world.event_scripts.get_script_by_id(
            E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE
        ).set_contents([JmpToEvent(E0022_BETTER_TIP_GRANTER)])
        cast(
            SetVarToRandom,
            world.event_scripts.get_command_by_identifier("cloud_spawn_rate"),
        ).set_value(2)
        
        
