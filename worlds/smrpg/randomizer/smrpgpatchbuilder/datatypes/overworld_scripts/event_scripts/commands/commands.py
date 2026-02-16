"""Individual event script command classes.
These are the building blocks of logical progression in SMRPG."""

from copy import deepcopy
from typing import cast
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import (
    LAYER_L1,
    LAYER_L2,
    LAYER_L3,
    LAYER_L4,
    NPC_SPRITES,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import (
    COORD_F,
)

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    ActionQueuePrototype,
    EventScriptCommand,
    EventScriptCommandNoArgs,
    EventScriptCommandAnySizeMem,
    EventScriptCommandBasicShortOperation,
    EventScriptCommandShortAddrAndValueOnly,
    EventScriptCommandWithJmps,
    EventScriptCommandShortMem,
    NonEmbeddedActionQueuePrototype,
    StartEmbeddedActionScriptPrototype,
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids.misc import (
    TOTAL_SCRIPTS,
)

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.ids.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS,
)

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)
from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.battlefield import (
    Battlefield,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.colour import Colour
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.coord import Coord
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.controller_input import (
    ControllerInput,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.direction import (
    Direction,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.intro_title_text import (
    IntroTitleText,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.palette_type import (
    PaletteType,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.layer import Layer
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.scene import Scene
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.tutorial import (
    Tutorial,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import Packet

from smrpgpatchbuilder.datatypes.overworld_scripts.ids.misc import (
    TOTAL_ROOMS,
    TOTAL_MUSIC,
    TOTAL_SOUNDS,
    TOTAL_SHOPS,
    TOTAL_WORLD_MAP_AREAS,
    TOTAL_DIALOGS,
)

from smrpgpatchbuilder.datatypes.items.classes import (
    Equipment,
    Item,
    Weapon,
    Armor,
    Accessory,
)

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt8
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.byte_var import (
    ByteVar,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.short_var import (
    ShortVar,
    TimerVar,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    InvalidCommandArgumentException,
)
from smrpgpatchbuilder.utils.number import bits_to_int, bools_to_int

# script operations


class StartLoopNFrames(UsableEventScriptCommand, EventScriptCommand):
    """Loop all commands (over a number of frames) between this command and the next `EndLoop` command.\n

    ## Lazy Shell command
        `Loop start, timer = ...`

    ## Opcode
        `0xD5`

    ## Size
        3 bytes

    Args:
        length (int): Duration (in frames) to loop over.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD5
    _size: int = 3
    _length: UInt16

    @property
    def length(self) -> UInt16:
        """The total duration of the loop, in frames"""
        return self._length

    def set_length(self, length: int) -> None:
        """Set the total duration of the loop, in frames"""
        self._length = UInt16(length)

    def __init__(self, length: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_length(length)

    def render(self, *args) -> bytearray:
        return super().render(self.length)


class StartLoopNTimes(UsableEventScriptCommand, EventScriptCommand):
    """Loop all commands (over a number of iterations) that are between this command and the next `EndLoop` command.\n

    ## Lazy Shell command
        `Loop start, count = ...`

    ## Opcode
        `0xD4`

    ## Size
        3 bytes

    Args:
        length (int): Number/count of times to loop.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD4
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        """The total number of times this loop should iterate"""
        return self._count

    def set_count(self, count: int) -> None:
        """Set the total number of times this loop should iterate"""
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self, *args) -> bytearray:
        return super().render(self.count)


class EndLoop(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """If previous commands were part of a loop, this is where the loop ends.\n

    ## Lazy Shell command
        `Loop end`

    ## Opcode
        `0xD7`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD7


class Jmp(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Goto a specific command. This uses another event's label instead of its address, which is calculated at build time.\n

    ## Lazy Shell command
        `Jump to address...`

    ## Opcode
        `0xD2`

    ## Size
        3 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of whatever command you want to jump to.
    """

    _opcode = 0xD2
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpToEvent(UsableEventScriptCommand, EventScriptCommand):
    """Goto event script by ID.\n

    ## Lazy Shell command
        `Run event...`

    ## Opcode
        `0xD0`

    ## Size
        3 bytes

    Args:
        destination (int): The ID of the event you want to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD0
    _size: int = 3
    _destination: UInt16

    @property
    def destination(self) -> UInt16:
        """The ID of the script to jump to."""
        return self._destination

    def set_destination(self, destination: int) -> None:
        """Set the ID of the script to jump to.\n
        It is highly recommended to use contextual event script
        const names for this."""
        assert 0 <= destination < TOTAL_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self, *args) -> bytearray:
        return super().render(self.destination)


class JmpToStartOfThisScript(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return to the beginning of the script containing this command.
    (Unknown how this differs from `JmpToStartOfThisScriptFA`.)

    ## Lazy Shell command
        `Jump to start of script`

    ## Opcode
        `0xF9`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF9


class JmpToStartOfThisScriptFA(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return to the beginning of the script containing this command.
    (Unknown how this differs from `JmpToStartOfThisScript`.)

    ## Lazy Shell command
        `Jump to start of script`

    ## Opcode
        `0xFA`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xFA


class JmpToSubroutine(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Run a chunk of event script code as a subroutine starting at a specified command. This uses another event's label instead of its address, which is calculated at build time.\n

    ## Lazy Shell command
        `Jump to subroutine...`

    ## Opcode
        `0xD3`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of the first command you want to run as part of your subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD3
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class MoveScriptToMainThread(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script from being a background process to being the main process.\n

    ## Lazy Shell command
        `Move script to main thread`

    ## Opcode
        `0xFD 0x40`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x40])


class MoveScriptToBackgroundThread1(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script to run as the first of two background processes.\n

    ## Lazy Shell command
        `Move script to background thread 1`

    ## Opcode
        `0xFD 0x41`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x41])


class MoveScriptToBackgroundThread2(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script to run as the second of two background processes.\n

    ## Lazy Shell command
        `Move script to background thread 2`

    ## Opcode
        `0xFD 0x42`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x42])


class Pause(UsableEventScriptCommand, EventScriptCommand):
    """Pause the active script for a number of frames.\n

    ## Lazy Shell command
        `Pause script for {xx} frames...`
        `Pause script for {xxxx} frames...`

    ## Opcode
        `0xF0`
        `0xF1`

    ## Size
        2 bytes
        3 bytes

    Args:
        length (int): Length of time (in frames) to pause. If this number is 256 or lower (you read that correctly, 256 or lower, not 255 or lower) this command will use the {xx} version (`0xF0`, 2 bytes). If larger, it will use the {xxxx} version (`0xF1`, 3 bytes).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _length: UInt8 | UInt16

    @property
    def length(self) -> int:
        """The length of the pause, in frames"""
        return self._length + 1

    @property
    def size(self) -> int:
        if isinstance(self._length, UInt8):
            return 2
        else:
            return 3

    def set_length(self, length: int) -> None:
        """Set the length of the pause, in frames, from 1 to 0x10000"""
        if 1 <= length <= 0x100:
            self._length = UInt8(length - 1)
        elif 1 <= length <= 0x10000:
            self._length = UInt16(length - 1)
        else:
            raise InvalidCommandArgumentException(
                f"illegal pause duration in {self.identifier}: {length}"
            )

    def __init__(self, length: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_length(length)

    def render(self, *args) -> bytearray:
        frames = self._length
        if isinstance(frames, UInt8):
            return super().render(0xF0, frames)
        return super().render(0xF1, frames)


class RememberLastObject(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)\n

    ## Lazy Shell command
        `Remember last object`

    ## Opcode
        `0xFD 0x32`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x32])


class ResumeBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """If a background event is paused, resume it.\n

    ## Lazy Shell command
        `Resume background event...`

    ## Opcode
        `0x47`

    ## Size
        2 bytes

    Args:
        timer_var (ShortVar): The timer memory variable to designate for this background event. You can use this to stop it later. Must a ShortVar instance of `0x701C`, `0x701E`, `0x7020`, or `0x7022`.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x47
    _size: int = 2
    _timer_var: TimerVar

    @property
    def timer_var(self) -> TimerVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown, but must be $701C, $701E, $7020, or $7022)"""
        self._timer_var = TimerVar(timer_var)

    def __init__(self, timer_var: ShortVar, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self, *args) -> bytearray:
        return super().render(self.timer_var)


class RunBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """Run an event (by ID) as a background event.\n

    ## Lazy Shell command
        `Run background event...`

    ## Opcode
        `0x40`

    ## Size
        3 bytes

    Args:
        event_id (int): The ID of the event you want to run in the background.
        return_on_level_exit (bool): If true, the background event will stop when the current level is unloaded.
        bit_6 (bool): (unknown)
        run_as_second_script (bool): If true, the event will run in background thread 2 instead of background thread 1.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x40
    _size: int = 3
    _event_id: UInt16
    _return_on_level_exit: bool
    _bit_6: bool
    _run_as_second_script: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def return_on_level_exit(self) -> bool:
        """If true, exit this script when the player exits the level."""
        return self._return_on_level_exit

    def set_return_on_level_exit(self, return_on_level_exit: bool) -> None:
        """If true, exit this script when the player exits the level."""
        self._return_on_level_exit = return_on_level_exit

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def run_as_second_script(self) -> bool:
        """If true, this script will run as the second background script (out of 2)."""
        return self._run_as_second_script

    def set_run_as_second_script(self, run_as_second_script: bool) -> None:
        """If true, this script will run as the second background script (out of 2)."""
        self._run_as_second_script = run_as_second_script

    def __init__(
        self,
        event_id: int,
        return_on_level_exit: bool = False,
        bit_6: bool = False,
        run_as_second_script: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.set_return_on_level_exit(return_on_level_exit)
        self.set_bit_6(bit_6)
        self.set_run_as_second_script(run_as_second_script)

    def render(self, *args) -> bytearray:
        flags: int = bools_to_int(
            self._return_on_level_exit, self.bit_6, self.run_as_second_script
        )
        flags = flags << 13
        arg_byte = UInt16(self.event_id + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPause(UsableEventScriptCommand, EventScriptCommand):
    """(unknown exactly how this differs from `RunBackgroundEvent`)\n

    ## Lazy Shell command
        `Run background event, pause...`

    ## Opcode
        `0x44`

    ## Size
        3 bytes

    Args:
        event_id (int): The ID of the event you want to run in the background.
        timer_var (ShortVar): The timer memory variable to designate for this background event. You can use this to stop it later. Must a ShortVar instance of `0x701C`, `0x701E`, `0x7020`, or `0x7022`.
        bit_4 (bool): (unknown)
        bit_5 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x44
    _size: int = 3
    _event_id: UInt16
    _timer_var: TimerVar
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> TimerVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        self._timer_var = TimerVar(timer_var)

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: ShortVar,
        bit_4: bool = False,
        bit_5: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.set_timer_var(timer_var)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)

    def render(self, *args) -> bytearray:
        flags: int = bools_to_int(self.bit_4, self.bit_5)
        flags = flags << 12
        timer = self.timer_var.to_byte() << 14
        arg_byte = UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPauseReturnOnExit(
    UsableEventScriptCommand, EventScriptCommand
):
    """(unknown exactly how this differs from `RunBackgroundEvent` with `return_on_level_exit` set to true)\n

    ## Lazy Shell command
        `Run background event, pause (return on exit)...`

    ## Opcode
        `0x45`

    ## Size
        3 bytes

    Args:
        event_id (int): The ID of the event you want to run in the background.
        timer_var (ShortVar): The timer memory variable to designate for this background event. You can use this to stop it later. Must a ShortVar instance of `0x701C`, `0x701E`, `0x7020`, or `0x7022`.
        bit_4 (bool): (unknown)
        bit_5 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x45
    _size: int = 3
    _event_id: UInt16
    _timer_var: TimerVar
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> TimerVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        self._timer_var = TimerVar(timer_var)

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: ShortVar,
        bit_4: bool = False,
        bit_5: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.set_timer_var(timer_var)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)

    def render(self, *args) -> bytearray:
        flags: int = bools_to_int(self.bit_4, self.bit_5)
        flags = flags << 12
        timer = self.timer_var.to_byte() << 14
        arg_byte = UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunEventAtReturn(UsableEventScriptCommand, EventScriptCommand):
    """When the current script ends, start running the script denoted by ID.\n

    ## Lazy Shell command
        `Run event at return...`

    ## Opcode
        `0xFD 0x46`

    ## Size
        4 bytes

    Args:
        event_id (int): The ID of the event you want to run on return.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x46])
    _size: int = 4
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to defer."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to defer.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)

    def render(self, *args) -> bytearray:
        return super().render(self.event_id)


class RunEventAsSubroutine(UsableEventScriptCommand, EventScriptCommand):
    """Run another event by ID as a subroutine (function).\n
    The game will crash if you call this method from code that is
    already itself being run as a subroutine, so be careful using it.\n

    ## Lazy Shell command
        `Run event as subroutine...`

    ## Opcode
        `0xD1`

    ## Size
        3 bytes

    Args:
        event_id (int): The ID of the event you want to run as a subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD1
    _size: int = 3
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run as a subroutine."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run as a subroutine.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)

    def render(self, *args) -> bytearray:
        return super().render(self.event_id)


class StopAllBackgroundEvents(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Halt all background events on all threads.\n

    ## Lazy Shell command
        `Stop all background events`

    ## Opcode
        `0xFD 0x43`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x43])


class StopBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """Stop a background event."\n

    ## Lazy Shell command
        `Stop background event...`

    ## Opcode
        `0x46`

    ## Size
        2 bytes

    Args:
        timer_var (ShortVar): The timer memory variable associated to the event you're stopping, probably set by `ResumeBackgroundEvent`, `RunBackgroundEventWithPause`, or `RunBackgroundEventWithPauseReturnOnExit`. Must a ShortVar instance of `0x701C`, `0x701E`, `0x7020`, or `0x7022`.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x46
    _size: int = 2
    _timer_var: TimerVar

    @property
    def timer_var(self) -> TimerVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        self._timer_var = TimerVar(timer_var)

    def __init__(self, timer_var: ShortVar, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self, *args) -> bytearray:
        return super().render(self.timer_var)


class Return(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Ends the script or subroutine.
    Every event needs to include this or `ReturnAll` because it indicates where the next script starts.\n

    ## Lazy Shell command
        `Return`

    ## Opcode
        `0xFE`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xFE


class ReturnAll(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Ends the script or subroutine. If this is run as part of a subroutine, it will also exit whatever code called the subroutine.
    Every event needs to include this or `Return` because it indicates where the next script starts.
    If your scripts do not add up to exactly the size of your bank, any remaining bytes are automatically filled with `ReturnAll` (you don't have to do this manually).\n

    ## Lazy Shell command
        `Return all`

    ## Opcode
        `0xFF`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xFF


class ReturnFD(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown, some kind of unused return command, unsure how it differs from others)\n

    ## Lazy Shell command
        N/A

    ## Opcode
        `0xFD 0xFE`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFE])


_valid_unknowncmd_opcodes: list[int] = [
    0,  # 00
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 10
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 20
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 30
    0,
    0,
    4,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    3,  # 40
    0,
    0,
    0,
    3,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    3,
    0,
    0,  # 50
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    0,  # 60
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    0,  # 70
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 80
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,  # 90
    0,
    0,
    0,
    0,
    0,
    3,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    3,
    0,  # A0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # B0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # C0
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    0,  # D0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # E0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # F0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    0,
]
_valid_unknowncmd_opcodes_fd: list[int] = [
    0,  # 00
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 10
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 20
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 30
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    4,
    0,  # 40
    0,
    0,
    0,
    2,
    2,
    0,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,  # 50
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,  # 60
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 70
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 80
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    3,
    0,
    5,
    2,
    5,
    3,
    0,  # 90
    0,
    0,
    0,
    0,
    3,
    0,
    0,
    3,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    0,  # A0
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    2,
    0,
    2,
    2,
    2,
    0,  # B0
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # C0
    2,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # D0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # E0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,  # F0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]


class UnknownCommand(UsableEventScriptCommand, EventScriptCommand):
    """Catch-all class for most undocumented commands that don't act as GOTOs.
    Use this sparingly. This command will verify that your bytearray is the correct length, but cannot validate it otherwise.
    You can't use this if your bytearray starts with an opcode that already has a class. For example `UnknownCommand(bytearray([0xA4, 0x24]))` will fail because `ClearBit` already uses opcode `0xA4`.

    ## Lazy Shell command
        Almost any lazy shell command represented solely as bytes, i.e. `{FD-45}` in the original game's event #478

    ## Opcode
        Any that don't already belong to another class

    ## Size
        Determined by the first byte (or two bytes if first byte is `0xFD`). Same as the length of `contents` if you did it right.

    Args:
        contents (bytearray): The entire byte string that this command consists of.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _contents: bytearray

    @property
    def contents(self) -> bytearray:
        """The whole contents of the command as bytes, including the opcode."""
        return self._contents

    def set_contents(self, contents: bytearray) -> None:
        """Set the whole contents of the command as bytes, including the opcode."""
        first_byte = contents[0]
        if first_byte == 0xFD:
            opcode = contents[1]
            expected_length = _valid_unknowncmd_opcodes_fd[opcode]
            if expected_length == 0:
                raise InvalidCommandArgumentException(
                    f"do not use UnknownCommand for opcode 0xFD 0x{opcode:02X}, there is already a class for it"
                )
            if len(contents) != expected_length:
                raise InvalidCommandArgumentException(
                    f"opcode 0xFD 0x{opcode:02X} expects {expected_length} total bytes (inclusive), got {len(contents)} bytes instead"
                )
        else:
            opcode = first_byte
            expected_length = _valid_unknowncmd_opcodes[opcode]
            if expected_length == 0:
                raise InvalidCommandArgumentException(
                    f"do not use UnknownCommand for opcode 0x{opcode:02X}, there is already a class for it"
                )
            if len(contents) != expected_length:
                raise InvalidCommandArgumentException(
                    f"opcode 0x{opcode:02X} expects {expected_length} total bytes (inclusive), got {len(contents)} bytes instead"
                )
        self._contents = contents

    @property
    def size(self) -> int:
        return len(self.contents)

    def __init__(self, contents: bytearray, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_contents(contents)

    def render(self, *args) -> bytearray:
        return super().render(self.contents)


# memory operations


class If0210Bits012ClearDoNotJump(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)

    ## Lazy Shell command
        `(not available in Lazy Shell)`

    ## Opcode
        `0xFD 0x62`

    ## Size
        4 bytes

    Args:
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of the first command you want to run as part of your subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x62])
    _size: int = 4

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIf316DIs3(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)

    ## Lazy Shell command
        `(not available in Lazy Shell)`

    ## Opcode
        `0x41`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of the first command you want to run as part of your subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x41
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIf7000AllBitsClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If all of the stated bits are clear on $7000, jump to the script command indicated by the given label.

    ## Lazy Shell command
        `If memory $7000 all bits {xx} clear...`

    ## Opcode
        `0xE6`

    ## Size
        5 bytes

    Args:
        bits (list[int]): The list of bits (0 to 7) all of which should be clear in order to GOTO.
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of the first command you want to run as part of your subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE6
    _size: int = 5
    _bits: set[int]

    @property
    def bits(self) -> set[int]:
        """All of the bit positions which should be clear in order to execute the goto."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Overwrite the list of the bit positions which should be clear
        in order to execute the goto."""
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = set(bits)

    def __init__(
        self,
        bits: list[int],
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt16(bits_to_int(list(self.bits)))
        return super().render(flags, *self.destinations)


class JmpIf7000AnyBitsSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If any of the stated bits are set on $7000, go to to the script command indicated by the given label.

    ## Lazy Shell command
        `If memory $7000 any bits {xx} set...`

    ## Opcode
        `0xE7`

    ## Size
        5 bytes

    Args:
        bits (list[int]): The list of bits (0 to 7) any of which should be clear in order to GOTO.
        destinations (list[str]): A list of exactly one string. The string will be the `identifier` property of the first command you want to run as part of your subroutine.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE7
    _size: int = 5
    _bits: set[int]

    @property
    def bits(self) -> set[int]:
        """The bit positions, of which any should be set in order to execute the goto."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Overwrite the list of the bit positions which, if any one is set,
        would execute the goto."""
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = set(bits)

    def __init__(
        self,
        bits: list[int],
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt16(bits_to_int(list(self.bits)))
        return super().render(flags, *self.destinations)


class JmpIfBitSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Goto a command indicated by its label, but only if the memory bit is set.

    ## Lazy Shell command
        `If memory $704x bit {xx} set...`

    ## Opcode
        `0xD8`
        `0xD9`
        `0xDA`

    ## Size
        4 bytes

    Args:
        bit (Flag): The byte bit that needs to be set for the goto to happen.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit which, if set, proceeds to go to the code section
        indicated by the provided identifier."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if set, proceeds to go to the code section
        indicated by the provided identifier."""
        self._bit = bit

    def __init__(
        self, bit: Flag, destinations: list[str], identifier: str | None = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bit(bit)

    def render(self, *args) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xDA)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xD9)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xD8)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg, *self.destinations)


class JmpIfBitClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Goto a command indicated by its label, but only if the memory bit is clear.

    ## Lazy Shell command
        `If memory $704x bit {xx} clear...`

    ## Opcode
        `0xDC`
        `0xDD`
        `0xDE`

    ## Size
        4 bytes

    Args:
        bit (Flag): The byte bit that needs to be clear for the goto to happen.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        self._bit = bit

    def clear_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        self.set_bit(bit)

    def __init__(
        self, bit: Flag, destinations: list[str], identifier: str | None = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bit(bit)

    def render(self, *args) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xDE)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xDD)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xDC)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg, *self.destinations)


