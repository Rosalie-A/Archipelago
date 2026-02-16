# Data module for Bowser's Keep door randomization.

from __future__ import annotations
import enum
import random
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpToEvent,
)

from ..variables.event_script_names import (
    E1878_KEEP_CANNONBALL_ROOM_EXIT_TO_PREVIOUS,
    E1879_KEEP_LINEAR_PLATFORM_ROOM_EXIT_TO_PREVIOUS,
    E1935_KEEP_ROTATING_ROOM_EXIT_TO_PREVIOUS,
    E1942_KEEP_VERTICAL_PLATFORM_ROOM_EXIT_TO_PREVIOUS,
    E1943_KEEP_INVISIBLE_FLOOR_ROOM_EXIT,
    E1944_KEEP_CHEWY_BATTLE_ROOM_EXIT,
    E1945_KEEP_CANNONBALL_ROOM_EXIT,
    E1946_KEEP_DONKEY_ROOM_EXIT_TO_PREVIOUS,
    E1947_KEEP_LINEAR_PLATFORM_ROOM_EXIT,
    E1948_KEEP_TERRA_CORRA_BATTLE_ROOM_EXIT,
    E1949_KEEP_ALLEY_RAT_BATTLE_ROOM_EXIT,
    E1950_KEEP_GOOMBA_BATTLE_ROOM_EXIT,
    E1951_KEEP_BARREL_COUNT_ROOM_EXIT_CONTAINER,
    E1952_KEEP_ENTER_MARATHON_PUZZLE_ROOM,
    E1953_KEEP_QUIZ_ROOM_EXIT_CONTAINER,
    E1954_KEEP_ENTER_BARREL_COUNT_ROOM,
    E1955_KEEP_COIN_GAME_ROOM_EXIT_CONTAINER,
    E1956_KEEP_ENTER_BUTTON_GAME_ROOM,
    E1957_KEEP_DOOR_5_CONTAINER,
    E1958_KEEP_ENTER_VERTICAL_PLATFORM_ROOM,
    E1959_KEEP_DOOR_4_CONTAINER,
    E1960_KEEP_ENTER_INVISIBLE_FLOOR_ROOM,
    E1961_KEEP_DOOR_6_CONTAINER,
    E1962_KEEP_ENTER_TERRA_COTTA_BATTLE_ROOM,
    E1963_KEEP_DOOR_3_CONTAINER,
    E1964_KEEP_ENTER_GOOMBA_BATTLE_ROOM,
    E1965_KEEP_DOOR_1_CONTAINER,
    E1966_KEEP_ENTER_QUIZ_ROOM,
    E1967_KEEP_DOOR_2_CONTAINER,
    E1968_KEEP_ENTER_COIN_GAME_ROOM,
    E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM,
    E3353_KEEP_ENTER_BALL_SOLITAIRE_ROOM,
)
from ..variables.room_names import (
    R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
    R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
    R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
    R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
    R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
    R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
    R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
    R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
    R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
    R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
    R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
    R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
    R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING,
    R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ,
    R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES,
    R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
    R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING,
    R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld

# Event ID 256 is a null event that does nothing (disables the return exit)
E_NULL = 256


class ExitType(enum.Enum):
    """Types of exits from Bowser's Keep door rooms."""
    Tile = enum.auto()
    Background = enum.auto()


class BowserDoorRoom:
    """Represents a single room in the Bowser's Keep door sequence.

    Attributes:
        room: Room ID constant.
        to_proceed: Event script ID to load when proceeding to the next room.
        to_return: Event script ID to load when going back to the previous room.
        exit_type: Whether the exit is triggered by a tile or automatically.
        proceed_index: Index in room.event_tiles for the proceed exit (for Tile exits),
            or the event script ID containing the JmpToEvent command (for Background exits).
        return_index: Index in room.event_tiles for the return exit (if applicable).
    """

    def __init__(
        self,
        room: int,
        to_proceed: int,
        proceed_index: int,
        exit_type: ExitType = ExitType.Tile,
        to_return: int | None = None,
        return_index: int | None = None,
    ) -> None:
        self.room = room
        self.to_proceed = to_proceed
        self.to_return = to_return
        self.exit_type = exit_type
        self.proceed_index = proceed_index
        self.return_index = return_index

    def __repr__(self) -> str:
        return f"<BowserDoorRoom: room {self.room}>"


# All 18 Bowser's Keep door rooms
# These are the rooms that can be shuffled into 6 hallways of 3 rooms each
ALL_DOOR_ROOMS = [
    # Action Room 2A - Slow Elevating Platforms
    BowserDoorRoom(
        R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
        E1958_KEEP_ENTER_VERTICAL_PLATFORM_ROOM,
        0,
        ExitType.Tile,
        E1878_KEEP_CANNONBALL_ROOM_EXIT_TO_PREVIOUS,
        1,
    ),
    # Action Room 1A - Jumping Terrapin
    BowserDoorRoom(
        R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
        E1960_KEEP_ENTER_INVISIBLE_FLOOR_ROOM,
        0,
        ExitType.Tile,
        E1879_KEEP_LINEAR_PLATFORM_ROOM_EXIT_TO_PREVIOUS,
        1,
    ),
    # Battle Room 2B - Chewy fight
    BowserDoorRoom(
        R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
        E1950_KEEP_GOOMBA_BATTLE_ROOM_EXIT,
        4,
    ),
    # Battle Room 2C - Sparky fight
    BowserDoorRoom(
        R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
        E1944_KEEP_CHEWY_BATTLE_ROOM_EXIT,
        4,
    ),
    # Action Room 2C - Very slow circling platforms
    BowserDoorRoom(
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
        E1945_KEEP_CANNONBALL_ROOM_EXIT,
        0,
        ExitType.Tile,
        None,
        1,
    ),
    # Action Room 1C - Gorilla throwing barrels (Donkey Kong room)
    BowserDoorRoom(
        R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
        E1947_KEEP_LINEAR_PLATFORM_ROOM_EXIT,
        0,
        ExitType.Tile,
        None,
        1,
    ),
    # Action Room 2B - Cannonball riding
    BowserDoorRoom(
        R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
        E1942_KEEP_VERTICAL_PLATFORM_ROOM_EXIT_TO_PREVIOUS,
        0,
        ExitType.Tile,
        E1935_KEEP_ROTATING_ROOM_EXIT_TO_PREVIOUS,
        1,
    ),
    # Action Room 1B - Moving platforms
    BowserDoorRoom(
        R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
        E1943_KEEP_INVISIBLE_FLOOR_ROOM_EXIT,
        0,
        ExitType.Tile,
        E1946_KEEP_DONKEY_ROOM_EXIT_TO_PREVIOUS,
        1,
    ),
    # Battle Room 1A - Terra Cotta fight
    BowserDoorRoom(
        R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
        E1962_KEEP_ENTER_TERRA_COTTA_BATTLE_ROOM,
        4,
    ),
    # Battle Room 1B - Alley Rat fight
    BowserDoorRoom(
        R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
        E1948_KEEP_TERRA_CORRA_BATTLE_ROOM_EXIT,
        4,
    ),
    # Battle Room 1C - Bob-omb fight
    BowserDoorRoom(
        R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
        E1949_KEEP_ALLEY_RAT_BATTLE_ROOM_EXIT,
        4,
    ),
    # Battle Room 2A - Gu Goomba fight
    BowserDoorRoom(
        R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
        E1964_KEEP_ENTER_GOOMBA_BATTLE_ROOM,
        4,
    ),
    # Puzzle Room 1B - Barrel counting (background exit)
    BowserDoorRoom(
        R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING,
        E1954_KEEP_ENTER_BARREL_COUNT_ROOM,
        E1951_KEEP_BARREL_COUNT_ROOM_EXIT_CONTAINER,
        ExitType.Background,
    ),
    # Puzzle Room 1A - Quiz (background exit)
    BowserDoorRoom(
        R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ,
        E1966_KEEP_ENTER_QUIZ_ROOM,
        E1953_KEEP_QUIZ_ROOM_EXIT_CONTAINER,
        ExitType.Background,
    ),
    # Puzzle Room 2B - Green switches (Marathon room)
    BowserDoorRoom(
        R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES,
        E1956_KEEP_ENTER_BUTTON_GAME_ROOM,
        0,
    ),
    # Puzzle Room 1C - Word problem
    BowserDoorRoom(
        R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
        E1952_KEEP_ENTER_MARATHON_PUZZLE_ROOM,
        0,
    ),
    # Puzzle Room 2A - Coin collecting (background exit)
    BowserDoorRoom(
        R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING,
        E1968_KEEP_ENTER_COIN_GAME_ROOM,
        E1955_KEEP_COIN_GAME_ROOM_EXIT_CONTAINER,
        ExitType.Background,
    ),
    # Puzzle Room 2C - Ball solitaire
    BowserDoorRoom(
        R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE,
        E3353_KEEP_ENTER_BALL_SOLITAIRE_ROOM,
        0,
    ),
]

# The 6 door container scripts that initially point to each hallway's first room
DOOR_CONTAINER_SCRIPTS = [
    E1957_KEEP_DOOR_5_CONTAINER,
    E1959_KEEP_DOOR_4_CONTAINER,
    E1961_KEEP_DOOR_6_CONTAINER,
    E1963_KEEP_DOOR_3_CONTAINER,
    E1965_KEEP_DOOR_1_CONTAINER,
    E1967_KEEP_DOOR_2_CONTAINER,
]


def randomize_bowser_doors(world: GameWorld) -> None:
    """Randomize the Bowser's Keep door sequences.

    Shuffles the 18 door rooms into 6 random sequences of 3 rooms each.
    Each door leads to a random set of 3 rooms that must be completed
    to count toward the door requirement.

    Args:
        world: The GameWorld instance to modify.
    """
    # Make a copy of the door list and shuffle it
    doors = list(ALL_DOOR_ROOMS)
    random.shuffle(doors)

    # Split into 6 hallways of 3 rooms each
    hallways = [
        doors[0:3],
        doors[3:6],
        doors[6:9],
        doors[9:12],
        doors[12:15],
        doors[15:18],
    ]

    # Update the 6 door container scripts to point to each hallway's first room
    for container_script_id, hallway in zip(DOOR_CONTAINER_SCRIPTS, hallways):
        container_script = world.get_event_script(container_script_id)
        # The container script has a single JmpToEvent command
        jmp_cmd = container_script.contents[0]
        if isinstance(jmp_cmd, JmpToEvent):
            jmp_cmd.set_destination(hallway[0].to_proceed)

    # Wire up each hallway's rooms
    for hallway in hallways:
        first_room = hallway[0]
        second_room = hallway[1]
        third_room = hallway[2]

        # First room: disable return exit, set proceed exit to second room
        if first_room.return_index is not None:
            room = world.get_room(first_room.room)
            room.event_tiles[first_room.return_index].set_event(E_NULL)

        if first_room.exit_type == ExitType.Tile:
            room = world.get_room(first_room.room)
            room.event_tiles[first_room.proceed_index].set_event(second_room.to_proceed)
        else:
            # Background exit: modify the container script's JmpToEvent
            container_script = world.get_event_script(first_room.proceed_index)
            jmp_cmd = container_script.contents[0]
            if isinstance(jmp_cmd, JmpToEvent):
                jmp_cmd.set_destination(second_room.to_proceed)

        # Second room: set return to first room's return (or null), proceed to third
        if second_room.return_index is not None:
            room = world.get_room(second_room.room)
            return_event = first_room.to_return if first_room.to_return is not None else E_NULL
            room.event_tiles[second_room.return_index].set_event(return_event)

        if second_room.exit_type == ExitType.Tile:
            room = world.get_room(second_room.room)
            room.event_tiles[second_room.proceed_index].set_event(third_room.to_proceed)
        else:
            container_script = world.get_event_script(second_room.proceed_index)
            jmp_cmd = container_script.contents[0]
            if isinstance(jmp_cmd, JmpToEvent):
                jmp_cmd.set_destination(third_room.to_proceed)

        # Third room: set return to second room's return (or null), proceed to reward
        if third_room.return_index is not None:
            room = world.get_room(third_room.room)
            return_event = second_room.to_return if second_room.to_return is not None else E_NULL
            room.event_tiles[third_room.return_index].set_event(return_event)

        # Final room exits to the reward room (E3350)
        if third_room.exit_type == ExitType.Tile:
            room = world.get_room(third_room.room)
            room.event_tiles[third_room.proceed_index].set_event(
                E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM
            )
        else:
            container_script = world.get_event_script(third_room.proceed_index)
            jmp_cmd = container_script.contents[0]
            if isinstance(jmp_cmd, JmpToEvent):
                jmp_cmd.set_destination(E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM)
