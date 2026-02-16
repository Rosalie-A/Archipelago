"""Base classes supporting battle animation script assembly."""

from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptCommand,
    ScriptCommandNoArgs,
    ScriptCommandWithJmps,
)
from smrpgpatchbuilder.datatypes.numbers.classes import Int16, UInt16, UInt8
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.types import Origin

class AnimationScriptCommand(ScriptCommand):
    """Base class that all animation script command classes inherit from."""

    def verify_position(self, position: int) -> None:
        """Issues a warning if commands labeled as queuestart are not at their intended address."""
        if "queuestart_" in self.identifier.label:
            chunks = "_".split(self.identifier.label)
            if len(chunks) == 2:
                try:
                    expected_addr: int = int(chunks[1], 16)
                    # Silently track address changes
                    _ = expected_addr != position
                except ValueError:
                    pass

class AnimationScriptCommandNoArgs(AnimationScriptCommand, ScriptCommandNoArgs):
    """Base class of animation script command classes that take no arguments."""

class AnimationScriptCommandWithJmps(AnimationScriptCommand, ScriptCommandWithJmps):
    """Base class of animation script command classes that use gotos."""

class AnimationScriptAMEMCommand(AnimationScriptCommand):
    """Base class of animation script command classes that target AMEM."""

    _amem: UInt8

    @property
    def amem(self) -> UInt8:
        """AMEM target address in range $60-$6F"""
        return self._amem

    def set_amem(self, amem: int) -> None:
        """Set AMEM target address from 0x60 to 0x6F"""
        assert 0x60 <= amem <= 0x6F
        self._amem = UInt8(amem)

    def _amem_bits(self) -> int:
        return self.amem & 0x0F

class AnimationScriptAMEM6XSoloCommand(AnimationScriptAMEMCommand):
    """base class of animation script command classes that target amem $6x
    and take no other arguments."""

    _size: int = 2

    def __init__(self, amem: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits())

class AnimationScriptAMEM6XCommand(AnimationScriptAMEMCommand):
    """Base class of animation script command classes that target AMEM $6X."""

    _size: int = 4

