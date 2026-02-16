"""RoomCollection class for managing and rendering all 512 rooms in the game."""

from smrpgpatchbuilder.datatypes.levels.classes import (
    Room, NPC, Partition, BaseRoomObject, RoomObject, Clone,
    BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone,
    RoomExit, MapExit
)

class RoomCollection:
    """Manages all 512 rooms and handles rendering them to ROM format."""

    _rooms: list[Room | None]
    _large_partition_table: bool

    def __init__(self, rooms: list[Room | None], large_partition_table: bool = False):
        """Initialize the room collection.

        Args:
            rooms: List of 512 rooms (some can be None)
            large_partition_table: If True, use extended partition table at 0x1DEBE0
        """
        assert len(rooms) == 512, f"Expected 512 rooms, got {len(rooms)}"
        # Ensure last room (511) is None
        assert rooms[511] is None, "Room 511 must be None"

        self._rooms = rooms
        self._large_partition_table = large_partition_table

    def _get_npc_signature(self, npc: NPC, room_obj: BaseRoomObject | None = None) -> tuple:
        """Get a unique signature for an NPC that includes all properties.

        If room_obj is provided, include any BaseRoomObject-level overrides.
        """
        sig = [
            npc.sprite_id,
            npc.shadow_size,
            npc.acute_axis,
            npc.obtuse_axis,
            npc.height,
            npc.y_shift,
            npc.show_shadow,
            npc.directions,
            npc.min_vram_size,
            npc.priority_0,
            npc.priority_1,
            npc.priority_2,
            npc.cannot_clone,
            npc.byte2_bit0,
            npc.byte2_bit1,
            npc.byte2_bit2,
            npc.byte2_bit3,
            npc.byte2_bit4,
            npc.byte5_bit6,
            npc.byte5_bit7,
            npc.byte6_bit2,
        ]

        # Add BaseRoomObject overrides if present
        if room_obj:
            sig.extend([
                room_obj.show_shadow if room_obj.show_shadow is not None else None,
                room_obj.shadow_size if room_obj.shadow_size is not None else None,
                room_obj.y_shift if room_obj.y_shift is not None else None,
                room_obj.acute_axis if room_obj.acute_axis is not None else None,
                room_obj.obtuse_axis if room_obj.obtuse_axis is not None else None,
                room_obj.height if room_obj.height is not None else None,
                room_obj.directions if room_obj.directions is not None else None,
                room_obj.min_vram_size if room_obj.min_vram_size is not None else None,
                room_obj.priority_0 if room_obj.priority_0 is not None else None,
                room_obj.priority_1 if room_obj.priority_1 is not None else None,
                room_obj.priority_2 if room_obj.priority_2 is not None else None,
                room_obj.cannot_clone if room_obj.cannot_clone is not None else None,
                room_obj.byte2_bit0 if room_obj.byte2_bit0 is not None else None,
                room_obj.byte2_bit1 if room_obj.byte2_bit1 is not None else None,
                room_obj.byte2_bit2 if room_obj.byte2_bit2 is not None else None,
                room_obj.byte2_bit3 if room_obj.byte2_bit3 is not None else None,
                room_obj.byte2_bit4 if room_obj.byte2_bit4 is not None else None,
                room_obj.byte5_bit6 if room_obj.byte5_bit6 is not None else None,
                room_obj.byte5_bit7 if room_obj.byte5_bit7 is not None else None,
                room_obj.byte6_bit2 if room_obj.byte6_bit2 is not None else None,
            ])

        return tuple(sig)

    def _collect_clone_group_requirements(self) -> list[tuple[int, int, list[tuple]]]:
        """Collect all clone group requirements across all rooms.

        Returns:
            List of (room_idx, parent_obj_idx, [signatures]) tuples where signatures
            is a list of NPC signatures that appear together in a clone group.
        """
        clone_groups = []

        for room_idx, room in enumerate(self._rooms):
            if room is None:
                continue

            # Scan for clone groups in this room
            obj_idx = 0
            while obj_idx < len(room.objects):
                obj = room.objects[obj_idx]

                if not isinstance(obj, Clone):
                    # This is a parent object - collect its clones
                    parent_sig = self._get_npc_signature(obj._npc, obj)
                    signatures = [parent_sig]

                    # Collect consecutive clones
                    clone_idx = obj_idx + 1
                    while clone_idx < len(room.objects) and isinstance(room.objects[clone_idx], Clone):
                        clone_sig = self._get_npc_signature(room.objects[clone_idx]._npc, room.objects[clone_idx])
                        signatures.append(clone_sig)
                        clone_idx += 1

                    # Only record if there are clones (more than just the parent)
                    if len(signatures) > 1:
                        clone_groups.append((room_idx, obj_idx, signatures))

                obj_idx += 1

        return clone_groups

    def _build_sequential_placement(self, clone_groups: list[tuple[int, int, list[tuple]]]) -> tuple[
        list[NPC],
        dict[tuple[int, int], dict[tuple, int]]
    ]:
        """Build NPC table with strategic sequential placement for clone groups.

        Args:
            clone_groups: List of (room_idx, parent_obj_idx, signatures) tuples

        Returns:
            Tuple of:
            - unique_npcs: List of NPC objects in the table
            - clone_group_mapping: dict[(room_idx, parent_obj_idx), dict[signature, table_index]]
        """
        unique_npcs = []
        clone_group_mapping = {}
        global_sig_to_npc = {}  # signature -> NPC object (for creating copies)

        # First pass: collect all unique signatures and create NPC objects
        all_signatures = set()
        for room_idx, room in enumerate(self._rooms):
            if room is None:
                continue
            for obj in room.objects:
                sig = self._get_npc_signature(obj._npc, obj)
                if sig not in global_sig_to_npc:
                    global_sig_to_npc[sig] = self._create_merged_npc(obj._npc, obj)
                all_signatures.add(sig)

        # Second pass: process clone groups and create sequential placements
        for room_idx, parent_obj_idx, signatures in clone_groups:
            # Deduplicate signatures while preserving order
            # (multiple objects in the clone group might use the same signature)
            unique_signatures = []
            seen = set()
            for sig in signatures:
                if sig not in seen:
                    unique_signatures.append(sig)
                    seen.add(sig)

            # Check if this clone group fits within 8 unique NPCs
            if len(unique_signatures) > 8:
                raise ValueError(
                    f"Room {room_idx} object {parent_obj_idx}: "
                    f"Clone group has {len(unique_signatures)} different NPCs (max 8)"
                )

            # Create a sequential block for this clone group using only unique signatures
            sig_to_index = {}
            base_index = len(unique_npcs)

            for i, sig in enumerate(unique_signatures):
                # Add NPC to table at sequential index
                npc_obj = global_sig_to_npc[sig]
                unique_npcs.append(npc_obj)
                sig_to_index[sig] = base_index + i

            # Store mapping for this clone group
            clone_group_mapping[(room_idx, parent_obj_idx)] = sig_to_index

        # Third pass: build global fallback mapping for all signatures
        # This is used for objects that aren't part of a clone group (standalone parents with no clones)
        # We need ALL signatures here because a signature might appear in a clone group in one room
        # but as a standalone object in another room
        global_fallback_mapping = {}
        for sig in all_signatures:
            # Check if this signature is already in the NPC table (from a clone group)
            already_in_table = False
            existing_index = None
            for group_mapping in clone_group_mapping.values():
                if sig in group_mapping:
                    already_in_table = True
                    existing_index = group_mapping[sig]
                    break

            if already_in_table:
                # Reuse the existing table index
                global_fallback_mapping[sig] = existing_index
            else:
                # Add new entry to table
                idx = len(unique_npcs)
                unique_npcs.append(global_sig_to_npc[sig])
                global_fallback_mapping[sig] = idx

        # Store fallback mapping for non-clone-group objects
        clone_group_mapping[(-1, -1)] = global_fallback_mapping

        return unique_npcs, clone_group_mapping

    def _create_merged_npc(self, base_npc: NPC, room_obj: BaseRoomObject) -> NPC:
        """Create a new NPC with room-level overrides merged in."""
        # Start with base NPC properties
        merged = NPC(
            sprite_id=base_npc.sprite_id,
            shadow_size=room_obj.shadow_size if room_obj.shadow_size is not None else base_npc.shadow_size,
            acute_axis=room_obj.acute_axis if room_obj.acute_axis is not None else base_npc.acute_axis,
            obtuse_axis=room_obj.obtuse_axis if room_obj.obtuse_axis is not None else base_npc.obtuse_axis,
            height=room_obj.height if room_obj.height is not None else base_npc.height,
            y_shift=room_obj.y_shift if room_obj.y_shift is not None else base_npc.y_shift,
            show_shadow=room_obj.show_shadow if room_obj.show_shadow is not None else base_npc.show_shadow,
            directions=room_obj.directions if room_obj.directions is not None else base_npc.directions,
            min_vram_size=room_obj.min_vram_size if room_obj.min_vram_size is not None else base_npc.min_vram_size,
            priority_0=room_obj.priority_0 if room_obj.priority_0 is not None else base_npc.priority_0,
            priority_1=room_obj.priority_1 if room_obj.priority_1 is not None else base_npc.priority_1,
            priority_2=room_obj.priority_2 if room_obj.priority_2 is not None else base_npc.priority_2,
            cannot_clone=room_obj.cannot_clone if room_obj.cannot_clone is not None else base_npc.cannot_clone,
            byte2_bit0=room_obj.byte2_bit0 if room_obj.byte2_bit0 is not None else base_npc.byte2_bit0,
            byte2_bit1=room_obj.byte2_bit1 if room_obj.byte2_bit1 is not None else base_npc.byte2_bit1,
            byte2_bit2=room_obj.byte2_bit2 if room_obj.byte2_bit2 is not None else base_npc.byte2_bit2,
            byte2_bit3=room_obj.byte2_bit3 if room_obj.byte2_bit3 is not None else base_npc.byte2_bit3,
            byte2_bit4=room_obj.byte2_bit4 if room_obj.byte2_bit4 is not None else base_npc.byte2_bit4,
            byte5_bit6=room_obj.byte5_bit6 if room_obj.byte5_bit6 is not None else base_npc.byte5_bit6,
            byte5_bit7=room_obj.byte5_bit7 if room_obj.byte5_bit7 is not None else base_npc.byte5_bit7,
            byte6_bit2=room_obj.byte6_bit2 if room_obj.byte6_bit2 is not None else base_npc.byte6_bit2,
        )
        return merged

    def _build_partition_table(self) -> tuple[list[Partition], dict]:
        """Build partition table.

        Returns:
            Tuple of (unique_partitions, room_to_partition_index)

        Raises:
            ValueError: If more than 128 unique partitions when large_partition_table is False
        """
        # Collect unique partitions (max 128)
        MAX_PARTITIONS = 128 if not self._large_partition_table else 256
        unique_partitions: list[Partition] = []
        partition_to_index: dict[int, int] = {}  # id(partition) -> index
        room_to_partition_index: dict[int, int] = {}

        for room_idx, room in enumerate(self._rooms):
            if room is None or room.partition is None:
                room_to_partition_index[room_idx] = 0  # Default partition
                if 0 not in partition_to_index:
                    # Add default partition
                    unique_partitions.append(Partition())
                    partition_to_index[0] = 0
                continue

            # Check if we already have this partition
            partition_id = None
            for existing_idx, existing_partition in enumerate(unique_partitions):
                if existing_partition.is_same(room.partition):
                    partition_id = existing_idx
                    break

            if partition_id is None:
                # New unique partition
                if len(unique_partitions) >= MAX_PARTITIONS:
                    raise ValueError(
                        f"Too many unique partitions: {len(unique_partitions)} exceeds maximum of {MAX_PARTITIONS}. "
                        f"Consider using --large-partition-table flag."
                    )
                partition_id = len(unique_partitions)
                unique_partitions.append(room.partition)
                partition_to_index[id(room.partition)] = partition_id

            room_to_partition_index[room_idx] = partition_id

        return unique_partitions, room_to_partition_index

    def render(self) -> dict[int, bytearray]:
        """Render all rooms to ROM patches.

        Returns:
            Dictionary mapping ROM addresses to byte data to write at those addresses

        Raises:
            ValueError: If constraints are violated
        """
        patches = {}

        # Build NPC table with intelligent sequential placement for clone groups
        clone_groups = self._collect_clone_group_requirements()
        unique_npcs, clone_group_mapping = self._build_sequential_placement(clone_groups)

        # Verify NPC count doesn't exceed maximum
        import sys
        print(f"DEBUG: RoomCollection.render() - {len(unique_npcs)} unique NPCs to patch")
        sys.stdout.flush()
        # Debug: Check for sprite 717 in unique NPCs
        for idx, npc in enumerate(unique_npcs):
            if npc.sprite_id == 717:
                print(f"DEBUG: NPC table index {idx} has sprite_id=717")
                sys.stdout.flush()
        if len(unique_npcs) > 1462:
            raise ValueError(
                f"Too many unique NPCs: {len(unique_npcs)} exceeds maximum of 1462. "
                f"Reduce the number of unique NPC variants across all rooms."
            )

        # Build partition table
        partitions, room_to_partition_index = self._build_partition_table()

        # Write partition table bank pointer
        if self._large_partition_table:
            # Write [0xE0 0xEB] to 0x008BB0 and 0x008B9D
            patches[0x008BB0] = bytearray([0xE0, 0xEB])
            patches[0x008B9D] = bytearray([0xE0, 0xEB])

            # Write partitions to 0x1DEBE0-0x1DF3DF (256 partitions * 4 bytes)
            partition_start = 0x1DEBE0
            assert len(partitions) <= 256, f"Expected at most 256 partitions, got {len(partitions)}"
        else:
            # Write [0x00 0xDE] to 0x008BB0 and 0x008B9D
            patches[0x008BB0] = bytearray([0x00, 0xDE])
            patches[0x008B9D] = bytearray([0x00, 0xDE])

            # Write partitions to 0x1DDE00-0x1DDFFF (128 partitions * 4 bytes)
            partition_start = 0x1DDE00
            assert len(partitions) <= 128, f"Expected at most 128 partitions, got {len(partitions)}"

        for idx, partition in enumerate(partitions):
            offset = partition_start + (idx * 4)
            patches[offset] = self._render_partition(partition)

        # Write NPC table to 0x1DB800-0x1DDDFF (or 0x1DDFFF with large partition table)
        npc_start = 0x1DB800
        for idx, npc in enumerate(unique_npcs):
            offset = npc_start + (idx * 7)
            patches[offset] = self._render_npc(npc)

        # Fill remaining NPC slots with 0xFF
        # End address depends on whether we're using large partition table
        if self._large_partition_table:
            npc_end = 0x1DE000  # Extended range
        else:
            npc_end = 0x1DDE00  # Standard range (stops before partition table)

        max_npc_slots = (npc_end - npc_start) // 7
        for idx in range(len(unique_npcs), max_npc_slots):
            offset = npc_start + (idx * 7)
            patches[offset] = bytearray([0xFF] * 7)

        # Render room object data (NPCs)
        room_object_patches = self._render_room_objects(clone_group_mapping, room_to_partition_index)
        patches.update(room_object_patches)

        # Render event data
        event_patches = self._render_events()
        patches.update(event_patches)

        # Render exit data
        exit_patches = self._render_exits()
        patches.update(exit_patches)

        return patches

    def _render_partition(self, partition: Partition) -> bytearray:
        """Render a partition to 4 bytes."""
        data = bytearray(4)

        # Byte 0
        data[0] = (partition.ally_sprite_buffer_size << 5) | (0x10 if partition.allow_extra_sprite_buffer else 0) | partition.extra_sprite_buffer_size | (0x80 if partition.full_palette_buffer else 0)

        # Bytes 1-3: buffers
        for buf_idx in range(3):
            buf = partition.buffers[buf_idx]
            byte_val = buf.buffer_type | (buf.main_buffer_space << 4) | (0x80 if buf.index_in_main_buffer else 0)
            data[buf_idx + 1] = byte_val

        return data

    def _render_npc(self, npc: NPC) -> bytearray:
        """Render an NPC to 7 bytes."""
        data = bytearray(7)

        # Bytes 0-1: sprite_id (10 bits) + vram_store (3 bits) + vram_size (3 bits)
        data[0] = npc.sprite_id & 0xFF
        data[1] = ((npc.sprite_id >> 8) & 0x03) | ((npc.directions & 0x07) << 2) | ((npc.min_vram_size & 0x07) << 5)

        # Byte 2: priority and misc bits
        data[2] = (
            (1 if npc.byte2_bit0 else 0) |
            ((1 if npc.byte2_bit1 else 0) << 1) |
            ((1 if npc.byte2_bit2 else 0) << 2) |
            ((1 if npc.byte2_bit3 else 0) << 3) |
            ((1 if npc.byte2_bit4 else 0) << 4) |
            ((1 if npc.priority_0 else 0) << 5) |
            ((1 if npc.priority_1 else 0) << 6) |
            ((1 if npc.priority_2 else 0) << 7)
        )

        # Byte 3: y_shift (4 bits) + shift_16_px_down (1 bit) + shadow_size (2 bits) + cannot_clone (1 bit)
        y_shift_val = npc.y_shift if npc.y_shift >= 0 else npc.y_shift + 16
        shift_16_down = 1 if npc.y_shift < 0 else 0
        data[3] = (y_shift_val & 0x0F) | ((shift_16_down) << 4) | ((npc.shadow_size & 0x03) << 5) | ((1 if npc.cannot_clone else 0) << 7)

        # Byte 4: acute_axis (4 bits) + obtuse_axis (4 bits)
        data[4] = (npc.acute_axis & 0x0F) | ((npc.obtuse_axis & 0x0F) << 4)

        # Byte 5: height (5 bits) + show_shadow (1 bit) + byte5_bit6 (1 bit) + byte5_bit7 (1 bit)
        data[5] = (npc.height & 0x1F) | ((1 if npc.show_shadow else 0) << 5) | ((1 if npc.byte5_bit6 else 0) << 6) | ((1 if npc.byte5_bit7 else 0) << 7)

        # Byte 6: byte6_bit2 and reserved bits
        data[6] = ((1 if npc.byte6_bit2 else 0) << 2)

        return data

    def _render_room_objects(self, clone_group_mapping: dict[tuple[int, int], dict[tuple, int]],
                            room_to_partition_index: dict[int, int]) -> dict[int, bytearray]:
        """Render room object (NPC) data.

        Pointer table: 0x148000-0x1483FF (512 rooms * 2 bytes)
        Base address: 0x140000
        Data starts at: offset 0x8400 (ROM address 0x148400)

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x148000
        base_address = 0x140000

        # Starting offset (without base) - matches LazyShell's offsetStart = 0x8400
        offset_without_base = 0x8400

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (offset without base address)
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                offset_without_base & 0xFF,
                (offset_without_base >> 8) & 0xFF
            ])

            if room is None or len(room.objects) == 0:
                # Empty room - next room will have same pointer (zero delta)
                continue

            # Build this room's data
            room_data = bytearray()

            # First byte: partition ID
            partition_id = room_to_partition_index.get(room_idx, 0)
            room_data.append(partition_id)

            # Render each object (track parent and base values for clones)
            last_parent = None
            last_parent_obj_idx = -1
            last_base_values = None  # (base_npc, base_action, base_event/base_pack)
            obj_idx = 0
            while obj_idx < len(room.objects):
                obj = room.objects[obj_idx]

                if isinstance(obj, Clone):
                    # This is a clone, render it with base values from parent
                    obj_data, _ = self._render_room_object(
                        obj, clone_group_mapping, last_parent, None,
                        room_idx, obj_idx, last_parent_obj_idx, last_base_values
                    )
                    room_data.extend(obj_data)
                    obj_idx += 1
                else:
                    # This is a parent object - collect all consecutive clones
                    clones = []
                    check_idx = obj_idx + 1
                    while check_idx < len(room.objects) and isinstance(room.objects[check_idx], Clone):
                        clones.append(room.objects[check_idx])
                        check_idx += 1

                    # Render parent with clones (to calculate proper base values and offsets)
                    obj_data, base_values = self._render_room_object(
                        obj, clone_group_mapping, None, clones,
                        room_idx, obj_idx, obj_idx, None
                    )
                    # Update byte 0 with clone count
                    obj_data[0] = (obj.object_type << 4) | (len(clones) & 0x0F)
                    room_data.extend(obj_data)

                    last_parent = obj
                    last_parent_obj_idx = obj_idx
                    last_base_values = base_values
                    obj_idx += 1

            # Write this room's data at its ROM address (base + offset)
            rom_address = base_address + offset_without_base
            patches[rom_address] = room_data

            # Update offset for next room
            offset_without_base += len(room_data)

        return patches

    def _render_room_object(self, obj: BaseRoomObject, clone_group_mapping: dict[tuple[int, int], dict[tuple, int]],
                           parent: RoomObject | None = None, clones: list[Clone] | None = None,
                           room_idx: int = -1, obj_idx: int = -1, parent_obj_idx: int = -1,
                           base_values: tuple | None = None) -> tuple[bytearray, tuple | None]:
        """Render a single room object to bytes.

        Args:
            obj: The room object to render
            clone_group_mapping: Context-aware mapping from (room_idx, parent_obj_idx) to {signature: table_index}
            parent: The parent object (required for clones)
            clones: List of clones following this parent object (used to calculate base values and offsets)
            room_idx: The room index (for error reporting)
            obj_idx: The object index within the room (for error reporting)
            parent_obj_idx: The parent object index (for looking up the correct NPC mapping)
        """
        # Get NPC index using context-aware mapping
        obj_sig = self._get_npc_signature(obj._npc, obj)

        # Look up the mapping for this clone group (or fallback for non-clone-group objects)
        if (room_idx, parent_obj_idx) in clone_group_mapping:
            sig_to_index = clone_group_mapping[(room_idx, parent_obj_idx)]
        else:
            # Use fallback mapping for standalone objects (not in a clone group)
            sig_to_index = clone_group_mapping[(-1, -1)]

        npc_index = sig_to_index[obj_sig]

        if isinstance(obj, Clone):
            # Clone: 4 bytes
            # Follows disassembler lines 744-784
            if parent is None:
                raise ValueError("Clone object requires parent object")

            data = bytearray(4)

            # Byte 0: Offsets (type-specific encoding)
            # IMPORTANT: All offsets are relative to BASE values, not parent's individual values!
            # LazyShell calculates: clone_value = base_value + clone_offset
            if base_values is None:
                raise ValueError(f"base_values required for clone rendering at room {room_idx} obj {obj_idx}")

            if isinstance(obj, RegularClone):
                assert isinstance(parent, RegularNPC), "Parent must be RegularNPC for RegularClone"
                # (event_offset << 5) + (action_offset << 3) + npc_offset
                # Note: action_offset is only 2 bits (0-3 range) for RegularClone

                # Unpack base values: (base_assigned_npc, base_action_script, base_event_script)
                base_assigned_npc, base_action_script, base_event_script = base_values

                # Calculate offsets relative to BASE values
                npc_offset = npc_index - base_assigned_npc
                action_offset = obj.action_script - base_action_script
                event_offset = obj.event_script - base_event_script

                data[0] = ((event_offset & 0x07) << 5) | ((action_offset & 0x03) << 3) | (npc_offset & 0x07)
            elif isinstance(obj, ChestClone):
                assert isinstance(parent, ChestNPC), "Parent must be ChestNPC for ChestClone"
                # (upper_70a7 << 4) + lower_70a7
                data[0] = (obj.upper_70a7 << 4) | (obj.lower_70a7 & 0x0F)
            elif isinstance(obj, BattlePackClone):
                assert isinstance(parent, BattlePackNPC), "Parent must be BattlePackNPC for BattlePackClone"
                # (pack_offset << 4) + action_offset

                # Unpack base values: (base_assigned_npc, base_action_script, base_battle_pack)
                base_assigned_npc, base_action_script, base_battle_pack = base_values

                # Calculate offsets relative to BASE values
                action_offset = obj.action_script - base_action_script
                pack_offset = obj.battle_pack - base_battle_pack

                data[0] = ((pack_offset & 0x0F) << 4) | (action_offset & 0x0F)
            else:
                data[0] = 0

            # Byte 1: (visible << 7) | x
            data[1] = (1 if obj.visible else 0) << 7 | (obj.x & 0x7F)

            # Byte 2: (z_half << 7) | y
            data[2] = (1 if obj.z_half else 0) << 7 | (obj.y & 0x7F)

            # Byte 3: (direction << 5) | z
            data[3] = (obj.direction << 5) | (obj.z & 0x1F)

            return data, None  # Clones don't return base values

        else:
            assert isinstance(obj, RoomObject), "Parent object must be RoomObject"
            # Parent object: 12 bytes + (extra_length * 4)
            # Follows disassembler lines 625-738

            # Calculate extra_length (number of clones)
            extra_length = 0
            # This will be set by _render_room_objects based on consecutive clones

            data = bytearray(12)

            # Byte 0: (object_type << 4) | extra_length
            # Note: extra_length will be updated by caller
            data[0] = (obj.object_type << 4) | 0  # Placeholder for extra_length

            # Byte 1: Movement flags byte 1
            # speed (bits 0-2), face_on_trigger (bit 3), cant_enter_doors (bit 4),
            # byte2_bit5 (bit 5), set_sequence_playback (bit 6), cant_float (bit 7)
            data[1] = (
                (obj.speed & 0x07) |
                ((1 if obj.face_on_trigger else 0) << 3) |
                ((1 if obj.cant_enter_doors else 0) << 4) |
                ((1 if obj.byte2_bit5 else 0) << 5) |
                ((1 if obj.set_sequence_playback else 0) << 6) |
                ((1 if obj.cant_float else 0) << 7)
            )

            # Byte 2: Movement flags byte 2
            data[2] = (
                (1 if obj.cant_walk_up_stairs else 0) |
                ((1 if obj.cant_walk_under else 0) << 1) |
                ((1 if obj.cant_pass_walls else 0) << 2) |
                ((1 if obj.cant_jump_through else 0) << 3) |
                ((1 if obj.cant_pass_npcs else 0) << 4) |
                ((1 if obj.byte3_bit5 else 0) << 5) |
                ((1 if obj.cant_walk_through else 0) << 6) |
                ((1 if obj.byte3_bit7 else 0) << 7)
            )

            # Calculate base values and offsets for parent + clones
            # We need to find the minimum value among parent and all clones for:
            # - assigned_npc (for RegularNPC)
            # - action_script (for all types except ChestNPC)
            # - event_script (for RegularNPC)
            # - battle_pack (for BattlePackNPC)

            clones = clones if clones is not None else []

            # Calculate base_assigned_npc (minimum NPC index among parent + clones)
            # NOTE: Only RegularNPC/RegularClone use assigned_npc offsets in byte 8!
            # ChestNPC and BattlePackNPC don't have assigned_npc offsets.
            if isinstance(obj, RegularNPC):
                all_npc_indices = [npc_index]
                for clone in clones:
                    if isinstance(clone, RegularClone):
                        clone_sig = self._get_npc_signature(clone._npc, clone)
                        clone_npc_index = sig_to_index[clone_sig]
                        all_npc_indices.append(clone_npc_index)
                base_assigned_npc = min(all_npc_indices)
                assigned_npc_offset = npc_index - base_assigned_npc

                if assigned_npc_offset > 7:
                    import logging
                    msg = (
                        f"⚠️  Room {room_idx} object {obj_idx}: Large assigned_npc offset detected!\n"
                        f"  assigned_npc offset: {assigned_npc_offset} out of range [0, 7]\n"
                        f"  Parent assigned_npc: {obj.assigned_npc}\n"
                        f"  Base action_script: {base_action_script}"
                    )
                    logging.warning(msg)
            else:
                # ChestNPC and BattlePackNPC: no assigned_npc offset, just use npc_index directly
                base_assigned_npc = npc_index
                assigned_npc_offset = 0

            # Calculate base_action_script (minimum action_script among parent + clones)
            if not isinstance(obj, ChestNPC):
                all_action_scripts = [obj.action_script]
                for clone in clones:
                    all_action_scripts.append(clone.action_script)
                base_action_script = min(all_action_scripts)
                action_script_offset = obj.action_script - base_action_script
            else:
                base_action_script = obj.action_script
                action_script_offset = 0

            if action_script_offset > (15 if isinstance(obj, BattlePackNPC) else 3):
                import logging
                msg = (
                    f"⚠️  Room {room_idx} object {obj_idx}: Large action_script offset detected!\n"
                    f"  action_script offset: {action_script_offset} out of range [0, 15]\n"
                    f"  Parent action_script: {obj.action_script}\n"
                    f"  Base action_script: {base_action_script}"
                )
                logging.warning(msg)

            # Bytes 3-5: NPC ID and action script (packed)
            # base_assigned_npc = ((d[offset + 4] & 0x0F) << 6) + (d[offset + 3] >> 2)
            # base_action_script = ((d[offset + 5] & 0x3F) << 4) + ((d[offset + 4] & 0xFF) >> 4)

            # Byte 3: (base_npc_id << 2) low 8 bits + slidable_along_walls (bit 0) + cant_move_if_in_air (bit 1)
            data[3] = ((base_assigned_npc << 2) & 0xFF) | (1 if obj.slidable_along_walls else 0) | ((1 if obj.cant_move_if_in_air else 0) << 1)

            # Byte 4: (action_script low 4 bits << 4) + (base_npc_id >> 6)
            data[4] = ((base_action_script & 0x0F) << 4) | ((base_assigned_npc >> 6) & 0x0F)

            # Byte 5: byte7_upper2 (bits 6-7) + (action_script >> 4 in low 6 bits)
            data[5] = ((obj.byte7_upper2 & 0x03) << 6) | ((base_action_script >> 4) & 0x3F)

            # Bytes 6-7: Event ID or battle pack + initiator
            if isinstance(obj, BattlePackNPC):
                # Calculate base_battle_pack (minimum battle_pack among parent + clones)
                all_battle_packs = [obj.battle_pack]
                for clone in clones:
                    if isinstance(clone, BattlePackClone):
                        all_battle_packs.append(clone.battle_pack)
                base_battle_pack = min(all_battle_packs)
                battle_pack_offset = obj.battle_pack - base_battle_pack

                # Debug logging for battle_pack (LazyShell max is 255 for BattlePack NPCs!)
                if base_battle_pack > 255:
                    import logging
                    msg = (
                        f"⚠️  Room {room_idx} object {obj_idx}: Large battle_pack detected!\n"
                        f"  base_battle_pack: {base_battle_pack} (LazyShell max for BattlePack NPC: 255)\n"
                        f"  Parent battle_pack: {obj.battle_pack}\n"
                        f"  All battle_packs in group: {all_battle_packs}"
                    )
                    logging.warning(msg)
                if battle_pack_offset > 15:
                    import logging
                    msg = (
                        f"⚠️  Room {room_idx} object {obj_idx}: Large battle_pack offset detected!\n"
                        f"  battle_pack offset: {battle_pack_offset} out of range [0, 15]\n"
                        f"  Parent battle_pack: {obj.battle_pack}\n"
                        f"  Base battle_pack: {base_battle_pack}"
                    )
                    logging.warning(msg)

                # Byte 6: base_battle_pack
                data[6] = base_battle_pack & 0xFF
                # Byte 7: (initiator << 4) + after_battle
                data[7] = (obj.initiator << 4) | (obj.after_battle & 0x0F)
            else:
                assert isinstance(obj, (RegularNPC, ChestNPC)), "Parent object must be RegularNPC, ChestNPC, or BattlePackNPC"

                if isinstance(obj, RegularNPC):
                    # Calculate base_event_script (minimum event_script among parent + clones)
                    all_event_scripts = [obj.event_script]
                    for clone in clones:
                        if isinstance(clone, RegularClone):
                            all_event_scripts.append(clone.event_script)
                    base_event_script = min(all_event_scripts)
                    event_script_offset = obj.event_script - base_event_script
                else:
                    # ChestNPC
                    base_event_script = obj.event_script
                    event_script_offset = 0

                # Debug logging for event_script
                if event_script_offset > 7:
                    import logging
                    msg = (
                        f"⚠️  Room {room_idx} object {obj_idx}: Large event_script offset detected!\n"
                        f"  event_script offset: {event_script_offset} out of range [0, 7]\n"
                        f"  Parent event_script: {obj.event_script}\n"
                        f"  Base event_script: {base_event_script}"
                    )
                    logging.warning(msg)

                # Regular or Chest NPC
                # Byte 6: base_event_id low 8 bits
                data[6] = base_event_script & 0xFF
                # Byte 7: (initiator << 4) + base_event_id high 4 bits
                data[7] = (obj.initiator << 4) | ((base_event_script >> 8) & 0x0F)

            # Byte 8: Offsets (calculated from parent's values relative to base)
            if isinstance(obj, RegularNPC):
                # (event_offset << 5) + (action_offset << 3) + npc_offset
                # Note: action_offset is only 2 bits (0-3 range) for RegularNPC
                # Validate offsets are in range
                if assigned_npc_offset < 0 or assigned_npc_offset > 7:
                    # Build detailed error message
                    clone_indices = []
                    for clone in clones:
                        if isinstance(clone, RegularClone):
                            clone_sig = self._get_npc_signature(clone._npc, clone)
                            clone_npc_index = npc_signature_to_index[clone_sig]
                            clone_indices.append(clone_npc_index)

                    raise ValueError(
                        f"Room {room_idx} object {obj_idx} (RegularNPC):\n"
                        f"  assigned_npc offset {assigned_npc_offset} out of range [0, 7]\n"
                        f"  Parent NPC index: {npc_index}\n"
                        f"  Clone NPC indices: {clone_indices}\n"
                        f"  Base assigned_npc: {base_assigned_npc}\n"
                        f"  All NPC indices in group: {all_npc_indices}"
                    )
                if action_script_offset < 0 or action_script_offset > 3:
                    raise ValueError(
                        f"Room {room_idx} object {obj_idx} (RegularNPC):\n"
                        f"  action_script offset {action_script_offset} out of range [0, 3]\n"
                        f"  Parent action_script: {obj.action_script}\n"
                        f"  Base action_script: {base_action_script}"
                    )
                if event_script_offset < 0 or event_script_offset > 7:
                    raise ValueError(
                        f"Room {room_idx} object {obj_idx} (RegularNPC):\n"
                        f"  event_script offset {event_script_offset} out of range [0, 7]\n"
                        f"  Parent event_script: {obj.event_script}\n"
                        f"  Base event_script: {base_event_script}"
                    )

                data[8] = ((event_script_offset & 0x07) << 5) | ((action_script_offset & 0x03) << 3) | (assigned_npc_offset & 0x07)
            elif isinstance(obj, ChestNPC):
                # (upper_70a7 << 4) + lower_70a7
                data[8] = (obj.upper_70a7 << 4) | (obj.lower_70a7 & 0x0F)
            elif isinstance(obj, BattlePackNPC):
                # (pack_offset << 4) + action_offset
                # Validate offsets are in range
                if battle_pack_offset < 0 or battle_pack_offset > 15:
                    raise ValueError(
                        f"Room {room_idx} object {obj_idx} (BattlePackNPC):\n"
                        f"  battle_pack offset {battle_pack_offset} out of range [0, 15]\n"
                        f"  Parent battle_pack: {obj.battle_pack}\n"
                        f"  Base battle_pack: {base_battle_pack}"
                    )
                if action_script_offset < 0 or action_script_offset > 15:
                    raise ValueError(
                        f"Room {room_idx} object {obj_idx} (BattlePackNPC):\n"
                        f"  action_script offset {action_script_offset} out of range [0, 15]\n"
                        f"  Parent action_script: {obj.action_script}\n"
                        f"  Base action_script: {base_action_script}"
                    )

                data[8] = ((battle_pack_offset & 0x0F) << 4) | (action_script_offset & 0x0F)
            else:
                data[8] = 0

            # Byte 9: (visible << 7) | x
            data[9] = (1 if obj.visible else 0) << 7 | (obj.x & 0x7F)

            # Byte 10: (z_half << 7) | y
            data[10] = (1 if obj.z_half else 0) << 7 | (obj.y & 0x7F)

            # Byte 11: (direction << 5) | z
            data[11] = (obj.direction << 5) | (obj.z & 0x1F)

            # Return base values for clones to use
            if isinstance(obj, RegularNPC):
                return data, (base_assigned_npc, base_action_script, base_event_script)
            elif isinstance(obj, BattlePackNPC):
                return data, (base_assigned_npc, base_action_script, base_battle_pack)
            else:  # ChestNPC
                return data, (base_assigned_npc, base_action_script, base_event_script)

    def _render_events(self) -> dict[int, bytearray]:
        """Render event data.

        Pointer table: 0x20E000-0x20E3FF (512 rooms * 2 bytes)
        Base address: 0x200000
        Data starts at: offset 0xE400 (ROM address 0x20E400)

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x20E000
        base_address = 0x200000

        # Starting offset (without base) - matches LazyShell's offsetStart = 0xE400
        offset_without_base = 0xE400

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (offset without base address)
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                offset_without_base & 0xFF,
                (offset_without_base >> 8) & 0xFF
            ])

            # Build this room's data
            room_data = bytearray()

            # Always write 3-byte header (music + entrance_event)
            if room is None:
                # Default header
                room_data.extend([0x00, 0x00, 0x00])
            else:
                assert isinstance(room, Room), "Expected Room instance"
                # Write music (byte 0) and entrance_event (bytes 1-2, little-endian)
                room_data.append(room.music)
                room_data.append(room.entrance_event & 0xFF)
                room_data.append((room.entrance_event >> 8) & 0xFF)

                # Write event tiles if any
                if room.event_tiles:
                    for event in room.event_tiles:
                        event_data = self._render_event(event)
                        room_data.extend(event_data)

            # Write this room's data at its ROM address (base + offset)
            rom_address = base_address + offset_without_base
            patches[rom_address] = room_data

            # Update offset for next room
            offset_without_base += len(room_data)

        return patches

    def _render_event(self, event) -> bytearray:
        """Render a single event tile to bytes.

        Follows disassembler lines 424-454.
        """
        from smrpgpatchbuilder.datatypes.levels.classes import Event

        if isinstance(event, Event):
            # Event: 5 or 6 bytes depending on length
            # Disassembler reads:
            # trigger_data[0-1]: event value (12 bits, little-endian)
            # trigger_data[2]: x + (nw_se_edge_active << 7)
            # trigger_data[3]: y + (ne_sw_edge_active << 7)
            # trigger_data[4]: z + (height << 5)
            # trigger_data[5] (optional): (length-1) + (byte_8_bit_4 << 4) + (f << 7)

            # Byte 0-1: event value (12 bits little-endian)
            data = bytearray()
            data.append(event.event & 0xFF)
            data.append((event.event >> 8) & 0x0F)

            # Check if we need the length byte
            if event.length > 1:
                data[1] |= 0x80  # Set bit 7 to indicate length byte present

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((event.x & 0x7F) | ((1 if event.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((event.y & 0x7F) | ((1 if event.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((event.z & 0x1F) | ((event.height & 0x07) << 5))

            # Byte 5 (optional): length and flags
            if event.length > 1:
                data.append(
                    ((event.length - 1) & 0x0F) |
                    ((1 if event.byte_8_bit_4 else 0) << 4) |
                    ((event.f & 0x01) << 7)
                )

            return data
        else:
            # Unknown event type
            return bytearray()

    def _render_exits(self) -> dict[int, bytearray]:
        """Render exit data.

        Pointer table: 0x1D2D64-0x1D3165 (512 rooms * 2 bytes)
        Base address: 0x1D0000
        Data starts at: offset 0x3166 (ROM address 0x1D3166)

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x1D2D64
        base_address = 0x1D0000

        # Starting offset (without base) - matches LazyShell's offsetStart = 0x3166
        offset_without_base = 0x3166

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (offset without base address)
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                offset_without_base & 0xFF,
                (offset_without_base >> 8) & 0xFF
            ])

            if room is None or not room.exit_fields:
                # Empty room - next room will have same pointer (zero delta)
                continue

            # Build this room's data
            room_data = bytearray()

            # Render exits
            for exit_obj in room.exit_fields:
                exit_data = self._render_exit(exit_obj)
                room_data.extend(exit_data)

            # Write this room's data at its ROM address (base + offset)
            rom_address = base_address + offset_without_base
            patches[rom_address] = room_data

            # Update offset for next room
            offset_without_base += len(room_data)

        return patches

    def _render_exit(self, exit_obj: RoomExit | MapExit) -> bytearray:
        """Render a single exit to bytes.

        Follows disassembler lines 488-551.
        """
        if isinstance(exit_obj, RoomExit):
            # RoomExit: 8 or 9 bytes (+ optional length byte)
            # Disassembler reads:
            # field_data[0-1]: destination (9 bits) + flags
            # field_data[2]: x + (nw_se_edge_active << 7)
            # field_data[3]: y + (ne_sw_edge_active << 7)
            # field_data[4]: z + (height << 5)
            # field_data[5-7]: destination coords (for room exits)
            # field_data[offset] (optional): length byte

            data = bytearray()

            # Byte 0: destination low 8 bits
            data.append(exit_obj.destination & 0xFF)

            # Byte 1: Complex flags byte
            # exit_type = (field_data[1] & 0x60) >> 6
            # dst = ((field_data[1] << 8) + field_data[0]) & 0x1FF
            # length_determinant = field_data[1] & 0x80 == 0x80
            byte1 = (exit_obj.destination >> 8) & 0x01  # Bit 0 of destination
            byte1 |= (0 << 5)  # Exit type 0 for ROOM (bits 5-6)
            if exit_obj.show_message:
                byte1 |= 0x08
            if exit_obj.byte_2_bit_2:
                byte1 |= 0x04
            # Length flag will be set later if needed
            data.append(byte1)

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((exit_obj.x & 0x7F) | ((1 if exit_obj.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((exit_obj.y & 0x7F) | ((1 if exit_obj.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((exit_obj.z & 0x1F) | ((exit_obj.height & 0x07) << 5))

            # Bytes 5-7: Destination properties (for ROOM exits)
            # Byte 5: dst_x + (x_bit_7 << 7)
            data.append((exit_obj.destination_props.x & 0x7F) | ((1 if exit_obj.destination_props.x_bit_7 else 0) << 7))

            # Byte 6: dst_y + (dst_z_half << 7)
            data.append((exit_obj.destination_props.y & 0x7F) | ((1 if exit_obj.destination_props.z_half else 0) << 7))

            # Byte 7: dst_z + (dst_f << 5)
            data.append((exit_obj.destination_props.z & 0x1F) | ((exit_obj.destination_props.f & 0x07) << 5))

            # Optional length byte
            if exit_obj.length > 1 or exit_obj.f != 0:
                data[1] |= 0x80  # Set length flag in byte 1
                data.append(((exit_obj.length - 1) & 0x0F) | ((exit_obj.f & 0x01) << 7))

            return data

        elif isinstance(exit_obj, MapExit):
            # MapExit: 5 or 6 bytes (+ optional length byte)
            data = bytearray()

            # Byte 0: destination low 8 bits
            data.append(exit_obj.destination & 0xFF)

            # Byte 1: Complex flags byte
            byte1 = 0
            byte1 |= (1 << 6)  # Exit type 1 for MAP (bits 5-6 = 01)
            if exit_obj.show_message:
                byte1 |= 0x08
            if exit_obj.byte_2_bit_2:
                byte1 |= 0x04
            if exit_obj.byte_2_bit_1:
                byte1 |= 0x02
            if exit_obj.byte_2_bit_0:
                byte1 |= 0x01
            # Length flag will be set later if needed
            data.append(byte1)

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((exit_obj.x & 0x7F) | ((1 if exit_obj.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((exit_obj.y & 0x7F) | ((1 if exit_obj.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((exit_obj.z & 0x1F) | ((exit_obj.height & 0x07) << 5))

            # Optional length byte
            if exit_obj.length > 1 or exit_obj.f != 0:
                data[1] |= 0x80  # Set length flag in byte 1
                data.append(((exit_obj.length - 1) & 0x0F) | ((exit_obj.f & 0x01) << 7))

            return data

        else:
            # Unknown exit type
            return bytearray()