class JmpIfLoadedMemoryIs0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command. Jump to the code indicated by the given label if the comparison result was zero (both values were equal).

    ## Lazy Shell command
        `If loaded memory = 0...`

    ## Opcode
        `0xEA`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xEA
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """'Loaded Memory' in most cases refers to the result of a comparison command. Jump to the code indicated by the given label if the comparison result indicated that the first value was less than or equal the second value.

    ## Lazy Shell command
        `If loaded memory >= 0...`

    ## Opcode
        `0xEF`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xEF
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command. Jump to another command (by label) if the comparison result indicated that the first value was greater than the second value.

    ## Lazy Shell command
        `If loaded memory < 0...`

    ## Opcode
        `0xEE`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xEE
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command. Jump to the code indicated by the given label if the comparison result was not zero (values were not equal, irrespective of which was larger or smaller).

    ## Lazy Shell command
        `If loaded memory != 0...`

    ## Opcode
        `0xEB`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xEB
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a command by label, but only if the bit corresponding to the index indicated by the value of $7000 is set.
    For example, if $7000 is set to 5, then this command will jump to the code beginning at the given destination if $7040 bit 5 is set. If $7000 is set to 12, then the jump will occur if $7041 bit 4 is set.

    ## Lazy Shell command
        `If Memory $704x [x @ $7000] bit {xx} set...`

    ## Opcode
        `0xDB`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xDB
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a command by label, but only if the bit corresponding to the index indicated by the value of $7000 is clear.
    For example, if $7000 is set to 5, then this command will jump to the code beginning at the given destination if $7040 bit 5 is clear. If $7000 is set to 12, then the jump will occur if $7041 bit 4 is clear.

    ## Lazy Shell command
        `If Memory $704x [x @ $7000] bit {xx} clear...`

    ## Opcode
        `0xDF`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 3
    _opcode = 0xDF

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class SetMem704XAt7000Bit(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the literal value currently stored at $7000, set the bit that corresponds to this index (starting from $7040 bit 0).
    For example, if $7000 is set to 5, then $7040 bit 5 will be set. If $7000 is set to 12, then $7041 bit 4 will be set.

    ## Lazy Shell command
        `Memory $704x [x is @ $7000] bit {xx} set...`

    ## Opcode
        `0xA3`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xA3


class ClearMem704XAt7000Bit(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the literal value currently stored at $7000, clear the bit that corresponds to this index (starting from $7040 bit 0).
    For example, if $7000 is set to 5, then $7040 bit 5 will be clear. If $7000 is set to 12, then $7041 bit 4 will be clear.

    ## Lazy Shell command
        `Memory $704x [x is @ $7000] bit {xx} clear...`

    ## Opcode
        `0xA7`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xA7


class Move70107015To7016701B(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7010, $7012, and $7014 to replace the 16 bit values stored at $7016, $7018, and $701A.

    ## Lazy Shell command
        (not documented in Lazy Shell)

    ## Opcode
        `0xBE`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBE


class Move7016701BTo70107015(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7016, $7018, and $701A to replace the 16 bit values stored at $7010, $7012, and $7014.

    ## Lazy Shell command
        (not documented in Lazy Shell)

    ## Opcode
        `0xBF`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBF


class SetVarToConst(UsableEventScriptCommand, EventScriptCommand):
    """Set the longterm mem var to a constant number value.

    ## Lazy Shell command
        `Memory $70Ax = ...`
        `Memory $7000 = ...`
        `Memory $7xxx = ...`

    ## Opcode
        `0xA8`
        `0xAC`
        `0xB0`

    ## Size
        3 bytes if the variable is $7000 or a single-byte var
        4 bytes if the variable is a short var

    Args:
        address (ShortVar | ByteVar): The variable you want to set
        value (int | type[Item]): The const you want to set the variable to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def set_value_and_address(
        self,
        address: ByteVar | ShortVar | None = None,
        value: int | type[Item] | None = None,
    ) -> None:
        """Set the literal value, the destination variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.label}: 0x{address:04x}: {value}"
            )
        if address == ShortVar(0x7000) or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> UInt8 | UInt16:
        """The literal value to set the variable to."""
        return self._value

    @property
    def address(self) -> ShortVar | ByteVar:
        """The variable to store the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def __init__(
        self,
        address: ShortVar | ByteVar,
        value: int | type[Item],
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_value_and_address(address, value)

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA8, self.address, self.value)
        if self.address == ShortVar(0x7000):
            return super().render(0xAC, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB0, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}: {self.value}"
        )


class ReadFromAddress(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        `(Don't think this one is available in Lazy Shell)`

    ## Opcode
        `0x5C`

    ## Size
        3 bytes

    Args:
        address (int): The address to read from. I don't know what this command does, so this can be any short uint.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x5C
    _size: int = 3
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        return super().render(self.address)


class Set7000To7FMemVar(UsableEventScriptCommand, EventScriptCommand):
    """Set the value of $7000 to the value of any address between $7FF800 and $7FFFFF. This includes long term battle memory like Super Jump PBs.

    ## Lazy Shell command
        `Memory $7000 = memory $7Fxxxx...`

    ## Opcode
        `0xFD 0xAC`

    ## Size
        4 bytes

    Args:
        address (int): The last four hex digits of the var you want to read
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xAC])
    _size: int = 4
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """The address to copy from."""
        return self._address

    def set_address(self, address: int) -> None:
        """Designate the address for this command to copy from.
        Must be from 0xF800 to 0xFFFF."""
        assert address >= 0xF800
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        return super().render(UInt16(self.address - 0xF800))


class SetBit(UsableEventScriptCommand, EventScriptCommand):
    """Set a bit in the range of long-term memory bits dedicated for use in event and action scripts.

    ## Lazy Shell command
        `Memory $704x bit {xx} set...`

    ## Opcode
        `0xA0`
        `0xA1`
        `0xA2`

    ## Size
        2 bytes

    Args:
        bit (Flag): The byte bit you wish to set.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit to set."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit to set."""
        self._bit = bit

    def __init__(self, bit: Flag, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self, *args) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xA2)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xA1)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xA0)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class ClearBit(UsableEventScriptCommand, EventScriptCommand):
    """Clear a bit in the range of long-term memory bits dedicated for use in event and action scripts.

    ## Lazy Shell command
        `Memory $704x bit {xx} clear...`

    ## Opcode
        `0xA4`
        `0xA5`
        `0xA6`

    ## Size
        2 bytes

    Args:
        bit (Flag): The byte bit you wish to clear.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit to clear."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit to clear."""
        self._bit = bit

    def clear_bit(self, bit: Flag) -> None:
        """Designate the exact bit to clear."""
        self.set_bit(bit)

    def __init__(self, bit: Flag, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self, *args) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xA6)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xA5)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xA4)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class Set0158Bit3Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x8B`

    ## Size
        3 bytes

    Args:
        address (int): Any 16 bit addr above 0x0158 (?)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x8B])
    _size: int = 3
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: str | None = None):
        super().__init__(identifier)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        return super().render(address_byte)


class Set0158Bit7Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x88`

    ## Size
        3 bytes

    Args:
        address (int): Any 16 bit addr above 0x0158 (?)
        bit_7 (bool): unknown
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x88])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self, address: int, bit_7: bool = False, identifier: str | None = None
    ):
        super().__init__(identifier)
        self.set_address(address)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        address_byte += self.bit_7 << 7
        return super().render(address_byte)


class Clear0158Bit7Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x89`

    ## Size
        3 bytes

    Args:
        address (int): Any 16 bit addr above 0x0158 (?)
        bit_7 (bool): unknown
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x89])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self, address: int, bit_7: bool = False, identifier: str | None = None
    ):
        super().__init__(identifier)
        self.set_address(address)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        address_byte += self.bit_7 << 7
        return super().render(address_byte)


class Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xC6`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xC6])
    _size: int = 2


class CopyVarToVar(UsableEventScriptCommand, EventScriptCommand):
    """Copy the value from one variable to another variable.

    ## Lazy Shell command
        `Memory $7000 = memory $70Ax...`
        `Memory $70Ax = memory $7000...`
        `Memory $7000 = memory $7xxx...`
        `Memory $7xxx = memory $7000...`
        `Memory $7xxx = memory $7xxx...`

    ## Opcode
        `0xB4`
        `0xB5`
        `0xBA`
        `0xBB`
        `0xBC`

    ## Size
        3 bytes if neither variable is $7000
        2 bytes otherwise

    Args:
        from_var (ShortVar | ByteVar): The variable you're copying the value **from**.
        to_var (ShortVar | ByteVar): The variable you're copying the value **to**.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _from_var: ShortVar | ByteVar
    _to_var: ShortVar | ByteVar

    def set_addresses(self, from_var=None, to_var=None):
        """Set the source variable, destination variable, or both.\n
        Can accept either two 16 bit ShortVars, or $7000 and one ByteVar or ShortVar.
        Cannot accept two ByteVars."""
        if from_var is None:
            from_var = self.from_var
        if to_var is None:
            to_var = self.to_var
        if isinstance(from_var, ByteVar) and isinstance(to_var, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.label}: 0x{from_var:04x} 0x{to_var:04x}"
            )

    @property
    def size(self) -> int:
        if ShortVar(0x7000) not in (self.from_var, self.to_var):
            return 3
        else:
            return 2

    @property
    def from_var(self) -> ShortVar | ByteVar:
        """The source variable, which the value is copied from."""
        return self._from_var

    def set_from_var(self, from_var: ShortVar | ByteVar) -> None:
        """Set the source variable, which the value is copied from."""
        self.set_addresses(from_var=from_var)

    @property
    def to_var(self) -> ShortVar | ByteVar:
        """The destination variable, where the value is written to."""
        return self._to_var

    def set_to_var(self, to_var: ShortVar | ByteVar) -> None:
        """Set the destination variable, where the value is written to."""
        self.set_addresses(to_var=to_var)

    def __init__(
        self,
        from_var: ShortVar | ByteVar,
        to_var: ShortVar | ByteVar,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self._from_var = from_var
        self._to_var = to_var
        self.set_addresses(from_var, to_var)

    def render(self, *args) -> bytearray:
        if self.to_var == ShortVar(0x7000) and isinstance(self.from_var, ByteVar):
            return super().render(0xB4, self.from_var)
        if self.from_var == ShortVar(0x7000) and isinstance(self.to_var, ByteVar):
            return super().render(0xB5, self.to_var)
        if self.to_var == ShortVar(0x7000) and isinstance(self.from_var, ShortVar):
            return super().render(0xBA, self.from_var)
        if self.from_var == ShortVar(0x7000) and isinstance(self.to_var, ShortVar):
            return super().render(0xBB, self.to_var)
        if isinstance(self.from_var, ShortVar) and isinstance(self.to_var, ShortVar):
            return super().render(0xBC, self.from_var, self.to_var)
        raise InvalidCommandArgumentException(
            f"""illegal args for {self.identifier.label}: 
            0x{self.from_var:04x} 0x{self.to_var:04x}"""
        )


class StoreBytesTo0335And0556(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x90`

    ## Size
        4 bytes

    Args:
        value_1 (int): Unknown 8 bit int
        value_2 (int): Unknown 8 bit int
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x90])
    _size: int = 4
    _value_1: UInt8
    _value_2: UInt8

    @property
    def value_1(self) -> UInt8:
        """(unknown)"""
        return self._value_1

    def set_value_1(self, value_1: int) -> None:
        """(unknown)"""
        self._value_1 = UInt8(value_1)

    @property
    def value_2(self) -> UInt8:
        """(unknown)"""
        return self._value_2

    def set_value_2(self, value_2: int) -> None:
        """(unknown)"""
        self._value_2 = UInt8(value_2)

    def __init__(
        self, value_1: int, value_2: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_value_1(value_1)
        self.set_value_2(value_2)

    def render(self, *args) -> bytearray:
        return super().render(self.value_1, self.value_2)


class Store00To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xFC`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFC])


class Store00To0334(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x93`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x93])


class Store01To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xFB`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFB])


class Store01To0335(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x92`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x92])


class Store02To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xFD`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFD])


class StoreFFTo0335(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0x91`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x91])


class Set7000ToMinecartTimer(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the value of $7000 to the latest value of the minecraft timer.

    ## Lazy Shell command
        `Memory $7000 = Moleville Mountain timer`

    ## Opcode
        `0xFD 0xB8`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB8])


class StoreSetBits(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        Registers as `Memory $704x bit {xx} set`, but this might be erroneous because that command's opcode is 0xA0 (no FD).
        Might not truly have a representative Lazy Shell command.

    ## Opcode
        `0xFD 0xA8`
        `0xFD 0xA9`
        `0xFD 0xAA`

    ## Size
        3 bytes

    Args:
        bit (Flag): Description here to be filled out by me
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 3
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """(unknown)"""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """(unknown)"""
        self._bit = bit

    def __init__(self, bit: Flag, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self, *args) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = bytearray([0xFD, 0xAA])
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = bytearray([0xFD, 0xA9])
            offset = ShortVar(0x7060)
        else:
            opcode = bytearray([0xFD, 0xA8])
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class SwapVars(UsableEventScriptCommand, EventScriptCommand):
    """Swap the two variables' vales.

    ## Lazy Shell command
        `Memory $7xxx <=> memory $7xxx...`

    ## Opcode
        `0xBD`

    ## Size
        3 bytes

    Args:
        memory_a (ShortVar): The first of the two variables you want to swap.
        memory_b (ShortVar): The second of the two variables you want to swap.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBD
    _size: int = 3
    _memory_a: ShortVar
    _memory_b: ShortVar

    @property
    def memory_a(self) -> ShortVar:
        """The first variable whose value to swap."""
        return self._memory_a

    def set_memory_a(self, memory_a: ShortVar) -> None:
        """Set the first variable whose value to swap."""
        self._memory_a = memory_a

    @property
    def memory_b(self) -> ShortVar:
        """The second variable whose value to swap."""
        return self._memory_b

    def set_memory_b(self, memory_b: ShortVar) -> None:
        """Set the second variable whose value to swap."""
        self._memory_b = memory_b

    def __init__(
        self,
        memory_a: ShortVar,
        memory_b: ShortVar,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_memory_a(memory_a)
        self.set_memory_b(memory_b)

    def render(self, *args) -> bytearray:
        return super().render(self.memory_b, self.memory_a)


# math operations


class AddConstToVar(UsableEventScriptCommand, EventScriptCommand):
    """Add a const number value to a longterm mem var.

    ## Lazy Shell command
        `Memory $70Ax += ...`
        `Memory $7000 += ...`
        `Memory $7xxx += ...`

    ## Opcode
        `0xA9`
        `0xAD`
        `0xB1`

    ## Size
        3 bytes if the variable is $7000 or a single-byte var
        4 bytes if the variable is a short var

    Args:
        address (ShortVar | ByteVar): The variable you want to add to
        value (int | type[Item]): The const you want to add to the variable
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _value: UInt8 | UInt16
    _address: ShortVar | ByteVar

    def set_value_and_address(self, address=None, value=None) -> None:
        """Set the literal value, the destination variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.label}: 0x{address:04x}: {value}"
            )
        if address == ShortVar(0x7000) or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> UInt8 | UInt16:
        """The literal value to set the variable to."""
        return self._value

    def set_value(self, value: int) -> None:
        """Set the literal value to add to the variable."""
        self.set_value_and_address(value=value)

    @property
    def address(self) -> ShortVar | ByteVar:
        """The variable to store the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def set_address(self, address: ShortVar | ByteVar) -> None:
        """Set the variable to add the value to."""
        self.set_value_and_address(address=address)

    def __init__(
        self,
        address: ShortVar | ByteVar,
        value: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_value_and_address(address, value)

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA9, self.address, self.value)
        if self.address == ShortVar(0x7000):
            return super().render(0xAD, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB1, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}: {self.value}"
        )


class Inc(UsableEventScriptCommand, EventScriptCommandAnySizeMem):
    """Increase a variable by 1.

    ## Lazy Shell command
        `Memory $70Ax += 1...`
        `Memory $7000 += 1`
        `Memory $7xxx += 1...`

    ## Opcode
        `0xAA`
        `0xAE`
        `0xB2`

    ## Size
        1 byte if the variable is $7000
        2 bytes if any other variable

    Args:
        address (ShortVar | ByteVar): The variable you want to increase by 1
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAA, self.address)
        if self.address == ShortVar(0x7000):
            return super().render(0xAE)
        if isinstance(self.address, ShortVar):
            return super().render(0xB2, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}"
        )