class AnimationScriptAMEMAndConst(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a constant value."""

    _value: UInt16

    @property
    def value(self) -> UInt16:
        """The const value to perform the AND operation against"""
        return self._value

    def set_value(self, value: int) -> None:
        """Set the const value to perform the AND operation against"""
        self._value = UInt16(value)

class AnimationScriptAMEMAnd7E(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a value stored at $7Exxxx."""

    _address: int

    @property
    def address(self) -> int:
        """The address containing the value to perform the AND operation against, $7Exxxx"""
        return self._address

    def set_address(self, address: int) -> None:
        """Set the address containing the value to perform the AND operation against, $7Exxxx"""
        assert 0x7E0000 <= address <= 0x7EFFFF
        self._address = address

class AnimationScriptAMEMAnd7F(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a value stored at $7Fxxxx."""

    _address: int

    @property
    def address(self) -> int:
        """The address containing the value to perform the AND operation against, $7Fxxxx"""
        return self._address

    def set_address(self, address: int) -> None:
        """Set the address containing the value to perform the AND operation against, $7Fxxxx"""
        assert 0x7F0000 <= address <= 0x7FFFFF
        self._address = address

class AnimationScriptAMEMAndAMEM(AnimationScriptAMEM6XCommand):
    """perform an and operation between an amem in range $60-$6f
    and another AMEM in range $60-$6F."""

    _source_amem: UInt8
    _upper: UInt8

    @property
    def upper(self) -> UInt8:
        """The optional upper bits on the source amem"""
        return self._upper

    def set_upper(self, upper: int) -> None:
        """Set the optional upper bits on the source amem"""
        self._upper = UInt8(upper)

    @property
    def source_amem(self) -> UInt8:
        """The AMEM in range $60-$6F being compared against"""
        return self._source_amem

    def set_source_amem(self, amem: int) -> None:
        """Set the AMEM in range $60-$6F being compared against"""
        assert 0x60 <= amem <= 0x6F
        self._source_amem = UInt8(amem)

class AnimationScriptAMEMAndOMEM(AnimationScriptAMEM6XCommand):
    """perform an and operation between an amem in range $60-$6f
    and the value at an OMEM address."""

    _omem: UInt8

    @property
    def omem(self) -> UInt8:
        """The OMEM address being compared against"""
        return self._omem

    def set_omem(self, omem: int) -> None:
        """Set the OMEM address being compared against"""
        self._omem = UInt8(omem)

class AnimationScriptUnknownJmp2X(AnimationScriptCommandWithJmps):
    """Performs a Goto. Context of other parameters is unknown."""

    _size: int = 6

    _param_1: UInt8
    _param_2: UInt16

    @property
    def param_1(self) -> UInt8:
        """Unknown argument"""
        return self._param_1

    def set_param_1(self, param_1: int) -> None:
        """Set value of unknown argument"""
        self._param_1 = UInt8(param_1)

    @property
    def param_2(self) -> UInt16:
        """Unknown argument"""
        return self._param_2

    def set_param_2(self, param_2: int) -> None:
        self._param_2 = UInt16(param_2)

    def __init__(
        self,
        param_1: int,
        param_2: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_param_1(param_1)
        self.set_param_2(param_2)

    def render(self, *args) -> bytearray:
        return super().render(self.param_1, self.param_2, *self.destinations)

class SetAMEMToXYZCoords(AnimationScriptCommand):
    """Stores coordinates relative to a given origin to AMEM."""

    _size: int = 8

    _origin: Origin
    _x: Int16
    _y: Int16
    _z: Int16
    _do_set_x: bool
    _do_set_y: bool
    _do_set_z: bool

    @property
    def origin(self) -> Origin:
        """The point at which the x-y-z coords are relative to."""
        return self._origin

    def set_origin(self, origin: Origin) -> None:
        """Set the point at which the x-y-z coords are relative to."""
        self._origin = origin

    @property
    def x(self) -> Int16:
        """Relative X coord."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set relative X coord."""
        self._x = Int16(x)

    @property
    def y(self) -> Int16:
        """Relative Y coord."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set relative Y coord."""
        self._y = Int16(y)

    @property
    def z(self) -> Int16:
        """Relative Z coord."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set relative Z coord."""
        self._z = Int16(z)

    @property
    def do_set_x(self) -> bool:
        """X coord will only be committed to AMEM if this is set to true."""
        return self._do_set_x

    def set_do_set_x(self, do_set_x: bool) -> None:
        """Set whether or not the X coord should be committed to AMEM."""
        self._do_set_x = do_set_x

    @property
    def do_set_y(self) -> bool:
        """Y coord will only be committed to AMEM if this is set to true."""
        return self._do_set_y

    def set_do_set_y(self, do_set_y: bool) -> None:
        """Set whether or not the Y coord should be committed to AMEM."""
        self._do_set_y = do_set_y

    @property
    def do_set_z(self) -> bool:
        """Z coord will only be committed to AMEM if this is set to true."""
        return self._do_set_z

    def set_do_set_z(self, do_set_z: bool) -> None:
        """Set whether or not the Z coord should be committed to AMEM."""
        self._do_set_z = do_set_z

    def __init__(
        self,
        origin: Origin,
        x: int,
        y: int,
        z: int,
        set_x: bool = False,
        set_y: bool = False,
        set_z: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_origin(origin)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_do_set_x(set_x)
        self.set_do_set_y(set_y)
        self.set_do_set_z(set_z)

    def render(self, *args) -> bytearray:
        byte1 = (
            (self.origin << 4)
            + (self.do_set_x * 0x01)
            + (self.do_set_y * 0x02)
            + (self.do_set_z * 0x04)
        )
        return super().render(byte1, self.x, self.y, self.z)

class AnimationScriptFadeObject(AnimationScriptCommand):
    """Base class for commands that fade objects."""

    _opcode = 0x85
    _size: int = 3

    _duration: UInt8

    @property
    def duration(self) -> UInt8:
        """Fade duration in frames."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set fade duration, in frames."""
        self._duration = UInt8(duration)

    def __init__(self, duration: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_duration(duration)

class AnimationScriptShakeObject(AnimationScriptCommand):
    """Base class for commands that shake objects."""

    _opcode = 0x86
    _size: int = 7

    _amount: UInt8
    _speed: UInt16

    @property
    def amount(self) -> UInt8:
        """Number of shakes."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set number of shakes."""
        self._amount = UInt8(amount)

    @property
    def speed(self) -> UInt16:
        """Shake speed."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set shake speed."""
        self._speed = UInt16(speed)

    def __init__(
        self, amount: int, speed: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amount(amount)
        self.set_speed(speed)

    def render(self, *args) -> bytearray:
        header = args[0]
        return super().render(header, 0, 0, self.amount, self.speed)

class AnimationScriptCommandInventory(AnimationScriptCommand):
    """Base class for commands that act on an inventory item."""

    _size: int = 3

    _item_id: UInt8

    @property
    def item_id(self) -> UInt8:
        """Item ID."""
        return self._item_id

    def set_item_id(self, item: type[Item]) -> None:
        """Set item ID."""
        assert issubclass(item, Item)
        self._item_id = UInt8(item().item_id)

    def __init__(self, item: type[Item], identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_item_id(item)

class UsableAnimationScriptCommand(AnimationScriptCommand):
    """subclass for commands that can actually be used in a script
    (no prototypes)."""
