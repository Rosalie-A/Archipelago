"""Ally (playable character) palette classes for SMRPG.

These classes manage palettes for the 5 playable characters (Mario, Mallow, Geno,
Bowser, Toadstool) and can update SpritePaletteCollection and EventPaletteCollection
instead of creating raw ROM patches.

Each character has multiple palette slots:
- Standard palettes (overworld, battle, portrait, etc.)
- Poison palettes (when poisoned status)
- Underwater palettes (underwater areas)
- Special palettes (doll, classic, minecart, etc.)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .palette import (
    CLASSIC_PALETTE_OFFSET,
    COLORS_PER_PALETTE,
    EVENT_PALETTE_OFFSET,
    HOTSPRING_PALETTE_OFFSET,
    MAP_PALETTE_OFFSET,
    MINECART_PALETTE_OFFSET,
    PALETTE_SIZE,
    SPRITE_PALETTE_OFFSET,
    SpritePalette,
    EventPalette,
    address_to_sprite_palette_index,
    address_to_event_palette_index,
    color_str_to_snes_bytes,
    color_to_snes_bytes,
    palette_str_to_bytes,
    parse_color,
)

if TYPE_CHECKING:
    from .palette import SpritePaletteCollection, EventPaletteCollection


@dataclass
class PaletteSlot:
    """A palette slot definition with address and optional palette index."""
    address: int
    sprite_palette_index: int | None = None
    event_palette_index: int | None = None

    def __post_init__(self):
        # Auto-compute indices from address
        if self.sprite_palette_index is None:
            self.sprite_palette_index = address_to_sprite_palette_index(self.address)
        if self.event_palette_index is None:
            self.event_palette_index = address_to_event_palette_index(self.address)

    @property
    def is_sprite_palette(self) -> bool:
        return self.sprite_palette_index is not None

    @property
    def is_event_palette(self) -> bool:
        return self.event_palette_index is not None

    @property
    def is_outside_range(self) -> bool:
        return self.sprite_palette_index is None and self.event_palette_index is None


class AllyPalette:
    """Base class for playable character palettes.

    This class manages a set of 15 colors that can be applied to multiple
    palette slots (addresses) for a character. It supports:
    - Standard colors (main palette)
    - Poison colors (when poisoned)
    - Underwater colors (underwater areas)
    - Special patches for locations outside palette ranges
    """

    # Class-level defaults (override in subclasses)
    hot_spring_reset_row: int = 0  # Event palette index for hot spring reset

    # Palette slot definitions (override in subclasses)
    _standard_slots: list[PaletteSlot] = []
    _poison_slots: list[PaletteSlot] = []
    _underwater_slots: list[PaletteSlot] = []
    _doll_slots: list[PaletteSlot] = []

    # Character identification
    name_address: int = 0
    clone_name_address: int = 0
    original_name: str = ""
    name: str = ""
    rename_character: bool = True

    # Class-level color defaults - subclasses can override these
    colours: list[str] = []
    poison_colours: list[str] = []
    underwater_colours: list[str] = []
    classic_colours: list[str] | None = None
    overworld_map_colours: list[str] | None = None

    def __init__(self):
        # Don't override class-level colors - subclasses define them as class attributes
        pass

    @property
    def colors_int(self) -> list[int]:
        """Get standard colors as integers (0xRRGGBB)."""
        return [int(c, 16) for c in self.colours] if self.colours else []

    @property
    def poison_colors_int(self) -> list[int]:
        """Get poison colors as integers (0xRRGGBB)."""
        return [int(c, 16) for c in self.poison_colours] if self.poison_colours else []

    @property
    def underwater_colors_int(self) -> list[int]:
        """Get underwater colors as integers (0xRRGGBB)."""
        return [int(c, 16) for c in self.underwater_colours] if self.underwater_colours else []

    @property
    def clone_name(self) -> str:
        """Generate clone name for Mario clones/copies."""
        name = (self.name if self.rename_character else self.original_name).upper()
        if len(name) <= 7:
            return f"{name} CLONE"
        if len(name) <= 8:
            return f"{name} COPY"
        if len(name) <= 11:
            return f"{name} 2"
        return f"{name[0:10]}. 2"

    @property
    def strong_clone_name(self) -> str:
        """Generate strong clone name."""
        name = (self.name if self.rename_character else self.original_name).upper()
        if len(name) <= 5:
            return f"{name} CLONE S"
        if len(name) <= 6:
            return f"{name} COPY S"
        if len(name) <= 11:
            return f"{name} 3"
        return f"{name[0:10]}. 3"

    def update_collections(
        self,
        sprite_palettes: "SpritePaletteCollection",
        event_palettes: "EventPaletteCollection"
    ) -> dict[int, bytearray]:
        """Update palette collections with this character's colors.

        Updates palettes in the collections for addresses that fall within
        collection ranges. Returns raw patches for addresses outside ranges.

        Args:
            sprite_palettes: The sprite palette collection to update.
            event_palettes: The event palette collection to update.

        Returns:
            Dictionary of raw patches for addresses outside collection ranges.
        """
        raw_patches: dict[int, bytearray] = {}

        if not self.colours:
            return raw_patches

        # Update standard palette slots
        for slot in self._standard_slots:
            self._update_slot(slot, self.colors_int, sprite_palettes, event_palettes, raw_patches)

        # Update poison palette slots
        if self.poison_colours:
            for slot in self._poison_slots:
                self._update_slot(slot, self.poison_colors_int, sprite_palettes, event_palettes, raw_patches)

        # Update underwater palette slots
        if self.underwater_colours:
            for slot in self._underwater_slots:
                self._update_slot(slot, self.underwater_colors_int, sprite_palettes, event_palettes, raw_patches)

        return raw_patches

    def _update_slot(
        self,
        slot: PaletteSlot,
        colors: list[int],
        sprite_palettes: "SpritePaletteCollection",
        event_palettes: "EventPaletteCollection",
        raw_patches: dict[int, bytearray]
    ) -> None:
        """Update a single palette slot."""
        if slot.is_sprite_palette:
            palette = sprite_palettes[slot.sprite_palette_index]
            palette.set_colors(colors)
        elif slot.is_event_palette:
            palette = event_palettes[slot.event_palette_index]
            palette.set_colors(colors)
        else:
            # Address is outside collection ranges, create raw patch
            raw_patches[slot.address] = bytearray(palette_str_to_bytes(
                [f"{c:06X}" for c in colors]
            ))

    def special_palette(
        self, color_indices: list[int | None], address: int
    ) -> dict[int, bytearray]:
        """Write specific colors from this palette to an address using index mapping.

        This allows writing a subset of colors to a different location,
        useful for special palette locations like dolls, minecart, etc.

        Args:
            color_indices: List of color indices to write. Use None to skip a slot.
                          e.g., [0, 1, None, 3] writes colors 0, 1, skips slot 2, writes color 3
            address: The ROM address to write to.

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        patch: dict[int, bytearray] = {}
        if not self.colours:
            return patch
        for j, i in enumerate(color_indices):
            if i is not None:
                colour = self.colours[i]
                patch[address + j * 2] = bytearray(color_str_to_snes_bytes(colour))
        return patch

    def palette_override(
        self, colours: list[str], address: int
    ) -> dict[int, bytearray]:
        """Write a list of colors to a specific ROM address.

        Args:
            colours: List of hex color strings.
            address: The ROM address to write to.

        Returns:
            Dictionary mapping ROM addresses to byte data.
        """
        patch: dict[int, bytearray] = {}
        for j, colour in enumerate(colours):
            patch[address + j * 2] = bytearray(color_str_to_snes_bytes(colour))
        return patch

    # Methods to be overridden by subclasses
    def doll_patch(self) -> dict[int, bytearray]:
        """Get raw patches for doll palette. Override in subclass."""
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        """Get raw patches for classic palette. Override in subclass."""
        return {}

    def minecart_patch(self) -> dict[int, bytearray]:
        """Get raw patches for minecart palette. Override in subclass."""
        return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        """Get raw patches for overworld map palette. Override in subclass."""
        return {}

    def heated_sprite(self) -> dict[int, bytearray]:
        """Get raw patches for heated/hot spring sprite. Override in subclass."""
        return {}

    def standard_patch(self) -> dict[int, bytearray]:
        """Get raw patches for standard palette addresses.

        This is the legacy method that returns raw patches. For new code,
        prefer update_collections() which updates the palette collections directly.
        """
        patch: dict[int, bytearray] = {}
        if self.colours:
            for slot in self._standard_slots:
                patch.update(self.palette_override(self.colours, slot.address))
        if self.poison_colours:
            for slot in self._poison_slots:
                patch.update(self.palette_override(self.poison_colours, slot.address))
        if self.underwater_colours:
            for slot in self._underwater_slots:
                patch.update(self.palette_override(self.underwater_colours, slot.address))
        return patch