class Dec(UsableEventScriptCommand, EventScriptCommandAnySizeMem):
    """Decrease a variable by 1.

    ## Lazy Shell command
        `Memory $70Ax -= 1...`
        `Memory $7000 -= 1`
        `Memory $7xxx -= 1...`

    ## Opcode
        `0xAB`
        `0xAF`
        `0xB3`

    ## Size
        1 byte if the variable is $7000
        2 bytes if any other variable

    Args:
        address (ShortVar | ByteVar): The variable you want to decrease by 1
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAB, self.address)
        if self.address == ShortVar(0x7000):
            return super().render(0xAF)
        if isinstance(self.address, ShortVar):
            return super().render(0xB3, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}"
        )


class AddVarTo7000(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Add the value stored at the given variable to $7000.

    ## Lazy Shell command
        `Memory $7000 += memory $7xxx...`

    ## Opcode
        `0xB8`

    ## Size
        2 bytes

    Args:
        address (ShortVar | ByteVar): The variable you want to add to $7000
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB8
    _size: int = 2


class DecVarFrom7000(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Subtract the value stored at the given variable from $7000.

    ## Lazy Shell command
        `Memory $7000 -= memory $7xxx...`

    ## Opcode
        `0xB9`

    ## Size
        2 bytes

    Args:
        address (ShortVar | ByteVar): The variable you want to subtract from $7000
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB9
    _size: int = 2


class GenerateRandomNumFromRangeVar(
    UsableEventScriptCommand, EventScriptCommandShortMem
):
    """Use the value of the given variable as an upper range
    to generate a random number with between 0 and that value.

        ## Lazy Shell command
            `Generate random # between 0 and memory $7xxx...`

        ## Opcode
            `0xFD 0xB7`

        ## Size
            3 bytes

        Args:
            identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB7])
    _size: int = 3


class JmpIfRandom2of3(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """There is a 2/3 chance that, when this command is executed, the script will jump to one of the two commands indicated by label.

    ## Lazy Shell command
        `If random # between 0 and 255 > 66...`

    ## Opcode
        `0xE9`

    ## Size
        5 bytes

    Args:
        destinations (list[str]): This should be a list of exactly two `str`s. The `str`s should be the labels of the two commands that there should be a 33% chance to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE9
    _size: int = 5

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandom1of2(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """There is a 50/50 chance that, when this command is executed, a goto will be performed to the command indicated by the given label.

    ## Lazy Shell command
        `If random # between 0 and 255 > 128...`

    ## Opcode
        `0xE8`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command that there should be a 50% chance to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE8
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(UsableEventScriptCommand, EventScriptCommandShortAddrAndValueOnly):
    """Set the given variable to a random number between 0 and the given upper bound.

    ## Lazy Shell command
        `Memory $7000 = random # between 0 and {xx}...`
        `Memory $7xxx = random # between 0 and {xx}...`

    ## Opcode
        `0xB6`
        `0xB7`

    ## Size
        3 bytes if the variable is $7000
        4 bytes otherwise

    Args:
        address (ShortVar | ByteVar): The variable you want to set
        value (int): The upper bound of possible random values (lower bound is always 0). 16 bit int.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        if self.address == ShortVar(0x7000):
            return super().render(0xB6, self.value)
        return super().render(0xB7, self.address, self.value)


class CompareVarToConst(
    UsableEventScriptCommand, EventScriptCommandShortAddrAndValueOnly
):
    """Compare a variable's value to a constant number.
    The result of this comparison can be used in `JmpIfComparisonResultIs...` commands or `JmpIfLoadedMemory...` commands.

    ## Lazy Shell command
        `Memory $7000 compare to {xx}...`
        `Memory $7xxx compare to {xx}...`

    ## Opcode
        `0xC0`
        `0xC2`

    ## Size
        3 bytes if the variable is $7000
        4 bytes otherwise

    Args:
        address (ShortVar): The variable in question
        value (int | type[Item]): The constant number to compare the variable to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        if self.address == ShortVar(0x7000):
            return super().render(0xC0, self.value)
        return super().render(0xC2, self.address, self.value)

    def __init__(
        self,
        address: ShortVar | ByteVar,
        value: int | type[Item],
        identifier: str | None = None,
    ) -> None:
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        addr = deepcopy(address)
        if isinstance(addr, ByteVar):
            addr = ShortVar(addr)
        super().__init__(addr, value, identifier)


class Compare7000ToVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Compare the value stored at $7000 to the value stored at a given variable.
    The result of this comparison can be used in `JmpIfComparisonResultIs`... commands
    or `JmpIfLoadedMemory`... commands.

    ## Lazy Shell command
        `Memory $7000 compare to $7xxx...`

    ## Opcode
        `0xC1`

    ## Size
        2 bytes

    Args:
        address (ShortVar): The variable to compare $7000 against
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xC1
    _size: int = 2


class JmpIfComparisonResultIsGreaterOrEqual(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depending on the result of an earlier `CompareVarToConst` or `Compare7000ToVar`, jump to another command (by label) if the comparison result returned greater or equal.

    ## Lazy Shell command
        `If comparison result is: >=...`

    ## Opcode
        `0xEC`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xEC
    _size = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depending on the result of an earlier `CompareVarToConst` or `Compare7000ToVar`, jump to another command (by label) if the comparison result returned lesser.

    ## Lazy Shell command
        `If comparison result is: <...`

    ## Opcode
        `0xED`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xED
    _size = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfVarEqualsConst(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the given variable matches the given value, jump to the section of code beginning with the given label.

    ## Lazy Shell command
        `If memory $70Ax = ...`
        `If memory $7000 =...`
        `If memory $7xxx = ...`

    ## Opcode
        `0xE0`
        `0xE2`
        `0xE4`

    ## Size
        5 bytes if `address` is $7000
        6 bytes otherwise

    Args:
        address (ShortVar | ByteVar): The variable you want to check
        value (int | type[Item]): The value to check the variable against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the variable equals the value.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _value: UInt8 | UInt16
    _address: ShortVar | ByteVar

    def set_value_and_address(
        self,
        address: ByteVar | ShortVar | None = None,
        value: int | type[Item] | None = None,
    ) -> None:
        """Set the literal value, the comparison variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.label}: 0x{address:04x}: {value}"
            )
        if address == ShortVar(0x7000) or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> UInt8 | UInt16:
        """The literal value to set the variable to."""
        return self._value

    def set_value(self, value: int | type[Item]) -> None:
        """Set the value to compare the variable against."""
        self.set_value_and_address(value=value)

    @property
    def address(self) -> ShortVar | ByteVar:
        """The variable to compare the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def set_address(self, address: ShortVar | ByteVar) -> None:
        """Set the variable to compare the value against."""
        self.set_value_and_address(address=address)

    def __init__(
        self,
        address: ByteVar | ShortVar,
        value: int | type[Item],
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(address, value)

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE0, self.address, self.value, *self.destinations)
        if self.address == ShortVar(0x7000):
            return super().render(0xE2, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE4, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}: {self.value}"
        )


class JmpIfVarNotEqualsConst(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the given variable does not match the given value, jump to the section of code beginning with the given label.

    ## Lazy Shell command
        `If memory $70Ax != ...`
        `If memory $7000 !=...`
        `If memory $7xxx != ...`

    ## Opcode
        `0xE1`
        `0xE3`
        `0xE5`

    ## Size
        5 bytes if `address` is $7000
        6 bytes otherwise

    Args:
        address (ShortVar | ByteVar): The variable you want to check
        value (int | type[Item]): The value to check the variable against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the variable doesn't equal the value.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _value: UInt8 | UInt16
    _address: ShortVar | ByteVar

    def set_value_and_address(
        self,
        address: ByteVar | ShortVar | None = None,
        value: int | type[Item] | None = None,
    ) -> None:
        """Set the literal value, the comparison variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.label}: 0x{address:04x}: {value}"
            )
        if address == ShortVar(0x7000) or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> UInt8 | UInt16:
        """The literal value to set the variable to."""
        return self._value

    def set_value(self, value: int | type[Item]) -> None:
        """Set the value to compare the variable against."""
        self.set_value_and_address(value=value)

    @property
    def address(self) -> ShortVar | ByteVar:
        """The variable to compare the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def set_address(self, address: ShortVar | ByteVar) -> None:
        """Set the variable to compare the value against."""
        self.set_value_and_address(address=address)

    def __init__(
        self,
        address: ByteVar | ShortVar,
        value: int | type[Item],
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(address, value)

    def render(self, *args) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE1, self.address, self.value, *self.destinations)
        if self.address == ShortVar(0x7000):
            return super().render(0xE3, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE5, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.label}: 0x{self.address:04x}: {self.value}"
        )


class Mem7000AndConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform a bitwise AND operation between the value of $7000 and a given literal number, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 &= {xx}...`

    ## Opcode
        `0xFD 0xB0`

    ## Size
        4 bytes

    Args:
        value (int): A number (up to 16 bits) to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB0])


class Mem7000AndVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform a bitwise AND operation between the value of $7000 and another variable, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 &= memory $7xxx...`

    ## Opcode
        `0xFD 0xB3`

    ## Size
        3 bytes

    Args:
        address (ShortVar | ByteVar): The variable you want to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem7000OrConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform a bitwise OR operation between the value of $7000 and a given literal number, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 |= {xx}...`

    ## Opcode
        `0xFD 0xB1`

    ## Size
        4 bytes

    Args:
        value (int): A number (up to 16 bits) to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB1])


class Mem7000OrVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform a bitwise OR operation between the value of $7000 and another variable, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 |= memory $7xxx...`

    ## Opcode
        `0xFD 0xB4`

    ## Size
        3 bytes

    Args:
        address (ShortVar | ByteVar): The variable you want to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem7000XorConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform a bitwise XOR operation between the value of $7000 and a given literal number, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 ^= {xx}...`

    ## Opcode
        `0xFD 0xB2`

    ## Size
        4 bytes

    Args:
        value (int): A number (up to 16 bits) to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB2])


class Mem7000XorVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform a bitwise XOR operation between the value of $7000 and another variable, save the result to $7000.

    ## Lazy Shell command
        `Memory $7000 ^= memory $7xxx...`

    ## Opcode
        `0xFD 0xB5`

    ## Size
        3 bytes

    Args:
        address (ShortVar | ByteVar): The variable you want to use in the bitwise operation.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(UsableEventScriptCommand, EventScriptCommand):
    """Shift the specified variable to the left by the given amount of bits.

    ## Lazy Shell command
        `Memory $7xxx shift left {xx} times...`

    ## Opcode
        `0xFD 0xB6`

    ## Size
        4 bytes

    Args:
        address (ShortVar): The variable to have its value shifted.
        shift (int): The amount of bits to shift the value left by.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xB6])
    _size: int = 4
    _address: ShortVar
    _shift: UInt8

    @property
    def address(self) -> ShortVar:
        """The variable to have its value shifted."""
        return self._address

    def set_address(self, address: ShortVar) -> None:
        """Designate te variable to have its value shifted."""
        self._address = address

    @property
    def shift(self) -> UInt8:
        """The amount of bits to shift the value left by."""
        return UInt8(self._shift + 1)

    def set_shift(self, shift: int) -> None:
        """Set the amount of bits to shift the value left by."""
        assert 1 <= shift <= 256
        self._shift = UInt8(shift - 1)

    def __init__(
        self, address: ShortVar, shift: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_shift(shift)

    def render(self, *args) -> bytearray:
        return super().render(self.address, 0xFF - self._shift)


class MultiplyAndAddMem3148StoreToOffset7fB000PlusOutputX2(
    UsableEventScriptCommand, EventScriptCommand
):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xC8`

    ## Size
        4 bytes

    Args:
        adding (int): Description here to be filled out by me
        multiplying (int): Description here to be filled out by me
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xC8])
    _size: int = 4
    _adding: UInt8
    _multiplying: UInt8

    @property
    def adding(self) -> UInt8:
        """(unknown)"""
        return self._adding

    def set_adding(self, adding: int) -> None:
        """(unknown)"""
        self._adding = UInt8(adding)

    @property
    def multiplying(self) -> UInt8:
        """(unknown)"""
        return self._multiplying

    def set_multiplying(self, multiplying: int) -> None:
        """(unknown)"""
        self._multiplying = UInt8(multiplying)

    def __init__(
        self, adding: int, multiplying: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_adding(adding)
        self.set_multiplying(multiplying)

    def render(self, *args) -> bytearray:
        return super().render(self.adding, self.multiplying)


class Xor3105With01(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        (not available in Lazy Shell)

    ## Opcode
        `0xFD 0xFE`

    ## Size
        ? bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFE])


# room objects & camera


class ActionQueueAsync(UsableEventScriptCommand, ActionQueuePrototype):
    """The specified NPC performs the given set of action script commands.
    The included action script must complete before the parent event script is allowed to continue.

    Unlike `StartAcyncEmbeddedActionScript`, this cannot be forcibly stopped with `StopEmbeddedActionScript`.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, action queue option, asynchronous case)

    ## Opcode
        The object ID and then the length of the subscript in bytes

    ## Size
        The subscript size in bytes plus 2

    Args:
        target (AreaObject): The actor that this action queue should apply to
        subscript (list[UsableActionScriptCommand] | None): A list of action script commands for the actor to perform (see action_scriots/commands/commands.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        if subscript is None:
            script = []
        else:
            script = deepcopy(subscript)
        super().__init__(target, False, script, identifier)


class ActionQueueSync(UsableEventScriptCommand, ActionQueuePrototype):
    """The specified NPC performs the given set of action script commands.
    The included action script does not need to achieve completion in order for the parent event script to continue.

    Unlike `StartSyncEmbeddedActionScript`, this cannot be forcibly stopped with `StopEmbeddedActionScript`.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, action queue option, synchronous case)

    ## Opcode
        The object ID and then the length of the subscript in bytes

    ## Size
        The subscript size in bytes plus 2

    Args:
        target (AreaObject): The actor that this action queue should apply to
        subscript (list[UsableActionScriptCommand] | None): A list of action script commands for the actor to perform (see action_scriots/commands/commands.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, True, subscript, identifier)


class StartAsyncEmbeddedActionScript(
    UsableEventScriptCommand, StartEmbeddedActionScriptPrototype
):
    """The specified NPC performs the given set of action script commands.
    The included action script must complete before the parent event script is allowed to continue.

    Unlike `ActionQueueAsync`, this **can** be forcibly stopped with `StopEmbeddedActionScript`.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, action queue option, asynchronous case)

    ## Opcode
        The object ID, the prefix (0xF0 0r 0xF1), and then the length of the subscript in bytes

    ## Size
        The subscript size in bytes plus 3

    Args:
        target (AreaObject): The actor that this action queue should apply to
        subscript (list[UsableActionScriptCommand] | None): A list of action script commands for the actor to perform (see action_scriots/commands/commands.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, prefix, False, subscript, identifier)


class StartSyncEmbeddedActionScript(
    UsableEventScriptCommand, StartEmbeddedActionScriptPrototype
):
    """The specified NPC performs the given set of action script commands.
    The included action script does not need to achieve completion in order for the parent event script to continue.

    Unlike `ActionQueueSync`, this can be forcibly stopped with `StopEmbeddedActionScript`.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, action queue option, synchronous case)

    ## Opcode
        The object ID, the prefix (0xF0 0r 0xF1), and then the length of the subscript in bytes

    ## Size
        The subscript size in bytes plus 3

    Args:
        target (AreaObject): The actor that this action queue should apply to
        subscript (list[UsableActionScriptCommand] | None): A list of action script commands for the actor to perform (see action_scriots/commands/commands.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        subscript: list[UsableActionScriptCommand] | None = None,
        identifier: str | None = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, prefix, True, subscript, identifier)


class NonEmbeddedActionQueue(UsableEventScriptCommand, NonEmbeddedActionQueuePrototype):
    """A section of unheadered code to be run as an action script instead of an event script.\n
    When assembled, these queues contain no header to indicate where they begin.
    The game understands  where these scripts are intended to begin via ASM that
    exists outside of the scope of the script bank.\n
    Do not allow the non-embedded action queue's starting address to exceed where it was in the original game.
    If there were 100 bytes in the event before a non-embedded action queue begins,
    there must always be 100 bytes in the event before the non-embedded action queue begins. If your code has less than 100 bytes before the NEAQ begins, the bank rendering method will fill enough space to put the NEAQ where it belongs.

    ## Lazy Shell command
        None, this is hardcoded in the game

    ## Opcode
        None, this begins at an arbitrary address set by the game

    ## Size
        The size of the subscript in bytes. No header.

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """


class _SetActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Force a given NPC to run an action script by ID.\n
    It is recommended to use contextual action script ID constant names for this."""

    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    @property
    def sync(self) -> bool:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        """The ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        """Set the ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        assert 0 <= action_script_id < TOTAL_ACTION_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        sync: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        self.set_action_script_id(action_script_id)

    def render(self, *args) -> bytearray:
        header_byte: int = (not self.sync) + 0xF2
        return super().render(self.target, header_byte, self.action_script_id)


class SetAsyncActionScript(
    _SetActionScript,
    UsableEventScriptCommand,
):
    """Force an actor to run an action script by ID.
    The action script must complete before further commands in the event script can run.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, set action script (sync))

    ## Opcode
        The object ID followed by `0xF3`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The actor that this action script should apply to
        action_script_id (int): The ID of the action script for the target to be animated by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, action_script_id, False, identifier)


class SetSyncActionScript(_SetActionScript, UsableEventScriptCommand):
    """Force an actor to run an action script by ID.
    The action script does not need to complete before further commands in the event script can run.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, set action script (async))

    ## Opcode
        The object ID followed by `0xF2`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The actor that this action script should apply to
        action_script_id (int): The ID of the action script for the target to be animated by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, action_script_id, True, identifier)


class _SetTempActionScript(EventScriptCommand):
    """Force a given NPC to run an action script by ID, where they will resume
    their original assigned action script upon completion.\n
    It is recommended to use contextual action script ID constant names for this."""

    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    @property
    def sync(self) -> bool:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        """The ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        """Set the ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        assert 0 <= action_script_id < TOTAL_ACTION_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        sync: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        self.set_action_script_id(action_script_id)

    def render(self, *args) -> bytearray:
        header_byte: int = (not self.sync) + 0xF4
        return super().render(self.target, header_byte, self.action_script_id)


class SetTempAsyncActionScript(_SetTempActionScript, UsableEventScriptCommand):
    """The specified actor acts out an action script by ID.
    The actor will resume their original assigned action script upon completion.
    This temporary action script must complete before the parent event script is allowed to continue.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, set temp action script (async))

    ## Opcode
        The object ID followed by `0xF5`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The actor that this action script should apply to
        action_script_id (int): The ID of the action script for the target to be animated by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, action_script_id, False, identifier)


