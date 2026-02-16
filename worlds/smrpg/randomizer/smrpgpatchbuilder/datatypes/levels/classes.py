from smrpgpatchbuilder.datatypes.numbers.classes import Int8, UInt16, UInt4, UInt8
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject, Direction
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import SOUTHWEST
from enum import IntEnum
from typing import TypeVar, Generic

class VramStore(IntEnum):
    """Defines how many directions an NPC will be allowed to face.\n
    For example, a NPC with only SWSE who tries to face north will
    simply have its south-facing sprites (sequence 0) loaded instead,
    but an NPC with SWSE/NWSE will actually be able to use its north-facing
    sprites (sequence 1) when it faces north.\n
    It is generally better to support as few directions as necessary for a NPC.
    There is no real use loading NWNE molds into VRAM for a NPC who you don't expect
    to face north in that room."""

    DIR0_SWSE_NWNE = 0
    DIR1_SWSE_NWNE_S = 1
    DIR2_SWSE = 2
    DIR3_SWSE_NWNE = 3
    DIR4_ALL_DIRECTIONS = 4
    DIR5_UNKNOWN = 5
    DIR6_UNKNOWN = 6
    DIR7_ALL_DIRECTIONS = 7

class ShadowSize(IntEnum):
    """The different shadow shapes available for any NPC."""

    OVAL_SMALL = 0
    OVAL_MED = 1
    OVAL_BIG = 2
    BLOCK = 3

class ObjectType(IntEnum):
    """Enum of NPC subtypes that control what properties they should have
    in the ROM."""

    OBJECT = 0
    CHEST = 1
    BATTLE = 2

class EventInitiator(IntEnum):
    """Enum of the rules by which an NPC can have its interaction triggered."""

    NONE = 0x0
    PRESS_A_FROM_ANY_SIDE = 0x1
    PRESS_A_FROM_FRONT = 0x2
    ANYTHING_EXCEPT_TOUCH_SIDE = 0x3
    PRESS_A_OR_TOUCH_ANY_SIDE = 0x4
    PRESS_A_OR_TOUCH_FRONT = 0x5
    DO_ANYTHING = 0x6
    HIT_FROM_BELOW = 0x7
    JUMP_ON = 0x8
    JUMP_ON_OR_HIT_FROM_BELOW = 0x9
    TOUCH_ANY_SIDE = 0xA
    TOUCH_FROM_FRONT = 0xB
    ANYTHING_EXCEPT_PRESS_A = 0xC

class PostBattleBehaviour(IntEnum):
    """Enum of the ways NPCs should behave in the overworld after defeated in battle"""

    REMOVE_PERMANENTLY = 0x0
    REMOVE_UNTIL_RELOAD = 0x1
    DO_NOT_REMOVE = 0x2
    REMOVE_PERMANENTLY_NO_IFRAME_COLLISION = 0x3
    REMOVE_UNTIL_RELOAD_NO_IFRAME_COLLISION = 0x4
    UNKNOWN = 0x08

class EdgeDirection(IntEnum):
    """Enum of directions an event or exit tile can face"""

    SOUTHEAST = 0x00
    SOUTHWEST = 0x01

class ExitType(IntEnum):
    """Enum of room exit types"""

    ROOM = 0x00
    MAP_LOCATION = 0x01

class BufferType(IntEnum):
    """Enum of partition buffer types"""

    THREE_SPRITES_PER_ROW = 0x00
    FOUR_SPRITES_PER_ROW = 0x01
    TREASURE_CHEST = 0x02
    EMPTY_TREASURE_CHEST = 0x03
    COINS = 0x04
    EMPTY_1 = 0x05
    EMPTY_2 = 0x06
    EMPTY_3 = 0x07

class BufferSpace(IntEnum):
    """Enum of partition buffer sizes"""

    BYTES_0 = 0x00
    BYTES_256 = 0x01
    BYTES_512 = 0x02
    BYTES_768 = 0x03
    BYTES_1024 = 0x04
    BYTES_1280 = 0x05
    BYTES_1536 = 0x06
    BYTES_1792 = 0x07

class Buffer:
    """Partition buffer, controls how sprites are loaded. Three to a partition"""

    _buffer_type: BufferType = BufferType.EMPTY_3
    _main_buffer_space: BufferSpace = BufferSpace.BYTES_0
    _index_in_main_buffer: bool = True

    @property
    def buffer_type(self) -> BufferType:
        """Buffer type"""
        return self._buffer_type

    def set_buffer_type(self, buffer_type: BufferType) -> None:
        """Set buffer type"""
        self._buffer_type = buffer_type

    @property
    def main_buffer_space(self) -> BufferSpace:
        """Buffer size"""
        return self._main_buffer_space

    def set_main_buffer_space(self, main_buffer_space: BufferSpace) -> None:
        """Set buffer size"""
        self._main_buffer_space = main_buffer_space

    @property
    def index_in_main_buffer(self) -> bool:
        """(unknown)"""
        return self._index_in_main_buffer

    def set_index_in_main_buffer(self, index_in_main_buffer: bool) -> None:
        """(unknown)"""
        self._index_in_main_buffer = index_in_main_buffer

    def __init__(
        self,
        buffer_type=BufferType.EMPTY_3,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True,
    ) -> None:
        self.set_buffer_type(buffer_type)
        self.set_main_buffer_space(main_buffer_space)
        self.set_index_in_main_buffer(index_in_main_buffer)

    def __str__(self) -> str:
        return (
            f"{self.buffer_type}, {self.main_buffer_space}, {self.index_in_main_buffer}"
        )

    def is_same(self, buffer: "Buffer") -> bool:
        """Compares this buffer to another buffer and returns true if all properties
        are the same."""
        return (
            self.buffer_type == buffer.buffer_type
            and self.main_buffer_space == buffer.main_buffer_space
            and self.index_in_main_buffer == buffer.index_in_main_buffer
        )

