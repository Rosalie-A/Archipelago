import typing
import logging
from logging import Logger

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

if typing.TYPE_CHECKING:
    from SNIClient import SNIContext
else:
    SNIContext = typing.Any
from . import Rom, Locations

snes_logger: Logger = logging.getLogger("SNES")


class SMRPGClient(SNIClient):
    game = "Super Mario RPG Legend of the Seven Stars"
    locations = Rom.location_data
    location_names = locations.keys()
    location_ids = None

    async def validate_rom(self, ctx: SNIContext) -> bool:
        from SNIClient import snes_read

        rom_name: bytes = await snes_read(ctx, Rom.rom_name_location, 20)
        if rom_name is None or rom_name[:5] != b"SMRPG":
            return False

        ctx.game = self.game
        # While this set of flags indicates a fully remote setup, it's worth noting we'll
        # be doing a hybrid approach, with only some "local" items being sent by the server.
        ctx.items_handling = 0b101
        ctx.rom = rom_name
        return True

    async def game_watcher(self, ctx: SNIContext) -> None:
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        if await self.connection_check(ctx) == False:
            return
        await self.location_check(ctx)
        await self.received_items_check(ctx)
        await self.check_victory(ctx)
        await snes_flush_writes(ctx)

    async def connection_check(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        rom: bytes = await snes_read(ctx, Rom.rom_name_location, 20)
        if rom != ctx.rom:
            ctx.rom = None
            return False

        if ctx.server is None or ctx.slot is None:
            # not successfully connected to a multiworld server, cannot process the game sending items
            return False

        if self.location_ids is None:
            self.location_ids = dict((v, k) for k, v in ctx.location_names.items())

        return await self.check_if_items_sendable(ctx)

    async def location_check(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        for key, value in Rom.location_data.items():
            location_name = key
            location_address = value.address
            location_id = Locations.location_table[location_name].id
            location_data = await snes_read(ctx, location_address, 1)
            location_byte = location_data
            if location_byte is not None and location_id not in ctx.locations_checked:
                location_byte = location_byte[0] & value.bit
                if ((location_byte > 0) and value.set_when_checked) \
                        or ((location_byte == 0) and not value.set_when_checked):
                    ctx.locations_checked.add(location_id)
                    snes_logger.info(
                        f'New Check: {location_name} '
                        f'({len(ctx.locations_checked)}/'
                        f'{len(ctx.missing_locations) + len(ctx.checked_locations)})')
                    await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [location_id]}])

    async def received_items_check(self, ctx):
        from SNIClient import snes_read
        items_received_data = await snes_read(ctx, Rom.items_received_address, 2)
        if items_received_data is None:
            return
        items_received_amount = int.from_bytes(items_received_data, "little")
        if items_received_amount >= len(ctx.items_received):
            return
        item = ctx.items_received[items_received_amount]
        item_id = item.item
        item_name = ctx.item_names[item_id]
        item_data = Rom.item_data[item_name]
        item_inventory_address = 0
        max_index = 0
        if item_data.category == Rom.ItemCategory.item:
            item_inventory_address = Rom.items_inventory_address
            max_index = 29
        elif item_data.category == Rom.ItemCategory.gear:
            item_inventory_address = Rom.gear_inventory_address
            max_index = 30
        elif item_data.category == Rom.ItemCategory.key:
            item_inventory_address = Rom.keys_inventory_address
            max_index = 16
        item_written = await self.write_item_to_inventory(ctx, item_data.id, item_inventory_address, max_index)
        if item_written:
            self.increment_items_received(ctx, items_received_amount)

    async def check_victory(self, ctx):
        if Locations.location_table["Smithy"].id in ctx.locations_checked:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

    def increment_items_received(self, ctx, items_received_amount):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        items_received_amount += 1
        snes_buffered_write(ctx, Rom.items_received_address, items_received_amount.to_bytes(2, 'little'))

    async def write_item_to_inventory(self, ctx, item_id, inventory_address, max_index):
        from SNIClient import snes_buffered_write, snes_read
        current_inventory_data = await snes_read(ctx, inventory_address, max_index)
        if current_inventory_data is None:
            return
        for index, item_byte in enumerate(current_inventory_data):
            if item_byte == 0:
                snes_buffered_write(ctx, inventory_address + index, item_id)
                return True
        return False

    async def check_if_items_sendable(self, ctx):
        from SNIClient import snes_read
        items_sendable_data_1 = await snes_read(ctx, Rom.items_sendable_address_1, 1)
        items_sendable_data_2 = await snes_read(ctx, Rom.items_sendable_address_2, 1)
        if items_sendable_data_1 is None or items_sendable_data_2 is None:
            return False
        if items_sendable_data_1[0] == 0 or items_sendable_data_2[0] in Rom.nonsendable_music_values:
            return False
        return True