class SetTempSyncActionScript(_SetTempActionScript, UsableEventScriptCommand):
    """The specified actor acts out an action script by ID.
    The actor will resume their original assigned action script upon completion.
    The action script does not need to complete before further commands in the event script can run.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, set temp action script (sync))

    ## Opcode
        The object ID followed by `0xF4`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The actor that this action script should apply to
        action_script_id (int): The ID of the action script for the target to be animated by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(target, action_script_id, True, identifier)


class UnsyncActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Changes an async script (blocks the progression of the main thread until completion) to
    a sync script (runs simultaneously with other event script commands).

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, un-sync action script)

    ## Opcode
        The object ID followed by `0xF6`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor that this action script should apply to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xF6)


class SummonObjectToSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Summon a NPC to the given level by its NPC ID within the level.
    This will not really do anything if the NPC has not already been removed from the given level.

    ## Lazy Shell command
        `"Object {xx}'s presence in level {xx} is...` (present case only)

    ## Opcode
        `0xF2`

    ## Size
        3 bytes

    Args:
        target_npc (AreaObject): The field object to make present in the level. Use the pre-defined ones in area_objects.py.
        level_id (int): The level to make the object present in.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF2
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC to be summoned to the given level."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC to be summoned to the given level."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC is to be summoned."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC is to be summoned.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg: int = UInt16(self.level_id + (self.target_npc << 9) + (1 << 15))
        return super().render(arg)


class SummonObjectToCurrentLevel(UsableEventScriptCommand, EventScriptCommand):
    """
    The target actor will become present in the level (`visible` set to true).

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, summon to current level)

    ## Opcode
        The object ID followed by `0xF8`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to make visible
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target to become active with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the target to become active with this command."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xF8)


class SummonObjectToCurrentLevelAtMariosCoords(
    UsableEventScriptCommand, EventScriptCommand
):
    """The specified actor will become present in the level (`visible` set to true)
    and teleported to the player's current coordinates.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, summon to current level @ Mario's coords)

    ## Opcode
        The object ID followed by `0xF7`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to make visible and teleport
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target to become active with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the target to become active with this command."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xF7)


class SummonObjectAt70A8ToCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player interacted with) will be summoned to the current level.
    This has no effect if the NPC has not already been removed from the level.

    ## Lazy Shell command
        `Summon object @ $70A8 to current level`

    ## Opcode
        `0xF4`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF4


class RemoveObjectFromSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Remove a NPC from the given level by its NPC ID within the level.
    This will not really do anything if the NPC has already been removed from the given level.

    ## Lazy Shell command
        `"Object {xx}'s presence in level {xx} is...` (absent case only)

    ## Opcode
        `0xF2`

    ## Size
        3 bytes

    Args:
        target_npc (AreaObject): The field object to remove in the level. Use the pre-defined ones in area_objects.py.
        level_id (int): The level to remove the object from.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF2
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC to be removed from the given level."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC to be removed from the given level."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC is to be removed."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC is to be removed.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class RemoveObjectFromCurrentLevel(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will no longer be present in the level (`visible` set to false).

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, remove from current level)

    ## Opcode
        The object ID followed by `0xF9`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to make invisible
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC to be removed from the current level."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to be removed from the current level."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xF9)


class RemoveObjectAt70A8FromCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player interacted with) will be removed from the current level.
    This has no effect if the NPC has already been removed from the level.

    ## Lazy Shell command
        `Remove object @ $70A8 in current level`

    ## Opcode
        `0xF5`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF5


class PauseActionScript(UsableEventScriptCommand, EventScriptCommand):
    """The actor's action script will pause until a `ResumeActionScript`
    command runs for the same actor target.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, pause action script)

    ## Opcode
        The object ID followed by `0xFA`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor whose animation to pause
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target whose action script to pause with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose action script should be paused."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFA)


class ResumeActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Resumes a paused action script for the target actor.
    This probably won't do anything if there was no `PauseActionScript` before this.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, resume action script)

    ## Opcode
        The object ID followed by `0xFB`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor whose paused animation to resume
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target whose paused action script to resume with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose paused action script should be resumed."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFB)


class EnableObjectTrigger(UsableEventScriptCommand, EventScriptCommand):
    """The specified actor can now be interacted with.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, enable trigger)

    ## Opcode
        The object ID followed by `0xFC`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor whose trigger to enable
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC that should become interact-able."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC that should become interact-able."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFC)


class DisableObjectTrigger(UsableEventScriptCommand, EventScriptCommand):
    """The actor will enter a state in which it cannot be interacted with.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, disable trigger)

    ## Opcode
        The object ID followed by `0xFD`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to disable interactions for
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC that should become un-interact-able."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC that should become un-interact-able."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFD)


class EnableObjectTriggerInSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Enable the object trigger of the NPC to the given level.
    This will not really do anything if the NPC's object trigger has not already been disabled in the given level.

    ## Lazy Shell command
        `Object {xx}'s event trigger is...` (activated case only)

    ## Opcode
        `0xF3`

    ## Size
        3 bytes

    Args:
        target_npc (AreaObject): The NPC whose object trigger to enable. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room in which the NPC whose object trigger is being enabled lives
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF3
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose object trigger to enable (belonging to the specified level)."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose object trigger to enable
        (belonging to the specified level)."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC whose object trigger is being enabled lives."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC
        whose object trigger is being enabled lives.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9) + (1 << 15)
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class DisableObjectTriggerInSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Disable the object trigger of the NPC to the given level.
    This will not really do anything if the NPC's object trigger has not already been enabled in the given level.

    ## Lazy Shell command
        `Object {xx}'s event trigger is...` (deactivated case only)

    ## Opcode
        `0xF3`

    ## Size
        3 bytes

    Args:
        target_npc (AreaObject): The NPC whose object trigger to disable. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room in which the NPC whose object trigger is being disabled lives
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF3
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose object trigger to disable (belonging to the specified level)."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose object trigger to disable
        (belonging to the specified level)."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC whose object trigger is being disabled lives."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC
        whose object trigger is being disabled lives.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class EnableTriggerOfObjectAt70A8InCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player interacted with) will have its object trigger enabled.
    Because you can't interact with a disabled NPC in order to automatically write it to $70A8 in the first place, this would require manually writing a value to $70A8 in order to use this command, and thus you won't see it very often as other similar commands are more useful.
    This provides no effect if the NPC in question has not already had its object trigger disabled.

    ## Lazy Shell command
        `Enable event trigger for object @ 70A8`

    ## Opcode
        `0xF6`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF6


class DisableTriggerOfObjectAt70A8InCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player interacted with) will have its object trigger disabled.
    This provides no effect if the NPC in question has already had its object trigger disabled.

    ## Lazy Shell command
        `Disable event trigger for object @ 70A8`

    ## Opcode
        `0xF7`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF7


class StopEmbeddedActionScript(UsableEventScriptCommand, EventScriptCommand):
    """If the NPC is running an action script that was applied to it
    via an `EmbeddedActionScript` (not an `ActionQueue`), this command
    will stop it regardless of how far along in its execution it is.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, stop embedded action script)

    ## Opcode
        The object ID followed by `0xFE`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to disable an animation for
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose embedded action queue is to be stopped."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose embedded action queue is to be stopped."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFE)


class ResetCoords(UsableEventScriptCommand, EventScriptCommand):
    """The given NPC will return to the coordinates as set in the room definition.

    ## Lazy Shell command
        `Objects (allies, NPCs, screens)...`
        (any object, reset coords)

    ## Opcode
        The object ID followed by `0xFF`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The actor to reset the position for
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose coords should be reset to the original coords listed
        in the room definition."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coords should be reset to the original coords listed
        in the room definition."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, 0xFF)


class CreatePacketAtObjectCoords(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet spawning at any NPC's current coordinates.

    ## Lazy Shell command
        `Create NPC @ object {xx}'s (x,y,z)...`

    ## Opcode
        `0x3E`

    ## Size
        5 bytes

    Args:
        packet (Packet): The packet object you want to spawn. Use the packets in packets.py, or define your own as long as the properties match what's in your ROM.
        target_npc (AreaObject): The field object whose coordinates to spawn the packet at. Use the pre-defined ones in area_objects.py.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if packet spawning fails (can be any command, but is usually a `ReturnQueue` command or whatever command comes after this one).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3E
    _size: int = 5
    _packet_id: UInt8
    _target_npc: AreaObject

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    @property
    def target_npc(self) -> AreaObject:
        """The NPC at whose coordinates the packet should spawn."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC at whose coordinates the packet should spawn."""
        self._target_npc = target_npc

    def __init__(
        self,
        packet: Packet,
        target_npc: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)
        self.set_target_npc(target_npc)

    def render(self, *args) -> bytearray:
        return super().render(self.packet_id, self.target_npc, *self.destinations)


class CreatePacketAt7010(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet at pixel coordinates determined by the current values of $7010, $7012, and $7014.

    ## Lazy Shell command
        `Create NPC @ (x,y,z) of $7010-15...`

    ## Opcode
        `0x3F`

    ## Size
        4 bytes

    Args:
        packet (Packet): The packet object you want to spawn. Use the packets in packets.py, or define your own as long as the properties match what's in your ROM.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if packet spawning fails (can be any command, but is usually a `ReturnQueue` command or whatever command comes after this one).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3F
    _size: int = 4
    _packet_id: UInt8

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    def __init__(
        self,
        packet: Packet,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)

    def render(self, *args) -> bytearray:
        return super().render(self.packet_id, *self.destinations)


class CreatePacketAt7010WithEvent(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet at pixel coordinates determined by the current values of $7010, $7012, and $7014. When touched, the packet will run the event specified by the given ID.\n

    ## Lazy Shell command
        `Create NPC + event {xx} @ (x,y,z) of $7010-15...`

    ## Opcode
        `0xFD 0x3E`

    ## Size
        7 bytes

    Args:
        packet (Packet): The packet object you want to spawn. Use the packets in packets.py, or define your own as long as the properties match what's in your ROM.
        event_id (int): The ID of the event that should run when the spawned packet is touched.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if packet spawning fails (can be any command, but is usually a `ReturnQueue` command or whatever command comes after this one).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x3E])
    _size: int = 7
    _packet_id: UInt8
    _event_id: UInt16

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run when the packet is touched."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """Set the ID of the event to run when the packet is touched.\n
        It is recommended to use contextual event ID constants for this."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(
        self,
        packet: Packet,
        event_id: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)
        self.set_event_id(event_id)

    def render(self, *args) -> bytearray:
        return super().render(self.packet_id, self.event_id, *self.destinations)


