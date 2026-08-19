import dataclasses
import re
from typing import TYPE_CHECKING, Self, override

from BaseClasses import CollectionState, MultiWorld
from rule_builder.rules import Rule, HasAll, True_, False_, HasAny, HasAllCounts, Has, HasGroupUnique
from .RequirementItem import RequirementItemMetaclass
from ... import LocationNames, ItemNames

if TYPE_CHECKING:
    from ...Options import SMRPGOptions
    from ....smrpg import SMRPGWorld


class RequirementMetaclass(type):
    items_needed: list[type[RequirementItemMetaclass]] = []
    other_requirements_or: list[Self] = []
    other_requirements_and: list[Self] = []
    name: str = " ".join(re.split(r'(?=[A-Z, 0-9])', __name__)).strip()

    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        return HasAll(*[item.name.value for item in self.items_needed])

    def unpack_requirements(self, options: "SMRPGOptions", total_items_needed_rule: Rule["SMRPGWorld"] = True_()) -> Rule["SMRPGWorld"]:
        if not self.check_option_enabled(options):
            return False_()
        items_needed_rule = self.get_rule_for_items_needed()
        if len(self.other_requirements_and) == 0 and len(self.other_requirements_or) == 0:
            return items_needed_rule & total_items_needed_rule
        unpacked_requirements: list[list[RequirementMetaclass]] = list()
        for requirement in self.other_requirements_or:
            unpacked_requirements_entry: list[RequirementMetaclass] = self.other_requirements_and.copy()
            unpacked_requirements_entry.append(requirement)
            unpacked_requirements.append(unpacked_requirements_entry)
        running_and_rule = True_()
        running_or_rule = False_()
        for requirement_list in unpacked_requirements:
            for requirement in requirement_list:
                running_and_rule &= requirement.unpack_requirements(options, items_needed_rule)
            running_or_rule |= running_and_rule
        return running_or_rule



    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return True

class Requirement(metaclass=RequirementMetaclass):
    """
    Defines a set of requirements for a Connection or Location.
    """
    items_needed: list[type[RequirementItemMetaclass]] = []
    other_requirements_or: list[RequirementMetaclass] = []
    other_requirements_and: list[RequirementMetaclass] = []
    name: str = " ".join(re.split(r'(?=[A-Z, 0-9])', __name__)).strip()

    def __init__(self,
                 items_needed: list[type[RequirementItemMetaclass]],
                 other_requirements_or: list[RequirementMetaclass] = None,
                 other_requirements_and: list[RequirementMetaclass] = None):
        """
        Creates a new Requirement object. The parameters are unpacked into a series of OR requirements where everything
        in ``items_required`` and ``other_requirements_and`` alongside one of the entries in ``other_requirements_or``
        must be met for the Requirement to be passed.

        :param items_needed: A list of items that are all required to be had.
        :param other_requirements_or: A list of Requirement objects.
            If not empty, one of these must be fulfilled in addition to the ``items_needed``.
        :param other_requirements_and: A list of Requirement objects.
            If not empty, all of these must be fulfilled in addition to the ``items_needed``.
        """
        if other_requirements_or is None:
            other_requirements_or = list()
        if other_requirements_and is None:
            other_requirements_and = list()
        self.items_needed = items_needed
        self.other_requirements_or = other_requirements_or
        self.other_requirements_and = other_requirements_and

    def __str__(self):
        return self.__repr__()



class GroupRequirement(Requirement):
    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        return HasAny(*[item.name.value for item in cls.items_needed])

class StarPieceRequirement(Requirement):
    count: int = -1

    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        from .RequirementItems import StarPiece
        return Has(StarPiece.name.value, count=cls.count)

class BossesRequirement(Requirement):
    count: int = -1

    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        from .RequirementItems import BossFights
        return HasGroupUnique(BossFights.name, count=cls.count)

def get_rule_from_requirements(requirements: list[RequirementMetaclass], options: "SMRPGOptions") -> Rule["SMRPGWorld"]:
    rule = None
    for requirement in requirements:
        if rule is None:
            rule = False_()
        new_rule = requirement.unpack_requirements(options)
        rule |= new_rule
    if rule is None:
        rule = True_()
    return rule

@dataclasses.dataclass()
class CanDamageWithSpells(Rule["SMRPGWorld"], game="Super Mario RPG"):

    @override
    def _instantiate(self, world: "SMRPGWorld") -> Rule.Resolved:
        return self.Resolved(player=world.player)

    class Resolved(Rule.Resolved):
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.can_defeat_with_spells[self.player]

location_name_lookup: dict[ItemNames, LocationNames] = {
    ItemNames.MUSHROOM_WAY: LocationNames.MUSHROOM_WAY_BOSS_FIGHT,
    ItemNames.MUSHROOM_KINGDOM: LocationNames.MUSHROOM_KINGDOM_BOSS_FIGHT,
    ItemNames.FOREST_MAZE: LocationNames.FOREST_MAZE_BOSS_FIGHT,
    ItemNames.MOLEVILLE_MINES: LocationNames.MOLEVILLE_MINES_SECOND_BOSS_FIGHT,
    ItemNames.BOOSTER_TOWER: LocationNames.BOOSTER_TOWER_BALCONY_BOSS_FIGHT,
    ItemNames.SEASIDE_TOWN: LocationNames.SEASIDE_TOWN_BOSS_FIGHT,
    ItemNames.BELOME_TEMPLE: LocationNames.BELOME_TEMPLE_BOSS_FIGHT,
    ItemNames.NIMBUS_LAND: LocationNames.NIMBUS_LAND_FINAL_BOSS_FIGHT
}

@dataclasses.dataclass()
class CanBeatLocation(Rule["SMRPGWorld"], game="Super Mario RPG"):
    location_name: ItemNames

    @override
    def _instantiate(self, world: "SMRPGWorld") -> Rule.Resolved:
        return self.Resolved(self.location_name, player=world.player)

    class Resolved(Rule.Resolved):
        location_name: ItemNames



        @override
        def _evaluate(self, state: CollectionState) -> bool:
            location = state.multiworld.get_location(
                location_name_lookup[self.location_name],
                self.player)
            if location.item:
                item = location.item.name
                return state.has(item, self.player)
            else:
                return False

class SpellsRequirement(Requirement):
    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        return CanDamageWithSpells()

class LocationClearRequirement(Requirement):
    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        return CanBeatLocation(cls.items_needed[0].name)