"""Script snippets that can be inserted easily."""

from randomizer.entities.items.items import (
    BadMushroom,
    MaxMushroom,
    MidMushroom,
    MoldyMush,
    Mushroom,
    Mushroom2,
    RottenMush,
    WiltShroom)
from randomizer.types.overworld_scripts.arguments.variables import (
    ITEM_ID,
    PRIMARY_TEMP_7000)

from randomizer.types.overworld_scripts.event_scripts import (
    EventScript)
from randomizer.types.overworld_scripts.event_scripts.commands import (
    JmpIfVarEqualsConst,
    SetVarToRandom)
from randomizer.types.overworld_scripts.event_scripts.commands.commands import (
    Return,
    SetVarToConst)


script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 21),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_21_set_0"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_21_set_0"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_21_set_0"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_21_set_0"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_21_set_1"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_21_set_1"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_21_set_1"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_21_set_1"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_21_set_2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_21_set_2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_21_set_2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["EVENT_21_set_2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_21_set_3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_21_set_3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["EVENT_21_set_3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_21_set_4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_21_set_4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_21_set_4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 18, ["EVENT_21_set_5"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 19, ["EVENT_21_set_6"]),
        SetVarToConst(ITEM_ID, WiltShroom),
        Return(),
        SetVarToConst(ITEM_ID, Mushroom, identifier="EVENT_21_set_0"),
        Return(),
        SetVarToConst(ITEM_ID, MidMushroom, identifier="EVENT_21_set_1"),
        Return(),
        SetVarToConst(ITEM_ID, MaxMushroom, identifier="EVENT_21_set_2"),
        Return(),
        SetVarToConst(ITEM_ID, BadMushroom, identifier="EVENT_21_set_3"),
        Return(),
        SetVarToConst(ITEM_ID, Mushroom2, identifier="EVENT_21_set_4"),
        Return(),
        SetVarToConst(ITEM_ID, RottenMush, identifier="EVENT_21_set_5"),
        Return(),
        SetVarToConst(ITEM_ID, MoldyMush, identifier="EVENT_21_set_6"),
        Return(),
    ]
)