class FreezeAllNPCsUntilReturn(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """All NPCs in the room will have their current actions frozen until the next
    `Return` command is run.

    ## Lazy Shell command
        `Freeze all NPCs until return`

    ## Opcode
        `0x30`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x30


class UnfreezeAllNPCs(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Cancels any commands that have frozen NPCs in the room.

    ## Lazy Shell command
        `Unfreeze all NPCs`

    ## Opcode
        `0x31`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x31


class FreezeCamera(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The camera will no longer adjust to the player's position.

    ## Lazy Shell command
        `Freeze screen`

    ## Opcode
        `0x31`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x31])


class UnfreezeCamera(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The camera will resume following the player's position.

    ## Lazy Shell command
        `Unfreeze screen`

    ## Opcode
        `0x30`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x30])


class JmpIfMarioOnObject(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the player is currently on top of the specific NPC,
    go to the command matching the destination label.

        ## Lazy Shell command
            `If Mario on top of object {xx}...`

        ## Opcode
            `0x39`

        ## Size
            4 bytes

        Args:
            target (AreaObject): The NPC to check if a player is on
            destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if Mario is on the NPC.
            identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x39
    _size: int = 4
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose positioning controls whether the goto executes or not."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose positioning controls whether the goto executes or not."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self._target, *self.destinations)


class JmpIfMarioOnAnObjectOrNot(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Accepts two identifiers for commands to go to:\n
    One in the case where the player is on top of any object, and
    one in the case where the player is not on top of any object.

    ## Lazy Shell command
        `If Mario is on top of an object...`

    ## Opcode
        `0x42`

    ## Size
        5 bytes

    Args:
        destinations (list[str]): This should be a list of exactly two `str`s. The first one should be the label of a command to jump to if the player **is** on another NPC and the second should be the label of the command to jump to if the player **is not** on an NPC.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x42
    _size: int = 5

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfObjectInAir(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is currently airborne, jump to the command matching the label.

    ## Lazy Shell command
        `If object {xx} is in the air...`

    ## Opcode
        `0xFD 0x3D`

    ## Size
        5 bytes

    Args:
        target_npc (AreaObject): The NPC to check. Use the pre-defined ones in area_objects.py.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC is airborne.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x3D])
    _size: int = 5
    _target_npc: AreaObject

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose airborne status to check."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose airborne status to check."""
        self._target_npc = target_npc

    def __init__(
        self,
        target_npc: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)

    def render(self, *args) -> bytearray:
        return super().render(self._target_npc, *self.destinations)


class JmpIfObjectInSpecificLevel(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is present in the specified level, jump to the command matching the specified label.

    ## Lazy Shell command
        `If object {xx} is present in level {xx}...` (present case only)

    ## Opcode
        `0xF8`

    ## Size
        5 bytes

    Args:
        target_npc (AreaObject): The NPC to check for. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room to check for the NPC
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC is present in the level.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF8
    _size: int = 5
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose presence to check in the given room."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose presence to check in the given room."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The room to check for the NPC's presence in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check for the NPC's presence in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target_npc: AreaObject,
        level_id: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg = UInt16(0x8000 + (self.target_npc << 9) + self.level_id)
        return super().render(arg, *self.destinations)


class JmpIfObjectInCurrentLevel(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is present in the current level, jump to the code section beginning with the specified identifier.

    ## Lazy Shell command
        `If object {xx} present in current level...`

    ## Opcode
        `0x32`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The NPC to check for. Use the pre-defined ones in area_objects.py.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC is present in the level.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x32
    _size: int = 4
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose presence to check in the current room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose presence to check in the current room."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectNotInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the specified NPC is not present in the specified level, jump to the command matching the specified label.

    ## Lazy Shell command
        `If object {xx} is present in level {xx}...` (absent case only)

    ## Opcode
        `0xF8`

    ## Size
        5 bytes

    Args:
        target_npc (AreaObject): The NPC to check for. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room to check for the NPC
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC is absent from the level.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xF8
    _size: int = 5
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose presence to check in the given room."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose presence to check in the given room."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The room to check for the NPC's presence in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check for the NPC's presence in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target_npc: AreaObject,
        level_id: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg = UInt16((self.target_npc << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerEnabledInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the NPC is interactable in the specified level, jump to the command matching the specified label.

    ## Lazy Shell command
        `If object {xx}'s event trigger in level {xx} is...` (enabled case only)

    ## Opcode
        `0xFD 0xF0`

    ## Size
        6 bytes

    Args:
        target_npc (AreaObject): The NPC to check. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room to check for the NPC's object trigger
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC's trigger is enabled.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _target: AreaObject
    _level_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC whose interactability state to check in the given room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose interactability stage to check in the given room."""
        self._target = target

    @property
    def level_id(self) -> UInt16:
        """The room to check the NPC's interactability state in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check the NPC's interactability state in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target: AreaObject,
        level_id: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg: int = UInt16(self.level_id + (self.target << 9) + (1 << 15))
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerDisabledInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the NPC is disabled/non-interactable in the specified level, jump to the command matching the specified label.

    ## Lazy Shell command
        `If object {xx}'s event trigger in level {xx} is...` (disabled case only)

    ## Opcode
        `0xFD 0xF0`

    ## Size
        6 bytes

    Args:
        target_npc (AreaObject): The NPC to check. Use the pre-defined ones in area_objects.py.
        level_id (int): The ID of the room to check for the NPC's object trigger
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC's trigger is disabled.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _target: AreaObject
    _level_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC whose interactability state to check in the given room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose interactability stage to check in the given room."""
        self._target = target

    @property
    def level_id(self) -> UInt16:
        """The room to check the NPC's interactability state in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check the NPC's interactability state in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target: AreaObject,
        level_id: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)
        self.set_level_id(level_id)

    def render(self, *args) -> bytearray:
        arg = UInt16((self.target << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectIsUnderwater(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is underwater in the current level,
    jump to the code section beginning with the specified identifier.

        ## Lazy Shell command
            `If object {xx} is underwater...`

        ## Opcode
            `0xFD 0x34`

        ## Size
            5 bytes

        Args:
            target (AreaObject): The NPC to check. Use the pre-defined ones in area_objects.py.
            destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC's trigger is disabled.
            identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x34])
    _size: int = 5
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose water submersion status to check."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose water submersion status to check."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectActionScriptIsRunning(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the NPC's action script is not paused or stopped,
    jump to the command with the specified label.

        ## Lazy Shell command
            `If object {xx}'s action script running...`

        ## Opcode
            `0xFD 0x33`

        ## Size
            5 bytes

        Args:
            target (AreaObject): The NPC to check. Use the pre-defined ones in area_objects.py.
            destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the NPC's trigger is disabled.
            identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x33])
    _size: int = 5
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose action script status to check."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose action script status to check."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectsAreLessThanXYStepsApart(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the two given NPCs are less than the given number of steps
    apart (ignoring Z axis), go to the section of code indicated by the identifier.

    ## Lazy Shell command
        `If object A & B < (x,y) steps and infinite Z coords apart...`

    ## Opcode
        `0x3A`

    ## Size
        7 bytes

    Args:
        object_1 (AreaObject): The first NPC to compare. Use the pre-defined ones in area_objects.py.
        object_2 (AreaObject): The second NPC to compare. Use the pre-defined ones in area_objects.py.
        x (int): The x component of the step threshold that the NPCs can be separated by.
        y (int): The y component of the step threshold that the NPCs can be separated by.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the two NPCs are separated by less than both the x and y distance.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3A
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        """The first NPC in the range check."""
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        """Designate the first object in the range check."""
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        """The second NPC in the range check."""
        return self._object_2

    def set_object_2(self, object_2: AreaObject) -> None:
        """Designate the second object in the range check."""
        self._object_2 = object_2

    @property
    def x(self) -> UInt8:
        """The max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        return self._x

    def set_x(self, x: int) -> None:
        """Designate the max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        return self._y

    def set_y(self, y: int) -> None:
        """Designate the max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)

    def render(self, *args) -> bytearray:
        return super().render(
            self.object_1, self.object_2, self.x, self.y, *self.destinations
        )


class JmpIfObjectsAreLessThanXYStepsApartSameZCoord(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the two given NPCs are less than the given number of steps apart (when on the same Z coord), go to the section of code indicated by the identifier.

    ## Lazy Shell command
        `If object A & B < (x,y,z) steps apart...`

    ## Opcode
        `0x3B`

    ## Size
        7 bytes

    Args:
        object_1 (AreaObject): The first NPC to compare. Use the pre-defined ones in area_objects.py.
        object_2 (AreaObject): The second NPC to compare. Use the pre-defined ones in area_objects.py.
        x (int): The x component of the step threshold that the NPCs can be separated by.
        y (int): The y component of the step threshold that the NPCs can be separated by.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the two NPCs are separated by less than both the x and y distance on the same z coord.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3B
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        """The first NPC in the range check."""
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        """Designate the first object in the range check."""
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        """The second NPC in the range check."""
        return self._object_2

    def set_object_2(self, object_2: AreaObject) -> None:
        """Designate the second object in the range check."""
        self._object_2 = object_2

    @property
    def x(self) -> UInt8:
        """The max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        return self._x

    def set_x(self, x: int) -> None:
        """Designate the max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        return self._y

    def set_y(self, y: int) -> None:
        """Designate the max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)

    def render(self, *args) -> bytearray:
        return super().render(
            self.object_1, self.object_2, self.x, self.y, *self.destinations
        )


class ReactivateObject70A8TriggerIfMarioOnTopOfIt(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will re-enter a state of interactability, but only if
    the player is currently on top of it.

        ## Lazy Shell command
            `Reactivate trigger if Mario on top of object`
            (unselectable)

        ## Opcode
            `0x5D`

        ## Size
            1 byte

        Args:
            identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x5D


class Set7000ToObjectCoord(UsableEventScriptCommand, EventScriptCommand):
    """Sets $7000 to the pixel or isometric coordinate value of one dimension from any NPC's current coordinates.

    ## Lazy Shell command
        `Memory $7000 = object's X coord...`
        `Memory $7000 = object's Y coord...`
        `Memory $7000 = object's Z coord...`
        `Memory $7000 = F coord of object...`

    ## Opcode
        `0xC4`
        `0xC5`
        `0xC6`
        `0xC9`

    ## Size
        2 bytes

    Args:
        target_npc (AreaObject): The field object whose coords to read. Use the pre-defined ones in area_objects.py.
        coord (Coord): Choose one of `COORD_X`, `COORD_Y`, `COORD_Z`, or `COORD_F`
        isometric (bool): If true, stores the isometric coord value (i.e. tile coord) instead of the pixel value. Exclusive with the `pixel` arg.
        pixel (bool): If true, stores the pixel coord value instead of the tile/isometric coord value. Exclusive with the `isometric` arg.
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _size: int = 2
    _target_npc: AreaObject
    _coord: Coord
    _is_isometric_not_pixel: bool = False
    _bit_7: bool = False

    @property
    def target_npc(self) -> AreaObject:
        """The NPC from whom this value comes from."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Choose the NPC from whom this value comes from."""
        self._target_npc = target_npc

    @property
    def coord(self) -> Coord:
        """The specific coordinate whose value to store to $7000."""
        return self._coord

    def set_coord(self, coord: Coord) -> None:
        """Set the specific coordinate whose value to store to $7000."""
        self._coord = coord

    @property
    def is_isometric_not_pixel(self) -> bool:
        """If true, stores the isometric coord value (i.e. tile coord)
        instead of the pixel value."""
        return self._is_isometric_not_pixel

    def set_is_isometric_not_pixel(self, is_isometric_not_pixel: bool) -> None:
        """If true, stores the isometric coord value (i.e. tile coord)
        instead of the pixel value."""
        self._is_isometric_not_pixel = is_isometric_not_pixel

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        target_npc: AreaObject,
        coord: Coord,
        isometric: bool = False,
        pixel: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        if coord != COORD_F:
            assert isometric ^ pixel
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_coord(coord)
        self.set_is_isometric_not_pixel(isometric)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        opcode = UInt8(0xC4 + self.coord)
        arg = UInt8(
            (self.bit_7 << 7) + (self.is_isometric_not_pixel << 6) + self.target_npc
        )
        return super().render(opcode, arg)


class Set70107015ToObjectXYZ(UsableEventScriptCommand, EventScriptCommand):
    """Copy the X, Y, and Z pixel coordinates of the NPC to $7010, $7012, and $7014.

    ## Lazy Shell command
        `Memory $7010-15 = (x,y,z) of object...`

    ## Opcode
        `0xC7`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The field object whose coords to read. Use the pre-defined ones in area_objects.py.
        bit_6 (bool): (unknown)
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xC7
    _size: int = 2
    _target: AreaObject
    _bit_6: bool
    _bit_7: bool

    @property
    def target(self) -> AreaObject:
        """The NPC whose coordinates to store."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coordinates to store."""
        self._target = target

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        target: AreaObject,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        return super().render(self.target + (self.bit_6 << 6) + (self.bit_7 << 7))


class Set7016701BToObjectXYZ(UsableEventScriptCommand, EventScriptCommand):
    """Copy the X, Y, and Z pixel coordinates of the NPC to $7016, $7018, and $701A.

    ## Lazy Shell command
        `Memory $7016-1B = (x,y,z) of object...`

    ## Opcode
        `0xC8`

    ## Size
        2 bytes

    Args:
        target (AreaObject): The field object whose coords to read. Use the pre-defined ones in area_objects.py.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xC8
    _size: int = 2
    _target: AreaObject
    _bit_6: bool = False
    _bit_7: bool = False

    @property
    def target(self) -> AreaObject:
        """The NPC whose coordinates to store."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coordinates to store."""
        self._target = target

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        target: AreaObject,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        return super().render(self.target + (self.bit_6 << 6) + (self.bit_7 << 7))


class SetObjectMemoryToVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """(unknown)

    ## Lazy Shell command
        `Object memory = memory $7xxx...`

    ## Opcode
        `0xD6`

    ## Size
        2 bytes

    Args:
        address (ShortVar): Any short var to read from
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD6
    _size: int = 2


# controls


class EnableControls(UsableEventScriptCommand, EventScriptCommand):
    """Buttons included in this command will be enabled, and buttons excluded will be disabled.

    Dpad Left = 0
    Dpad Right = 1
    Dpad Down = 2
    Dpad Up = 3
    X = 4
    A = 5
    Y = 6
    B = 7

    ## Lazy Shell command
        `Enable buttons {xx} only...`

    ## Opcode
        `0x35`

    ## Size
        2 bytes

    Args:
        enabled_buttons (list[ControllerInput] | set[ControllerInput]): All of the buttons that should be enabled to the exclusion of all others
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x35
    _size: int = 2
    _enabled_buttons: set[ControllerInput]

    @property
    def enabled_buttons(self) -> set[ControllerInput]:
        """The complete list of buttons that the player can use as of this command."""
        return self._enabled_buttons

    def set_enabled_buttons(
        self, enabled_buttons: list[ControllerInput] | set[ControllerInput]
    ) -> None:
        """Overwrite the complete list of buttons that the player can use as of this command."""
        self._enabled_buttons = set(enabled_buttons)

    def __init__(
        self,
        enabled_buttons: list[ControllerInput] | set[ControllerInput],
        identifier: str | None = None,
    ):
        super().__init__(identifier)
        self.set_enabled_buttons(enabled_buttons)

    def render(self, *args) -> bytearray:
        buttons_as_ints: list[int] = cast(
            list[int], [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class EnableControlsUntilReturn(UsableEventScriptCommand, EventScriptCommand):
    """Buttons included in this command will be enabled, and buttons excluded will be disabled.\n
    When the next `Return` command is run, all controls will be re-enabled.

    Dpad Left = 0
    Dpad Right = 1
    Dpad Down = 2
    Dpad Up = 3
    X = 4
    A = 5
    Y = 6
    B = 7

    ## Lazy Shell command
        `Enable buttons {xx} only, reset @ return...`

    ## Opcode
        `0x34`

    ## Size
        2 bytes

    Args:
        enabled_buttons (list[ControllerInput] | set[ControllerInput]): All of the buttons that should be enabled to the exclusion of all others
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x34
    _size: int = 2
    _enabled_buttons: set[ControllerInput]

    @property
    def enabled_buttons(self) -> set[ControllerInput]:
        """The complete list of buttons that the player can use as of this command."""
        return self._enabled_buttons

    def set_enabled_buttons(
        self, enabled_buttons: set[ControllerInput] | list[ControllerInput]
    ) -> None:
        """Overwrite the complete list of buttons that the player can use as of this command."""
        self._enabled_buttons = set(enabled_buttons)

    def __init__(
        self,
        enabled_buttons: list[ControllerInput] | None = None,
        identifier: str | None = None,
    ):
        super().__init__(identifier)
        if enabled_buttons is None:
            enabled_buttons = []
        self.set_enabled_buttons(enabled_buttons)

    def render(self, *args) -> bytearray:
        buttons_as_ints: list[int] = cast(
            list[int], [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class Set7000ToPressedButton(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the bits of $7000 to correspond to all currently pressed buttons.
    Dpad Left = 0
    Dpad Right = 1
    Dpad Down = 2
    Dpad Up = 3
    X = 4
    A = 5
    Y = 6
    B = 7

    ## Lazy Shell command
        `Memory $7000 = pressed button`

    ## Opcode
        `0xCA`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCA


class Set7000ToTappedButton(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the bits of $7000 to correspond to an individual tapped button.
    Dpad Left = 0
    Dpad Right = 1
    Dpad Down = 2
    Dpad Up = 3
    X = 4
    A = 5
    Y = 6
    B = 7

    ## Lazy Shell command
        `Memory $7000 = tapped button`

    ## Opcode
        `0xCB`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCB


# inventory / party


class AddCoins(UsableEventScriptCommand, EventScriptCommand):
    """Add this many coins to the player's coin count.

    ## Lazy Shell command
        `Coins += ...`
        `Coins += memory $7000`

    ## Opcode
        `0x52`
        `0xFD 0x52`

    ## Size
        2 bytes

    Args:
        amount (int | ShortVar): The number of coins to add (8 bit int), or variable $7000 (cannot be any other var).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _amount: ShortVar | UInt8

    @property
    def amount(self) -> ShortVar | UInt8:
        """The number of coins to grant."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the number of coins to grant."""
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = ShortVar(amount)

    def __init__(self, amount: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self, *args) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray([0xFD, 0x52]))
        return super().render(0x52, self.amount)


class Dec7000FromCoins(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's coin count by the amount stored to $7000.

    ## Lazy Shell command
        `Coins -= memory $7000`

    ## Opcode
        `0xFD 0x53`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x53])


class AddFrogCoins(UsableEventScriptCommand, EventScriptCommand):
    """Add this many coins to the player's frog coin count.

    ## Lazy Shell command
        `Frog coins += ...`
        `Frog coins += memory $7000`

    ## Opcode
        `0x53`
        `0xFD 0x54`

    ## Size
        2 bytes

    Args:
        amount (int | ShortVar): The number of frog coins to add (8 bit int), or variable $7000 (cannot be any other var).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _amount: ShortVar | UInt8

    @property
    def amount(self) -> ShortVar | UInt8:
        """The number of Frog Coins to grant."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the number of Frog Coins to grant."""
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = ShortVar(amount)

    def __init__(self, amount: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self, *args) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray([0xFD, 0x54]))
        return super().render(0x53, self.amount)


class Dec7000FromFrogCoins(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's frog coin count by the amount stored to $7000.

    ## Lazy Shell command
        `Frog coins -= memory $7000`

    ## Opcode
        `0xFD 0x55`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x55])


class Add7000ToCurrentFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Add the amount stored to $7000 to the player's current FP fill.

    ## Lazy Shell command
        `Current FP += memory $7000`

    ## Opcode
        `0xFD 0x56`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x56])


class Dec7000FromCurrentFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's current FP fill by the amount stored to $7000.

    ## Lazy Shell command
        `TFP -= memory $7000`

    ## Opcode
        `0x57`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x57


class Add7000ToMaxFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Add the amount stored to $7000 to the player's current max FP threshold.

    ## Lazy Shell command
        `Maximum FP += memory $7000`

    ## Opcode
        `0xFD 0x57`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x57])


class Dec7000FromCurrentHP(UsableEventScriptCommand, EventScriptCommand):
    """Decrease the given character's current HP fill by the amount stored to $7000.

    ## Lazy Shell command
        `Character {xx}'s HP -= memory $7000`

    ## Opcode
        `0x56`

    ## Size
        2 bytes

    Args:
        character (PartyCharacter): The character who will be damaged
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x56
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The playable character whose HP to decrease."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Set the playable character whose HP to decrease."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self, *args) -> bytearray:
        return super().render(self.character)


class EquipItemToCharacter(UsableEventScriptCommand, EventScriptCommand):
    """Arbitrarily equip an item to a specified character. The item does not need to exist in the player's inventory.

    ## Lazy Shell command
        `Equip item {xx} to character {xx}...`

    ## Opcode
        `0x54`

    ## Size
        3 bytes

    Args:
        item (type[Equipment]): The item to equip (use an item class name from datatypes/items/implementations.py)
        character (PartyCharacter): The character to equip the item to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x54
    _size: int = 3
    _character: PartyCharacter
    _item: type[Equipment]

    @property
    def character(self) -> PartyCharacter:
        """The playable character to equip the item to."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Designate the playable character to equip the item to."""
        self._character = character

    @property
    def item(self) -> type[Equipment]:
        """The class of item to equip to the character."""
        return self._item

    def set_item(self, item: type[Equipment]) -> None:
        """Set the class of item to equip to the character."""
        self._item = item

    def __init__(
        self,
        item: type[Equipment],
        character: PartyCharacter,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)
        self.set_item(item)

    def render(self, *args) -> bytearray:
        return super().render(self.character, self.item().item_id)


class IncEXPByPacket(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The amount of EXP belonging to the packet index designated by `SetEXPPacketTo7000` will be added to the EXP of all recruited characters.

    ## Lazy Shell command
        `Experience += experience packet`

    ## Opcode
        `0xFD 0x4B`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4B])


class CharacterJoinsParty(UsableEventScriptCommand, EventScriptCommand):
    """The specified character is recruited.

    ## Lazy Shell command
        `Add or remove character {xx} in party...`
        (add case only)

    ## Opcode
        `0x36`

    ## Size
        2 bytes

    Args:
        character (PartyCharacter): The character who joins the party
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x36
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The character being recruited."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Indicate the character being recruited."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self, *args) -> bytearray:
        return super().render(self.character + (1 << 7))


class CharacterLeavesParty(UsableEventScriptCommand, EventScriptCommand):
    """The specified character is dismissed from the party.

    ## Lazy Shell command
        `Add or remove character {xx} in party...`
        (remove case only)

    ## Opcode
        `0x36`

    ## Size
        2 bytes

    Args:
        character (PartyCharacter): The character who leaves the party
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x36
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The character being dismissed."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Indicate the character being dismissed."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self, *args) -> bytearray:
        return super().render(self.character & 0x7F)


class LearnSpell(UsableEventScriptCommand, EventScriptCommand):
    """**DO NOT ATTEMPT TO USE THIS UNLESS YOU ARE DEVELOPING FOR SMRPG RANDOMIZER! It is a custom command that does not exist in the original game.**

    ## Lazy Shell command
        `Memory $7000 = tapped button`

    ## Opcode
        `0xCE`

    ## Size
        1 byte

    Args:
        character (PartyCharacter): The character who should learn the spell
        spell (Type[CharacterSpell]): The character spell class to learn.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _character: PartyCharacter
    _spell: type[CharacterSpell]
    _opcode = 0xCE

    @property
    def character(self) -> PartyCharacter:
        """The character being dismissed."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Indicate the character being dismissed."""
        self._character = character

    @property
    def spell(self) -> type[CharacterSpell]:
        """The character spell being learned."""
        return self._spell

    def set_spell(self, spell: type[CharacterSpell]) -> None:
        """Set the character spell being learned."""
        self._spell = spell

    def __init__(
        self,
        character: PartyCharacter,
        spell: type[CharacterSpell],
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        assert character <= 4
        self.set_character(character)
        assert spell().index <= 0x1A
        self.set_spell(spell)

    def render(self, *args) -> bytearray:
        return super().render(self.spell().index | (self.character << 5))


class Store70A7ToEquipsInventory(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The item whose ID matches the current value of $70A7 is added to the equips inventory pocket.

    ## Lazy Shell command
        `Store memory $70A7 to equipment inventory`

    ## Opcode
        `0xFD 0x51`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x51])


class AddToInventory(UsableEventScriptCommand, EventScriptCommand):
    """The item matching the given ID, or the ID stored at $70A7, will be added to the appropriate inventory pocket.

    ## Lazy Shell command
        `Store 1 of item {xx} to inventory...`
        `Store memory $70A7 to item inventory`

    ## Opcode
        `0x50`
        `0xFD 0x50`

    ## Size
        2 bytes

    Args:
        item (type[Item] | ByteVar): Either the item to equip (use an item class name from datatypes/items/implementations.py), OR the `ByteVar(0x70A7)` ByteVar to store whatever item ID is in $70A7.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _item: type[Item] | ByteVar

    @property
    def item(self) -> type[Item] | ByteVar:
        """The item (or variable) being stored to inventory."""
        return self._item

    def set_item(self, item: type[Item] | ByteVar) -> None:
        """Acceptable values: an item class, or ByteVar(0x70A7) variable."""
        if isinstance(item, ByteVar):
            assert item == ByteVar(0x70A7)
            self._item = ByteVar(item)
        else:
            assert issubclass(item, Item)
            self._item = item

    def __init__(
        self, item: type[Item] | ByteVar, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self, *args) -> bytearray:
        if isinstance(self.item, ByteVar):
            return super().render(bytearray([0xFD, 0x50]))
        item = self.item
        return super().render(0x50, item().item_id)


class RemoveOneOfItemFromInventory(UsableEventScriptCommand, EventScriptCommand):
    """One item matching the given ID will be removed from inventory.

    ## Lazy Shell command
        `Remove 1 of item {xx} from inventory...`

    ## Opcode
        `0x51`

    ## Size
        2 bytes

    Args:
        item (type[Item]): The item to equip (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x51
    _size: int = 2
    _item: type[Item]

    @property
    def item(self) -> type[Item]:
        """The item to remove one of from inventory."""
        return self._item

    def set_item(self, item: type[Item]) -> None:
        """Set the item to remove one of from inventory."""
        self._item = item

    def __init__(self, item: type[Item], identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self, *args) -> bytearray:
        return super().render(self.item().item_id)


class RestoreAllFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's FP will be filled to its current maximum.

    ## Lazy Shell command
        `Restore all FP`

    ## Opcode
        `0xFD 0x5C`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x5C])


class RestoreAllHP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """All recruited characters' HP will be filled to their current maximum.

    ## Lazy Shell command
        `Restore all HP`

    ## Opcode
        `0xFD 0x5B`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x5B])


class SetEXPPacketTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the active EXP packet to the ID corresponding to the current value of $7000.
    This will be used by `IncEXPByPacket`.

    ## Lazy Shell command
        `Experience packet = memory $7000`

    ## Opcode
        `0xFD 0x64`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x64])


class Set7000ToIDOfMemberInSlot(UsableEventScriptCommand, EventScriptCommand):
    """The value of $7000 will be set to the character ID who currently occupies the given slot by party index (0 to 4).

    ## Lazy Shell command
        `Memory $7000 = character in {xx} slot...`

    ## Opcode
        `0x38`

    ## Size
        2 bytes

    Args:
        slot (int): The slot to look at (0 to 4)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x38
    _size: int = 2
    _slot: UInt8

    @property
    def slot(self) -> UInt8:
        """The slot of the character whose ID to store to $7000."""
        return self._slot

    def set_slot(self, slot: int) -> None:
        """The slot of the character whose ID to store to $7000."""
        assert 0 <= slot <= 4
        self._slot = UInt8(slot)

    def __init__(self, slot: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_slot(slot)

    def render(self, *args) -> bytearray:
        return super().render(0x08 + self.slot)


class Set7000ToPartySize(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Store the total party size to $7000.

    ## Lazy Shell command
        `Memory $7000 = party capacity`

    ## Opcode
        `0x37`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x37


class StoreItemAt70A7QuantityTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the item whose ID matches the current value of $70A7, check how many of that item are currently in the player inventory, and store that amount to $7000.

    ## Lazy Shell command
        `Memory $7000 = quantity of item @ memory $70A7`

    ## Opcode
        `0xFD 0x5E`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x5E])


