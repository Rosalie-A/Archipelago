import dataclasses
import re
from typing import TYPE_CHECKING, Self, override

from BaseClasses import CollectionState, MultiWorld
from rule_builder.rules import Rule, HasAll, True_, False_, HasAny, HasAllCounts, Has, HasGroupUnique
from .RequirementItem import RequirementItemMetaclass

if TYPE_CHECKING:
    from ...Options import SMRPGOptions
    from ....smrpg import SMRPGWorld


class RequirementMetaclass(type):
    items_needed: list[type[RequirementItemMetaclass]] = []
    other_requirements_or: list[Self] = []
    other_requirements_and: list[Self] = []
    name: str = " ".join(re.split(r'(?=[A-Z, 0-9])', __name__)).strip()

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

    def get_rule(self) -> Rule["SMRPGWorld"]:
        return self.unpack_requirements(True_())

    @classmethod
    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        return HasAll(*[item.name.value for item in self.items_needed])

    def unpack_requirements(self, total_items_needed_rule: Rule["SMRPGWorld"]) -> Rule["SMRPGWorld"]:
        items_needed_rule = self.get_rule_for_items_needed()
        if len(self.other_requirements_and) == 0 and len(self.other_requirements_or) == 0:
            return items_needed_rule & total_items_needed_rule
        unpacked_requirements: list[list[RequirementMetaclass]] = list()
        for requirement in self.other_requirements_or:
            unpacked_requirements_entry: list[RequirementMetaclass] = self.other_requirements_and
            unpacked_requirements_entry.append(requirement)
            unpacked_requirements.append(unpacked_requirements_entry)
        running_and_rule = True_()
        running_or_rule = False_()
        for requirement_list in unpacked_requirements:
            for requirement in requirement_list:
                running_and_rule &= requirement.unpack_requirements(items_needed_rule)
            running_or_rule |= running_and_rule
        return running_or_rule

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return True

class GroupRequirement(Requirement):
    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        return HasAny(*[item.name.value for item in self.items_needed])

class StarPieceRequirement(Requirement):
    count: int = -1
    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        from .RequirementItems import StarPiece
        return Has(StarPiece.name.value, count=self.count)

class BossesRequirement(Requirement):
    count: int = -1
    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        from .RequirementItems import BossFights
        return HasGroupUnique(BossFights.name, count=self.count)



@dataclasses.dataclass()
class CanDamageWithSpells(Rule["SMRPGWorld"], game="Super Mario RPG"):

    @override
    def _instantiate(self, world: "SMRPGWorld") -> Rule.Resolved:
        return self.Resolved(player=world.player)

    class Resolved(Rule.Resolved):
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.can_defeat_with_spells[self.player]

class SpellsRequirement(Requirement):
    def get_rule_for_items_needed(self) -> Rule["SMRPGWorld"]:
        return CanDamageWithSpells()
