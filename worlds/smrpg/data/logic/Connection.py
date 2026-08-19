from typing import TYPE_CHECKING

from .Requirement import Requirement, RequirementMetaclass

if TYPE_CHECKING:
    from .SMRPGRegion import SMRPGRegion

class Connection:
    destination: "SMRPGRegion"
    requirements: list[RequirementMetaclass]

    def __init__(self, destination, requirements = None):
        if requirements is None:
            requirements = list()
        self.destination = destination
        self.requirements = requirements
