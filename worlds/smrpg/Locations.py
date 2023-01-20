from typing import Dict, List

from BaseClasses import Location
from enum import Enum, auto


class SMRPGRegions(Enum):
    marios_pad = auto()
    mushroom_way = auto()
    mushroom_kingdom = auto()
    bandits_way = auto()
    kero_sewers = auto()
    midas_river = auto()
    tadpole_pond = auto()
    rose_way = auto()
    rose_town = auto()
    forest_maze = auto()
    pipe_vault = auto()
    yoster_isle = auto()
    moleville = auto()
    moleville_mines_back = auto()
    booster_pass = auto()
    booster_tower = auto()
    booster_hill = auto()
    marrymore = auto()
    star_hill = auto()
    seaside_town = auto()
    sea = auto()
    sunken_ship = auto()
    sunken_ship_back = auto()
    lands_end = auto()
    belome_temple = auto()
    monstro_town = auto()
    bean_valley = auto()
    nimbus_land = auto()
    nimbus_castle_front = auto()
    nimbus_castle_middle = auto()
    nimbus_castle_back = auto()
    barrel_volcano = auto()
    bowsers_keep = auto()
    factory = auto()


class LocationData():
    name = ""
    star_piece_eligible = False
    region = None
    id = 0
    rando_name = ""

    def __init__(self, name: str, star_piece_eligible: bool, region: SMRPGRegions, id: int):
        self.name = name
        self.star_piece_eligible = star_piece_eligible
        self.region = region
        self.id = id
        # The internal name used by the randomizer.
        self.rando_name = name.replace(" ", "").replace("'", "")