class StoreCharacterEquipmentTo7000(UsableEventScriptCommand, EventScriptCommand):
    """For the given equipment type on the given character, store the ID of the currently equipped item to $7000

    ## Lazy Shell command
        `Memory $7000 = equipment {xx} of {xx} character...`

    ## Opcode
        `0xFD 0x5D`

    ## Size
        4 bytes

    Args:
        character (PartyCharacter): The character whose equipment to look at.
        equip_slot (type[Equipment]): The equip slot to read (`WeaponItem`, `ArmorItem`, or `AccessoryItem`)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x5D])
    _size: int = 4
    _character: PartyCharacter
    _equip_slot: type[Equipment]

    @property
    def character(self) -> PartyCharacter:
        """The character whose equipment to store."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Designate the character whose equipment to store."""
        self._character = character

    @property
    def equip_slot(self) -> type[Equipment]:
        """The equipment type to check."""
        return self._equip_slot

    def set_equip_slot(self, equip_slot: type[Equipment]) -> None:
        """Designate the equipment type to check."""
        assert 0 <= equip_slot().item_id <= 2
        self._equip_slot = equip_slot

    def __init__(
        self,
        character: PartyCharacter,
        equip_slot: type[Equipment],
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)
        self.set_equip_slot(equip_slot)

    def render(self, *args) -> bytearray:
        return super().render(self.character, self.equip_slot().item_id)


class StoreCurrentFPTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current FP fill amount is stored to $7000.

    ## Lazy Shell command
        `Memory $7000 = current FP`

    ## Opcode
        `0x58`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x58


class StoreEmptyItemInventorySlotCountTo7000(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The number of available spaces in the player's main inventory pocket is stored to $7000.

    ## Lazy Shell command
        `Memory $7000 = # of open item slots`

    ## Opcode
        `0x55`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x55


class StoreCoinCountTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's current coin count is stored to $7000.

    ## Lazy Shell command
        `Memory $7000 = coins`

    ## Opcode
        `0xFD 0x59`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x59])


class StoreItemAmountTo7000(UsableEventScriptCommand, EventScriptCommand):
    """Check how many of the given item are currently in the player's inventory, and store that amount to $7000.

    ## Lazy Shell command
        `Memory $7000 = quantity of item {xx} in inventory...`

    ## Opcode
        `0xFD 0x58`

    ## Size
        3 bytes

    Args:
        item (type[Item]): The item to count (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x58])
    _size: int = 3
    _item: type[Item]

    @property
    def item(self) -> type[Item]:
        """The item whose inventory quantity to check."""
        return self._item

    def set_item(self, item: type[Item]) -> None:
        """Set the item whose inventory quantity to check."""
        self._item = item

    def __init__(self, item: type[Item], identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self, *args) -> bytearray:
        return super().render(self.item().item_id)


class StoreFrogCoinCountTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's current Frog Coin count is stored to $7000.

    ## Lazy Shell command
        `Memory $7000 = frog coins`

    ## Opcode
        `0xFD 0x5A`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x5A])


# yourself


class JmpIfMarioInAir(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the player is currently airborne, go to the section of code beginning with the specified identifier.

    ## Lazy Shell command
        `If Mario is in the air...`

    ## Opcode
        `0x3D`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to if the player is airborne.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3D
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class MarioGlows(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player will glow as they normally do during an EXP star animation.

    ## Lazy Shell command
        `Mario glowing begins`

    ## Opcode
        `0xFD 0xF9`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xF9])


class MarioStopsGlowing(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The effect of a prior `MarioGlows` command is canceled.

    ## Lazy Shell command
        `Mario glowing stops`

    ## Opcode
        `0xFD 0xFA`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xFA])


# palettes & screen effects


class PaletteSet(UsableEventScriptCommand, EventScriptCommand):
    """(The inner workings of this command are unknown.)

    ## Lazy Shell command
        `Palette set = ...`

    ## Opcode
        `0x8A`

    ## Size
        3 bytes

    Args:
        palette_set (int): The palette set to apply to the NPCs in the current level (8 bit)
        row (int): The row offset relative to the palette (8 bit)
        bit_0 (bool): (unknown)
        bit_1 (bool): (unknown)
        bit_2 (bool): (unknown)
        bit_3 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x8A
    _size: int = 3
    _palette_set: UInt8
    _row: UInt8
    _bit_0: bool
    _bit_1: bool
    _bit_2: bool
    _bit_3: bool

    @property
    def palette_set(self) -> UInt8:
        """The palette set to apply to the NPCs in the current level."""
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        """Designate the palette set to apply to the NPCs in the current level."""
        self._palette_set = UInt8(palette_set)

    @property
    def row(self) -> UInt8:
        """The row offset relative to the palette."""
        return self._row

    def set_row(self, row: int) -> None:
        """Designate the row offset relative to palette for this command."""
        assert 1 <= row <= 16
        self._row = UInt8(row)

    @property
    def bit_0(self) -> bool:
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def bit_1(self) -> bool:
        """(unknown)"""
        return self._bit_1

    def set_bit_1(self, bit_1: bool) -> None:
        """(unknown)"""
        self._bit_1 = bit_1

    @property
    def bit_2(self) -> bool:
        """(unknown)"""
        return self._bit_2

    def set_bit_2(self, bit_2: bool) -> None:
        """(unknown)"""
        self._bit_2 = bit_2

    @property
    def bit_3(self) -> bool:
        """(unknown)"""
        return self._bit_3

    def set_bit_3(self, bit_3: bool) -> None:
        """(unknown)"""
        self._bit_3 = bit_3

    def __init__(
        self,
        palette_set: int,
        row: int,
        bit_0: bool = False,
        bit_1: bool = False,
        bit_2: bool = False,
        bit_3: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_palette_set(palette_set)
        self.set_row(row)
        self.set_bit_0(bit_0)
        self.set_bit_1(bit_1)
        self.set_bit_2(bit_2)
        self.set_bit_3(bit_3)

    def render(self, *args) -> bytearray:
        flags: int = bools_to_int(self.bit_0, self.bit_1, self.bit_2, self.bit_3)
        arg_1 = UInt8(flags + ((self.row - 1) << 4))
        return super().render(arg_1, self.palette_set)


class PaletteSetMorphs(UsableEventScriptCommand, EventScriptCommand):
    """(The inner workings of this command are unknown.)

    ## Lazy Shell command
        `Palette set morphs to {xx} set...`

    ## Opcode
        `0x89`

    ## Size
        4 bytes

    Args:
        palette_type (PaletteType): The effect to use in applying this palette
        palette_set (int): The palette set to apply to the NPCs in the current level
        duration (int): The number of frames over which this palette morph should occur
        row (int): The row offset relative to the palette
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x89
    _size: int = 4
    _palette_type: PaletteType
    _palette_set: UInt8
    _duration: UInt8
    _row: UInt8

    @property
    def palette_type(self) -> PaletteType:
        """The effect to use in applying this palette."""
        return self._palette_type

    def set_palette_type(self, palette_type: PaletteType) -> None:
        """Set the effect to use in applying this palette."""
        self._palette_type = palette_type

    @property
    def palette_set(self) -> UInt8:
        """The palette set to apply to the NPCs in the current level."""
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        """Designate the palette set to apply to the NPCs in the current level."""
        self._palette_set = UInt8(palette_set)

    @property
    def duration(self) -> UInt8:
        """The number of frames over which this palette morph should occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the number of frames (0-15) over which this palette morph should occur."""
        assert 0 <= duration <= 15
        self._duration = UInt8(duration)

    @property
    def row(self) -> UInt8:
        """The row offset relative to the palette."""
        return self._row

    def set_row(self, row: int) -> None:
        """Designate the row offset relative to palette for this command."""
        assert 1 <= row <= 16
        self._row = UInt8(row)

    def __init__(
        self,
        palette_type: PaletteType,
        palette_set: int,
        duration: int,
        row: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_palette_type(palette_type)
        self.set_palette_set(palette_set)
        self.set_duration(duration)
        self.set_row(row)

    def render(self, *args) -> bytearray:
        arg_1 = UInt8(self.duration + (self.palette_type << 4))
        return super().render(arg_1, self.row, self.palette_set)


class PauseScriptUntilEffectDone(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The script will not continue until an active graphical effect has finished.

    ## Lazy Shell command
        `Pause script until screen effect done`

    ## Opcode
        `0x7F`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7F


class PixelateLayers(UsableEventScriptCommand, EventScriptCommand):
    """Pixelate the given layers according to the given stylistic rules.

    ## Lazy Shell command
        `Pixellate layers {xx} by {xx} amount...`

    ## Opcode
        `0x84`

    ## Size
        3 bytes

    Args:
        layers (list[Layer] | set[Layer]): The list of layers to be pixelated
        pixel_size (int): The size of the rendered pixels
        duration (int): The number of frames over which to complete the pixel effect
        bit_6 (bool): (unknown)
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x84
    _size: int = 3
    _layers: set[Layer]
    _pixel_size: UInt8
    _duration: UInt8
    _bit_6: bool = False
    _bit_7: bool = False

    @property
    def layers(self) -> set[Layer]:
        """The list of layers to be pixelated."""
        return self._layers

    def set_layers(self, layers: list[Layer] | set[Layer]) -> None:
        """Overwrite the layers to be pixelated."""
        for layer in layers:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4]
        self._layers = set(layers)

    @property
    def pixel_size(self) -> UInt8:
        """The size of the rendered pixels."""
        return self._pixel_size

    def set_pixel_size(self, pixel_size: int) -> None:
        """Set the size (0-15) of the rendered pixels."""
        assert 0 <= pixel_size <= 15
        self._pixel_size = UInt8(pixel_size)

    @property
    def duration(self) -> UInt8:
        """The number of frames over which to complete the pixel effect."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the number of frames (0-63) over which to complete the pixel effect."""
        assert 0 <= duration <= 63
        self._duration = UInt8(duration)

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        layers: list[Layer] | set[Layer],
        pixel_size: int,
        duration: int,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_layers(layers)
        self.set_pixel_size(pixel_size)
        self.set_duration(duration)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        layers: int = bits_to_int(cast(list[int], self.layers))
        arg_1 = UInt8(layers + (self.pixel_size << 4))
        return super().render(
            arg_1, self.duration + (self.bit_6 << 6) + (self.bit_7 << 7)
        )