class Partition:
    """Determines how NPC sprites within the room are loaded into VRAM"""

    _ally_sprite_buffer_size: UInt4 = UInt4(1)
    _allow_extra_sprite_buffer: bool = False
    _extra_sprite_buffer_size: UInt4 = UInt4(0)
    _buffers: list[Buffer] = []
    _full_palette_buffer: bool = True

    @property
    def ally_sprite_buffer_size(self) -> UInt4:
        """The expected max size you will need for any action you expect
        your player character to take. Calculated the same way as NPC
        vram size: 0 if you only expect gridplanes, otherwise
        floor(max # of tiles in your sprite / 4)."""
        return self._ally_sprite_buffer_size

    def set_ally_sprite_buffer_size(self, ally_sprite_buffer_size: int) -> None:
        """Set the expected max size you will need for any action you expect
        your player character to take. Calculated the same way as NPC
        vram size: 0 if you only expect gridplanes, otherwise
        floor(max # of tiles in your sprite / 4). \n
        Must be 3 or less."""
        assert ally_sprite_buffer_size <= 3
        self._ally_sprite_buffer_size = UInt4(ally_sprite_buffer_size)

    @property
    def allow_extra_sprite_buffer(self) -> bool:
        """Set this to true if you expect a packet to be created at any time."""
        return self._allow_extra_sprite_buffer

    def set_allow_extra_sprite_buffer(self, allow_extra_sprite_buffer: bool) -> None:
        """Set this to true if you expect a packet to be created at any time."""
        self._allow_extra_sprite_buffer = allow_extra_sprite_buffer

    @property
    def extra_sprite_buffer_size(self) -> UInt4:
        """The max number of packets you expect to be active at any given time."""
        return self._extra_sprite_buffer_size

    def set_extra_sprite_buffer_size(self, extra_sprite_buffer_size: int) -> None:
        """Set the max number of packets you expect to be active at any given time."""
        self._extra_sprite_buffer_size = UInt4(extra_sprite_buffer_size)

    @property
    def buffers(self) -> list[Buffer]:
        """Buffers define the ways in which NPC sprites are loaded into vram."""
        assert len(self._buffers) == 3
        return self._buffers

    def set_buffers(self, buffers: list[Buffer]) -> None:
        """Buffers define the ways in which NPC sprites are loaded into vram."""
        assert len(buffers) == 3
        self._buffers = buffers

    @property
    def full_palette_buffer(self) -> bool:
        """(unknown)"""
        return self._full_palette_buffer

    def set_full_palette_buffer(self, full_palette_buffer: bool) -> None:
        """(unknown)"""
        self._full_palette_buffer = full_palette_buffer

    def __init__(
        self,
        ally_sprite_buffer_size: int = 1,
        allow_extra_sprite_buffer: bool = False,
        extra_sprite_buffer_size: int = 0,
        buffers: list[Buffer] | None = None,
        full_palette_buffer: bool = True,
    ) -> None:
        if buffers is None:
            buffers = [Buffer(), Buffer(), Buffer()]
        self.set_ally_sprite_buffer_size(ally_sprite_buffer_size)
        self.set_allow_extra_sprite_buffer(allow_extra_sprite_buffer)
        self.set_extra_sprite_buffer_size(extra_sprite_buffer_size)
        self.set_buffers(buffers)
        self.set_full_palette_buffer(full_palette_buffer)

    def __str__(self):
        buf_str = ";".join([b.__str__() for b in self.buffers])
        return (
            f"ally: {self.ally_sprite_buffer_size}, "
            f"packet: {self.allow_extra_sprite_buffer}, "
            f"{self.extra_sprite_buffer_size}, "
            f"buffers: {buf_str}, "
            f"full: {self.full_palette_buffer}"
        )

    def is_same(self, partition: "Partition"):
        """Determines if this partition's properties are all the same as another one's."""
        return (
            self.ally_sprite_buffer_size == partition.ally_sprite_buffer_size
            and self.allow_extra_sprite_buffer == partition.allow_extra_sprite_buffer
            and self.extra_sprite_buffer_size == partition.extra_sprite_buffer_size
            and self.buffers[0].is_same(partition.buffers[0])
            and self.buffers[1].is_same(partition.buffers[1])
            and self.buffers[2].is_same(partition.buffers[2])
            and self.full_palette_buffer == partition.full_palette_buffer
        )

    def is_similar_but_larger_packet_buffer(self, partition: "Partition"):
        """Determines if this partition's properties are all the same as another one's,
        except for having a larger packet buffer."""
        return (
            self.ally_sprite_buffer_size == partition.ally_sprite_buffer_size
            and self.allow_extra_sprite_buffer
            and partition.allow_extra_sprite_buffer
            and self.extra_sprite_buffer_size > partition.extra_sprite_buffer_size
            and self.extra_sprite_buffer_size <= 2
            and self.buffers[0].is_same(partition.buffers[0])
            and self.buffers[1].is_same(partition.buffers[1])
            and self.buffers[2].is_same(partition.buffers[2])
            and self.full_palette_buffer == partition.full_palette_buffer
        )

class DestinationProps:
    """Params that need to be set for a level being loaded via an exit tile."""

    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _z_half: bool = False
    _f: Direction = SOUTHWEST
    _x_bit_7: bool = False

    @property
    def x(self) -> UInt8:
        """The X coord at which the player will be positioned when the destination loads."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coord at which the player will be positioned when the destination loads."""
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coord at which the player will be positioned when the destination loads."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the X coord at which the player will be positioned when the destination loads.\n
        Must be 0-127."""
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coord at which the player will be positioned when the destination loads."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the X coord at which the player will be positioned when the destination loads.\n
        Must be 0-31."""
        assert z <= 31
        self._z = UInt8(z)

    @property
    def z_half(self) -> bool:
        """If true, adds half a unit to the player's starting Z coordinate."""
        return self._z_half

    def set_z_half(self, z_half: bool) -> None:
        """If true, adds half a unit to the player's starting Z coordinate."""
        self._z_half = z_half

    @property
    def f(self) -> Direction:
        """The direction that the player will face when the room loads."""
        return self._f

    def set_f(self, f: Direction) -> None:
        """Choose the direction that the player will face when the room loads."""
        self._f = f

    @property
    def x_bit_7(self) -> bool:
        """(unknown)"""
        return self._x_bit_7

    def set_x_bit_7(self, x_bit_7: bool) -> None:
        """(unknown)"""
        self._x_bit_7 = x_bit_7

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        f: Direction = SOUTHWEST,
        x_bit_7: bool = False,
    ) -> None:
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_z_half(z_half)
        self.set_f(f)
        self.set_x_bit_7(x_bit_7)

class Exit:
    """A tile that exits to either another level or to a dot on the world map."""

    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _f: EdgeDirection
    _length: UInt8 = UInt8(0)
    _height: UInt4 = UInt4(0)
    _nw_se_edge_active: bool = True
    _ne_sw_edge_active: bool = False
    _destination_type: ExitType = ExitType.ROOM
    _byte_2_bit_2: bool = False
    _destination: UInt8 | UInt16
    _show_message: bool = False
    _destination_props: DestinationProps

    @property
    def x(self) -> UInt8:
        """The X coord at which to place the tile."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coord (0-63) at which to place the tile."""
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coord at which to place the tile."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord (0-127) at which to place the tile."""
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coord at which to place the tile."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coord (0-31) at which to place the tile."""
        assert z <= 31
        self._z = UInt8(z)

    @property
    def f(self) -> EdgeDirection:
        """The orientation of the tile."""
        return self._f

    def set_f(self, f: EdgeDirection) -> None:
        """Set the orientation of the tile."""
        self._f = f

    @property
    def length(self) -> UInt8:
        """The number of standard-sized tiles in a row this exit should encompass."""
        return self._length

    def set_length(self, length: int) -> None:
        """Set the number of standard-sized tiles (0-16) in a row this exit should encompass."""
        assert 1 <= length <= 16
        self._length = UInt8(length)

    @property
    def height(self) -> UInt4:
        """If >0, the exit can be triggered at any Z coordinate instead of just stepping on it."""
        return self._height

    def set_height(self, height: int) -> None:
        """If >0, the exit can be triggered at any Z coordinate instead of just stepping on it.\n
        Must be <= 7."""
        assert height <= 7
        self._height = UInt4(height)

    @property
    def nw_se_edge_active(self) -> bool:
        """If true, the NW/SE diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        return self._nw_se_edge_active

    def set_nw_se_edge_active(self, nw_se_edge_active: bool) -> None:
        """If true, the NW/SE diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        self._nw_se_edge_active = nw_se_edge_active

    @property
    def ne_sw_edge_active(self) -> bool:
        """If true, the NE/SW diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        return self._ne_sw_edge_active

    def set_ne_sw_edge_active(self, ne_sw_edge_active: bool) -> None:
        """If true, the NE/SW diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        self._ne_sw_edge_active = ne_sw_edge_active

    @property
    def destination_type(self) -> ExitType:
        """Determines if this exit loads a room, or the world map."""
        return self._destination_type

    def set_destination_type(self, destination_type: ExitType) -> None:
        """Determine if this exit loads a room, or the world map."""
        self._destination_type = destination_type

    @property
    def byte_2_bit_2(self) -> bool:
        """(unknown)"""
        return self._byte_2_bit_2

    def set_byte_2_bit_2(self, byte_2_bit_2: bool) -> None:
        """(unknown)"""
        self._byte_2_bit_2 = byte_2_bit_2

    @property
    def show_message(self) -> bool:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        return self._show_message

    def set_show_message(self, show_message: bool) -> None:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        self._show_message = show_message

    @property
    def destination_props(self) -> DestinationProps:
        """A set of properties controlling the player's positioning when the destination room
        loads."""
        return self._destination_props

    def set_destination_props(self, destination_props: DestinationProps) -> None:
        """Replace the set of properties controlling the player's positioning when the
        destination room loads."""
        self._destination_props = destination_props

