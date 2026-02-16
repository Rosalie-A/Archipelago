"""WorldMapLocation class for SMRPG world map location data."""

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag

# Constants
WORLD_MAP_LOCATION_BASE_ADDRESS = 0x3EF830
WORLD_MAP_NAME_POINTER_BASE_ADDRESS = 0x3EFD00
WORLD_MAP_NAME_DATA_BASE_ADDRESS = 0x3EFD80
TOTAL_WORLD_MAP_LOCATIONS = 56

class WorldMapLocation:
    """A world map location in Super Mario RPG."""

    _index: int
    _name: str
    _x: int
    _y: int
    _show_check_flag: Flag | None
    _go_location: bool
    _run_event: int | None
    _which_location_check_flag: Flag | None
    _go_location_a: int | None
    _go_location_b: int | None
    _enabled_to_east: bool
    _enabled_to_south: bool
    _enabled_to_west: bool
    _enabled_to_north: bool
    _check_flag_to_east: Flag | None
    _check_flag_to_south: Flag | None
    _check_flag_to_west: Flag | None
    _check_flag_to_north: Flag | None
    _location_to_east: int | None
    _location_to_south: int | None
    _location_to_west: int | None
    _location_to_north: int | None

    @property
    def index(self) -> int:
        """The location's index (0-55)."""
        return self._index

    def set_index(self, index: int) -> None:
        """Set the location's index."""
        assert 0 <= index < TOTAL_WORLD_MAP_LOCATIONS, \
            f"WorldMapLocation index must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._index = index

    @property
    def name(self) -> str:
        """The location's name."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set the location's name."""
        self._name = name

    @property
    def x(self) -> int:
        """The location's X coordinate."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the location's X coordinate."""
        assert 0 <= x <= 255, "X coordinate must be 0-255"
        self._x = x

    @property
    def y(self) -> int:
        """The location's Y coordinate."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the location's Y coordinate."""
        assert 0 <= y <= 255, "Y coordinate must be 0-255"
        self._y = y

    @property
    def show_check_flag(self) -> Flag | None:
        """Flag that controls whether this location is shown."""
        return self._show_check_flag

    def set_show_check_flag(self, flag: Flag | None) -> None:
        """Set the show check flag."""
        self._show_check_flag = flag

    @property
    def go_location(self) -> bool:
        """If True, go to a location; if False, run an event."""
        return self._go_location

    def set_go_location(self, value: bool) -> None:
        """Set whether this triggers a location change or event."""
        self._go_location = value

    @property
    def run_event(self) -> int | None:
        """Event to run (only if go_location is False)."""
        return self._run_event

    def set_run_event(self, event: int | None) -> None:
        """Set the event to run."""
        if event is not None:
            assert 0 <= event <= 0xFFFF, "Event must be 0-0xFFFF"
        self._run_event = event

    @property
    def which_location_check_flag(self) -> Flag | None:
        """Flag that determines which location to go to (only if go_location is True)."""
        return self._which_location_check_flag

    def set_which_location_check_flag(self, flag: Flag | None) -> None:
        """Set the which location check flag."""
        self._which_location_check_flag = flag

    @property
    def go_location_a(self) -> int | None:
        """First location option (only if go_location is True)."""
        return self._go_location_a

    def set_go_location_a(self, location: int | None) -> None:
        """Set the first location option."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._go_location_a = location

    @property
    def go_location_b(self) -> int | None:
        """Second location option (only if go_location is True)."""
        return self._go_location_b

    def set_go_location_b(self, location: int | None) -> None:
        """Set the second location option."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._go_location_b = location

    @property
    def enabled_to_east(self) -> bool:
        """Whether travel to the east is enabled."""
        return self._enabled_to_east

    def set_enabled_to_east(self, value: bool) -> None:
        """Set whether travel to the east is enabled."""
        self._enabled_to_east = value

    @property
    def enabled_to_south(self) -> bool:
        """Whether travel to the south is enabled."""
        return self._enabled_to_south

    def set_enabled_to_south(self, value: bool) -> None:
        """Set whether travel to the south is enabled."""
        self._enabled_to_south = value

    @property
    def enabled_to_west(self) -> bool:
        """Whether travel to the west is enabled."""
        return self._enabled_to_west

    def set_enabled_to_west(self, value: bool) -> None:
        """Set whether travel to the west is enabled."""
        self._enabled_to_west = value

    @property
    def enabled_to_north(self) -> bool:
        """Whether travel to the north is enabled."""
        return self._enabled_to_north

    def set_enabled_to_north(self, value: bool) -> None:
        """Set whether travel to the north is enabled."""
        self._enabled_to_north = value

    @property
    def check_flag_to_east(self) -> Flag | None:
        """Flag that controls travel to the east."""
        return self._check_flag_to_east

    def set_check_flag_to_east(self, flag: Flag | None) -> None:
        """Set the check flag for travel to the east."""
        self._check_flag_to_east = flag

    @property
    def check_flag_to_south(self) -> Flag | None:
        """Flag that controls travel to the south."""
        return self._check_flag_to_south

    def set_check_flag_to_south(self, flag: Flag | None) -> None:
        """Set the check flag for travel to the south."""
        self._check_flag_to_south = flag

    @property
    def check_flag_to_west(self) -> Flag | None:
        """Flag that controls travel to the west."""
        return self._check_flag_to_west

    def set_check_flag_to_west(self, flag: Flag | None) -> None:
        """Set the check flag for travel to the west."""
        self._check_flag_to_west = flag

    @property
    def check_flag_to_north(self) -> Flag | None:
        """Flag that controls travel to the north."""
        return self._check_flag_to_north

    def set_check_flag_to_north(self, flag: Flag | None) -> None:
        """Set the check flag for travel to the north."""
        self._check_flag_to_north = flag

    @property
    def location_to_east(self) -> int | None:
        """Location index to the east."""
        return self._location_to_east

    def set_location_to_east(self, location: int | None) -> None:
        """Set the location to the east."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._location_to_east = location

    @property
    def location_to_south(self) -> int | None:
        """Location index to the south."""
        return self._location_to_south

    def set_location_to_south(self, location: int | None) -> None:
        """Set the location to the south."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._location_to_south = location

    @property
    def location_to_west(self) -> int | None:
        """Location index to the west."""
        return self._location_to_west

    def set_location_to_west(self, location: int | None) -> None:
        """Set the location to the west."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._location_to_west = location

    @property
    def location_to_north(self) -> int | None:
        """Location index to the north."""
        return self._location_to_north

    def set_location_to_north(self, location: int | None) -> None:
        """Set the location to the north."""
        if location is not None:
            assert 0 <= location < TOTAL_WORLD_MAP_LOCATIONS, \
                f"Location must be 0-{TOTAL_WORLD_MAP_LOCATIONS-1}"
        self._location_to_north = location

    def __init__(
        self,
        index: int,
        name: str = "",
        x: int = 0,
        y: int = 0,
        show_check_flag: Flag | None = None,
        go_location: bool = False,
        run_event: int | None = None,
        which_location_check_flag: Flag | None = None,
        go_location_a: int | None = None,
        go_location_b: int | None = None,
        enabled_to_east: bool = False,
        enabled_to_south: bool = False,
        enabled_to_west: bool = False,
        enabled_to_north: bool = False,
        check_flag_to_east: Flag | None = None,
        check_flag_to_south: Flag | None = None,
        check_flag_to_west: Flag | None = None,
        check_flag_to_north: Flag | None = None,
        location_to_east: int | None = None,
        location_to_south: int | None = None,
        location_to_west: int | None = None,
        location_to_north: int | None = None,
    ) -> None:
        """Initialize a WorldMapLocation.

        Args:
            index: The location's index (0-55)
            name: The location's name
            x: X coordinate (0-255)
            y: Y coordinate (0-255)
            show_check_flag: Flag that controls whether this location is shown
            go_location: If True, go to a location; if False, run an event
            run_event: Event to run (only if go_location is False)
            which_location_check_flag: Flag that determines which location to go to
            go_location_a: First location option (only if go_location is True)
            go_location_b: Second location option (only if go_location is True)
            enabled_to_east: Whether travel to the east is enabled
            enabled_to_south: Whether travel to the south is enabled
            enabled_to_west: Whether travel to the west is enabled
            enabled_to_north: Whether travel to the north is enabled
            check_flag_to_east: Flag that controls travel to the east
            check_flag_to_south: Flag that controls travel to the south
            check_flag_to_west: Flag that controls travel to the west
            check_flag_to_north: Flag that controls travel to the north
            location_to_east: Location index to the east
            location_to_south: Location index to the south
            location_to_west: Location index to the west
            location_to_north: Location index to the north
        """
        self.set_index(index)
        self.set_name(name)
        self.set_x(x)
        self.set_y(y)
        self.set_show_check_flag(show_check_flag)
        self.set_go_location(go_location)
        self.set_run_event(run_event)
        self.set_which_location_check_flag(which_location_check_flag)
        self.set_go_location_a(go_location_a)
        self.set_go_location_b(go_location_b)
        self.set_enabled_to_east(enabled_to_east)
        self.set_enabled_to_south(enabled_to_south)
        self.set_enabled_to_west(enabled_to_west)
        self.set_enabled_to_north(enabled_to_north)
        self.set_check_flag_to_east(check_flag_to_east)
        self.set_check_flag_to_south(check_flag_to_south)
        self.set_check_flag_to_west(check_flag_to_west)
        self.set_check_flag_to_north(check_flag_to_north)
        self.set_location_to_east(location_to_east)
        self.set_location_to_south(location_to_south)
        self.set_location_to_west(location_to_west)
        self.set_location_to_north(location_to_north)

    def render(self) -> dict[int, bytearray]:
        """Render the world map location data to ROM format.

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching
        """
        offset = WORLD_MAP_LOCATION_BASE_ADDRESS + (self.index * 16)
        data = bytearray()

        # Byte 0: X coordinate
        data.append(self.x)

        # Byte 1: Y coordinate
        data.append(self.y)

        # Bytes 2-3: Show check flag (2 bytes: address and bit packed)
        if self.show_check_flag:
            show_check_value = ((self.show_check_flag.byte - 0x7045) << 3) | self.show_check_flag.bit
        else:
            show_check_value = 0  # Default to Flag(0x7045, 0)
        data.append(show_check_value & 0xFF)
        data.append((show_check_value >> 8) & 0x01)

        # Byte 3 bit 6: go_location flag
        if self.go_location:
            data[3] |= 0x40

        # Bytes 4-7: Either event (2 bytes) + padding or location data (4 bytes)
        if not self.go_location:
            # Run event mode: 2 bytes for event, 2 bytes padding (0xFFFF)
            event_value = self.run_event if self.run_event is not None else 0
            data.append(event_value & 0xFF)
            data.append((event_value >> 8) & 0xFF)
            data.append(0xFF)
            data.append(0xFF)
        else:
            # Go location mode: which_location_check_flag (2 bytes) + locations (2 bytes)
            if self.which_location_check_flag:
                which_loc_value = ((self.which_location_check_flag.byte - 0x7045) << 3) | \
                                  self.which_location_check_flag.bit
            else:
                which_loc_value = 0
            data.append(which_loc_value & 0xFF)
            data.append((which_loc_value >> 8) & 0x01)
            data.append(self.go_location_a if self.go_location_a is not None else 0)
            data.append(self.go_location_b if self.go_location_b is not None else 0)

        # Bytes 8-9: East direction
        if not self.enabled_to_east:
            data.append(0xFF)
            data.append(0xFF)
        else:
            if self.check_flag_to_east:
                east_check_value = ((self.check_flag_to_east.byte - 0x7045) << 3) | \
                                   self.check_flag_to_east.bit
            else:
                east_check_value = 0
            data.append(east_check_value & 0xFF)
            loc_east = self.location_to_east if self.location_to_east is not None else 0
            data.append(((east_check_value >> 8) & 0x01) | (loc_east << 1))

        # Bytes 10-11: South direction
        if not self.enabled_to_south:
            data.append(0xFF)
            data.append(0xFF)
        else:
            if self.check_flag_to_south:
                south_check_value = ((self.check_flag_to_south.byte - 0x7045) << 3) | \
                                    self.check_flag_to_south.bit
            else:
                south_check_value = 0
            data.append(south_check_value & 0xFF)
            loc_south = self.location_to_south if self.location_to_south is not None else 0
            data.append(((south_check_value >> 8) & 0x01) | (loc_south << 1))

        # Bytes 12-13: West direction
        if not self.enabled_to_west:
            data.append(0xFF)
            data.append(0xFF)
        else:
            if self.check_flag_to_west:
                west_check_value = ((self.check_flag_to_west.byte - 0x7045) << 3) | \
                                   self.check_flag_to_west.bit
            else:
                west_check_value = 0
            data.append(west_check_value & 0xFF)
            loc_west = self.location_to_west if self.location_to_west is not None else 0
            data.append(((west_check_value >> 8) & 0x01) | (loc_west << 1))

        # Bytes 14-15: North direction
        if not self.enabled_to_north:
            data.append(0xFF)
            data.append(0xFF)
        else:
            if self.check_flag_to_north:
                north_check_value = ((self.check_flag_to_north.byte - 0x7045) << 3) | \
                                    self.check_flag_to_north.bit
            else:
                north_check_value = 0
            data.append(north_check_value & 0xFF)
            loc_north = self.location_to_north if self.location_to_north is not None else 0
            data.append(((north_check_value >> 8) & 0x01) | (loc_north << 1))

        return {offset: data}

class WorldMapLocationCollection:
    """Collection of all world map locations in the game."""

    _locations: list[WorldMapLocation]

    @property
    def locations(self) -> list[WorldMapLocation]:
        """The list of 56 world map locations."""
        return self._locations

    def __init__(self, locations: list[WorldMapLocation]) -> None:
        """Initialize a WorldMapLocationCollection with exactly 56 locations.

        Args:
            locations: A list of exactly 56 WorldMapLocation instances

        Raises:
            AssertionError: If not exactly 56 locations are provided
        """
        assert len(locations) == TOTAL_WORLD_MAP_LOCATIONS, \
            f"WorldMapLocationCollection requires exactly {TOTAL_WORLD_MAP_LOCATIONS} locations, " \
            f"got {len(locations)}"
        self._locations = locations

    def render(self) -> dict[int, bytearray]:
        """Render all world map locations to ROM format.

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching
        """
        patch: dict[int, bytearray] = {}

        for location in self._locations:
            location_patch = location.render()
            patch.update(location_patch)

        return patch
