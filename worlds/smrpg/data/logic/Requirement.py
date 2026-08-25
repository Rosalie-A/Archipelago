import dataclasses
import re
from typing import TYPE_CHECKING, Self, override

from BaseClasses import CollectionState, MultiWorld
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, HasAll, True_, False_, HasAny, HasAllCounts, Has, HasGroupUnique, Or, Filtered
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
    rule: Rule["SMRPGWorld"] = None
    option_filter: OptionFilter = None

    def get_rule(self) -> Rule["SMRPGWorld"]:
        if self.rule is None:
            rule = HasAll(*[item.name.value for item in self.items_needed])
        else:
            rule = self.rule
        if self.option_filter is not None:
            rule = Filtered(rule, options=[self.option_filter])
        return rule


    def get_name(self):
        return " ".join(re.split(r'(?=[A-Z, 0-9])', self.__name__)).strip()

    def __repr__(self):
        return self.get_name()

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


class OpenRequirement(Requirement):
    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        return True_()

class GroupRequirement(Requirement):
    @classmethod
    def get_rule_for_items_needed(cls) -> Rule["SMRPGWorld"]:
        return HasAny(*[item.name.value for item in cls.items_needed])

class StarPieceRequirement(Requirement):
    count: int = -1

    @classmethod
    def get_rule(cls) -> Rule["SMRPGWorld"]:
        from .RequirementItems import StarPiece
        rule = Has(StarPiece.name.value, count=cls.count)
        if cls.option_filter is not None:
            rule = Filtered(rule, options=[cls.option_filter])
        return rule

class BossesRequirement(Requirement):
    count: int = -1

    @classmethod
    def get_rule(cls) -> Rule["SMRPGWorld"]:
        from .RequirementItems import BossFights
        return HasGroupUnique(BossFights.name, count=cls.count)

def get_rule_from_requirements(requirements: list[RequirementMetaclass], options: "SMRPGOptions") -> Rule["SMRPGWorld"]:
    if len(requirements) == 0:
        return True_()
    else:
        return requirements[0].get_rule()

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
    ItemNames.SUNKEN_SHIP: LocationNames.SUNKEN_SHIP_FINAL_BOSS_FIGHT,
    ItemNames.BELOME_TEMPLE: LocationNames.BELOME_TEMPLE_BOSS_FIGHT,
    ItemNames.SEALED_DOOR: LocationNames.MONSTRO_TOWN_SEALED_DOOR_BOSS_FIGHT,
    ItemNames.NIMBUS_LAND: LocationNames.NIMBUS_LAND_FINAL_BOSS_FIGHT,
    ItemNames.BARREL_VOLCANO: LocationNames.BARREL_VOLCANO_SECOND_BOSS_FIGHT,
    ItemNames.BOWSERS_KEEP: LocationNames.BOWSERS_KEEP_THIRD_BOSS_FIGHT,
    ItemNames.FACTORY: LocationNames.FACTORY_FINAL_BOSS_FIGHT
}

@dataclasses.dataclass()
class CanBeatLocation(Rule["SMRPGWorld"], game="Super Mario RPG"):
    location_name: ItemNames

    @override
    def _instantiate(self, world: "SMRPGWorld") -> Rule.Resolved:
        return self.Resolved(self.location_name, player=world.player)

    class Resolved(Rule.Resolved):
        location_name: ItemNames # noqa

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
    def get_rule(cls) -> Rule["SMRPGWorld"]:
        return CanDamageWithSpells()

class LocationClearRequirement(Requirement):
    @classmethod
    def get_rule(cls) -> Rule["SMRPGWorld"]:
        rule = None
        for item in cls.items_needed:
            if rule is None:
                rule = CanBeatLocation(item.name)
            else:
                rule &= CanBeatLocation(item.name)
        if cls.option_filter is not None:
            rule = Filtered(rule, options=[cls.option_filter])
        return rule