locations_data = [
    ("Hammer Bros", SMRPGRegions.mushroom_way),
    ("Croco 1 (Boss)", SMRPGRegions.bandits_way),
    ("Mack", SMRPGRegions.mushroom_kingdom),
    ("Pandorite", SMRPGRegions.kero_sewers),
    ("Belome 1", SMRPGRegions.kero_sewers),
    ("Bowyer", SMRPGRegions.forest_maze),
    ("Croco 2 (Boss)", SMRPGRegions.moleville),
    ("Punchinello", SMRPGRegions.moleville_mines_back),
    ("Booster", SMRPGRegions.booster_tower),
    ("Clown Bros", SMRPGRegions.booster_tower),
    ("Bundt", SMRPGRegions.marrymore),
    ("Star Hill", SMRPGRegions.star_hill),
    ("King Calamari", SMRPGRegions.sunken_ship),
    ("Hidon", SMRPGRegions.sunken_ship_back),
    ("Johnny", SMRPGRegions.sunken_ship_back),
    ("Yaridovich (Boss)", SMRPGRegions.seaside_town),
    ("Belome 2", SMRPGRegions.belome_temple),
    ("Jagger", SMRPGRegions.monstro_town),
    ("Jinx 1", SMRPGRegions.monstro_town),
    ("Jinx 2", SMRPGRegions.monstro_town),
    ("Jinx 3 (Boss)", SMRPGRegions.monstro_town),
    ("Culex", SMRPGRegions.monstro_town),
    ("Box Boy", SMRPGRegions.bean_valley),
    ("Mega Smilax", SMRPGRegions.bean_valley),
    ("Dodo", SMRPGRegions.nimbus_castle_front),
    ("Birdo (Boss)", SMRPGRegions.nimbus_castle_middle),
    ("Valentina", SMRPGRegions.nimbus_castle_back),
    ("Czar Dragon", SMRPGRegions.barrel_volcano),
    ("Axem Rangers", SMRPGRegions.barrel_volcano),
    ("Magikoopa", SMRPGRegions.bowsers_keep),
    ("Boomer", SMRPGRegions.bowsers_keep),
    ("Exor", SMRPGRegions.bowsers_keep),
    ("Countdown", SMRPGRegions.factory),
    ("Cloaker and Domino", SMRPGRegions.factory),
    ("Clerk", SMRPGRegions.factory),
    ("Manager", SMRPGRegions.factory),
    ("Director", SMRPGRegions.factory),
    ("Gunyolk", SMRPGRegions.factory),
    ("Smithy", SMRPGRegions.factory),

    ("Mario's Bed", SMRPGRegions.marios_pad),
    ("Croco 1", SMRPGRegions.bandits_way),
    ("Rare Frog Coin Reward", SMRPGRegions.mushroom_kingdom),
    ("Melody Bay Song 1", SMRPGRegions.tadpole_pond),
    ("Melody Bay Song 2", SMRPGRegions.tadpole_pond),
    ("Melody Bay Song 3", SMRPGRegions.tadpole_pond),
    ("Rose Town Sign", SMRPGRegions.rose_town),
    ("Yo'ster Isle Goal", SMRPGRegions.yoster_isle),
    ("Croco 2", SMRPGRegions.moleville),
    ("Booster Tower Ancestors", SMRPGRegions.booster_tower),
    ("Booster Tower Checkerboard ", SMRPGRegions.booster_tower),
    ("Knife Guy", SMRPGRegions.booster_tower),
    ("Seaside Town Key", SMRPGRegions.seaside_town),
    ("Monstro Town Key", SMRPGRegions.monstro_town),
    ("Cricket Jam Chest", SMRPGRegions.lands_end),
    ("Seed", SMRPGRegions.bean_valley),
    ("Nimbus Land Castle Key", SMRPGRegions.nimbus_castle_front),
    ("Birdo", SMRPGRegions.nimbus_castle_middle),
    ("Fertilizer", SMRPGRegions.nimbus_castle_back),

    ("Mushroom Way 1", SMRPGRegions.mushroom_way),
    ("Mushroom Way 2", SMRPGRegions.mushroom_way),
    ("Mushroom Way 3", SMRPGRegions.mushroom_way),
    ("Mushroom Way 4", SMRPGRegions.mushroom_way),
    ("Mushroom KingdomVault 1", SMRPGRegions.mushroom_kingdom),
    ("Mushroom KingdomVault 2", SMRPGRegions.mushroom_kingdom),
    ("Mushroom KingdomVault 3", SMRPGRegions.mushroom_kingdom),
    ("Bandit's Way 1", SMRPGRegions.bandits_way),
    ("Bandit's Way 2", SMRPGRegions.bandits_way),
    ("Bandit's Way Star Chest", SMRPGRegions.bandits_way),
    ("Bandit's Way Dog Jump", SMRPGRegions.bandits_way),
    ("Bandit's Way Croco", SMRPGRegions.bandits_way),
    ("Kero Sewers Pandorite Room", SMRPGRegions.kero_sewers),
    ("Kero Sewers Star Chest", SMRPGRegions.kero_sewers),
    ("Rose Way Platform", SMRPGRegions.rose_way),
    ("Rose Town Store 1", SMRPGRegions.rose_town),
    ("Rose Town Store 2", SMRPGRegions.rose_town),
    ("Gardener Cloud 1", SMRPGRegions.rose_town),
    ("Gardener Cloud 2", SMRPGRegions.rose_town),
    ("Forest Maze 1", SMRPGRegions.forest_maze),
    ("Forest Maze 2", SMRPGRegions.forest_maze),
    ("Forest Maze Underground 1", SMRPGRegions.forest_maze),
    ("Forest Maze Underground 2", SMRPGRegions.forest_maze),
    ("Forest Maze Underground 3", SMRPGRegions.forest_maze),
    ("Forest Maze Red Essence", SMRPGRegions.forest_maze),
    ("Pipe Vault Slide 1", SMRPGRegions.pipe_vault),
    ("Pipe Vault Slide 2", SMRPGRegions.pipe_vault),
    ("Pipe Vault Slide 3", SMRPGRegions.pipe_vault),
    ("Pipe Vault Nippers 1", SMRPGRegions.pipe_vault),
    ("Pipe Vault Nippers 2", SMRPGRegions.pipe_vault),
    ("Yo'ster Isle Entrance", SMRPGRegions.yoster_isle),
    ("Moleville Mines Star Chest", SMRPGRegions.moleville_mines_back),
    ("Moleville Mines Coins", SMRPGRegions.moleville_mines_back),
    ("Moleville Mines Punchinello 1", SMRPGRegions.moleville_mines_back),
    ("Moleville Mines Punchinello 2", SMRPGRegions.moleville_mines_back),
    ("Booster Pass 1", SMRPGRegions.booster_pass),
    ("Booster Pass 2", SMRPGRegions.booster_pass),
    ("Booster Pass Secret 1", SMRPGRegions.booster_pass),
    ("Booster Pass Secret 2", SMRPGRegions.booster_pass),
    ("Booster Pass Secret 3", SMRPGRegions.booster_pass),
    ("Booster Tower Spookum", SMRPGRegions.booster_tower),
    ("Booster Tower Thwomp", SMRPGRegions.booster_tower),
    ("Booster Tower Masher", SMRPGRegions.booster_tower),
    ("Booster Tower Parachute", SMRPGRegions.booster_tower),
    ("Booster Tower Zoom Shoes", SMRPGRegions.booster_tower),
    ("Booster Tower Top1", SMRPGRegions.booster_tower),
    ("Booster Tower Top2", SMRPGRegions.booster_tower),
    ("Booster Tower Top3", SMRPGRegions.booster_tower),
    ("Marrymore Inn", SMRPGRegions.marrymore),
    ("Sea Star Chest", SMRPGRegions.sea),
    ("Sea Save Room 1", SMRPGRegions.sea),
    ("Sea Save Room 2", SMRPGRegions.sea),
    ("Sea Save Room 3", SMRPGRegions.sea),
    ("Sea Save Room 4", SMRPGRegions.sea),
    ("Sunken Ship Rat Stairs", SMRPGRegions.sunken_ship),
    ("Sunken Ship Shop", SMRPGRegions.sunken_ship),
    ("Sunken Ship Coins 1", SMRPGRegions.sunken_ship),
    ("Sunken Ship Coins 2", SMRPGRegions.sunken_ship),
    ("Sunken Ship Clone Room", SMRPGRegions.sunken_ship_back),
    ("Sunken Ship Frog Coin Room", SMRPGRegions.sunken_ship_back),
    ("Sunken Ship Hidon Mushroom", SMRPGRegions.sunken_ship_back),
    ("Sunken Ship Safety Ring", SMRPGRegions.sunken_ship_back),
    ("Sunken Ship Bandana Reds", SMRPGRegions.sunken_ship_back),
    ("Land's End Red Essence", SMRPGRegions.lands_end),
    ("Land's End Chow Pit 1", SMRPGRegions.lands_end),
    ("Land's End Chow Pit 2", SMRPGRegions.lands_end),
    ("Land's End Bee Room", SMRPGRegions.lands_end),
    ("Land's End Secret 1", SMRPGRegions.lands_end),
    ("Land's End Secret 2", SMRPGRegions.lands_end),
    ("Land's End Shy Away", SMRPGRegions.lands_end),
    ("Land's End Star Chest 1", SMRPGRegions.lands_end),
    ("Land's End Star Chest 2", SMRPGRegions.lands_end),
    ("Land's End Star Chest 3", SMRPGRegions.lands_end),
    ("Belome Temple Fortune Teller", SMRPGRegions.belome_temple),
    ("Belome Temple After Fortune 1", SMRPGRegions.belome_temple),
    ("Belome Temple After Fortune 2", SMRPGRegions.belome_temple),
    ("Belome Temple After Fortune 3", SMRPGRegions.belome_temple),
    ("Belome Temple After Fortune 4", SMRPGRegions.belome_temple),
    ("Monstro Town Entrance", SMRPGRegions.monstro_town),
    ("Bean Valley 1", SMRPGRegions.bean_valley),
    ("Bean Valley 2", SMRPGRegions.bean_valley),
    ("Bean Valley Box Boy Room", SMRPGRegions.bean_valley),
    ("Bean Valley Slot Room", SMRPGRegions.bean_valley),
    ("Bean Valley Piranha Plants", SMRPGRegions.bean_valley),
    ("Bean Valley Beanstalk", SMRPGRegions.bean_valley),
    ("Bean Valley Cloud 1", SMRPGRegions.bean_valley),
    ("Bean Valley Cloud 2", SMRPGRegions.bean_valley),
    ("Bean Valley Fall 1", SMRPGRegions.bean_valley),
    ("Bean Valley Fall 2", SMRPGRegions.bean_valley),
    ("Nimbus Land Shop", SMRPGRegions.nimbus_land),
    ("Nimbus Castle Before Birdo 1", SMRPGRegions.nimbus_castle_front),
    ("Nimbus Castle Before Birdo 2", SMRPGRegions.nimbus_castle_front),
    ("Nimbus Castle Out Of Bounds 1", SMRPGRegions.nimbus_castle_back),
    ("Nimbus Castle Out Of Bounds 2", SMRPGRegions.nimbus_castle_back),
    ("Nimbus Castle Single Gold Bird", SMRPGRegions.nimbus_castle_back),
    ("Nimbus Castle Star Chest", SMRPGRegions.nimbus_castle_back),
    ("Nimbus Castle Star After Valentina", SMRPGRegions.nimbus_castle_back),
    ("Barrel Volcano Secret 1", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Secret 2", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Before Star 1", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Before Star 2", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Star Room", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Save Room 1", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Save Room 2", SMRPGRegions.barrel_volcano),
    ("Barrel Volcano Hinnopio", SMRPGRegions.barrel_volcano),
    ("Bowser's Keep Dark Room", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Croco Shop 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Croco Shop 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Invisible Bridge 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Invisible Bridge 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Invisible Bridge 3", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Invisible Bridge 4", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Moving Platforms 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Moving Platforms 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Moving Platforms 3", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Moving Platforms 4", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Elevator Platforms", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Cannonball Room 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Cannonball Room 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Cannonball Room 3", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Cannonball Room 4", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Cannonball Room 5", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 3", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 4", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 5", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Rotating Platforms 6", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 1", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 2", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 3", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 4", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 5", SMRPGRegions.bowsers_keep),
    ("Bowser's Keep Door Reward 6", SMRPGRegions.bowsers_keep),
    ("Factory Save Room", SMRPGRegions.factory),
    ("Factory Bolt Platforms", SMRPGRegions.factory),
    ("Factory Falling Axems", SMRPGRegions.factory),
    ("Factory Treasure Pit 1", SMRPGRegions.factory),
    ("Factory Treasure Pit 2", SMRPGRegions.factory),
    ("Factory Conveyor Platforms 1", SMRPGRegions.factory),
    ("Factory Conveyor Platforms 2", SMRPGRegions.factory),
    ("Factory Behind Snakes 1", SMRPGRegions.factory),
    ("Factory Behind Snakes 2", SMRPGRegions.factory),

    ("Toad Rescue 1", SMRPGRegions.mushroom_way),
    ("Toad Rescue 2", SMRPGRegions.mushroom_way),
    ("Hammer Bros Reward", SMRPGRegions.mushroom_way),
    ("Wallet Guy 1", SMRPGRegions.mushroom_kingdom),
    ("Wallet Guy 2", SMRPGRegions.mushroom_kingdom),
    ("Mushroom Kingdom Store", SMRPGRegions.mushroom_kingdom),
    ("Peach Surprise", SMRPGRegions.mushroom_kingdom),
    ("Invasion Family", SMRPGRegions.mushroom_kingdom),
    ("Invasion Guest Room", SMRPGRegions.mushroom_kingdom),
    ("Invasion Guard", SMRPGRegions.mushroom_kingdom),
    ("Croco 1 Reward", SMRPGRegions.bandits_way),
    ("Pandorite Reward", SMRPGRegions.kero_sewers),
    ("Midas River First Time", SMRPGRegions.midas_river),
    ("Rose Town Toad", SMRPGRegions.rose_town),
    ("Gaz", SMRPGRegions.rose_town),
    ("Treasure Seller 1", SMRPGRegions.moleville),
    ("Treasure Seller 2", SMRPGRegions.moleville),
    ("Treasure Seller 3", SMRPGRegions.moleville),
    ("Croco Flunkie 1", SMRPGRegions.moleville),
    ("Croco Flunkie 2", SMRPGRegions.moleville),
    ("Croco Flunkie 3", SMRPGRegions.moleville),
    ("Booster Tower Railway", SMRPGRegions.booster_tower),
    ("Booster Tower Chomp", SMRPGRegions.booster_tower),
    ("Booster Tower Curtain Game", SMRPGRegions.booster_tower),
    ("Seaside Town Rescue", SMRPGRegions.seaside_town),
    ("Sunken Ship 3D Maze", SMRPGRegions.sunken_ship),
    ("Sunken Ship Cannonball Puzzle", SMRPGRegions.sunken_ship),
    ("Sunken Ship Hidon Reward", SMRPGRegions.sunken_ship_back),
    ("Belome Temple Treasure 1", SMRPGRegions.belome_temple),
    ("Belome Temple Treasure 2", SMRPGRegions.belome_temple),
    ("Belome Temple Treasure 3", SMRPGRegions.belome_temple),
    ("Jinx Dojo Reward", SMRPGRegions.monstro_town),
    ("Culex Reward", SMRPGRegions.monstro_town),
    ("Super Jumps 30", SMRPGRegions.monstro_town),
    ("Super Jumps 100", SMRPGRegions.monstro_town),
    ("Three Musty Fears", SMRPGRegions.monstro_town),
    ("Troopa Climb", SMRPGRegions.lands_end),
    ("Dodo Reward", SMRPGRegions.nimbus_castle_front),
    ("Nimbus Land Inn", SMRPGRegions.nimbus_land),
    ("Nimbus Land Prisoners", SMRPGRegions.nimbus_castle_front),
    ("Nimbus Land Signal Ring", SMRPGRegions.nimbus_castle_back),
    ("Nimbus Land Cellar", SMRPGRegions.nimbus_castle_back),
    ("Factory Toad Gift", SMRPGRegions.factory),
    ("Goomba Thumping 1", SMRPGRegions.pipe_vault),
    ("Goomba Thumping 2", SMRPGRegions.pipe_vault),
    ("Cricket Pie Reward", SMRPGRegions.tadpole_pond),
    ("Cricket Jam Reward", SMRPGRegions.tadpole_pond),
]

star_piece_locations: List[str] = [
    "Hammer Bros", "Croco 1 (Boss)", "Mack", "Pandorite", "Belome 1", "Bowyer", "Croco 2 (Boss)",
    "Punchinello", "Booster", "Clown Bros", "Bundt", "Star Hill", "King Calamari", "Hidon", "Johnny",
    "Yaridovich (Boss)", "Belome 2", "Jagger", "Jinx 3 (Boss)", "Culex", "Box Boy", "Mega Smilax", "Dodo",
    "Birdo (Boss)", "Valentina", "Czar Dragon", "Axem Rangers", "Magikoopa", "Boomer", "Exor"
]

additional_bambino_locks: List[str] = [
    "Melody Bay Song 2", "Melody Bay Song 3"
]

tier_1_locations = ["Mushroom Way 1", "Mushroom Way 2", "Mushroom Way 4",
                    "Mushroom Kingdom Vault 1", "Mushroom Kingdom Vault 2", "Mushroom Kingdom Vault 3",
                    "Mushroom Kingdom Store", "Bandit's Way 1", "Bandit's Way 2", "Bandit's Way Star Chest",
                    "Bandit's Way Croco", "Kero Sewers Pandorite Room", "Kero Sewers Star Chest",
                    "Rose Town Store 1", "Rose Town Store 2", "Forest Maze 1", "Forest Maze 2",
                    "Forest Maze Underground 1", "Booster Pass 2", "Booster Tower Spookum",
                    "Booster Tower Thwomp", "Booster Tower Parachute", "Marrymore Inn", "Sea Star Chest",
                    "Sea Save Room 1", "Sea Save Room 2", "Sea Save Room 3", "Sunken Ship Rat Stairs",
                    "Land's End Red Essence", "Land's End Secret 1", "Land's End Secret 2", "Land's End Shy Away",
                    "Monstro Town Entrance", "Bean Valley 2", "Nimbus Land Shop", "Nimbus Castle Before Birdo 1",
                    "Nimbus Castle Single Gold Bird", "Barrel Volcano Before Star 1", "Barrel Volcano Before Star 2",
                    "Barrel Volcano Star Room", "Bowser's Keep Dark Room", "Bowser's Keep Croco Shop 1",
                    "Bowser's Keep Croco Shop 2", "Mario's Bed", "Rose Town Sign", "Monstro Town Key"]

tier_2_locations = ["Mushroom Way 3", "Toad Rescue 1", "Toad Rescue 2", "Peach Surprise", "Rose Way Platform",
                    "Forest Maze Underground 3", "Forest Maze Red Essence", "Pipe Vault Slide 1",
                    "Pipe Vault Slide 2", "Pipe Vault Slide 3", "Pipe Vault Nippers 1", "Pipe Vault Nippers 2",
                    "Booster Pass 1", "Booster Tower Top 1", "Booster Tower Top 2", "Booster Tower Top 3",
                    "Booster Tower Railway", "Sea Save Room 4", "Sunken Ship Cannonball Puzzle",
                    "Land's End Chow Pit 1", "Land's End Chow Pit 2", "Land's End Bee Room", "Land's End Star Chest 1",
                    "Land's End Star Chest 2", "Belome Temple Fortune Teller", "Belome Temple After Fortune 1",
                    "Belome Temple After Fortune 2", "Belome Temple After Fortune 3", "Belome Temple After Fortune 4",
                    "Bean Valley 1", "Bean Valley Box Boy Room", "Bean Valley Slot Room", "Bean Valley Piranha Plants",
                    "Nimbus Castle Out Of Bounds 1", "Nimbus Castle Out Of Bounds 2", "Barrel Volcano Secret",
                    "Barrel Volcano Secret 1", "Barrel Volcano Secret 2", "Barrel Volcano Save Room 1",
                    "Barrel Volcano Save Room 2", "Barrel Volcano Hinnopio", "Bowser's Keep Invisible Bridge 1",
                    "Bowser's Keep Invisible Bridge 2", "Bowser's Keep Invisible Bridge 3",
                    "Bowser's Keep Invisible Bridge 4", "Bowser's Keep Elevator Platforms",
                    "Bowser's Keep Cannonball Room 1", "Bowser's Keep Cannonball Room 2",
                    "Bowser's Keep Cannonball Room 3", "Bowser's Keep Cannonball Room 4",
                    "Bowser's Keep Cannonball Room 5", "Bowser's Keep Rotating Platforms 1",
                    "Bowser's Keep Rotating Platforms 4", "Bowser's Keep Rotating Platforms 6", "Cricket Jam Chest",
                    "Melody Bay Song 1", "Booster Tower Ancestors", "Booster Tower Checkerboard", "Knife Guy",
                    "Nimbus Land Castle Key"]

tier_3_locations = ["Hammer Bros Reward", "Invasion Family", "Invasion Guest Room", "Invasion Guard",
                    "Bandit's Way Dog Jump", "Croco 1 Reward", "Pandorite Reward", "Midas River First Time",
                    "Cricket Pie Reward", "Cricket Jam Reward", "Rose Town Toad", "Gaz", "Forest Maze Underground 2",
                    "Goomba Thumping 1", "Goomba Thumping 2", "Yo'ster Isle Entrance", "Moleville Mines Star Chest",
                    "Moleville Mines Coins", "Moleville Mines Punchinello 1", "Moleville Mines Punchinello 2",
                    "Croco Flunkie 1", "Croco Flunkie 2", "Croco Flunkie 3", "Booster Pass Secret 1",
                    "Booster Pass Secret 2", "Booster Pass Secret 3", "Booster Tower Masher",
                    "Booster Tower Zoom Shoes", "Booster Tower Chomp", "Booster Tower Curtain Game",
                    "Seaside Town Rescue", "Sunken Ship Shop", "Sunken Ship Coins 1", "Sunken Ship Coins 2",
                    "Sunken Ship Clone Room", "Sunken Ship Frog Coin Room", "Sunken Ship Hidon Mushroom",
                    "Sunken Ship Safety Ring", "Sunken Ship Bandana Reds", "Sunken Ship 3D Maze",
                    "Land's End Star Chest 3", "Troopa Climb", "Belome Temple Treasure 1", "Belome Temple Treasure 2",
                    "Belome Temple Treasure 3", "Bean Valley Beanstalk", "Bean Valley Cloud 1", "Bean Valley Cloud 2",
                    "Bean Valley Fall 1", "Bean Valley Fall 2", "Nimbus Land Inn", "Dodo Reward",
                    "Nimbus Land Prisoners", "Bowser's Keep Moving Platforms 1", "Bowser's Keep Moving Platforms 2",
                    "Bowser's Keep Moving Platforms 3", "Bowser's Keep Moving Platforms 4",
                    "Bowser's Keep Rotating Platforms 2", "Bowser's Keep Rotating Platforms 3",
                    "Bowser's Keep Rotating Platforms 5", "Croco 1", "Rare Frog Coin Reward", "Yo'ster Isle Goal",
                    "Croco 2", "Seaside Town Key", "Seed"]

tier_4_locations = ["Wallet Guy 1", "Wallet Guy 2", "Gardener Cloud 1", "Gardener Cloud 2", "Treasure Seller 1",
                    "Treasure Seller 2", "Treasure Seller 3", "Sunken Ship Hidon Reward", "Jinx Dojo Reward",
                    "Culex Reward", "Super Jumps 30", "Super Jumps 100", "Three Musty Fears",
                    "Nimbus Castle Before Birdo 2", "Nimbus Castle Star Chest", "Nimbus Castle Star After Valentina",
                    "Nimbus Land Signal Ring", "Nimbus Land Cellar", "Bowser's Keep Door Reward 1",
                    "Bowser's Keep Door Reward 2", "Bowser's Keep Door Reward 3", "Bowser's Keep Door Reward 4",
                    "Bowser's Keep Door Reward 5", "Bowser's Keep Door Reward 6", "Factory Save Room",
                    "Factory Bolt Platforms", "Factory Falling Axems", "Factory Treasure Pit 1",
                    "Factory Treasure Pit 2", "Factory Conveyor Platforms 1", "Factory Conveyor Platforms 2",
                    "Factory Behind Snakes 1", "Factory Behind Snakes 2", "Factory Toad Gift", "Melody Bay Song 2",
                    "Melody Bay Song 3", "Birdo", "Fertilizer"]

location_table: Dict[str, LocationData] = dict()
for index, value in enumerate(locations_data):
    star_piece_eligible = value[0] in star_piece_locations
    location = LocationData(value[0], star_piece_eligible, value[1], index)
    location_table[location.name] = location
