
import settings
import typing

from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region, Entrance, CollectionState
from rule_builder.rules import False_, True_

from worlds.AutoWorld import World, WebWorld, LogicMixin
from .Options import SMRPGOptions
from .data.itempools import get_vanilla_pool

from .data.items import all_item_data
from .data.logic.RequirementItems import DamagingSpells
from .data.locations import all_location_data, SMRPGLocation
from .data.logic.regions import all_regions, MariosPad


class SMRPGSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Final Fantasy Tactics ISO"""
        description = "Super Mario RPG USA ROM File"
        copy_to = "Super Mario RPG - Legend of the Seven Stars (USA).sfc "
        md5s = ["d0b68d68d9efc0558242f5476d1c5b81"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = False

class SpellState(LogicMixin):
    can_defeat_with_spells: dict[int, bool]  # per player

    def init_mixin(self, multiworld: MultiWorld) -> None:
        self.can_defeat_with_spells = {
            player: False for player in multiworld.get_game_players("Super Mario RPG")
        }
        pass

    def copy_mixin(self, new_state: CollectionState) -> CollectionState:
        new_state.can_defeat_with_spells = {
            player: can_defeat for player, can_defeat in self.can_defeat_with_spells.items()
        }
        return new_state

class SMRPGWeb(WebWorld):
    theme = "grass"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Final Fantasy Tactics for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie"]
    )

    tutorials = [setup]

    rich_text_options_doc = True
    #option_groups = fftii_option_groups


class SMRPGWorld(World):
    """
    An open world mod for Final Fantasy Tactics for Archipelago.
    Find all the Zodiac Stones and make your way to Murond Death City to confront Altima!
    """
    settings: typing.ClassVar[SMRPGSettings]
    game = "Super Mario RPG"
    options_dataclass = SMRPGOptions
    options: SMRPGOptions

    web = SMRPGWeb()

    item_name_to_id = {item.name.value: item.game_id for item in all_item_data}
    location_name_to_id = {location.name: location.id for location in all_location_data}
    character_spells: dict[str, list[str]] = {}
    damaging_spells = [member.name.value for member in DamagingSpells.members]

    filler_items = None

    version = "1.0.0"
    debug = False
    topology_present = debug

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.character_spells = {
            "Mario": [],
            "Mallow": [],
            "Geno": [],
            "Bowser": [],
            "Toadstool": [],
        }
        self.filler_items = None

    def create_item(self, name: str) -> "SMRPGItem":
        return SMRPGItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_event(self, name: str) -> "SMRPGItem":
        return SMRPGItem(name, ItemClassification.progression, None, self.player)

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for region_data in all_regions:
            region = Region(region_data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Will be adjusted for different starting regions.
        starting_region = self.get_region(MariosPad.name)
        menu.connect(starting_region)

        # Define connections
        for origin_region_data in all_regions:
            origin_region = self.get_region(origin_region_data.name)
            for connection in origin_region_data.connections:
                rule = None
                for requirement in connection.requirements:
                    if rule is None:
                        rule = False_()
                    new_rule = requirement.get_rule_for_items_needed()
                    rule |= new_rule
                if rule is None:
                    rule = True_()
                connecting_region = self.get_region(connection.destination.name)
                if self.debug:
                    print(f"Connection: {origin_region.name} to {connecting_region.name}")
                connection_name = f"{origin_region.name} to {connecting_region.name}"
                self.create_entrance(origin_region, connecting_region, rule, connection_name)
            for location in origin_region_data.locations:
                if location.check_enabled(self.options):
                    new_location = SMRPGLocation(
                        self.player,
                        location.name,
                        self.location_name_to_id[location.name],
                        origin_region)
                    origin_region.locations.append(new_location)

        if self.debug:
            from Utils import visualize_regions
            visualize_regions(menu, f"smrpgdiagram{self.player}.puml")

    def create_items(self):
        itempool = []
        vanilla_pool = get_vanilla_pool(self.options)
        for item in all_item_data:
            if item.name in vanilla_pool.keys():
                for i in range(vanilla_pool[item.name]):
                    itempool.append(item.name)
        for item in map(self.create_item, itempool):
            self.multiworld.itempool.append(item)

    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and not state.can_defeat_with_spells[self.player] and item.name in self.damaging_spells:
            for character in self.character_spells.keys():
                if state.has(character, self.player) and item.name in self.character_spells[character]:
                    state.can_defeat_with_spells[self.player] = True
                    break
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and state.can_defeat_with_spells[self.player] and item.name in self.damaging_spells:
            state.can_defeat_with_spells[self.player] = False
            for character in self.character_spells.keys():
                if state.has(character, self.player):
                    for spell_name in self.character_spells[character]:
                        if spell_name in self.damaging_spells and state.has(spell_name):
                            state.can_defeat_with_spells[self.player] = True
                            break
                    if state.can_defeat_with_spells[self.player]:
                        break
        return change

    def set_rules(self):
        pass

    def pre_fill(self) -> None:
        pass

    def generate_basic(self):
        pass

    def generate_output(self, output_directory: str) -> None:
        pass

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = ["Potion"]
        return self.random.choice(self.filler_items)


class SMRPGItem(Item):
    game = "Super Mario RPG"