ExitT = TypeVar("ExitT", bound=Exit)

class RoomExit(Exit):
    """Exit tiles that specifically launch another room instead of the world map.\n
    It is recommended to use room ID constant names for this."""

    _destination_type = ExitType.ROOM

    @property
    def destination(self) -> UInt16:
        """The ID of the room to load."""
        return UInt16(self._destination)

    def set_destination(self, destination: int) -> None:
        """Set the ID of the room to load.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= destination < 510
        self._destination = UInt16(destination)

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        f: EdgeDirection = EdgeDirection.SOUTHWEST,
        length: int = 2,
        height: int = 0,
        nw_se_edge_active: bool = True,
        ne_sw_edge_active: bool = False,
        byte_2_bit_2: bool = False,
        destination: int = 0,
        show_message: bool = False,
        dst_x: int = 0,
        dst_y: int = 0,
        dst_z: int = 0,
        dst_z_half: bool = False,
        dst_f: Direction = SOUTHWEST,
        x_bit_7: bool = False,
    ) -> None:
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_f(f)
        super().set_length(length)
        super().set_height(height)
        super().set_nw_se_edge_active(nw_se_edge_active)
        super().set_ne_sw_edge_active(ne_sw_edge_active)
        super().set_byte_2_bit_2(byte_2_bit_2)
        self.set_destination(destination)
        super().set_show_message(show_message)
        props = DestinationProps(
            x=dst_x, y=dst_y, z=dst_z, z_half=dst_z_half, f=dst_f, x_bit_7=x_bit_7
        )
        super().set_destination_props(props)

class MapExit(Exit):
    """Exit tiles that specifically launch the world map instead of another room\n
    It is recommended to use overworld location ID constant names for this."""

    _destination_type: ExitType = ExitType.MAP_LOCATION
    _byte_2_bit_1: bool = False
    _byte_2_bit_0: bool = False

    @property
    def destination(self) -> UInt8:
        """The world map dot to return to."""
        return UInt8(self._destination)

    def set_destination(self, destination: int) -> None:
        """Set the world map dot to return to.\n
        It is recommended to use overworld location ID constant names for this."""
        assert 0 <= destination < 56
        self._destination = UInt8(destination)

    @property
    def byte_2_bit_1(self) -> bool:
        """(unknown)"""
        return self._byte_2_bit_1

    def set_byte_2_bit_1(self, byte_2_bit_1: bool) -> None:
        """(unknown)"""
        self._byte_2_bit_1 = byte_2_bit_1

    @property
    def byte_2_bit_0(self) -> bool:
        """(unknown)"""
        return self._byte_2_bit_0

    def set_byte_2_bit_0(self, byte_2_bit_0: bool) -> None:
        """(unknown)"""
        self._byte_2_bit_0 = byte_2_bit_0

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        f: EdgeDirection = EdgeDirection.SOUTHWEST,
        length: int = 2,
        height: int = 0,
        nw_se_edge_active: bool = True,
        ne_sw_edge_active: bool = False,
        byte_2_bit_2: bool = False,
        destination: int = 0,
        show_message: bool = False,
        byte_2_bit_1: bool = False,
        byte_2_bit_0: bool = False,
    ) -> None:
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_f(f)
        super().set_length(length)
        super().set_height(height)
        super().set_nw_se_edge_active(nw_se_edge_active)
        super().set_ne_sw_edge_active(ne_sw_edge_active)
        super().set_byte_2_bit_2(byte_2_bit_2)
        self.set_destination(destination)
        super().set_show_message(show_message)
        super().set_byte_2_bit_2(byte_2_bit_1)
        super().set_byte_2_bit_2(byte_2_bit_0)

class Event:
    """A tile that activates a specific event script.\n
    It is recommended to use event ID constant names for this."""

    _event: UInt16 = UInt16(0)
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _f: EdgeDirection = EdgeDirection.SOUTHWEST
    _length: UInt8 = UInt8(1)
    _height: UInt4 = UInt4(0)
    _nw_se_edge_active: bool = True
    _ne_sw_edge_active: bool = False
    _byte_8_bit_4: bool = False

    @property
    def event(self) -> UInt16:
        """The ID of the event that this tile launches."""
        return self._event

    def set_event(self, event: int) -> None:
        """Set the ID of the event that this tile launches.\n
        It is recommended to use event ID constant names for this."""
        assert 0 <= event < 4096
        self._event = UInt16(event)

    @property
    def x(self) -> UInt8:
        """The X coord at which to place the tile."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coord (0-63) at which to place the tile."""
        assert x <= 63
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coord at which to place the tile."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord (0-127) at which to place the tile."""
        assert y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coord at which to place the tile."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coord (0-31) at which to place the tile."""
        assert z <= 31
        self._z = UInt8(z)

    @property
    def f(self) -> EdgeDirection:
        """The orientation of the tile."""
        return self._f

    def set_f(self, f: EdgeDirection) -> None:
        """Set the orientation of the tile."""
        self._f = f

    @property
    def length(self) -> UInt8:
        """The number of standard-sized tiles in a row this exit should encompass."""
        return self._length

    def set_length(self, length: int) -> None:
        """Set the number of standard-sized tiles (0-16) in a row this exit should encompass."""
        assert 1 <= length <= 16
        self._length = UInt8(length)

    @property
    def height(self) -> UInt4:
        """If >0, the exit can be triggered at any Z coordinate instead of just stepping on it."""
        return self._height

    def set_height(self, height: int) -> None:
        """If >0, the exit can be triggered at any Z coordinate instead of just stepping on it.\n
        Must be <= 7."""
        assert height <= 7
        self._height = UInt4(height)

    @property
    def nw_se_edge_active(self) -> bool:
        """If true, the NW/SE diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        return self._nw_se_edge_active

    def set_nw_se_edge_active(self, nw_se_edge_active: bool) -> None:
        """If true, the NW/SE diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        self._nw_se_edge_active = nw_se_edge_active

    @property
    def ne_sw_edge_active(self) -> bool:
        """If true, the NE/SW diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        return self._ne_sw_edge_active

    def set_ne_sw_edge_active(self, ne_sw_edge_active: bool) -> None:
        """If true, the NE/SW diagonal edge is the edge from which you can enter the exit tile
        to trigger it."""
        self._ne_sw_edge_active = ne_sw_edge_active

    @property
    def byte_8_bit_4(self) -> bool:
        """(unknown)"""
        return self._byte_8_bit_4

    def set_byte_8_bit_4(self, byte_8_bit_4: bool) -> None:
        """(unknown)"""
        self._byte_8_bit_4 = byte_8_bit_4

    def __init__(
        self,
        event: int,
        x: int,
        y: int,
        z: int,
        f: EdgeDirection,
        length: int,
        height: int,
        nw_se_edge_active: bool,
        ne_sw_edge_active: bool,
        byte_8_bit_4: bool,
    ) -> None:
        self.set_event(event)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_f(f)
        self.set_length(length)
        self.set_height(height)
        self.set_nw_se_edge_active(nw_se_edge_active)
        self.set_ne_sw_edge_active(ne_sw_edge_active)
        self.set_byte_8_bit_4(byte_8_bit_4)

class NPC:
    """Base class for any object that can occupy an NPC placeholder.
    These properties are generally for things that should always be true
    about a given character, such as their collision height, shadow size,
    vram size, etc. Some of these properties can be overridden according
    to the needs of a specific room, so they are not 100% absolute."""

    _sprite_id: UInt16 = UInt16(1023)
    _priority_0: bool = False
    _priority_1: bool = False
    _priority_2: bool = True
    _show_shadow: bool = True
    _shadow_size = ShadowSize.OVAL_MED
    _y_shift: Int8 = Int8(0)
    _acute_axis: UInt4 = UInt4(1)
    _obtuse_axis: UInt4 = UInt4(1)
    _height: UInt8 = UInt8(1)
    _directions: VramStore = VramStore.DIR2_SWSE
    _min_vram_size: int = 0
    _cannot_clone: bool = False

    _byte2_bit0: bool = False
    _byte2_bit1: bool = False
    _byte2_bit2: bool = False
    _byte2_bit3: bool = False
    _byte2_bit4: bool = False
    _byte5_bit6: bool = False
    _byte5_bit7: bool = False
    _byte6_bit2: bool = False

    @property
    def sprite_id(self) -> UInt16:
        """The ID of the sprite that will be loaded into the room for this NPC.\n
        It is recommended to use sprite constant names for this."""
        assert self._sprite_id <= 1023
        return UInt16(self._sprite_id)

    @property
    def shadow_size(self) -> ShadowSize:
        """The size of the NPC's displayed shadow when airborne."""
        return self._shadow_size

    @property
    def acute_axis(self) -> UInt4:
        """The collision width of this NPC.
        If projected onto a flat plane, this axis would run top right to bottom left."""
        return UInt4(self._acute_axis)

    @property
    def obtuse_axis(self) -> UInt4:
        """The collision length of this NPC.
        If projected onto a flat plane, this axis would run top left to bottom right."""
        return UInt4(self._obtuse_axis)

    @property
    def height(self) -> UInt8:
        """The collision height of this NPC."""
        assert self._height <= 31
        return UInt8(self._height)

    @property
    def y_shift(self) -> Int8:
        """The distance in pixels (from -16 to +15) to shift the sprite up or down
        as displayed, without also moving its collision box."""
        assert -16 <= self._y_shift <= 15
        return Int8(self._y_shift)

    @property
    def show_shadow(self) -> bool:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM."""
        return self._show_shadow

    @property
    def byte2_bit0(self) -> bool:
        """(unknown)"""
        return self._byte2_bit0

    @property
    def byte2_bit1(self) -> bool:
        """(unknown)"""
        return self._byte2_bit1

    @property
    def byte2_bit2(self) -> bool:
        """(unknown)"""
        return self._byte2_bit2

    @property
    def byte2_bit3(self) -> bool:
        """(unknown)"""
        return self._byte2_bit3

    @property
    def byte2_bit4(self) -> bool:
        """(unknown)"""
        return self._byte2_bit4

    @property
    def byte5_bit6(self) -> bool:
        """(unknown)"""
        return self._byte5_bit6

    @property
    def byte5_bit7(self) -> bool:
        """(unknown)"""
        return self._byte5_bit7

    @property
    def byte6_bit2(self) -> bool:
        """(unknown)"""
        return self._byte6_bit2

    @property
    def directions(self) -> VramStore:
        """The directions which the NPC can be expected to face."""
        return self._directions

    @property
    def min_vram_size(self) -> UInt4:
        """The minimum number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require.\n
        Generally, this number is 0 for gridplane sprites. \n
        For non-gridplane sprites, this number is usually total tiles divided by 4,
        rounded down (where a tile is a group of four subtiles).\n
        This calculation should be based on the largest mold (in terms of tiles used)
        that you expect to see displayed from the sprite."""
        assert self._min_vram_size <= 7
        return UInt4(self._min_vram_size)

    @property
    def priority_0(self) -> bool:
        """Priority bit 0 for sprite layering."""
        return self._priority_0

    @property
    def priority_1(self) -> bool:
        """Priority bit 1 for sprite layering."""
        return self._priority_1

    @property
    def priority_2(self) -> bool:
        """Priority bit 2 for sprite layering."""
        return self._priority_2

    @property
    def cannot_clone(self) -> bool:
        """If true, this NPC cannot be cloned."""
        return self._cannot_clone

    def set_sprite_id(self, sprite_id: int) -> None:
        """Set the ID of the sprite that will be loaded into the room for this NPC."""
        assert sprite_id <= 1023
        self._sprite_id = UInt16(sprite_id)

    def set_shadow_size(self, shadow_size: ShadowSize) -> None:
        """Set the size of the NPC's displayed shadow when airborne."""
        self._shadow_size = shadow_size

    def set_acute_axis(self, acute_axis: int) -> None:
        """Set the collision width of this NPC."""
        self._acute_axis = UInt4(acute_axis)

    def set_obtuse_axis(self, obtuse_axis: int) -> None:
        """Set the collision length of this NPC."""
        self._obtuse_axis = UInt4(obtuse_axis)

    def set_height(self, height: int) -> None:
        """Set the collision height of this NPC."""
        assert height <= 31
        self._height = UInt8(height)

    def set_y_shift(self, y_shift: int) -> None:
        """Set the distance in pixels (from -16 to +15) to shift the sprite up or down."""
        assert -16 <= y_shift <= 15
        self._y_shift = Int8(y_shift)

    def set_show_shadow(self, show_shadow: bool) -> None:
        """Set whether a shadow for the NPC when airborne will be loaded to VRAM."""
        self._show_shadow = show_shadow

    def set_byte2_bit0(self, byte2_bit0: bool) -> None:
        """(unknown)"""
        self._byte2_bit0 = byte2_bit0

    def set_byte2_bit1(self, byte2_bit1: bool) -> None:
        """(unknown)"""
        self._byte2_bit1 = byte2_bit1

    def set_byte2_bit2(self, byte2_bit2: bool) -> None:
        """(unknown)"""
        self._byte2_bit2 = byte2_bit2

    def set_byte2_bit3(self, byte2_bit3: bool) -> None:
        """(unknown)"""
        self._byte2_bit3 = byte2_bit3

    def set_byte2_bit4(self, byte2_bit4: bool) -> None:
        """(unknown)"""
        self._byte2_bit4 = byte2_bit4

    def set_byte5_bit6(self, byte5_bit6: bool) -> None:
        """(unknown)"""
        self._byte5_bit6 = byte5_bit6

    def set_byte5_bit7(self, byte5_bit7: bool) -> None:
        """(unknown)"""
        self._byte5_bit7 = byte5_bit7

    def set_byte6_bit2(self, byte6_bit2: bool) -> None:
        """(unknown)"""
        self._byte6_bit2 = byte6_bit2

    def set_directions(self, directions: VramStore) -> None:
        """Set the directions which the NPC can be expected to face."""
        self._directions = directions

    def set_min_vram_size(self, min_vram_size: int) -> None:
        """Set the minimum number (0 to 7) of VRAM chunks the NPC's sprite requires."""
        assert min_vram_size <= 7
        self._min_vram_size = min_vram_size

    def set_priority_0(self, priority_0: bool) -> None:
        """Set priority bit 0 for sprite layering."""
        self._priority_0 = priority_0

    def set_priority_1(self, priority_1: bool) -> None:
        """Set priority bit 1 for sprite layering."""
        self._priority_1 = priority_1

    def set_priority_2(self, priority_2: bool) -> None:
        """Set priority bit 2 for sprite layering."""
        self._priority_2 = priority_2

    def set_cannot_clone(self, cannot_clone: bool) -> None:
        """Set whether this NPC can be cloned."""
        self._cannot_clone = cannot_clone

    def __init__(self,
                 sprite_id: int = 1023,
                 shadow_size: ShadowSize = ShadowSize.OVAL_MED,
                 acute_axis: int = 1,
                 obtuse_axis: int = 1,
                 height: int = 1,
                 y_shift: int = 0,
                 show_shadow: bool = True,
                 directions: VramStore = VramStore.DIR2_SWSE,
                 min_vram_size: int = 0,
                 priority_0: bool = False,
                 priority_1: bool = False,
                 priority_2: bool = True,
                 cannot_clone: bool = False,
                 byte2_bit0: bool = False,
                 byte2_bit1: bool = False,
                 byte2_bit2: bool = False,
                 byte2_bit3: bool = False,
                 byte2_bit4: bool = False,
                 byte5_bit6: bool = False,
                 byte5_bit7: bool = False,
                 byte6_bit2: bool = False) -> None:
        self._sprite_id = UInt16(sprite_id)
        self._shadow_size = shadow_size
        self._acute_axis = UInt4(acute_axis)
        self._obtuse_axis = UInt4(obtuse_axis)
        self._height = UInt8(height)
        self._y_shift = Int8(y_shift)
        self._show_shadow = show_shadow
        self._directions = directions
        self._min_vram_size = min_vram_size
        self._priority_0 = priority_0
        self._priority_1 = priority_1
        self._priority_2 = priority_2
        self._cannot_clone = cannot_clone
        self._byte2_bit0 = byte2_bit0
        self._byte2_bit1 = byte2_bit1
        self._byte2_bit2 = byte2_bit2
        self._byte2_bit3 = byte2_bit3
        self._byte2_bit4 = byte2_bit4
        self._byte5_bit6 = byte5_bit6
        self._byte5_bit7 = byte5_bit7
        self._byte6_bit2 = byte6_bit2

