"""Minigame randomization logic."""
from __future__ import annotations
import random
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    RunDialog,
    Return,
    JmpIfVarNotEqualsConst,
    Inc,
    ActionQueueAsync,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0
from ...data.variables.variable_names import (
    SECONDARY_TEMP_7024,
    TEMP_7026,
    TEMP_7028,
    TEMP_702A,
    TEMP_702C,
    TEMP_702E,
    TEMP_70AC,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_14

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def randomize_tadpole_pond(world: GameWorld) -> None:
    """Randomize the Melody Bay song minigame."""
    from ...data.minigames.melody_bay import all_songs
    from ...data.variables.event_script_names import (
        E1082_MELODY_BAY_SONG_1_INPUT,
        E1079_MELODY_BAY_SONG_1_VALIDATOR,
        E1083_MELODY_BAY_SONG_2_INPUT,
        E1080_MELODY_BAY_SONG_2_VALIDATOR,
        E1084_MELODY_BAY_SONG_3_INPUT,
        E1081_MELODY_BAY_SONG_3_VALIDATOR,
        E3132_MOLEVILLE_MINERS_SONG,
        E2061_MONSTRO_TOWN_STAR,
        E1088_MELODY_BAY_THIRD_SONG_HINT,
    )
    from ...data.variables.dialog_names import (
        DI2718_SONG_1_SCROLL_HINT,
        DI2664_TADPOLE_SONG_1_HINT,
        DI2665_TADPOLE_SONG_2_HINT,
        DI1615_MOLEVILLE_BLUES_8,
    )

    selection = random.sample(all_songs, 3)
    world.event_scripts.get_script_by_id(E1082_MELODY_BAY_SONG_1_INPUT).set_contents(
        selection[0].generate_input_script(0)
    )
    world.event_scripts.get_script_by_id(
        E1079_MELODY_BAY_SONG_1_VALIDATOR
    ).set_contents(selection[0].generate_playback_script(0))
    world.update_dialog(
        DI2718_SONG_1_SCROLL_HINT, selection[0].scroll_text
    )
    world.update_dialog(
        DI2664_TADPOLE_SONG_1_HINT, selection[0].apprentice_hint_1
    )

    world.event_scripts.get_script_by_id(E1083_MELODY_BAY_SONG_2_INPUT).set_contents(
        selection[1].generate_input_script(1)
    )
    world.event_scripts.get_script_by_id(
        E1080_MELODY_BAY_SONG_2_VALIDATOR
    ).set_contents(selection[1].generate_playback_script(1))
    world.update_dialog(
        DI2665_TADPOLE_SONG_2_HINT, selection[1].apprentice_hint_2
    )
    world.update_dialog(
        DI1615_MOLEVILLE_BLUES_8, selection[1].mole_hint
    )
    world.event_scripts.get_script_by_id(E3132_MOLEVILLE_MINERS_SONG).set_contents(
        [
            RunDialog(
                DI1615_MOLEVILLE_BLUES_8,
                NPC_0,
                closable=True,
                sync=False,
                multiline=True,
                use_background=True,
            ),
            Return(),
        ]
    )
    world.event_scripts.get_script_by_id(E3132_MOLEVILLE_MINERS_SONG).set_contents(
        [
            RunDialog(dialog_id=DI1615_MOLEVILLE_BLUES_8, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	        Return()
        ]
    )

    world.event_scripts.get_script_by_id(E1084_MELODY_BAY_SONG_3_INPUT).set_contents(
        selection[2].generate_input_script(2)
    )
    world.event_scripts.get_script_by_id(
        E1081_MELODY_BAY_SONG_3_VALIDATOR
    ).set_contents(selection[2].generate_playback_script(2))
    cast(
        ActionQueueAsync,
        world.event_scripts.get_command_by_identifier("starfish_dance_hint"),
    ).set_subscript(
        selection[2].generate_starfish_hint(
            cast(
                ActionQueueAsync,
                world.event_scripts.get_command_by_identifier("starfish_dance_hint"),
            ).subscript.contents
        )
    )
    world.event_scripts.get_script_by_id(
        E1088_MELODY_BAY_THIRD_SONG_HINT
    ).set_contents(selection[2].generate_tadpole_hint())

    world.song_1 = selection[0].scroll_text
    world.song_2 = selection[1].scroll_text
    world.song_3 = selection[2].scroll_text

    world.song_authors = list(
        set(
            selection[0].submitter_credits
            + selection[1].submitter_credits
            + selection[2].submitter_credits
        )
    )


def randomize_password(world: GameWorld) -> None:
    """Randomize the ship password minigame."""
    from ...data.minigames.ship_password import (
        pool as password_pool,
        suggest_letter_bank,
        box_dialog_ids,
        recitation_ids,
        hint_authors,
    )
    from ...data.variables.event_script_names import E3411_SHIP_PASSWORD_CORRECTNESS_CHECK
    from ...data.variables.dialog_names import (
        DI1664_TROOPA_PUZZLE_HINT,
        DI1665_TRAMPOLINE_PUZZLE_HINT,
        DI1666_MAZE_PUZZLE_HINT,
        DI1667_SNAKE_PUZZLE_HINT,
        DI1668_CANNONBALL_PUZZLE_HINT,
        DI1669_BARREL_PUZZLE_HINT,
        DI1673_SHIP_ENTRANCE_NOTE,
        DI1674_SHIP_SAVEROOM_NOTE,
        DI1675_SHIP_GREAPER_1_NOTE,
        DI1676_SHIP_GREAPER_2_NOTE,
        DI1656_SLEEPING_DRY_BONES,
    )

    password = random.choice(password_pool)
    world.password = password.word
    decoy_word = random.choice([p for p in password_pool if p != password])
    correct_positions = []

    # create password submission logic
    for index, letter in enumerate(list(password.word)):
        letters = suggest_letter_bank(password.word, index, decoy_word.word)
        correct_position = letters.index(password.word[index])
        correct_positions.append(correct_position)

        # generate the dialogs that display your letter selection when you stand under the boxes
        box_dialogs = []
        box_dialogs.append(
            """[page]\n Key letter%i  <%s> %s  %s  %s  %s[end]"""
            % (
                index + 1,
                letters[0],
                letters[1],
                letters[2],
                letters[3],
                letters[4],
            )
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s <%s> %s  %s  %s[end]"""
            % (
                index + 1,
                letters[0],
                letters[1],
                letters[2],
                letters[3],
                letters[4],
            )
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s <%s> %s  %s[end]"""
            % (
                index + 1,
                letters[0],
                letters[1],
                letters[2],
                letters[3],
                letters[4],
            )
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s  %s <%s> %s[end]"""
            % (
                index + 1,
                letters[0],
                letters[1],
                letters[2],
                letters[3],
                letters[4],
            )
        )
        box_dialogs.append(
            """[page]\n Key letter%i   %s  %s  %s  %s <%s>[end]"""
            % (
                index + 1,
                letters[0],
                letters[1],
                letters[2],
                letters[3],
                letters[4],
            )
        )
        box_dialog_pairs = zip(box_dialogs, box_dialog_ids[index])
        for dialog_content, dialog_id in box_dialog_pairs:
            world.update_dialog(dialog_id, dialog_content)
        recitation_pairs = zip(letters, recitation_ids[index])
        for letter, dialog_id in recitation_pairs:
            world.update_dialog(dialog_id, """%s[end]""" % letter)

    # calibrate correctness checker
    world.event_scripts.get_script_by_id(
        E3411_SHIP_PASSWORD_CORRECTNESS_CHECK
    ).set_contents(
        [
            JmpIfVarNotEqualsConst(
                SECONDARY_TEMP_7024, correct_positions[0], ["ship_password_check_2"]
            ),
            Inc(TEMP_70AC),
            JmpIfVarNotEqualsConst(
                TEMP_7026,
                correct_positions[1],
                ["ship_password_check_3"],
                identifier="ship_password_check_2",
            ),
            Inc(TEMP_70AC),
            JmpIfVarNotEqualsConst(
                TEMP_7028,
                correct_positions[2],
                ["ship_password_check_4"],
                identifier="ship_password_check_3",
            ),
            Inc(TEMP_70AC),
            JmpIfVarNotEqualsConst(
                TEMP_702A,
                correct_positions[3],
                ["ship_password_check_5"],
                identifier="ship_password_check_4",
            ),
            Inc(TEMP_70AC),
            JmpIfVarNotEqualsConst(
                TEMP_702C,
                correct_positions[4],
                ["ship_password_check_6"],
                identifier="ship_password_check_5",
            ),
            Inc(TEMP_70AC),
            JmpIfVarNotEqualsConst(
                TEMP_702E,
                correct_positions[5],
                ["ship_password_check_end"],
                identifier="ship_password_check_6",
            ),
            Inc(TEMP_70AC),
            Return(identifier="ship_password_check_end"),
        ]
    )

    # populate hint dialogs
    hint_authors_copy = list(hint_authors)
    random.shuffle(hint_authors_copy)
    # guarantee that the hint submitter will get their name on one of the hints
    writers = [password.submitter_hint_prefix] + hint_authors_copy
    RWRITER = "%RANDOM_WRITER%"
    number_of_writers = len(
        [
            h
            for h in [
                password.troopa_hint,
                password.trampoline_hint,
                password.maze_hint,
                password.snake_hint,
                password.cannonball_hint,
                password.barrel_hint,
                password.entrance_hint,
                password.saveroom_hint,
                password.greaper_hint_2,
                password.greaper_hint,
                password.drybones_hint,
            ]
            if h is not None and RWRITER in h
        ]
    )
    writers = writers[:number_of_writers]
    random.shuffle(writers)
    for s in writers:
        if RWRITER in password.troopa_hint:
            password.troopa_hint = password.troopa_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.trampoline_hint:
            password.trampoline_hint = password.trampoline_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.maze_hint:
            password.maze_hint = password.maze_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.snake_hint:
            password.snake_hint = password.snake_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.cannonball_hint:
            password.cannonball_hint = password.cannonball_hint.replace(RWRITER, s)
            continue
        if RWRITER in password.barrel_hint:
            password.barrel_hint = password.barrel_hint.replace(RWRITER, s)
            continue
        if password.entrance_hint and RWRITER in password.entrance_hint:
            password.entrance_hint = password.entrance_hint.replace(RWRITER, s)
            continue
        if password.saveroom_hint and RWRITER in password.saveroom_hint:
            password.saveroom_hint = password.saveroom_hint.replace(RWRITER, s)
            continue
        if password.greaper_hint and RWRITER in password.greaper_hint:
            password.greaper_hint = password.greaper_hint.replace(RWRITER, s)
            continue
        if password.greaper_hint_2 and RWRITER in password.greaper_hint_2:
            password.greaper_hint_2 = password.greaper_hint_2.replace(RWRITER, s)
            continue
        if password.drybones_hint and RWRITER in password.drybones_hint:
            password.drybones_hint = password.drybones_hint.replace(RWRITER, s)
            continue
    world.update_dialog(
        DI1664_TROOPA_PUZZLE_HINT, password.troopa_hint
    )
    world.update_dialog(
        DI1665_TRAMPOLINE_PUZZLE_HINT, password.trampoline_hint
    )
    world.update_dialog(
        DI1666_MAZE_PUZZLE_HINT, password.maze_hint
    )
    world.update_dialog(
        DI1667_SNAKE_PUZZLE_HINT, password.snake_hint
    )
    world.update_dialog(
        DI1668_CANNONBALL_PUZZLE_HINT, password.cannonball_hint
    )
    world.update_dialog(
        DI1669_BARREL_PUZZLE_HINT, password.barrel_hint
    )
    if password.entrance_hint is not None:
        world.update_dialog(
            DI1673_SHIP_ENTRANCE_NOTE, password.entrance_hint
        )
    if password.saveroom_hint is not None:
        world.update_dialog(
            DI1674_SHIP_SAVEROOM_NOTE, password.saveroom_hint
        )
    if password.greaper_hint is not None:
        world.update_dialog(
            DI1675_SHIP_GREAPER_1_NOTE, password.greaper_hint
        )
    if password.greaper_hint_2 is not None:
        world.update_dialog(
            DI1676_SHIP_GREAPER_2_NOTE, password.greaper_hint_2
        )
    if password.drybones_hint is not None:
        world.update_dialog(
            DI1656_SLEEPING_DRY_BONES, password.drybones_hint
        )

    world.password_author = password.submitter_credits