class PrioritySet(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)

    ## Lazy Shell command
        `Priority set = ...`

    ## Opcode
        `0x81`

    ## Size
        4 bytes

    Args:
        mainscreen (list[Layer] | set[Layer]): (unknown)
        subscreen (list[Layer] | set[Layer]): (unknown)
        colour_math (list[Layer] | set[Layer]): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x81
    _size: int = 4
    _mainscreen: set[Layer]
    _subscreen: set[Layer]
    _colour_math: set[Layer]

    @property
    def mainscreen(self) -> set[Layer]:
        """(unknown)"""
        return self._mainscreen

    def set_mainscreen(self, mainscreen: list[Layer] | set[Layer]) -> None:
        """(unknown)"""
        for layer in mainscreen:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, NPC_SPRITES]
        self._mainscreen = set(mainscreen)

    @property
    def subscreen(self) -> set[Layer]:
        """(unknown)"""
        return self._subscreen

    def set_subscreen(self, subscreen: list[Layer] | set[Layer]) -> None:
        """(unknown)"""
        for layer in subscreen:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, NPC_SPRITES]
        self._subscreen = set(subscreen)

    @property
    def colour_math(self) -> set[Layer]:
        """(unknown)"""
        return self._colour_math

    def set_colour_math(self, colour_math: list[Layer] | set[Layer]) -> None:
        """(unknown)"""
        for layer in colour_math:
            assert layer != LAYER_L4
        self._colour_math = set(colour_math)

    def __init__(
        self,
        mainscreen: list[Layer] | set[Layer],
        subscreen: list[Layer] | set[Layer],
        colour_math: list[Layer] | set[Layer],
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_mainscreen(mainscreen)
        self.set_subscreen(subscreen)
        self.set_colour_math(colour_math)

    def render(self, *args) -> bytearray:
        mainscreen: int = bits_to_int(cast(list[int], self.mainscreen))
        subscreen: int = bits_to_int(cast(list[int], self.subscreen))
        colour_math: int = bits_to_int(cast(list[int], self.colour_math))
        return super().render(mainscreen, subscreen, colour_math)


class ResetPrioritySet(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        `Reset priority set`

    ## Opcode
        `0x82`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x82


class ScreenFlashesWithColour(UsableEventScriptCommand, EventScriptCommand):
    """Briefly flash a colour over the whole screen.

    ## Lazy Shell command
        `Screen flashes with {xx} color...`

    ## Opcode
        `0x83`

    ## Size
        2 bytes

    Args:
        colour (Colour): The colour to flash
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x83
    _size: int = 2
    _colour: Colour

    @property
    def colour(self) -> Colour:
        """The colour to flash."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the colour to flash."""
        self._colour = colour

    def __init__(
        self,
        colour: Colour,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_colour(colour)

    def render(self, *args) -> bytearray:
        return super().render(self.colour)


class TintLayers(UsableEventScriptCommand, EventScriptCommand):
    """Tint the selected layers with an RGB value.
    RGB values must be divisible by 8.

    ## Lazy Shell command
        `Tint layers {xx} with {xx} color...`

    ## Opcode
        `0x80`

    ## Size
        5 bytes

    Args:
        layers (list[Layer]): The list of layers to be tinted
        red (int): The red value of the RGB colour. Must be divisible by 8
        green (int): The green value of the RGB colour. Must be divisible by 8
        blue (int): The blue value of the RGB colour. Must be divisible by 8
        speed (int): The speed at which to perform the tint
        bit_15 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x80
    _size: int = 5
    _layers: list[Layer]
    _red: UInt8
    _green: UInt8
    _blue: UInt8
    _speed: UInt8
    _bit_15: bool

    @property
    def layers(self) -> list[Layer]:
        """The list of layers to be tinted."""
        return self._layers

    def set_layers(self, layers: list[Layer]) -> None:
        """Overwrite the list of layers to be tinted."""
        self._layers = layers

    @property
    def red(self) -> UInt8:
        """The red value of the RGB colour."""
        return self._red

    def set_red(self, red: int) -> None:
        """Set the red value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= red <= 248 and red % 8 == 0
        self._red = UInt8(red)

    @property
    def green(self) -> UInt8:
        """The green value of the RGB colour."""
        return self._green

    def set_green(self, green: int) -> None:
        """Set the green value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= green <= 248 and green % 8 == 0
        self._green = UInt8(green)

    @property
    def blue(self) -> UInt8:
        """The blue value of the RGB colour."""
        return self._blue

    def set_blue(self, blue: int) -> None:
        """Set the blue value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= blue <= 248 and blue % 8 == 0
        self._blue = UInt8(blue)

    @property
    def speed(self) -> UInt8:
        """The speed at which to perform the tint."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed at which to perform the tint."""
        self._speed = UInt8(speed)

    @property
    def bit_15(self) -> bool:
        """(unknown)"""
        return self._bit_15

    def set_bit_15(self, bit_15: bool) -> None:
        """(unknown)"""
        self._bit_15 = bit_15

    def __init__(
        self,
        layers: list[Layer],
        red: int,
        green: int,
        blue: int,
        speed: int,
        bit_15: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_layers(layers)
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)
        self.set_speed(speed)
        self.set_bit_15(bit_15)

    def render(self, *args) -> bytearray:
        assembled_raw: int = (
            (self.red >> 3) + (self.green << 2) + (self.blue << 7) + (self.bit_15 << 15)
        )
        assembled_short = UInt16(assembled_raw)
        assembled_layers_raw: int = bits_to_int(cast(list[int], self.layers))
        assembled_layers = UInt8(assembled_layers_raw)
        return super().render(assembled_short, assembled_layers, self.speed)


# screen transitions


class CircleMaskExpandFromScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A circle mask expands from the center to reveal the whole level.

    ## Lazy Shell command
        `Circle mask, expand from screen center`

    ## Opcode
        `0x7C`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7C


class CircleMaskShrinkToScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A circle mask shrinks to the screen center to black out most of the level.

    ## Lazy Shell command
        `Circle mask, shrink to screen center`

    ## Opcode
        `0x7D`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7D


class CircleMaskShrinkToObject(UsableEventScriptCommand, EventScriptCommand):
    """A circle mask shrinks to surround a given object, blacking out most of the level.

    ## Lazy Shell command
        `Circle mask, shrink to object {xx} (non-static)...`
        `Circle mask, shrink to object {xx} (static)...`

    ## Opcode
        `0x87`
        `0x8F`

    ## Size
        4 bytes

    Args:
        target (AreaObject): The field object to follow. Use the pre-defined ones in area_objects.py.
        width (int): The diameter of the circle mask in pixels
        speed (int): The speed at which the mask effect should complete
        static (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 4
    _static: bool
    _target: AreaObject
    _width: UInt8
    _speed: UInt8

    @property
    def static(self) -> bool:
        """(unknown)"""
        return self._static

    def set_static(self, static: bool) -> None:
        """(unknown)"""
        self._static = static

    @property
    def target(self) -> AreaObject:
        """The target which the circle mask will be following."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Set the target which the circle mask will be following."""
        self._target = target

    @property
    def width(self) -> UInt8:
        """The width of the circle mask in pixels."""
        return self._width

    def set_width(self, width: int) -> None:
        """Set the width of the circle mask in pixels."""
        self._width = UInt8(width)

    @property
    def speed(self) -> UInt8:
        """The speed at which the mask effect should complete."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed at which the mask effect should complete."""
        self._speed = UInt8(speed)

    def __init__(
        self,
        target: AreaObject,
        width: int,
        speed: int,
        static: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_width(width)
        self.set_speed(speed)
        self.set_static(static)

    def render(self, *args) -> bytearray:
        opcode: int = 0x8F if self.static else 0x87
        return super().render(opcode, self.target, self.width, self.speed)


class StarMaskExpandFromScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A star mask expands from the center to reveal the whole level.

    ## Lazy Shell command
        `Star mask, expand from screen center`

    ## Opcode
        `0x7A`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7A


class StarMaskShrinkToScreenCenter(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """A star mask shrinks to the screen center to black out most of the level.

    ## Lazy Shell command
        `Star mask, shrink to screen center`

    ## Opcode
        `0x7B`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7B


class FadeInFromBlack(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen in from being unloaded.

    ## Lazy Shell command
        `Fade in from black (sync)`
        `Fade in from black (async)`
        `Fade in from black (sync) for {xx} duration...`
        `Fade in from black (async) for {xx} duration...`

    ## Opcode
        `0x70`
        `0x71`
        `0x72`
        `0x73`

    ## Size
        1 byte with no duration
        2 bytes with a duration

    Args:
        sync (bool): If false, the fade must finish before the script can continue
        duration (int | None): The length of time in frames that the fade should take
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _sync: bool = False
    _duration: UInt8 | None = None

    @property
    def sync(self) -> bool:
        """If false, the fade must finish before the script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the fade must finish before the script can continue."""
        self._sync = sync

    @property
    def duration(self) -> UInt8 | None:
        """The length of time in frames that the fade should take."""
        if self._duration is not None:
            return UInt8(self._duration)
        return self._duration

    def set_duration(self, duration: int | None = None) -> None:
        """Define the length of time in frames that the fade should take."""
        if duration is not None:
            self._duration = UInt8(duration)
        if self.duration is None:
            self._size = 1
        else:
            self._size = 2

    def __init__(
        self,
        sync: bool,
        duration: int | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sync(sync)
        self.set_duration(duration)

    def render(self, *args) -> bytearray:
        opcode: int = 0x70 + (not self.sync)
        if self.duration is not None:
            opcode += 2
            return super().render(opcode, self.duration)
        return super().render(opcode)


class FadeInFromColour(UsableEventScriptCommand, EventScriptCommand):
    """Draw an opaque colour over the screen, and then fade the screen in.

    ## Lazy Shell command
        `Fade in from {xx} color...`

    ## Opcode
        `0x78`

    ## Size
        3 bytes

    Args:
        duration (int): The length of time in frames that the fade should take
        colour (Colour): The initial colour to draw over the screen
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x78
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        """The length of time in frames that the fade should take."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Define the length of time in frames that the fade should take."""
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        """The initial colour to draw over the screen."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the initial colour to draw over the screen."""
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.colour)


class FadeOutToBlack(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen out to solid black.

    ## Lazy Shell command
        `Fade out to black (sync)`
        `Fade out to black (async)`
        `Fade out to black (sync) for {xx} duration...`
        `Fade out to black (async) for {xx} duration...`

    ## Opcode
        `0x74`
        `0x75`
        `0x76`
        `0x77`

    ## Size
        1 byte with no duration
        2 bytes with a duration

    Args:
        sync (bool): If false, the fade must finish before the script can continue
        duration (int | None): The length of time in frames that the fade should take
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _sync: bool = False
    _duration: UInt8 | None = None

    @property
    def sync(self) -> bool:
        """If false, the fade must finish before the script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the fade must finish before the script can continue."""
        self._sync = sync

    @property
    def duration(self) -> UInt8 | None:
        """The length of time in frames that the fade should take."""
        if self._duration is not None:
            return UInt8(self._duration)
        return self._duration

    def set_duration(self, duration: int | None = None) -> None:
        """Define the length of time in frames that the fade should take."""
        if duration is not None:
            self._duration = UInt8(duration)
        if self.duration is None:
            self._size = 1
        else:
            self._size = 2

    def __init__(
        self,
        sync: bool,
        duration: int | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sync(sync)
        self.set_duration(duration)

    def render(self, *args) -> bytearray:
        opcode: int = 0x74 + (not self.sync)
        if self.duration is not None:
            opcode += 2
            return super().render(opcode, self.duration)
        return super().render(opcode)


class FadeOutToColour(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen out to any solid colour.

    ## Lazy Shell command
        `Fade out to {xx} color...`

    ## Opcode
        `0x79`

    ## Size
        3 bytes

    Args:
        duration (int): The length of time in frames that the fade should take
        colour (Colour): The final colour to draw over the screen
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x79
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        """The length of time in frames that the fade should take."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Define the length of time in frames that the fade should take."""
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        """The final colour to draw over the screen."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the final colour to draw over the screen."""
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.colour)


class InitiateBattleMask(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Perform the screen effect that precedes a battle.

    ## Lazy Shell command
        `Initiate battle mask`

    ## Opcode
        `0x7E`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7E


# music


class SlowDownMusicTempoBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to slow down the music.

    ## Lazy Shell command
        `Adjust music tempo by {xx} amount...`

    ## Opcode
        `0x97`

    ## Size
        3 bytes

    Args:
        duration (int): The time in frames over which the tempo change should gradually occur
        change (int): Set the time in frames over which the tempo change should gradually occur (0 to 127)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the tempo change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the tempo change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in tempo to apply as a slowdown."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set he difference in tempo to apply as a slowdown (0 to 127)."""
        assert 0 <= change <= 127
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.change)


class SpeedUpMusicTempoBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to speed up the music.

    ## Lazy Shell command
        `Adjust music tempo by {xx} amount...`

    ## Opcode
        `0x97`

    ## Size
        3 bytes

    Args:
        duration (int): The time in frames over which the tempo change should gradually occur.
        change (int): The difference in tempo to apply as a speedup (0 to 128).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the tempo change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the tempo change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in tempo to apply as a speedup."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set he difference in tempo to apply as a speedup (0 to 128)."""
        assert 0 < change <= 128
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, 256 - self.change)


class ReduceMusicPitchBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to lower the pitch.

    ## Lazy Shell command
        `Adjust music pitch by {xx} amount...`

    ## Opcode
        `0x98`

    ## Size
        3 bytes

    Args:
        duration (int): The time in frames over which the tempo change should gradually occur
        change (int): Set the time in frames over which the tempo change should gradually occur (0 to 127)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x98
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the pitch change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the pitch change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in pitch to lower by."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set the difference in pitch to lower by (0 to 127)."""
        assert 0 <= change <= 127
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, 256 - self.change)


class IncreaseMusicPitchBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to increase the pitch.

    ## Lazy Shell command
        `Adjust music pitch by {xx} amount...`

    ## Opcode
        `0x98`

    ## Size
        3 bytes

    Args:
        duration (int): The time in frames over which the tempo change should gradually occur.
        change (int): The difference in tempo to apply as a speedup (0 to 128)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x98
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the pitch change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the pitch change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in pitch to raise by."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set the difference in pitch to raise by (0 to 128)."""
        assert 0 < change <= 128
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.change)


class DeactivateSoundChannels(UsableEventScriptCommand, EventScriptCommand):
    """Sound channels identified by the given bits (0-7) will be silenced.

    ## Lazy Shell command
        `Deactivate {xx} sound channels...`

    ## Opcode
        `0xFD 0x94`

    ## Size
        3 bytes

    Args:
        bits (set[int]): i.e. include bit 4 to silence channel 4
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x94])
    _size: int = 3
    _bits: set[int]

    @property
    def bits(self) -> set[int]:
        """i.e. include bit 4 to silence channel 4"""
        return self._bits

    def set_bits(self, bits: set[int]) -> None:
        """0-7. i.e. include bit 4 to silence channel 4"""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = bits

    def __init__(
        self,
        bits: set[int],
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt8(bits_to_int(list(self.bits)))
        return super().render(flags)


class FadeInMusic(UsableEventScriptCommand, EventScriptCommand):
    """Fade music in from a silent state.
    It is recommended to use music ID constant names for this.

    ## Lazy Shell command
        `Fade in music {xx} ...`

    ## Opcode
        `0x92`

    ## Size
        2 bytes

    Args:
        music (int): The ID of the music to fade in.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x92
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to fade in."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to fade in.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self, *args) -> bytearray:
        return super().render(self.music)


class FadeOutMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current background music fades out to silence.

    ## Lazy Shell command
        `Fade out current music`

    ## Opcode
        `0x93`

    ## Size
        1 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x93


class FadeOutMusicFDA3(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current background music fades out to silence.
    Unknown how this differs from `FadeOutMusic`.

    ## Lazy Shell command
        Renders in scripts as `Fade out current music` but is unselectable

    ## Opcode
        `0xFD 0xA3`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA3])
    _size: int = 2


class FadeOutMusicToVolume(UsableEventScriptCommand, EventScriptCommand):
    """Fade out the currently playing background music to a specified volume over a specified time period (in frames).

    ## Lazy Shell command
        `Fade out current music to {xx} volume...`

    ## Opcode
        `0x95`

    ## Size
        3 bytes

    Args:
        duration (int): The duration, in frames, over which to perform the fade.
        volume (int): The final volume of the background music.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x95
    _size: int = 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, over which to perform the fade."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, over which to perform the fade."""
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        """The final volume of the background music."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        """Set the final volume of the background music."""
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.volume)


class FadeOutSoundToVolume(UsableEventScriptCommand, EventScriptCommand):
    """Fade out the currently playing sound to a specified volume over a specified time period (in frames).

    ## Lazy Shell command
        `Fade out current sound to {xx} volume...`

    ## Opcode
        `0x9E`

    ## Size
        3 bytes

    Args:
        duration (int): The duration, in frames, over which to perform the fade.
        volume (int): The desired ending volume for the sound effect.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x9E
    _size: int = 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, over which to perform the fade."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, over which to perform the fade."""
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        """The desired ending volume for the sound effect."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        """Specify the desired ending volume for the sound effect."""
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self, *args) -> bytearray:
        return super().render(self.duration, self.volume)


class JmpIfAudioMemoryIsAtLeast(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)

    ## Lazy Shell command
        `If audio memory $69 >= ...`

    ## Opcode
        `0xFD 0x96`

    ## Size
        5 bytes

    Args:
        threshold (int): (unknown)
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x96])
    _size: int = 5
    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        """(unknown)"""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """(unknown)"""
        self._threshold = UInt8(threshold)

    def __init__(
        self,
        threshold: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_threshold(threshold)

    def render(self, *args) -> bytearray:
        return super().render(self.threshold, *self.destinations)


class JmpIfAudioMemoryEquals(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)

    ## Lazy Shell command
        `If audio memory $69 = ...`

    ## Opcode
        `0xFD 0x97`

    ## Size
        5 bytes

    Args:
        value (int): (unknown)
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x97])
    _size: int = 5
    _value: UInt8

    @property
    def value(self) -> UInt8:
        """(unknown)"""
        return self._value

    def set_value(self, value: int) -> None:
        """(unknown)"""
        self._value = UInt8(value)

    def __init__(
        self,
        value: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self.value, *self.destinations)


class PlayMusic(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track.

    ## Lazy Shell command
        (doesn't seem to be used)

    ## Opcode
        `0xFD 0x9E`

    ## Size
        3 bytes

    Args:
        music (int): The ID of the music to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x9E])
    _size: int = 3
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self, *args) -> bytearray:
        return super().render(self.music)


class PlayMusicAtCurrentVolume(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track, at the same volume as the current track.

    ## Lazy Shell command
        `Play music {xx} at current volume...`

    ## Opcode
        `0x90`

    ## Size
        2 bytes

    Args:
        music (int): The ID of the music to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x90
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self, *args) -> bytearray:
        return super().render(self.music)


class PlayMusicAtDefaultVolume(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track (at default volume).

    ## Lazy Shell command
        `Play music {xx} at default volume...`

    ## Opcode
        `0x91`

    ## Size
        2 bytes

    Args:
        music (int): The ID of the music to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x91
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self, *args) -> bytearray:
        return super().render(self.music)


class PlaySound(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect by ID on the specified channel.

    ## Lazy Shell command
        `Play {xx} sound (ch.6,7)...`
        `Play {xx} sound (ch.4,5)...`

    ## Opcode
        `0x9C`
        `0xFD 0x9C`

    ## Size
        2 bytes on channel 6
        3 bytes on channel 4

    Args:
        sound (int): The ID of the sound to play.
        channel (int): The channel on which to play the sound. Needs to be 4 or 6.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _sound: UInt8
    _channel: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def channel(self) -> UInt8:
        """The channel on which to play the sound."""
        return self._channel

    def set_channel(self, channel: int) -> None:
        """Set the channel on which to play the sound.\n
        Valid values are 4 or 6."""
        assert channel in [4, 6]
        self._channel = UInt8(channel)
        if self.channel == 4:
            self._size = 3
            self._opcode = bytearray([0xFD, 0x9C])
        else:
            self._size = 2
            self._opcode = 0x9C

    def __init__(self, sound: int, channel: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_channel(channel)

    def render(self, *args) -> bytearray:
        return super().render(self.sound)


class PlaySoundBalance(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect at a given balance.

    ## Lazy Shell command
        `Play {xx} sound (ch.6,7) with {xx} speaker balance...`

    ## Opcode
        `0x9D`

    ## Size
        3 bytes

    Args:
        sound (int): The ID of the sound to play.
        balance (int): The balance level to play the sound at.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x9D
    _size: int = 3
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        """The balance level to play the sound at."""
        return self._balance

    def set_balance(self, balance: int) -> None:
        """Set the balance level to play the sound at."""
        self._balance = UInt8(balance)

    def __init__(self, sound: int, balance: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self, *args) -> bytearray:
        return super().render(self.sound, self.balance)


class PlaySoundBalanceFD9D(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect at a given balance.
    Unknown how this differs from `PlaySoundBalance`.

    ## Lazy Shell command
        Renders as "Play {xx} sound (ch.6,7) with {xx} speaker balance" but is not selectable

    ## Opcode
        `0xFD 0x9D`

    ## Size
        4 bytes

    Args:
        sound (int): The ID of the sound to play.
        balance (int): The balance level to play the sound at.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x9D])
    _size: int = 4
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        """The balance level to play the sound at."""
        return self._balance

    def set_balance(self, balance: int) -> None:
        """Set the balance level to play the sound at."""
        self._balance = UInt8(balance)

    def __init__(self, sound: int, balance: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self, *args) -> bytearray:
        return super().render(self.sound, self.balance)


class SlowDownMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Show down the current music to an unspecified tempo, over a constant duration.

    ## Lazy Shell command
        `Lower current music tempo`

    ## Opcode
        `0xFD 0xA4`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA4])


class SpeedUpMusicToDefault(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return the current music tempo to default, over a constant duration.

    ## Lazy Shell command
        `Slide current music tempo to default`

    ## Opcode
        `0xFD 0xA5`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA5])


class StopMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.

    ## Lazy Shell command
        `Stop current music`

    ## Opcode
        `0x94`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x94


class StopMusicFD9F(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.
    It is unknown how this differs from `StopMusic`.

    ## Lazy Shell command
        Renders as `Stop current music` but is not selectable

    ## Opcode
        `0xFD 0x9F`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x9F])


class StopMusicFDA0(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.
    It is unknown how this differs from `StopMusic`.

    ## Lazy Shell command
        Renders as `Stop current music` but is not selectable

    ## Opcode
        `0xFD 0xA0`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA0])


class StopMusicFDA1(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.
    It is unknown how this differs from `StopMusic`.

    ## Lazy Shell command
        Renders as `Stop current music` but is not selectable

    ## Opcode
        `0xFD 0xA1`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA1])


class StopMusicFDA2(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.
    It is unknown how this differs from `StopMusic`.

    ## Lazy Shell command
        Renders as `Stop current music` but is not selectable

    ## Opcode
        `0xFD 0xA2`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA2])


class StopMusicFDA6(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.
    It is unknown how this differs from `StopMusic`.

    ## Lazy Shell command
        Renders as `Stop current music` but is not selectable

    ## Opcode
        `0xFD 0xA6`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xA6])


class StopSound(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Halt the playback of any sound effect that is currently playing.

    ## Lazy Shell command
        `Stop current sound`

    ## Opcode
        `0x9B`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x9B


# dialogs


class AppendDialogAt7000ToCurrentDialog(UsableEventScriptCommand, EventScriptCommand):
    """The dialog whose ID corresponds to the current value of $7000 will be appended to the end of a dialog that is already being displayed.

    ## Lazy Shell command
        `Append to dialogue @ memory $7000...`

    ## Opcode
        `0x63`

    ## Size
        2 bytes

    Args:
        closable (bool): If false, the dialog will remain on screen instead of being clearable
        sync (bool): If false, events will continue to run and the player can continue to move.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x63
    _size: int = 2
    _closable: bool
    _sync: bool

    @property
    def closable(self) -> bool:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        return self._closable

    def set_closable(self, closable: bool) -> None:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        self._closable = closable

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
        self._sync = sync

    def __init__(
        self, closable: bool, sync: bool, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_closable(closable)
        self.set_sync(sync)

    def render(self, *args) -> bytearray:
        flags = (self.closable << 5) + ((not self.sync) << 7)
        return super().render(flags)


class CloseDialog(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """If there is an open dialog, it will be forcibly closed.

    ## Lazy Shell command
        `Close dialogue`

    ## Opcode
        `0x64`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x64


class JmpIfDialogOptionBSelected(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Depends on the results of a previously displayed dialog which had only 2 options. If the second option was selected, go to the section of code beginning with the command matching the given label.

    ## Lazy Shell command
        `If dialogue option B selected...`

    ## Opcode
        `0x66`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x66
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class JmpIfDialogOptionBOrCSelected(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depends on the results of a previously displayed dialog which had 3 options. If the second or third option was selected, go to the section of code beginning with the command matching the first or second identifier, respectively.

    ## Lazy Shell command
        `If dialogue option B / C selected...`

    ## Opcode
        `0x67`

    ## Size
        5 bytes

    Args:
        destinations (list[str]): This should be a list of exactly two `str`s. The `str`s should be the labels of commands to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x67
    _size: int = 5

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)


class PauseScriptResumeOnNextDialogPageA(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The active script will be paused until the next dialog page is loaded.
    Unknown how this differs from `PauseScriptResumeOnNextDialogPageB`.

    ## Lazy Shell command
        `Pause script, resume on next dialogue page A`

    ## Opcode
        `0xFD 0x60`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x60])


class PauseScriptResumeOnNextDialogPageB(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The active script will be paused until the next dialog page is loaded.
    Unknown how this differs from `PauseScriptResumeOnNextDialogPageA`.

    ## Lazy Shell command
        `Pause script, resume on next dialogue page B`

    ## Opcode
        `0xFD 0x61`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x61])


class RunDialog(UsableEventScriptCommand, EventScriptCommand):
    """Display a dialog by ID, or whose ID matches the current value of $7000.
    If not displaying the dialog whose ID matches the value currently stored to $7000, it is recommended to use dialog ID constant names for this.

    ## Lazy Shell command
        `Run dialogue...`
        `Run dialogue @ memory $7000...`

    ## Opcode
        `0x60`
        `0x61`

    ## Size
        3 bytes if dialogue is at $7000
        4 bytes otherwise

    Args:
        dialog_id (int | ShortVar): The ID of the dialog to display, or the var containing an ID to display.
        above_object (AreaObject): The field object to anchor the dialog on. Use the pre-defined ones in area_objects.py.
        closable (bool): If false, the dialog will remain on screen instead of being clearable
        sync (bool): If false, events will continue to run and the player can continue to move.
        multiline (bool): If true, the dialog will display up to 3 lines.
        use_background (bool): If true, the dialog will be displayed over the parchment asset.
        bit_6 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _dialog_id: UInt16 | ShortVar
    _above_object: AreaObject
    _closable: bool
    _bit_6: bool
    _sync: bool
    _multiline: bool
    _use_background: bool

    @property
    def dialog_id(self) -> UInt16 | ShortVar:
        """The ID of the dialog to display, or the var containing an ID to display. If using a var, it has to be `ShortVar(0x7000)`."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int | ShortVar) -> None:
        """Accepts one of two things:\n
        1. The ID of the dialog to display
        (it is recommended to use dialog ID constant names for this),\n
        2. A short var, whose value indicates the ID to run (only `ShortVar(0x7000)` accepted).
        """
        if dialog_id == ShortVar(0x7000):
            self._dialog_id = ShortVar(dialog_id)
        else:
            assert 0 <= dialog_id < TOTAL_DIALOGS
            self._dialog_id = UInt16(dialog_id)

        if isinstance(self.dialog_id, ShortVar):
            self._size = 3
            self._opcode = 0x61
        else:
            self._size = 4
            self._opcode = 0x60

    @property
    def above_object(self) -> AreaObject:
        """The NPC or other target which the dialog should be above."""
        return self._above_object

    def set_above_object(self, above_object: AreaObject) -> None:
        """Indicate the NPC or other target which the dialog should be above."""
        self._above_object = above_object

    @property
    def closable(self) -> bool:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        return self._closable

    def set_closable(self, closable: bool) -> None:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        self._closable = closable

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
        self._sync = sync

    @property
    def multiline(self) -> bool:
        """If true, the dialog will display up to 3 lines.\n
        If false, the dialog will display only 1 line."""
        return self._multiline

    def set_multiline(self, multiline: bool) -> None:
        """If true, the dialog will display up to 3 lines.\n
        If false, the dialog will display only 1 line."""
        self._multiline = multiline

    @property
    def use_background(self) -> bool:
        """If true, the dialog will be displayed over the parchment asset.\n
        If false, the dialog should be displayed as blue text over a transparent
        background, although this is not always respected."""
        return self._use_background

    def set_use_background(self, use_background: bool) -> None:
        """If true, the dialog will be displayed over the parchment asset.\n
        If false, the dialog should be displayed as blue text over a transparent
        background, although this is not always respected."""
        self._use_background = use_background

    def __init__(
        self,
        dialog_id: int | ShortVar,
        above_object: AreaObject,
        closable: bool,
        sync: bool,
        multiline: bool,
        use_background: bool,
        bit_6: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)
        self.set_above_object(above_object)
        self.set_closable(closable)
        self.set_bit_6(bit_6)
        self.set_sync(sync)
        self.set_multiline(multiline)
        self.set_use_background(use_background)

    def render(self, *args) -> bytearray:
        flags_lower: int = (
            (self.closable << 5) + (self.bit_6 << 6) + ((not self.sync) << 7)
        )
        flags_upper: int = (self.multiline << 6) + (self.use_background << 7)
        final_arg = UInt8(self.above_object + flags_upper)
        if isinstance(self.dialog_id, ShortVar):
            return super().render(flags_lower, final_arg)
        id_arg = UInt16((flags_lower << 8) + self.dialog_id)
        return super().render(id_arg, final_arg)


class RunDialogForDuration(UsableEventScriptCommand, EventScriptCommand):
    """Display a dialog by ID for a given duration in frames.

    ## Lazy Shell command
        `Run dialogue for {xx} duration...`

    ## Opcode
        `0x62`

    ## Size
        3 bytes

    Args:
        dialog_id (int): The ID of the dialog to display.
        duration (int): The duration, in frames, for which the dialog should be active.
        sync (bool): If false, events will continue to run and the player can continue to move.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x62
    _size: int = 3
    _dialog_id: UInt16
    _duration: UInt8
    _sync: bool

    @property
    def dialog_id(self) -> UInt16:
        """The ID of the dialog to display."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        """Set the ID of the dialog to display.\n
        It is recommended to use dialog ID constant names for this."""
        assert 0 <= dialog_id < TOTAL_DIALOGS
        self._dialog_id = UInt16(dialog_id)

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, for which the dialog should be active."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, for which the dialog should be active."""
        assert 0 <= duration <= 3
        self._duration = UInt8(duration)

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
        self._sync = sync

    def __init__(
        self,
        dialog_id: int,
        duration: int,
        sync: bool,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)
        self.set_duration(duration)
        self.set_sync(sync)

    def render(self, *args) -> bytearray:
        arg = UInt16(self.dialog_id + (self.duration << 13) + ((not self.sync) << 15))
        return super().render(arg)


class UnsyncDialog(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Event scripts and player movements will resume without waiting for the dialog to close.

    ## Lazy Shell command
        `Un-sync dialogue`

    ## Opcode
        `0x65`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x65


# levels


class EnterArea(UsableEventScriptCommand, EventScriptCommand):
    """Immediately teleport to a specified level.

    ## Lazy Shell command
        `Open level...`

    ## Opcode
        `0x68`

    ## Size
        6 bytes

    Args:
        room_id (int): The ID of the level to open.
        face_direction (Direction): The direction that the player will face when the room loads.
        x (int): The X coordinate at which the player will be standing when the room loads.
        y (int): The Y coordinate at which the player will be standing when the room loads.
        z (int): The Z coordinate at which the player will be standing when the room loads.
        z_add_half_unit (bool): If true, adds half a unit to the player's starting Z coordinate.
        show_banner (bool): If the room has an associated message, the message will be temporarily
        run_entrance_event (bool): If true, the entrance event associated to the room will run on load.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x68
    _size: int = 6
    _room_id: UInt16
    _face_direction: Direction
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _z_add_half_unit: bool
    _show_banner: bool
    _run_entrance_event: bool

    @property
    def room_id(self) -> UInt16:
        """The ID of the level to open."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the level to open.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def face_direction(self) -> Direction:
        """The direction that the player will face when the room loads."""
        return self._face_direction

    def set_face_direction(self, face_direction: Direction) -> None:
        """Choose the direction that the player will face when the room loads."""
        self._face_direction = face_direction

    @property
    def x(self) -> UInt8:
        """The X coordinate at which the player will be standing when the room loads."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which the player will be standing when the room loads."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which the player will be standing when the room loads."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate (0-127) at which the player will be standing
        when the room loads."""
        assert 0 <= y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coordinate at which the player will be standing when the room loads."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coordinate (0-31) at which the player will be standing when the room loads."""
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def z_add_half_unit(self) -> bool:
        """If true, adds half a unit to the player's starting Z coordinate."""
        return self._z_add_half_unit

    def set_z_add_half_unit(self, z_add_half_unit: bool) -> None:
        """If true, adds half a unit to the player's starting Z coordinate."""
        self._z_add_half_unit = z_add_half_unit

    @property
    def show_banner(self) -> bool:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        return self._show_banner

    def set_show_banner(self, show_banner: bool) -> None:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        self._show_banner = show_banner

    @property
    def run_entrance_event(self) -> bool:
        """If true, the entrance event associated to the room will run on load."""
        return self._run_entrance_event

    def set_run_entrance_event(self, run_entrance_event: bool) -> None:
        """If true, the entrance event associated to the room will run on load."""
        self._run_entrance_event = run_entrance_event

    def __init__(
        self,
        room_id: int,
        face_direction: Direction,
        x: int,
        y: int,
        z: int,
        z_add_half_unit: bool = False,
        show_banner: bool = False,
        run_entrance_event: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_face_direction(face_direction)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_z_add_half_unit(z_add_half_unit)
        self.set_show_banner(show_banner)
        self.set_run_entrance_event(run_entrance_event)

    def render(self, *args) -> bytearray:
        room_short = UInt16(
            self.room_id + (self.show_banner << 11) + (self.run_entrance_event << 15)
        )
        y_z_arg = UInt8(self.y + (self.z_add_half_unit << 7))
        direction_z_arg = UInt8(self.z + (self.face_direction << 5))
        return super().render(room_short, self.x, y_z_arg, direction_z_arg)


class ApplyTileModToLevel(UsableEventScriptCommand, EventScriptCommand):
    """If the specified room has tile modifications available, this command can apply one.

    ## Lazy Shell command
        `Apply tile mod to level...`

    ## Opcode
        `0x6A`

    ## Size
        3 bytes

    Args:
        room_id (int): The ID of the room applying a tile mod.
        mod_id (int): The ID of the mod to apply.
        use_alternate (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x6A
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _use_alternate: bool

    @property
    def room_id(self) -> UInt16:
        """The ID of the room applying a tile mod."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the room applying a tile mod.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        """The ID of the mod to apply."""
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        """Set the ID of the mod to apply (0-63).\n
        It is the dev's responsibility to make sure that the mod actually exists."""
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def use_alternate(self) -> bool:
        """(unknown)"""
        return self._use_alternate

    def set_use_alternate(self, use_alternate: bool) -> None:
        """(unknown)"""
        self._use_alternate = use_alternate

    def __init__(
        self,
        room_id: int,
        mod_id: int,
        use_alternate: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_mod_id(mod_id)
        self.set_use_alternate(use_alternate)

    def render(self, *args) -> bytearray:
        assembled_raw: int = (
            self.room_id + (self.mod_id << 9) + (self.use_alternate << 15)
        )
        return super().render(UInt16(assembled_raw))


class ApplySolidityModToLevel(UsableEventScriptCommand, EventScriptCommand):
    """If the specified room has collision modifications available, this command can apply one.
    It is recommended to use room ID constant names for this.

    ## Lazy Shell command
        `Apply solid mod to level...`

    ## Opcode
        `0x6B`

    ## Size
        3 bytes

    Args:
        room_id (int): The ID of the room applying a collision mod.
        mod_id (int): The ID of the mod to apply.
        permanent (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x6B
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _permanent: bool

    @property
    def room_id(self) -> UInt16:
        """The ID of the room applying a collision mod."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the room applying a collision mod.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        """The ID of the mod to apply."""
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        """Set the ID of the mod to apply (0-63).\n
        It is the dev's responsibility to make sure that the mod actually exists."""
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def permanent(self) -> bool:
        """(unknown)"""
        return self._permanent

    def set_permanence(self, permanent: bool) -> None:
        """(unknown)"""
        self._permanent = permanent

    def __init__(
        self,
        room_id: int,
        mod_id: int,
        permanent: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_mod_id(mod_id)
        self.set_permanence(permanent)

    def render(self, *args) -> bytearray:
        assembled_raw: int = self.room_id + (self.mod_id << 9) + (self.permanent << 15)
        return super().render(UInt16(assembled_raw))


class ExitToWorldMap(UsableEventScriptCommand, EventScriptCommand):
    """Leaves the given level forcibly, and returns to the world map.
    It is recommended to use overworld location ID constant names for this.

    ## Lazy Shell command
        `Open location...`

    ## Opcode
        `0x4B`

    ## Size
        3 bytes

    Args:
        area (int): The world map dot to return to.
        bit_5 (bool): (unknown)
        bit_6 (bool): (unknown)
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4B
    _size: int = 3
    _area: UInt8
    _bit_5: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def area(self) -> UInt8:
        """The world map dot to return to."""
        return self._area

    def set_area(self, area: int) -> None:
        """Set the world map dot to return to.\n
        It is recommended to use overworld location ID constant names for this."""
        assert 0 <= area < TOTAL_WORLD_MAP_AREAS
        self._area = UInt8(area)

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        area: int,
        bit_5: bool = False,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_area(area)
        self.set_bit_5(bit_5)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        flags: int = bools_to_int(self.bit_5, self.bit_6, self.bit_7)
        flags = flags << 5
        return super().render(self.area, flags)


class Set7000ToCurrentLevel(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the value of $7000 to the ID of the currently loaded level.

    ## Lazy Shell command
        `Memory $7000 = current level`

    ## Opcode
        `0xC3`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xC3


# scenes


class DisplayIntroTitleText(UsableEventScriptCommand, EventScriptCommand):
    """Text that normally appears in the game intro. Unused in rando.

    ## Lazy Shell command
        `Display pre-game intro title...`

    ## Opcode
        `0xFD 0x66`

    ## Size
        4 bytes

    Args:
        text (IntroTitleText): The predefined text to display.
        y (int): The Y coord at which to display the text.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x66])
    _size: int = 4
    _text: IntroTitleText
    _y: UInt8

    @property
    def text(self) -> IntroTitleText:
        """The predefined text to display."""
        return self._text

    def set_text(self, text: IntroTitleText) -> None:
        """Choose the predefined text to display."""
        self._text = text

    @property
    def y(self) -> UInt8:
        """The Y coord at which to display the text."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord at which to display the text."""
        self._y = UInt8(y)

    def __init__(
        self, text: IntroTitleText, y: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_text(text)
        self.set_y(y)

    def render(self, *args) -> bytearray:
        return super().render(self.y, self.text)


class ExorCrashesIntoKeep(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Run the cutscene where Exor shatters the star road.
    Unused in rando.

    ## Lazy Shell command
        `Exor crashes into keep`

    ## Opcode
        `0xFD 0xF8`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0xF8])


class RunMenuOrEventSequence(UsableEventScriptCommand, EventScriptCommand):
    """Runs one of a various selection of menus or automatic cutscenes.

    ## Lazy Shell command
        `Open menu/run event sequence...`

    ## Opcode
        `0x4F`

    ## Size
        2 bytes

    Args:
        scene (Scene): The menu or cutscene to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4F
    _size: int = 2
    _scene: Scene

    @property
    def scene(self) -> Scene:
        """The menu or cutscene to play."""
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        """Choose the menu or cutscene to play."""
        self._scene = scene

    def __init__(self, scene: Scene, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_scene(scene)

    def render(self, *args) -> bytearray:
        return super().render(self.scene)


class OpenSaveMenu(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Open the save menu.

    ## Lazy Shell command
        `Open save game menu`

    ## Opcode
        `0xFD 0x4A`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4A])


class OpenShop(UsableEventScriptCommand, EventScriptCommand):
    """Open a shop by ID.
    It is recommended to use shop ID constant names for this.

    ## Lazy Shell command
        Open shop menu...`

    ## Opcode
        `0x4C`

    ## Size
        2 bytes

    Args:
        shop_id (int): The ID of the shop to open.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4C
    _size: int = 2
    _shop_id: UInt8

    @property
    def shop_id(self) -> UInt8:
        """The ID of the shop to open."""
        return self._shop_id

    def set_shop_id(self, shop_id: int) -> None:
        """Set the ID of the shop to open.\n
        It is recommended to use shop ID constant names for this."""
        assert 0 <= shop_id < TOTAL_SHOPS
        self._shop_id = UInt8(shop_id)

    def __init__(self, shop_id: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_shop_id(shop_id)

    def render(self, *args) -> bytearray:
        return super().render(self.shop_id)


class PauseScriptIfMenuOpen(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Pauses the running script if a menu is opened.

    ## Lazy Shell command
        `Pause script if menu open`

    ## Opcode
        `0x5B`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x5B


class ResetAndChooseGame(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Reloads your last save. Character EXP is not reset.

    ## Lazy Shell command
        `Reset game, choose game`

    ## Opcode
        `0xFB`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xFB


class ResetGame(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Reset to the file select screen (presumably?).

    ## Lazy Shell command
        `Reset game`

    ## Opcode
        `0xFC`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xFC


class RunEndingCredits(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Begin the ending credits sequence.

    ## Lazy Shell command
        `Run ending credit sequence`

    ## Opcode
        `0xFD 0x67`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x67])


class RunEventSequence(UsableEventScriptCommand, EventScriptCommand):
    """Run a special cutscene. Normally used for star pieces in the ending credits.

    ## Lazy Shell command
        `Run event sequence...`

    ## Opcode
        `0x4E`

    ## Size
        3 bytes

    Args:
        scene (Scene): The specific cutscene to run.
        value (int): A value needed by the chosen cutscene.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4E
    _size: int = 3
    _scene: Scene
    _value: UInt8

    @property
    def scene(self) -> Scene:
        """The specific cutscene to run."""
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        """Choose the specific cutscene to run."""
        self._scene = scene

    @property
    def value(self) -> UInt8:
        """A value needed by the chosen cutscene."""
        return self._value

    def set_value(self, value: int) -> None:
        """Provide a value needed by the chosen cutscene."""
        self._value = UInt8(value)

    def __init__(
        self, scene: Scene, value: int = 0, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_scene(scene)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self.scene, self.value)


class RunLevelupBonusSequence(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Launch the levelup screen.

    ## Lazy Shell command
        `Run level-up bonus sequence`

    ## Opcode
        `0xFD 0x65`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x65])


class RunMenuTutorial(UsableEventScriptCommand, EventScriptCommand):
    """Run a specific menu tutorial.

    ## Lazy Shell command
        `Run menu tutorial...`

    ## Opcode
        `0xFD 0x4C`

    ## Size
        3 bytes

    Args:
        tutorial (Tutorial): The specific tutorial to run.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4C])
    _size: int = 3
    _tutorial: Tutorial

    @property
    def tutorial(self) -> Tutorial:
        """The specific tutorial to run."""
        return self._tutorial

    def set_tutorial(self, tutorial: Tutorial) -> None:
        """Choose the specific tutorial to run."""
        self._tutorial = tutorial

    def __init__(self, tutorial: Tutorial, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_tutorial(tutorial)

    def render(self, *args) -> bytearray:
        return super().render(self.tutorial)


class RunMolevilleMountainIntroSequence(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """Runs the Moleville Mountain sequence found in the original game's attract mode. Unused in rando.

    ## Lazy Shell command
        `Run moleville mountain intro sequence`

    ## Opcode
        `0xFD 0x4F`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4F])


class RunMolevilleMountainSequence(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Enter the Moleville Mountain minigame.

    ## Lazy Shell command
        `Run moleville mountain sequence`

    ## Opcode
        `0xFD 0x4E`

    ## Size
        2 bytes

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4E])


class RunStarPieceSequence(UsableEventScriptCommand, EventScriptCommand):
    """Run a star piece collection cutscene.

    ## Lazy Shell command
        `Run star piece sequence...`

    ## Opcode
        `0xFD 0x4D`

    ## Size
        3 bytes

    Args:
        star (int): The specific star piece to collect.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = bytearray([0xFD, 0x4D])
    _size: int = 3
    _star: UInt8

    @property
    def star(self) -> UInt8:
        """The specific star piece to collect."""
        return self._star

    def set_star(self, star: int) -> None:
        """Choose the specific star piece to collect (1-7, 8 is valid for game ending)."""
        assert 1 <= star <= 8
        self._star = UInt8(star)

    def __init__(self, star: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_star(star)

    def render(self, *args) -> bytearray:
        return super().render(self.star)


class StartBattleAtBattlefield(UsableEventScriptCommand, EventScriptCommand):
    """Enter into a battle with a given pack ID and battlefield.
    It is recommended to use pack ID constant names for this.

    ## Lazy Shell command
        `Engage in battle with pack {xx}...`

    ## Opcode
        `0x4A`

    ## Size
        4 bytes

    Args:
        pack_id (int): The ID of the pack to fight.
        battlefield (Battlefield): The battlefield on which the battle should take place.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4A
    _pack_id: UInt8
    _battlefield: Battlefield
    _size = 4

    @property
    def pack_id(self) -> UInt8:
        """The ID of the pack to fight."""
        return self._pack_id

    def set_pack_id(self, pack_id: int) -> None:
        """Set the ID of the pack to fight.\n
        It is recommended to use pack ID constant names for this."""
        self._pack_id = UInt8(pack_id)

    @property
    def battlefield(self) -> Battlefield:
        """The battlefield on which the battle should take place."""
        return self._battlefield

    def set_battlefield(self, battlefield: Battlefield) -> None:
        """The battlefield on which the battle should take place."""
        assert 0 <= battlefield <= 25 or 28 <= battlefield <= 51
        self._battlefield = battlefield

    def __init__(
        self, pack_id: int, battlefield: Battlefield, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_pack_id(pack_id)
        self.set_battlefield(battlefield)

    def render(self, *args) -> bytearray:
        return super().render(UInt16(self.pack_id), self.battlefield)


class StartBattleWithPackAt700E(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Initiates a battle on the default battlefield associated to the current level against the pack ID matching the current value of $700E.

    ## Lazy Shell command
        `Engage in battle with pack @ $700E`

    ## Opcode
        `0x49`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x49