class BaseRoomObject:
    """The base definition for a room NPC, including placement and
    interaction type. Some properties from the NPC editor are also here
    if they are more relevant to vram than character design."""

    _npc: NPC

    _object_id: AreaObject = NPC_0
    _object_type: ObjectType = ObjectType.OBJECT
    _visible: bool = False
    _x: UInt8 = UInt8(0)
    _y: UInt8 = UInt8(0)
    _z: UInt8 = UInt8(0)
    _z_half: bool = False
    _direction: Direction = SOUTHWEST

    # NPC properties that can be overridden at room level
    _show_shadow: bool | None = None
    _shadow_size: ShadowSize | None = None
    _y_shift: Int8 | None = None
    _acute_axis: UInt4 | None = None
    _obtuse_axis: UInt4 | None = None
    _height: UInt8 | None = None
    _directions: VramStore | None = None
    _min_vram_size: int | None = None
    _priority_0: bool | None = None
    _priority_1: bool | None = None
    _priority_2: bool | None = None
    _cannot_clone: bool | None = None

    # Unknown bit flags
    _byte2_bit0: bool | None = None
    _byte2_bit1: bool | None = None
    _byte2_bit2: bool | None = None
    _byte2_bit3: bool | None = None
    _byte2_bit4: bool | None = None
    _byte5_bit6: bool | None = None
    _byte5_bit7: bool | None = None
    _byte6_bit2: bool | None = None

    @property
    def shadow_size(self) -> ShadowSize | None:
        """The size of the NPC's displayed shadow when airborne."""
        return self._shadow_size

    @property
    def acute_axis(self) -> UInt4 | None:
        """The collision width of this NPC.
        If projected onto a flat plane, this axis would run top right to bottom left."""
        return UInt4(self._acute_axis) if self._acute_axis is not None else None

    @property
    def obtuse_axis(self) -> UInt4 | None:
        """The collision length of this NPC.
        If projected onto a flat plane, this axis would run top left to bottom right."""
        return UInt4(self._obtuse_axis) if self._obtuse_axis is not None else None

    @property
    def height(self) -> UInt8 | None:
        """The collision height of this NPC."""
        if self._height is not None:
            assert self._height <= 31
            return UInt8(self._height)
        return None

    @property
    def y_shift(self) -> Int8 | None:
        """The distance in pixels (from -16 to +15) to shift the sprite up or down
        as displayed, without also moving its collision box."""
        if self._y_shift is not None:
            assert -16 <= self._y_shift <= 15
            return Int8(self._y_shift)
        return None

    @property
    def show_shadow(self) -> bool | None:
        """If false, a shadow for the NPC when airborne will not be loaded to VRAM."""
        return self._show_shadow

    @property
    def byte2_bit0(self) -> bool | None:
        """(unknown)"""
        return self._byte2_bit0

    @property
    def byte2_bit1(self) -> bool | None:
        """(unknown)"""
        return self._byte2_bit1

    @property
    def byte2_bit2(self) -> bool | None:
        """(unknown)"""
        return self._byte2_bit2

    @property
    def byte2_bit3(self) -> bool | None:
        """(unknown)"""
        return self._byte2_bit3

    @property
    def byte2_bit4(self) -> bool | None:
        """(unknown)"""
        return self._byte2_bit4

    @property
    def byte5_bit6(self) -> bool | None:
        """(unknown)"""
        return self._byte5_bit6

    @property
    def byte5_bit7(self) -> bool | None:
        """(unknown)"""
        return self._byte5_bit7

    @property
    def byte6_bit2(self) -> bool | None:
        """(unknown)"""
        return self._byte6_bit2

    @property
    def directions(self) -> VramStore | None:
        """The directions which the NPC can be expected to face."""
        return self._directions

    @property
    def min_vram_size(self) -> UInt4 | None:
        """The minimum number (0 to 7) of VRAM chunks the NPC's sprite can be expected to require.\n
        Generally, this number is 0 for gridplane sprites. \n
        For non-gridplane sprites, this number is usually total tiles divided by 4,
        rounded down (where a tile is a group of four subtiles).\n
        This calculation should be based on the largest mold (in terms of tiles used)
        that you expect to see displayed from the sprite."""
        if self._min_vram_size is not None:
            assert self._min_vram_size <= 7
            return UInt4(self._min_vram_size)
        return None

    @property
    def priority_0(self) -> bool | None:
        """Priority bit 0 for sprite layering."""
        return self._priority_0

    @property
    def priority_1(self) -> bool | None:
        """Priority bit 1 for sprite layering."""
        return self._priority_1

    @property
    def priority_2(self) -> bool | None:
        """Priority bit 2 for sprite layering."""
        return self._priority_2

    @property
    def cannot_clone(self) -> bool | None:
        """If true, this NPC cannot be cloned."""
        return self._cannot_clone

    def set_sprite_id(self, sprite_id: int) -> None:
        """Set the ID of the sprite that will be loaded into the room for this NPC."""
        assert sprite_id <= 1023
        self._sprite_id = UInt16(sprite_id)

    def set_shadow_size(self, shadow_size: ShadowSize | None) -> None:
        """Set the size of the NPC's displayed shadow when airborne."""
        self._shadow_size = shadow_size

    def set_acute_axis(self, acute_axis: int | None) -> None:
        """Set the collision width of this NPC."""
        self._acute_axis = UInt4(acute_axis) if acute_axis is not None else None

    def set_obtuse_axis(self, obtuse_axis: int | None) -> None:
        """Set the collision length of this NPC."""
        self._obtuse_axis = UInt4(obtuse_axis) if obtuse_axis is not None else None

    def set_height(self, height: int | None) -> None:
        """Set the collision height of this NPC."""
        if height is not None:
            assert height <= 31
            self._height = UInt8(height)
        else:
            self._height = None

    def set_y_shift(self, y_shift: int | None) -> None:
        """Set the distance in pixels (from -16 to +15) to shift the sprite up or down."""
        if y_shift is not None:
            assert -16 <= y_shift <= 15
            self._y_shift = Int8(y_shift)
        else:
            self._y_shift = None

    def set_show_shadow(self, show_shadow: bool | None) -> None:
        """Set whether a shadow for the NPC when airborne will be loaded to VRAM."""
        self._show_shadow = show_shadow

    def set_byte2_bit0(self, byte2_bit0: bool | None) -> None:
        """(unknown)"""
        self._byte2_bit0 = byte2_bit0

    def set_byte2_bit1(self, byte2_bit1: bool | None) -> None:
        """(unknown)"""
        self._byte2_bit1 = byte2_bit1

    def set_byte2_bit2(self, byte2_bit2: bool | None) -> None:
        """(unknown)"""
        self._byte2_bit2 = byte2_bit2

    def set_byte2_bit3(self, byte2_bit3: bool | None) -> None:
        """(unknown)"""
        self._byte2_bit3 = byte2_bit3

    def set_byte2_bit4(self, byte2_bit4: bool | None) -> None:
        """(unknown)"""
        self._byte2_bit4 = byte2_bit4

    def set_byte5_bit6(self, byte5_bit6: bool | None) -> None:
        """(unknown)"""
        self._byte5_bit6 = byte5_bit6

    def set_byte5_bit7(self, byte5_bit7: bool | None) -> None:
        """(unknown)"""
        self._byte5_bit7 = byte5_bit7

    def set_byte6_bit2(self, byte6_bit2: bool | None) -> None:
        """(unknown)"""
        self._byte6_bit2 = byte6_bit2

    def set_directions(self, directions: VramStore | None) -> None:
        """Set the directions which the NPC can be expected to face."""
        self._directions = directions

    def set_min_vram_size(self, min_vram_size: int | None) -> None:
        """Set the minimum number (0 to 7) of VRAM chunks the NPC's sprite requires."""
        if min_vram_size is not None:
            assert min_vram_size <= 7
        self._min_vram_size = min_vram_size

    def set_priority_0(self, priority_0: bool | None) -> None:
        """Set priority bit 0 for sprite layering."""
        self._priority_0 = priority_0

    def set_priority_1(self, priority_1: bool | None) -> None:
        """Set priority bit 1 for sprite layering."""
        self._priority_1 = priority_1

    def set_priority_2(self, priority_2: bool | None) -> None:
        """Set priority bit 2 for sprite layering."""
        self._priority_2 = priority_2

    def set_cannot_clone(self, cannot_clone: bool | None) -> None:
        """Set whether this NPC can be cloned."""
        self._cannot_clone = cannot_clone

    @property
    def type(self) -> ObjectType:
        """Whether this NPC is a chest, battle, or regular object."""
        return self._object_type

    def set_type(self, object_type: ObjectType) -> None:
        """Whether this NPC is a chest, battle, or regular object."""
        self._object_type = object_type

    @property
    def visible(self) -> bool:
        """If false, the NPC is hidden by default."""
        return self._visible

    def set_visible(self, visible: bool) -> None:
        """If false, the NPC is hidden by default."""
        self._visible = visible

    @property
    def x(self) -> UInt8:
        """The initial X coord of this NPC."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the initial X coord of this NPC."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The initial Y coord of this NPC."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the initial Y coord of this NPC."""
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The initial Z coord of this NPC."""
        return self._z

    def set_z(self, z: int) -> None:
        """The initial Z (0-31) coord of this NPC."""
        assert z <= 31
        self._z = UInt8(z)

    @property
    def z_half(self) -> bool:
        """If true, adds half a unit to the NPC's starting Z coordinate."""
        return self._z_half

    def set_z_half(self, z_half: bool) -> None:
        """If true, adds half a unit to the NPC's starting Z coordinate."""
        self._z_half = z_half

    @property
    def direction(self) -> Direction:
        """The direction that the NPC will face when the room loads."""
        return self._direction

    def set_direction(self, direction: Direction) -> None:
        """Choose the direction that the NPC will face when the room loads."""
        self._direction = direction

