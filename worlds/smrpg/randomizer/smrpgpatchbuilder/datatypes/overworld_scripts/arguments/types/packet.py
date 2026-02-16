

from smrpgpatchbuilder.datatypes.numbers.classes import UInt8, UInt16

# Constants to avoid circular imports
TOTAL_SPRITES = 0x400
TOTAL_SCRIPTS = 0x400

# Packet sprites are in range 192-255 (offset 0-63 stored in 6 bits)
PACKET_SPRITE_BASE = 192


class Packet:
    """An object to be spawned on the field that does not exist in the room's
    list of NPCs.

    Packets are fairly limited in what they can do, they are not as complex
    as NPCs. They are usually meant to be temporary, such as collectable items or
    treasure chest contents.

    Structure (5 bytes total at 0x1DB000 + packet_id * 5):
    - Byte 0: sprite (bits 0-5), b0 (bits 6-7)
    - Byte 1: b1a (bits 0-2), b1b (bits 3-4), b1c (bits 5-7)
    - Byte 2: bits 0-1 unused, b2b2 (bit 2), b2b3 (bit 3), b2b4 (bit 4), show_shadow (bit 5), b2 (bits 6-7)
    - Bytes 3-4: action_script_id (bits 0-9), b4 (byte 4 bits 4-7)

    It is recommended to use packet ID, sprite ID, and action script ID constant names.
    """

    _packet_id: UInt8 = UInt8(0)
    _sprite_id: UInt16 = UInt16(PACKET_SPRITE_BASE)  # Sprite ID (any valid sprite)
    _b0: UInt8 = UInt8(0)  # B0,b6-7: bits 6-7 of byte 0 (0-3)
    _b1a: UInt8 = UInt8(0)  # B1,b0-2: bits 0-2 of byte 1 (0-7)
    _b1b: UInt8 = UInt8(0)  # B1,b3-4: bits 3-4 of byte 1 (0-3)
    _b1c: UInt8 = UInt8(0)  # B1,b5-7: bits 5-7 of byte 1 (0-7)
    _b2b2: bool = False  # B2,b2: bit 2 of byte 2
    _b2b3: bool = False  # B2,b3: bit 3 of byte 2
    _b2b4: bool = False  # B2,b4: bit 4 of byte 2
    _show_shadow: bool = False  # SHOW SHADOW: bit 5 of byte 2
    _b2: UInt8 = UInt8(0)  # B2,b6-7: bits 6-7 of byte 2 (0-3)
    _action_script_id: UInt16 = UInt16(0)  # Action #: bits 0-9 of bytes 3-4 (0-1023)
    _b4: UInt8 = UInt8(0)  # B4,b4-7: bits 4-7 of byte 4 (0-15)

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet (0-255)."""
        return self._packet_id

    @property
    def sprite_id(self) -> UInt16:
        """The sprite ID for the packet."""
        return self._sprite_id

    def _set_sprite_id(self, sprite_id: int) -> None:
        """Set the sprite ID for the packet.
        Any valid sprite ID (0-1023) is accepted. During render(), only the
        lower 6 bits are used, so sprites are effectively grouped in ranges of 64."""
        assert 0 <= sprite_id < TOTAL_SPRITES, \
            f"sprite_id must be 0-{TOTAL_SPRITES-1}, got {sprite_id}"
        self._sprite_id = UInt16(sprite_id)

    @property
    def b0(self) -> UInt8:
        """B0,b6-7: bits 6-7 of byte 0 (0-3)."""
        return self._b0

    def _set_b0(self, b0: int) -> None:
        """Set B0,b6-7 (0-3)."""
        assert 0 <= b0 <= 3, f"b0 must be 0-3, got {b0}"
        self._b0 = UInt8(b0)

    @property
    def b1a(self) -> UInt8:
        """B1,b0-2: bits 0-2 of byte 1 (0-7)."""
        return self._b1a

    def _set_b1a(self, b1a: int) -> None:
        """Set B1,b0-2 (0-7)."""
        assert 0 <= b1a <= 7, f"b1a must be 0-7, got {b1a}"
        self._b1a = UInt8(b1a)

    @property
    def b1b(self) -> UInt8:
        """B1,b3-4: bits 3-4 of byte 1 (0-3)."""
        return self._b1b

    def _set_b1b(self, b1b: int) -> None:
        """Set B1,b3-4 (0-3)."""
        assert 0 <= b1b <= 3, f"b1b must be 0-3, got {b1b}"
        self._b1b = UInt8(b1b)

    @property
    def b1c(self) -> UInt8:
        """B1,b5-7: bits 5-7 of byte 1 (0-7)."""
        return self._b1c

    def _set_b1c(self, b1c: int) -> None:
        """Set B1,b5-7 (0-7)."""
        assert 0 <= b1c <= 7, f"b1c must be 0-7, got {b1c}"
        self._b1c = UInt8(b1c)

    @property
    def b2b2(self) -> bool:
        """B2,b2: bit 2 of byte 2."""
        return self._b2b2

    def _set_b2b2(self, b2b2: bool) -> None:
        """Set B2,b2."""
        self._b2b2 = b2b2

    @property
    def b2b3(self) -> bool:
        """B2,b3: bit 3 of byte 2."""
        return self._b2b3

    def _set_b2b3(self, b2b3: bool) -> None:
        """Set B2,b3."""
        self._b2b3 = b2b3

    @property
    def b2b4(self) -> bool:
        """B2,b4: bit 4 of byte 2."""
        return self._b2b4

    def _set_b2b4(self, b2b4: bool) -> None:
        """Set B2,b4."""
        self._b2b4 = b2b4

    @property
    def show_shadow(self) -> bool:
        """SHOW SHADOW: bit 5 of byte 2."""
        return self._show_shadow

    def _set_show_shadow(self, show_shadow: bool) -> None:
        """Set show_shadow."""
        self._show_shadow = show_shadow

    @property
    def b2(self) -> UInt8:
        """B2,b6-7: bits 6-7 of byte 2 (0-3)."""
        return self._b2

    def _set_b2(self, b2: int) -> None:
        """Set B2,b6-7 (0-3)."""
        assert 0 <= b2 <= 3, f"b2 must be 0-3, got {b2}"
        self._b2 = UInt8(b2)

    @property
    def action_script_id(self) -> UInt16:
        """Action #: The action script for this packet to run when spawned (0-1023)."""
        return self._action_script_id

    def _set_action_script_id(self, action_script_id: int) -> None:
        """Set the action script for this packet to run when spawned.
        It is recommended to use action script ID constant names for this."""
        assert 0 <= action_script_id <= 1023, \
            f"action_script_id must be 0-1023, got {action_script_id}"
        self._action_script_id = UInt16(action_script_id)

    @property
    def b4(self) -> UInt8:
        """B4,b4-7: bits 4-7 of byte 4 (0-15)."""
        return self._b4

    def _set_b4(self, b4: int) -> None:
        """Set B4,b4-7 (0-15)."""
        assert 0 <= b4 <= 15, f"b4 must be 0-15, got {b4}"
        self._b4 = UInt8(b4)

    def __init__(
        self,
        packet_id: int,
        sprite_id: int = PACKET_SPRITE_BASE,
        action_script_id: int = 0,
        b0: int = 0,
        b1a: int = 0,
        b1b: int = 0,
        b1c: int = 0,
        b2b2: bool = False,
        b2b3: bool = False,
        b2b4: bool = False,
        show_shadow: bool = False,
        b2: int = 0,
        b4: int = 0,
    ) -> None:
        self._packet_id = UInt8(packet_id)
        self._set_sprite_id(sprite_id)
        self._set_action_script_id(action_script_id)
        self._set_b0(b0)
        self._set_b1a(b1a)
        self._set_b1b(b1b)
        self._set_b1c(b1c)
        self._set_b2b2(b2b2)
        self._set_b2b3(b2b3)
        self._set_b2b4(b2b4)
        self._set_show_shadow(show_shadow)
        self._set_b2(b2)
        self._set_b4(b4)

    def render(self) -> bytearray:
        """Render the packet to 5 bytes for ROM.

        Structure:
        - Byte 0: sprite offset (bits 0-5) | b0 (bits 6-7)
        - Byte 1: b1a (bits 0-2) | b1b (bits 3-4) | b1c (bits 5-7)
        - Byte 2: b2b2 (bit 2) | b2b3 (bit 3) | b2b4 (bit 4) | show_shadow (bit 5) | b2 (bits 6-7)
        - Byte 3: action_script_id low byte
        - Byte 4: action_script_id high bits (bits 0-1) | b4 (bits 4-7)
        """
        output = bytearray(5)

        # Byte 0: sprite offset (0-63) in bits 0-5, b0 in bits 6-7
        # Use lower 6 bits of sprite_id for offset
        sprite_offset = self.sprite_id & 0x3F
        output[0] = sprite_offset | (self.b0 << 6)

        # Byte 1: b1a (bits 0-2), b1b (bits 3-4), b1c (bits 5-7)
        output[1] = (self.b1a & 0x07) | ((self.b1b & 0x03) << 3) | ((self.b1c & 0x07) << 5)

        # Byte 2: b2b2 (bit 2), b2b3 (bit 3), b2b4 (bit 4), show_shadow (bit 5), b2 (bits 6-7)
        output[2] = (
            ((1 if self.b2b2 else 0) << 2) |
            ((1 if self.b2b3 else 0) << 3) |
            ((1 if self.b2b4 else 0) << 4) |
            ((1 if self.show_shadow else 0) << 5) |
            ((self.b2 & 0x03) << 6)
        )

        # Byte 3: action_script_id low 8 bits
        output[3] = self.action_script_id & 0xFF

        # Byte 4: action_script_id high 2 bits (bits 0-1), b4 (bits 4-7)
        output[4] = ((self.action_script_id >> 8) & 0x03) | ((self.b4 & 0x0F) << 4)

        return output


class PacketCollection:
    """Collection of up to 256 packets with rendering support.

    Each packet occupies 5 bytes in the ROM. When a packet slot is None,
    it is represented by 5 0xFF bytes.
    """

    def __init__(self, packets: list[Packet | None]):
        """Initialize the collection with a list of up to 256 optional packets.

        Args:
            packets: list of optional Packet objects (up to 256 entries)

        Raises:
            ValueError: if more than 256 packets are provided
        """
        if len(packets) > 256:
            raise ValueError(
                f"PacketCollection can contain at most 256 packets, "
                f"but {len(packets)} were provided."
            )

        # Pad with None to ensure exactly 256 entries
        self.packets = packets + [None] * (256 - len(packets))

    def render(self) -> dict[int, bytearray]:
        """Render all packets to ROM format.

        Returns:
            dictionary mapping ROM address (0x1DB000) to bytearray of all packet data
        """
        data = bytearray()

        for packet in self.packets:
            if packet is None:
                # Empty packet slot: 5 bytes of 0xFF
                data.extend([0xFF] * 5)
            else:
                # Render the packet
                data.extend(packet.render())

        return {0x1DB000: data}
