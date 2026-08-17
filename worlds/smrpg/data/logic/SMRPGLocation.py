from enum import Enum

from .Requirement import Requirement, RequirementMetaclass
from .Requirements import CanAccessMonstroTown
from ..ItemNames import ItemNames
from ...Options import SMRPGOptions
from ..LocationNames import LocationNames


class SMRPGLocation:
    name: str
    requirements: list[RequirementMetaclass]
    default_item: None | ItemNames

    def __init__(self, name: LocationNames, requirements: list[RequirementMetaclass] = None):
        if requirements is None:
            requirements = list()
        self.name = name.value
        self.requirements = requirements

    def __repr__(self):
        return f"{self.__class__} -- {self.name}"

    def check_enabled(self, options: SMRPGOptions):
        return True

class UnusedLocation(SMRPGLocation):
    def check_enabled(self, options: SMRPGOptions):
        return False

class InvisibleFlagLocation(SMRPGLocation):
    def __init__(self, name: LocationNames, requirements: list[RequirementMetaclass] = None, default_item=None):
        super().__init__(name, requirements)
        self.requirements.append(CanAccessMonstroTown)

    def check_enabled(self, options: SMRPGOptions):
        return False

class StarPieceLocation(SMRPGLocation):
    pass

class BossFightLocation(SMRPGLocation):
    pass

class CharacterRecruitLocation(SMRPGLocation):
    pass

class RemakeLocation(SMRPGLocation):
    def check_enabled(self, options: SMRPGOptions):
        return options.enable_remake_content

class RemakeBossFightLocation(BossFightLocation, RemakeLocation):
    pass

class RemakeStarPieceLocation(StarPieceLocation, RemakeLocation):
    pass

class EXPStarLocation(SMRPGLocation):
    pass