BaseRoomObjectT = TypeVar("BaseRoomObjectT", bound=BaseRoomObject)

class RoomObject(BaseRoomObject):
    _initiator: EventInitiator = EventInitiator.NONE
    _action_script: UInt16 = UInt16(0)
    _speed: UInt4 = UInt4(0)
    _face_on_trigger: bool = False
    _cant_enter_doors: bool = False
    _byte2_bit5: bool = False
    _set_sequence_playback: bool = False
    _cant_float: bool = False
    _cant_walk_up_stairs: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _cant_pass_npcs: bool = False
    _byte3_bit5: bool = False
    _cant_walk_through: bool = False
    _byte3_bit7: bool = False
    _slidable_along_walls: bool = False
    _cant_move_if_in_air: bool = False
    _byte7_upper2: int = 0
    _object_type: ObjectType

    @property
    def object_type(self) -> ObjectType:
        """Whether this NPC is a chest, battle, or regular object."""
        return self._object_type

    @property
    def initiator(self) -> EventInitiator:
        """The specific action needed to trigger this NPC."""
        return self._initiator

    def set_initiator(self, initiator: EventInitiator) -> None:
        """Set the specific action needed to trigger this NPC."""
        self._initiator = initiator

    @property
    def action_script(self) -> UInt16:
        """The default action script run by this NPC on load."""
        return self._action_script

    def set_action_script(self, action_script: int) -> None:
        """The default action script run by this NPC on load.\n
        It is recommended to use action script ID constant names for this."""
        assert 0 <= action_script < 1024
        self._action_script = UInt16(action_script)

    @property
    def speed(self) -> UInt4:
        """(unknown)"""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """(unknown)"""
        assert speed <= 7
        self._speed = UInt4(speed)

    @property
    def face_on_trigger(self) -> bool:
        """If true, the NPC faces the player when triggered."""
        return self._face_on_trigger

    def set_face_on_trigger(self, face_on_trigger: bool) -> None:
        """If true, the NPC faces the player when triggered."""
        self._face_on_trigger = face_on_trigger

    @property
    def cant_enter_doors(self) -> bool:
        """If true, the NPC is unable to pass through doors."""
        return self._cant_enter_doors

    def set_cant_enter_doors(self, cant_enter_doors: bool) -> None:
        """If true, the NPC is unable to pass through doors."""
        self._cant_enter_doors = cant_enter_doors

    @property
    def byte2_bit5(self) -> bool:
        """(unknown)"""
        return self._byte2_bit5

    def set_byte2_bit5(self, byte2_bit5: bool) -> None:
        """(unknown)"""
        self._byte2_bit5 = byte2_bit5

    @property
    def set_sequence_playback(self) -> bool:
        """(unknown)"""
        return self._set_sequence_playback

    def set_set_sequence_playback(self, set_sequence_playback: bool) -> None:
        """(unknown)"""
        self._set_sequence_playback = set_sequence_playback

    @property
    def cant_float(self) -> bool:
        """(unknown)"""
        return self._cant_float

    def set_cant_float(self, cant_float: bool) -> None:
        """(unknown)"""
        self._cant_float = cant_float

    @property
    def cant_walk_up_stairs(self) -> bool:
        """If true, the NPC is unable to walk up slopes."""
        return self._cant_walk_up_stairs

    def set_cant_walk_up_stairs(self, cant_walk_up_stairs: bool) -> None:
        """If true, the NPC is unable to walk up slopes."""
        self._cant_walk_up_stairs = cant_walk_up_stairs

    @property
    def cant_walk_under(self) -> bool:
        """If true, the NPC cannot be passed from underneath."""
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        """If true, the NPC cannot be passed from underneath."""
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        """If true, the NPC respects the collision data of walls."""
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        """If true, the NPC respects the collision data of walls."""
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        """If true, the NPC can't be passed through while the player is airborne."""
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        """If true, the NPC can't be passed through while the player is airborne."""
        self._cant_jump_through = cant_jump_through

    @property
    def cant_pass_npcs(self) -> bool:
        """If true, the NPC respects the collision dat of other NPCs."""
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        """If true, the NPC respects the collision dat of other NPCs."""
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def byte3_bit5(self) -> bool:
        """(unknown)"""
        return self._byte3_bit5

    def set_byte3_bit5(self, byte3_bit5: bool) -> None:
        """(unknown)"""
        self._byte3_bit5 = byte3_bit5

    @property
    def cant_walk_through(self) -> bool:
        """If true, the NPC can't be passed through while the player is on the ground."""
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        """If true, the NPC can't be passed through while the player is on the ground."""
        self._cant_walk_through = cant_walk_through

    @property
    def byte3_bit7(self) -> bool:
        """(unknown)"""
        return self._byte3_bit7

    def set_byte3_bit7(self, byte3_bit7: bool) -> None:
        """(unknown)"""
        self._byte3_bit7 = byte3_bit7

    @property
    def slidable_along_walls(self) -> bool:
        """(unknown)"""
        return self._slidable_along_walls

    def set_slidable_along_walls(self, slidable_along_walls: bool) -> None:
        """(unknown)"""
        self._slidable_along_walls = slidable_along_walls

    @property
    def cant_move_if_in_air(self) -> bool:
        """If true, the NPC cannot move in any direction while airborne."""
        return self._cant_move_if_in_air

    def set_cant_move_if_in_air(self, cant_move_if_in_air: bool) -> None:
        """If true, the NPC cannot move in any direction while airborne."""
        self._cant_move_if_in_air = cant_move_if_in_air

    @property
    def byte7_upper2(self) -> int:
        """(unknown)"""
        return self._byte7_upper2

    def set_byte7_upper2(self, byte7_upper2: int) -> None:
        """(unknown)"""
        assert 0 <= byte7_upper2 <= 3
        self._byte7_upper2 = byte7_upper2

