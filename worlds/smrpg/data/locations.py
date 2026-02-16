class LocationData:
    name: str


class NPCLocation(LocationData):
    room_id: int
    npc_id: int

    def __init__(self, name: str, room_id: int, npc_id: int):
        self.name = name
        self.room_id = room_id
        self.npc_id = npc_id


class FlagLocation(LocationData):
    flag_byte: int
    flag_bit: int

    def __init__(self, name: str, flag_byte: int, flag_bit: int):
        self.name = name
        self.flag_byte = flag_byte
        self.flag_bit = flag_bit


all_location_data: list[LocationData] = [
    NPCLocation("Mushroom Way 1 Lower Chest", 203, 0),
    NPCLocation("Mushroom Way 1 Upper Chest", 203, 1),
    FlagLocation("Mushroom Way 1 Toad Rescue", 0x7052, 4),
    NPCLocation("Mushroom Way 2 Ledge Chest", 204, 0),
    FlagLocation("Mushroom Way 2 Toad Rescue", 0x7052, 5),
    NPCLocation("Mushroom Way Right Goomba", 204, 1),
    NPCLocation("Mushroom Way Left Item Remake", 204, 10),
    NPCLocation("Mushroom Way Right Item Remake", 204, 11),
    FlagLocation("Mushroom Way Boss Fight", 0x7052, 6),
    FlagLocation("Mushroom Way Star Piece", 0x7052, 6),
    FlagLocation("Mushroom Way Boss Fight Reward Item", 0x7052, 6),
    FlagLocation("Mushroom Way Character", 0x7052, 6),

]