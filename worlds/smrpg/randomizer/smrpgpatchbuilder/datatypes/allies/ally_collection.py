"""AllyCollection class for assembling ally/character data to ROM."""

from smrpgpatchbuilder.datatypes.allies.ally import Ally, LevelUp, AllyCoordinate

class AllyCollection:
    """Collection of all 5 allies for rendering to ROM."""

    def __init__(self, allies: list[Ally]):
        """Initialize the AllyCollection.

        Args:
            allies: List of exactly 5 Ally objects (Mario, Mallow, Geno, Bowser, Toadstool)
        """
        if len(allies) != 5:
            raise ValueError(f"AllyCollection requires exactly 5 allies, got {len(allies)}")

        self._allies = allies

    def get_by_type(self, ally_type: type[Ally]) -> Ally:
        """Return the ally that matches the specified type.

        Args:
            ally_type: The Ally subclass to search for.

        Returns:
            The ally instance matching the type.

        Raises:
            KeyError: If no ally of the specified type is found.
        """
        for ally in self._allies:
            if type(ally) is ally_type:
                return ally
        raise KeyError(f"No ally of type {ally_type.__name__} found in collection")

    def render(self) -> dict[int, bytearray]:
        """Render all ally data to patches.

        Based on Character.Assemble() lines 121-149.

        Returns:
            Dictionary mapping ROM addresses to byte data to write at those addresses
        """
        patches = {}

        for ally in self._allies:
            ally_patches = self._render_ally(ally)
            patches.update(ally_patches)

        # Render ally name pointers and strings at 0x2D3A5 and 0x2F9B0
        name_patches = self._render_levelup_screen_name_pointers()
        patches.update(name_patches)

        return patches

    def _render_ally(self, ally: Ally) -> dict[int, bytearray]:
        """Render a single ally to patches.

        Based on Character.Assemble() lines 121-149.

        Returns:
            Dictionary of patches
        """
        patches = {}

        # Starting stats - 20 bytes per character at 0x3A002C
        base_offset = (ally.index * 20) + 0x3A002C
        stats_data = bytearray(20)
        offset = 0

        stats_data[offset] = ally.starting_level
        offset += 1

        # Starting current HP (little-endian short)
        stats_data[offset] = ally.starting_current_hp & 0xFF
        stats_data[offset + 1] = (ally.starting_current_hp >> 8) & 0xFF
        offset += 2

        # Starting max HP (little-endian short)
        stats_data[offset] = ally.starting_max_hp & 0xFF
        stats_data[offset + 1] = (ally.starting_max_hp >> 8) & 0xFF
        offset += 2

        stats_data[offset] = ally.starting_speed
        offset += 1
        stats_data[offset] = ally.starting_attack
        offset += 1
        stats_data[offset] = ally.starting_defense
        offset += 1
        stats_data[offset] = ally.starting_mg_attack
        offset += 1
        stats_data[offset] = ally.starting_mg_defense
        offset += 1

        # Starting experience (little-endian short)
        stats_data[offset] = ally.starting_experience & 0xFF
        stats_data[offset + 1] = (ally.starting_experience >> 8) & 0xFF
        offset += 2

        # Convert item classes to bytes using _index
        stats_data[offset] = ally.starting_weapon().index if ally.starting_weapon is not None else 0xFF
        offset += 1
        stats_data[offset] = ally.starting_armor().index if ally.starting_armor is not None else 0xFF
        offset += 1
        stats_data[offset] = ally.starting_accessory().index if ally.starting_accessory is not None else 0xFF
        offset += 2  # Skip one byte

        # Starting magic - convert list of spell classes to 32 bits (4 bytes)
        # Build a set of spell indices the character has
        spell_indices = set()
        for spell_class in ally.starting_magic:
            # Access the _index class attribute
            spell_indices.add(spell_class._index)

        # Write 32 bits (4 bytes)
        for byte_idx in range(4):
            byte_val = 0
            for bit_idx in range(8):
                spell_index = byte_idx * 8 + bit_idx
                if spell_index in spell_indices:
                    byte_val |= (1 << bit_idx)
            stats_data[offset] = byte_val
            offset += 1

        patches[base_offset] = stats_data

        # Character name - 10 characters at 0x3A134D
        name_offset = (ally.index * 10) + 0x3A134D
        name_bytes = ally.name.ljust(10)[:10].encode('latin1')
        patches[name_offset] = bytearray(name_bytes)

        # Level-ups
        for level_up in ally.levels:
            level_patches = self._render_level_up(level_up, ally.index)
            patches.update(level_patches)

        # Coordinates
        coord_patches = self._render_coordinates(ally.coordinates, ally.index)
        patches.update(coord_patches)

        return patches

    def _render_level_up(self, level_up: LevelUp, owner: int) -> dict[int, bytearray]:
        """Render level-up data for a specific level.

        Based on LevelUp.Assemble() lines 233-253.

        Returns:
            Dictionary of patches
        """
        patches = {}
        level = level_up.level

        # Experience needed (only write for Mario, index 0)
        if owner == 0:
            exp_offset = ((level - 2) * 2) + 0x3A1AFF
            exp_data = bytearray(2)
            exp_data[0] = level_up.exp_needed & 0xFF
            exp_data[1] = (level_up.exp_needed >> 8) & 0xFF
            patches[exp_offset] = exp_data

        # Stat increases - 3 bytes per character, 15 bytes per level
        stat_offset = (owner * 3) + ((level - 2) * 15) + 0x3A1B39
        stat_data = bytearray(3)

        stat_data[0] = level_up.hp_plus
        stat_data[1] = ((level_up.attack_plus << 4) | (level_up.defense_plus & 0x0F))
        stat_data[2] = ((level_up.mg_attack_plus << 4) | (level_up.mg_defense_plus & 0x0F))

        patches[stat_offset] = stat_data

        # Bonus stat increases - same structure
        bonus_offset = (owner * 3) + ((level - 2) * 15) + 0x3A1CEC
        bonus_data = bytearray(3)

        bonus_data[0] = level_up.hp_plus_bonus
        bonus_data[1] = ((level_up.attack_plus_bonus << 4) | (level_up.defense_plus_bonus & 0x0F))
        bonus_data[2] = ((level_up.mg_attack_plus_bonus << 4) | (level_up.mg_defense_plus_bonus & 0x0F))

        patches[bonus_offset] = bonus_data

        # Spell learned - convert from spell class to byte
        spell_offset = owner + ((level - 2) * 5) + 0x3A42F5
        if level_up.spell_learned is None:
            spell_byte = 0xFF  # No spell
        else:
            # Get the spell index from the class
            spell_byte = level_up.spell_learned._index

        patches[spell_offset] = bytearray([spell_byte])

        return patches

    def _render_coordinates(self, coords: AllyCoordinate, index: int) -> dict[int, bytearray]:
        """Render ally battle coordinates.

        Based on AllyCoordinate.Assemble() lines 313-323.

        Returns:
            Dictionary of patches
        """
        patches = {}

        # Regular coordinates
        patches[0x029752 + index] = bytearray([((coords.cursor_x << 4) | (coords.cursor_y & 0x0F))])
        patches[0x023685 + (index * 2)] = bytearray([coords.sprite_abxy_y])

        # Scarecrow coordinates (only write for index 0/Mario)
        if index == 0:
            patches[0x029757] = bytearray([((coords.cursor_x_scarecrow << 4) | (coords.cursor_y_scarecrow & 0x0F))])
            patches[0x02346E] = bytearray([coords.sprite_abxy_y_scarecrow])

        return patches

    def _render_levelup_screen_name_pointers(self) -> dict[int, bytearray]:
        """Render ally name pointers and strings.

        Writes ally names starting at 0x2F9B0, each null-terminated.
        Writes pointers to those names at 0x2D3A5 (5 pointers * 2 bytes = 10 bytes).

        Returns:
            Dictionary of patches
        """
        patches = {}

        pointer_table_offset = 0x2D3A5
        name_data_offset = 0x2F9B0
        current_name_offset = name_data_offset

        # Build pointer table
        pointer_data = bytearray()
        # Build name data
        name_data = bytearray()

        for ally in self._allies:
            # Add pointer to table (little-endian, relative to bank 0x02)
            # The pointer is just the low 16 bits since we're in the same bank
            pointer_value = current_name_offset & 0xFFFF
            pointer_data.append(pointer_value & 0xFF)
            pointer_data.append((pointer_value >> 8) & 0xFF)

            # Add name string (no trailing spaces, null-terminated)
            name_trimmed = ally.name.rstrip()
            name_bytes = name_trimmed.encode('latin1')
            name_data.extend(name_bytes)
            name_data.append(0x00)  # Null terminator

            current_name_offset += len(name_bytes) + 1

        patches[pointer_table_offset] = pointer_data
        patches[name_data_offset] = name_data

        return patches
