from BaseClasses import Location
from .logic.regions import all_regions
from .logic import topologies # noqa


class SMRPGLocation(Location):
    game = "Super Mario RPG"


class LocationData:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

id = 1
all_location_data: list[LocationData] = list()

for region in all_regions:
    for location in region.locations:
        new_location = LocationData(location.name, id)
        all_location_data.append(new_location)
        id += 1