class MarioAllyPalette(AllyPalette):
    """Mario's palette configuration."""

    hot_spring_reset_row = (0x37A9D8 - EVENT_PALETTE_OFFSET) // PALETTE_SIZE  # = 84

    _standard_slots = [
        PaletteSlot(0x257998),  # overworld - sprite 628
        PaletteSlot(0x257B78),  # battle - sprite 644
        PaletteSlot(0x256B88),  # portrait - sprite 508
        PaletteSlot(0x257A4C),  # doll 2 - sprite 634
        PaletteSlot(0x256AF2),  # scarecrow/mushroom - sprite 503
        PaletteSlot(0x257AE2),  # ? - sprite 639
        PaletteSlot(0x37A9D8),  # ending - event 84
        PaletteSlot(0x3EDFFD),  # ? - outside range
        PaletteSlot(0x3EE0FF),  # ? - outside range
    ]
    _doll_slots = [
        PaletteSlot(0x258D66),  # doll 1 - sprite 797
    ]
    _poison_slots = [
        PaletteSlot(0x2579D4),  # poison overworld - sprite 630
        PaletteSlot(0x257BB4),  # poison battle - sprite 646
        PaletteSlot(0x256BC4),  # poison portrait - sprite 510
        PaletteSlot(0x257722),  # ? - sprite 607
    ]
    _underwater_slots = [
        PaletteSlot(0x257A10),  # underwater overworld - sprite 632
        PaletteSlot(0x257BF0),  # underwater battle - sprite 648
        PaletteSlot(0x37B31A),  # underwater ending - event 163
    ]

    name_address = 0x3A134D
    clone_name_address = 0x399A96
    name = "Mario"
    original_name = "Mario"

    def doll_patch(self) -> dict[int, bytearray]:
        """Mario doll uses special color mapping."""
        if not self.colours:
            return {}
        # Mapping: [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14]
        return self.special_palette(
            [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14],
            self._doll_slots[0].address
        )

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, CLASSIC_PALETTE_OFFSET)
        if not self.colours:
            return {}
        return self.special_palette(
            [10, 6, 1, None, None, None, None, None, None, None, None, None, None, None, None],
            CLASSIC_PALETTE_OFFSET,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        return self.special_palette(
            [None, 13, 1, 2, None, 5, 3, 6, 7, 9, 4, 9, 8, 10, 11],
            MINECART_PALETTE_OFFSET,
        )

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        return self.special_palette(
            [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14],
            MAP_PALETTE_OFFSET,
        )

    def heated_sprite(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        colours = [*self.colours]
        colours[1] = "F85030"
        b = palette_str_to_bytes(colours)
        return {HOTSPRING_PALETTE_OFFSET: bytearray(b[0:4])}


class MallowAllyPalette(AllyPalette):
    """Mallow's palette configuration."""

    hot_spring_reset_row = (0x37A9F6 - EVENT_PALETTE_OFFSET) // PALETTE_SIZE  # = 85

    _standard_slots = [
        PaletteSlot(0x2581AE),  # overworld - sprite 697
        PaletteSlot(0x258244),  # battle - sprite 702
        PaletteSlot(0x256B4C),  # portrait - sprite 506
        PaletteSlot(0x37A9F6),  # ending - event 85
    ]
    _poison_slots = [
        PaletteSlot(0x2581EA),  # poison overworld - sprite 699
        PaletteSlot(0x258280),  # poison battle - sprite 704
    ]
    _underwater_slots = [
        PaletteSlot(0x258226),  # underwater overworld - sprite 701
        PaletteSlot(0x2582BC),  # underwater battle - sprite 706
        PaletteSlot(0x37B374),  # underwater ending - event 166
    ]

    name_address = 0x3A1375
    clone_name_address = 0x399ACA
    name = "Mallow"
    original_name = "Mallow"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, CLASSIC_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, CLASSIC_PALETTE_OFFSET)
        return {}

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours:
            return self.palette_override(self.colours, MINECART_PALETTE_OFFSET)
        return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, MAP_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, MAP_PALETTE_OFFSET)
        return {}

    def heated_sprite(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        colours = [*self.colours]
        colours[0] = "F85030"
        colours[1] = "F85030"
        b = palette_str_to_bytes(colours)
        return {HOTSPRING_PALETTE_OFFSET: bytearray(b[0:4])}


class GenoAllyPalette(AllyPalette):
    """Geno's palette configuration."""

    hot_spring_reset_row = (0x37AA14 - EVENT_PALETTE_OFFSET) // PALETTE_SIZE  # = 86

    _standard_slots = [
        PaletteSlot(0x258046),  # overworld - sprite 685
        PaletteSlot(0x2580FA),  # battle - sprite 691
        PaletteSlot(0x256B6A),  # portrait - sprite 507
        PaletteSlot(0x257A88),  # doll 1 - sprite 636
        PaletteSlot(0x37AA14),  # ending - event 86
    ]
    _poison_slots = [
        PaletteSlot(0x258082),  # poison overworld - sprite 687
        PaletteSlot(0x258136),  # poison battle - sprite 693
    ]
    _underwater_slots = [
        PaletteSlot(0x2580BE),  # underwater overworld - sprite 689
        PaletteSlot(0x258172),  # underwater battle - sprite 695
        PaletteSlot(0x37B392),  # underwater ending - event 167
    ]

    name_address = 0x3A136B
    clone_name_address = 0x399ABD
    name = "Geno"
    original_name = "Geno"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, CLASSIC_PALETTE_OFFSET)
        if not self.colours:
            return {}
        return self.special_palette(
            [3, 6, 1, None, None, None, None, None, None, None, None, None, None, None, None],
            CLASSIC_PALETTE_OFFSET,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours:
            return self.palette_override(self.colours, MINECART_PALETTE_OFFSET)
        return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, MAP_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, MAP_PALETTE_OFFSET)
        return {}

    def heated_sprite(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        colours = [*self.colours]
        colours[1] = "F85030"
        b = palette_str_to_bytes(colours)
        return {HOTSPRING_PALETTE_OFFSET: bytearray(b[0:4])}


class BowserAllyPalette(AllyPalette):
    """Bowser's palette configuration."""

    hot_spring_reset_row = (0x37B068 - EVENT_PALETTE_OFFSET) // PALETTE_SIZE  # = 140

    _standard_slots = [
        PaletteSlot(0x257DD0),  # overworld - sprite 664
        PaletteSlot(0x257E66),  # battle - sprite 669
        PaletteSlot(0x256B2E),  # portrait - sprite 505
        PaletteSlot(0x257AA6),  # doll 1 - sprite 637
        PaletteSlot(0x37B068),  # ending - event 140
    ]
    _poison_slots = [
        PaletteSlot(0x257E0C),  # poison overworld - sprite 666
        PaletteSlot(0x257EA2),  # poison battle - sprite 671
    ]
    _underwater_slots = [
        PaletteSlot(0x257E48),  # underwater overworld - sprite 668
        PaletteSlot(0x257EDE),  # underwater battle - sprite 673
        PaletteSlot(0x37B356),  # underwater ending - event 165
    ]

    name_address = 0x3A1361
    clone_name_address = 0x399AB0
    name = "Bowser"
    original_name = "Bowser"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, CLASSIC_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, CLASSIC_PALETTE_OFFSET)
        return {}

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours:
            return self.palette_override(self.colours, MINECART_PALETTE_OFFSET)
        return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, MAP_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, MAP_PALETTE_OFFSET)
        return {}

    def heated_sprite(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        # No change for Bowser - main skin tone is past first 2 bytes
        b = palette_str_to_bytes(self.colours)
        return {HOTSPRING_PALETTE_OFFSET: bytearray(b[0:4])}


class ToadstoolAllyPalette(AllyPalette):
    """Toadstool's palette configuration."""

    hot_spring_reset_row = (0x37B086 - EVENT_PALETTE_OFFSET) // PALETTE_SIZE  # = 141

    _standard_slots = [
        PaletteSlot(0x257CA4),  # overworld - sprite 654
        PaletteSlot(0x257D3A),  # battle - sprite 659
        PaletteSlot(0x256B10),  # portrait - sprite 504
        PaletteSlot(0x257AC4),  # doll 1 - sprite 638
        PaletteSlot(0x37B086),  # ending - event 141
    ]
    _poison_slots = [
        PaletteSlot(0x257CE0),  # poison overworld - sprite 656
        PaletteSlot(0x257D76),  # poison battle - sprite 661
    ]
    _underwater_slots = [
        PaletteSlot(0x257D1C),  # underwater overworld - sprite 658
        PaletteSlot(0x257DB2),  # underwater battle - sprite 663
        PaletteSlot(0x37B338),  # underwater ending - event 164
    ]

    name_address = 0x3A1357
    clone_name_address = 0x399AA3
    name = "Toadstool"
    original_name = "Toadstool"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, CLASSIC_PALETTE_OFFSET)
        if not self.colours:
            return {}
        return self.special_palette(
            [6, 3, 1, None, None, None, None, None, None, None, None, None, None, None, None],
            CLASSIC_PALETTE_OFFSET,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours:
            return self.palette_override(self.colours, MINECART_PALETTE_OFFSET)
        return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, MAP_PALETTE_OFFSET)
        if self.colours:
            return self.palette_override(self.colours, MAP_PALETTE_OFFSET)
        return {}

    def heated_sprite(self) -> dict[int, bytearray]:
        if not self.colours:
            return {}
        colours = [*self.colours]
        colours[1] = "F85030"
        b = palette_str_to_bytes(colours)
        return {HOTSPRING_PALETTE_OFFSET: bytearray(b[0:4])}


# Convenient type aliases
MarioPalette = MarioAllyPalette
MallowPalette = MallowAllyPalette
GenoPalette = GenoAllyPalette
BowserPalette = BowserAllyPalette
ToadstoolPalette = ToadstoolAllyPalette