class Clone(BaseRoomObject):
    """A basic class for a clone NPC.\n
    A clone inherits some properties from the nearest prior regular NPC."""

    _action_script: UInt16 = UInt16(0)

    @property
    def action_script(self) -> UInt16:
        """The default action script run by this clone on load."""
        return self._action_script

    def set_action_script(self, action_script: int) -> None:
        """The default action script run by this clone on load.\n
        It is recommended to use action script ID constant names for this."""
        assert 0 <= action_script < 1024
        self._action_script = UInt16(action_script)

class BattlePackNPC(RoomObject):
    """A basic non-clone NPC that initiates a battle when interacted with."""

    _object_type = ObjectType.BATTLE
    _battle_pack: UInt8 = UInt8(0)
    _after_battle = PostBattleBehaviour.REMOVE_PERMANENTLY

    @property
    def battle_pack(self) -> UInt8:
        """When you interact with this NPC, it engages in battle against
        this pack ID."""
        return self._battle_pack

    def set_battle_pack(self, battle_pack: int) -> None:
        """When you interact with this NPC, it engages in battle against
        this pack ID.\n
        It is recommended to use pack ID constant names for this."""
        self._battle_pack = UInt8(battle_pack)

    @property
    def after_battle(self) -> PostBattleBehaviour:
        """The behaviour this NPC should exhibit after battle."""
        return self._after_battle

    def set_after_battle(self, after_battle: PostBattleBehaviour) -> None:
        """Set the behaviour this NPC should exhibit after battle."""
        self._after_battle = after_battle

    def __init__(self,
        npc: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        after_battle: PostBattleBehaviour = PostBattleBehaviour.REMOVE_PERMANENTLY,
        battle_pack: int = 0,
        action_script: int = 0,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: int = 0,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        super().set_initiator(initiator)
        self.set_after_battle(after_battle)
        self.set_battle_pack(battle_pack)
        super().set_action_script(action_script)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class RegularNPC(RoomObject):
    """A basic non-clone NPC that is not a chest or a
    battle initiator."""

    _object_type = ObjectType.OBJECT
    _event_script: UInt16 = UInt16(256)

    @property
    def event_script(self) -> UInt16:
        """The ID of the event script that should run when this NPC
        is interacted with."""
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        """Set the ID of the event script that should run when this NPC
        is interacted with.\n
        It is recommended to use event script ID constant names for this."""
        self._event_script = UInt16(event_script)

    def __init__(self,
        npc: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        event_script: int = 256,
        action_script: int = 0,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: int = 0,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        super().set_initiator(initiator)
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class ChestNPC(RoomObject):
    """A basic non-clone NPC that is a treasure chest."""

    _object_type = ObjectType.CHEST
    _event_script: UInt16 = UInt16(256)
    _lower_70a7: UInt4 = UInt4(0)
    _upper_70a7: UInt4 = UInt4(0)

    @property
    def event_script(self) -> UInt16:
        """The ID of the event script that should run when this chest
        is hit."""
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        """Set the ID of the event script that should run when this chest
        is hit.\n
        It is recommended to use event script ID constant names for this."""
        self._event_script = UInt16(event_script)

    @property
    def lower_70a7(self) -> UInt4:
        """The lower 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        return self._lower_70a7

    def set_lower_70a7(self, lower_70a7: int) -> None:
        """Set the lower 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        self._lower_70a7 = UInt4(lower_70a7)

    @property
    def upper_70a7(self) -> UInt4:
        """The upper 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        return self._upper_70a7

    def set_upper_70a7(self, upper_70a7: int) -> None:
        """Set the upper 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        self._upper_70a7 = UInt4(upper_70a7)

    def __init__(self,
        npc: NPC,
        initiator: EventInitiator = EventInitiator.NONE,
        event_script: int = 256,
        action_script: int = 0,
        lower_70a7: int = 0,
        upper_70a7: int = 0,
        speed: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        face_on_trigger: bool = False,
        cant_enter_doors: bool = False,
        byte2_bit5: bool = False,
        set_sequence_playback: bool = False,
        cant_float: bool = False,
        cant_walk_up_stairs: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        cant_pass_npcs: bool = False,
        byte3_bit5: bool = False,
        cant_walk_through: bool = False,
        byte3_bit7: bool = False,
        slidable_along_walls: bool = False,
        cant_move_if_in_air: bool = False,
        byte7_upper2: int = 0,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        super().set_initiator(initiator)
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        self.set_lower_70a7(lower_70a7)
        self.set_upper_70a7(upper_70a7)
        super().set_speed(speed)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        super().set_face_on_trigger(face_on_trigger)
        super().set_cant_enter_doors(cant_enter_doors)
        super().set_byte2_bit5(byte2_bit5)
        super().set_set_sequence_playback(set_sequence_playback)
        super().set_cant_float(cant_float)
        super().set_cant_walk_up_stairs(cant_walk_up_stairs)
        super().set_cant_walk_under(cant_walk_under)
        super().set_cant_pass_walls(cant_pass_walls)
        super().set_cant_jump_through(cant_jump_through)
        super().set_cant_pass_npcs(cant_pass_npcs)
        super().set_byte3_bit5(byte3_bit5)
        super().set_cant_walk_through(cant_walk_through)
        super().set_byte3_bit7(byte3_bit7)
        super().set_slidable_along_walls(slidable_along_walls)
        super().set_cant_move_if_in_air(cant_move_if_in_air)
        super().set_byte7_upper2(byte7_upper2)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class BattlePackClone(Clone):
    """A basic clone NPC that initiates a battle when interacted with."""

    _object_type = ObjectType.BATTLE
    _battle_pack: UInt8 = UInt8(0)

    @property
    def battle_pack(self) -> UInt8:
        """When you interact with this clone, it engages in battle against
        this pack ID."""
        return self._battle_pack

    def set_battle_pack(self, battle_pack: int) -> None:
        """When you interact with this clone, it engages in battle against
        this pack ID.\n
        It is recommended to use pack ID constant names for this."""
        self._battle_pack = UInt8(battle_pack)

    def __init__(self,
        npc: NPC,
        battle_pack: int = 0,
        action_script: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        self.set_battle_pack(battle_pack)
        super().set_action_script(action_script)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class RegularClone(Clone):
    """A basic clone NPC that is not a chest or a
    battle initiator."""

    _object_type = ObjectType.OBJECT
    _event_script: UInt16 = UInt16(256)

    @property
    def event_script(self) -> UInt16:
        """The ID of the event script that should run when this clone
        is interacted with."""
        return self._event_script

    def set_event_script(self, event_script: int) -> None:
        """Set the ID of the event script that should run when this clone
        is interacted with.\n
        It is recommended to use event script ID constant names for this."""
        self._event_script = UInt16(event_script)
    def __init__(self,
        npc: NPC,
        event_script: int = 256,
        action_script: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        self.set_event_script(event_script)
        super().set_action_script(action_script)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class ChestClone(Clone):
    """A basic clone NPC that is a treasure chest."""

    _object_type = ObjectType.CHEST
    _lower_70a7: UInt4 = UInt4(0)
    _upper_70a7: UInt4 = UInt4(0)

    @property
    def lower_70a7(self) -> UInt4:
        """The lower 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        return self._lower_70a7

    def set_lower_70a7(self, lower_70a7: int) -> None:
        """Set the lower 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        self._lower_70a7 = UInt4(lower_70a7)

    @property
    def upper_70a7(self) -> UInt4:
        """The upper 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        return self._upper_70a7

    def set_upper_70a7(self, upper_70a7: int) -> None:
        """Set the upper 4 bits of a built-in value that can be used in place of
        manually setting $70a7 (the usual item ID variable)."""
        self._upper_70a7 = UInt4(upper_70a7)

    def __init__(self,
        npc: NPC,
        lower_70a7: int = 0,
        upper_70a7: int = 0,
        visible: bool = False,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        z_half: bool = False,
        direction: Direction = SOUTHWEST,
        priority_0: bool | None = None,
        priority_1: bool | None = None,
        priority_2: bool | None = None,
        show_shadow: bool | None = None,
        shadow_size: ShadowSize | None = None,
        y_shift: Int8 | None = None,
        acute_axis: UInt4 | None = None,
        obtuse_axis: UInt4 | None = None,
        height: UInt8 | None = None,
        directions: VramStore | None = None,
        vram_size: int | None = None,
        cannot_clone: bool | None = None,
        byte2_bit0: bool | None = None,
        byte2_bit1: bool | None = None,
        byte2_bit2: bool | None = None,
        byte2_bit3: bool | None = None,
        byte2_bit4: bool | None = None,
        byte5_bit6: bool | None = None,
        byte5_bit7: bool | None = None,
        byte6_bit2: bool | None = None,
    ):
        self.set_lower_70a7(lower_70a7)
        self.set_upper_70a7(upper_70a7)
        super().set_visible(visible)
        super().set_x(x)
        super().set_y(y)
        super().set_z(z)
        super().set_z_half(z_half)
        super().set_direction(direction)
        self._npc = npc

        # Set BaseRoomObject optional properties
        super().set_priority_0(priority_0)
        super().set_priority_1(priority_1)
        super().set_priority_2(priority_2)
        super().set_show_shadow(show_shadow)
        super().set_shadow_size(shadow_size)
        super().set_y_shift(y_shift)
        super().set_acute_axis(acute_axis)
        super().set_obtuse_axis(obtuse_axis)
        super().set_height(height)
        super().set_directions(directions)
        super().set_min_vram_size(vram_size)
        super().set_cannot_clone(cannot_clone)
        super().set_byte2_bit0(byte2_bit0)
        super().set_byte2_bit1(byte2_bit1)
        super().set_byte2_bit2(byte2_bit2)
        super().set_byte2_bit3(byte2_bit3)
        super().set_byte2_bit4(byte2_bit4)
        super().set_byte5_bit6(byte5_bit6)
        super().set_byte5_bit7(byte5_bit7)
        super().set_byte6_bit2(byte6_bit2)

class Room(Generic[BaseRoomObjectT, ExitT]):
    """The base definition for each of the 512 levels in the game."""

    _partition: Partition | None = None
    _music: UInt8 = UInt8(0)
    _entrance_event: UInt16 = UInt16(0)
    _event_tiles: list[Event] = []
    _exit_fields: list[ExitT] = []
    _objects: list[BaseRoomObjectT] = []

    @property
    def partition(self) -> Partition | None:
        """A partition is a VRAM configuration for a specific room."""
        return self._partition

    def set_partition(self, partition: Partition | None) -> None:
        """A partition is a VRAM configuration for a specific room."""
        self._partition = partition

    @property
    def music(self) -> UInt8:
        """The ID of the music that should play on loading this room."""
        return self._music

    def set_music(self, music: int) -> None:
        """Set the ID of the music that should play on loading this room.\n
        It is recommended to use music ID constant names for this."""
        self._music = UInt8(music)

    @property
    def entrance_event(self) -> UInt16:
        """The ID of the event script that should play upon loading the room."""
        return self._entrance_event

    def set_entrance_event(self, entrance_event: int) -> None:
        """Set the ID of the event script that should play upon loading the room.\n
        It is recommended to use event script ID constant names for this."""
        self._entrance_event = UInt16(entrance_event)

    @property
    def event_tiles(self) -> list[Event]:
        """A list of specific tile designations that run event scripts when entered."""
        return self._event_tiles

    def set_event_tiles(self, event_tiles: list[Event]) -> None:
        """Overwrite the list of specific tile designations that run event scripts when entered."""
        self._event_tiles = event_tiles

    @property
    def exit_fields(self) -> list[ExitT]:
        """A list of specific tile designations that load other rooms or the world map."""
        return self._exit_fields

    def set_exit_fields(self, exit_fields: list[ExitT]) -> None:
        """Overwrite list of specific tile designations that load other rooms or the world map."""
        self._exit_fields = exit_fields

    def add_object(self, item: BaseRoomObjectT) -> None:
        """Add an object to the room."""
        assert len(self.objects) + 1 <= 28
        self.objects.append(item)

    def add_objects(self, items: list[BaseRoomObjectT]) -> None:
        """Add several objects to the room."""
        assert len(self.objects) + len(items) <= 28
        self.objects.extend(items)

    @property
    def objects(
        self,
    ) -> list[BaseRoomObjectT]:
        """A list of all the NPCs in the room."""
        return self._objects

    def set_objects(
        self,
        objects: list[BaseRoomObjectT],
    ) -> None:
        """Overwrite the list of NPCs in the room."""
        assert len(objects) <= 28
        self._objects = objects

    def __init__(
        self,
        partition: Partition = Partition(),
        music: int = 0,
        entrance_event: int = 15,
        events: list[Event] | None = None,
        exits: list[ExitT] | None = None,
        objects: list[BaseRoomObjectT] | None = None,
    ):
        if events is None:
            events = []
        if exits is None:
            exits = []
        if objects is None:
            objects = []
        self.set_partition(partition)
        self.set_music(music)
        self.set_entrance_event(entrance_event)
        self.set_event_tiles(events)
        self.set_exit_fields(exits)
        self.set_objects(objects)

    def get_npc_by_target_id(self, target: AreaObject) -> BaseRoomObjectT:
        """Get the first NPC in the room that matches the given target ID."""
        assert target >= 0x14 and target < 0x14 + len(self.objects)
        return self.objects[target - 0x14]
    
    def get_target_id_by_npc(self, index: int) -> AreaObject:
        """Get the target ID for the given NPC in the room."""
        return AreaObject(0x14 + index)