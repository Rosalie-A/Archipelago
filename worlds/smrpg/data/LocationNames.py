import re
from enum import StrEnum


class LocationNames(StrEnum):
    BANDITS_WAY_BOSS_FIGHT = "Bandit's Way Boss Fight"
    BANDITS_WAY_BOSS_REWARD_1 = "Bandit's Way Boss Item Reward 1"
    BANDITS_WAY_BOSS_REWARD_2 = "Bandit's Way Boss Item Reward 2"
    BANDITS_WAY_1ST_COIN = "Bandit's Way 1st Coin"
    BANDITS_WAY_2ND_COIN = "Bandit's Way 2nd Coin"
    BANDITS_WAY_3RD_COIN = "Bandit's Way 3rd Coin"
    BANDITS_WAY_CROCO_CHASE_CHEST = "Bandit's Way Croco Chase Chest"
    BANDITS_WAY_LONG_ROOM_CHEST = "Bandit's Way Long Room Chest"
    BANDITS_WAY_FLOWER_CHEST = "Bandit's Way Flower Chest"
    BANDITS_WAY_STAR_CHEST = "Bandit's Way Star Chest"
    BANDITS_WAY_DOG_JUMP_CHEST = "Bandit's Way Dog Jump Chest"
    BANDITS_WAY_BOSS_STAR_PIECE = "Bandit's Way Boss Star Piece"
    BARREL_VOLCANO_FIRST_BOSS_FIGHT = "Barrel Volcano First Boss Fight"
    BARREL_VOLCANO_FIRST_BOSS_STAR_PIECE = "Barrel Volcano First Boss Star Piece"
    BARREL_VOLCANO_SECOND_ARROW_SIGN_ROOM_LEFT_CHEST = "Barrel Volcano Second Arrow Sign Room Left Chest"
    BARREL_VOLCANO_SECOND_ARROW_SIGN_ROOM_RIGHT_CHEST = "Barrel Volcano Second Arrow Sign Room Right Chest"
    BARREL_VOLCANO_STAR_CHEST = "Barrel Volcano Star Chest"
    BARREL_VOLCANO_SECOND_BOSS_FIGHT = "Barrel Volcano Second Boss Fight"
    BARREL_VOLCANO_SECOND_BOSS_STAR_PIECE = "Barrel Volcano Second Boss Star Piece"
    BARREL_VOLCANO_SECRET_ROOM_LEFT_CHEST = "Barrel Volcano Early Secret Room Left Chest"
    BARREL_VOLCANO_SECRET_ROOM_RIGHT_CHEST = "Barrel Volcano Early Secret Room Right Chest"
    BARREL_VOLCANO_LAVA_POOL_FREESTANDING_FROG_COIN = "Barrel Volcano Lava Pool Freestanding Frog Coin"
    BARREL_VOLCANO_FIRST_DONUT_LIFT_ROOM_LEFT_FREESTANDING_FROG_COIN = "Barrel Volcano First Donut Lift Room Left Freestanding Frog Coin"
    BARREL_VOLCANO_REVERSE_LAVA_RECOIL_FROG_COIN = "Barrel Volcano Reverse Lava Recoil Frog Coin"
    BARREL_VOLCANO_FIRST_DONUT_LIFT_ROOM_RIGHT_FREESTANDING_FROG_COIN = "Barrel Volcano First Donut Lift Room Right Freestanding Frog Coin"
    BARREL_VOLCANO_SAVE_ROOM_LOWER_CHEST = "Barrel Volcano Save Room Lower Chest"
    BARREL_VOLCANO_SAVE_ROOM_UPPER_CHEST = "Barrel Volcano Save Room Upper Chest"
    BARREL_VOLCANO_HINOPIO_SHOP_CHEST = "Barrel Volcano Hinopio Shop Chest"
    BEAN_VALLEY_LOWEST_VINE_ROOM_FREESTANDING_FROG_COIN = "Bean Valley Lowest Vine Room Freestanding Frog Coin"
    BEAN_VALLEY_LOWEST_VINE_ROOM_LOWER_FREESTANDING_COIN = "Bean Valley Lowest Vine Room Lower Freestanding Coin"
    BEAN_VALLEY_LOWEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN = "Bean Valley Lowest Vine Room Middle Freestanding Coin"
    BEAN_VALLEY_LOWEST_VINE_ROOM_UPPER_FREESTANDING_COIN = "Bean Valley Lowest Vine Room Upper Freestanding Coin"
    BEAN_VALLEY_BOSS_REWARD = "Bean Valley Boss Reward"
    BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE_CHEST = "Bean Valley Bottom Left Piranha Pipe Chest"
    BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER_CHEST = "Bean Valley Bottom Right Piranha Pipe Lower Chest"
    BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER_CHEST = "Bean Valley Bottom Right Piranha Pipe Upper Chest"
    BEAN_VALLEY_EAST_VINE_ROOM_LOWEST_FREESTANDING_COIN = "Bean Valley East Vine Room Lowest Freestanding Coin"
    BEAN_VALLEY_EAST_VINE_ROOM_LOWER_FREESTANDING_COIN = "Bean Valley East Vine Room Lower Freestanding Coin"
    BEAN_VALLEY_EAST_VINE_ROOM_MIDDLE_FREESTANDING_COIN = "Bean Valley East Vine Room Middle Freestanding Coin"
    BEAN_VALLEY_EAST_VINE_ROOM_HIGHER_FREESTANDING_COIN = "Bean Valley East Vine Room Higher Freestanding Coin"
    BEAN_VALLEY_EAST_VINE_ROOM_HIGHEST_FREESTANDING_COIN = "Bean Valley East Vine Room Highest Freestanding Coin"
    BEAN_VALLEY_SOUTH_UPPER_LEVEL_CHEST = "Bean Valley South Upper Level Chest"
    BEAN_VALLEY_NORTH_UPPER_LEVEL_CHEST = "Bean Valley North Upper Level Chest"
    BEAN_VALLEY_LEFT_PIRANHA_PIPE_CHEST = "Bean Valley Left Piranha Pipe Chest"
    BEAN_VALLEY_BOSS_FIGHT = "Bean Valley Boss Fight"
    BEAN_VALLEY_BOSS_STAR_PIECE = "Bean Valley Boss Star Piece"
    BEAN_VALLEY_CHEST_ABOVE_BOX_BOYS_ROOM = "Bean Valley Chest Above Box Boy's Room"
    BEAN_VALLEY_RIGHT_PIRANHA_PIPE_LEFT_CHEST = "Bean Valley Right Piranha Pipe Left Chest"
    BEAN_VALLEY_RIGHT_PIRANHA_PIPE_RIGHT_CHEST = "Bean Valley Right Piranha Pipe Right Chest"
    BEAN_VALLEY_RIGHT_PIRANHA_PIPE_HIDDEN_STAIRWAY_ITEM = "Bean Valley Right Piranha Pipe Hidden Stairway Item"
    BEAN_VALLEY_WEST_VINE_ROOM_LOWER_FREESTANDING_COIN = "Bean Valley West Vine Room Lower Freestanding Coin"
    BEAN_VALLEY_WEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN = "Bean Valley West Vine Room Middle Freestanding Coin"
    BEAN_VALLEY_WEST_VINE_ROOM_UPPER_FREESTANDING_COIN = "Bean Valley West Vine Room Upper Freestanding Coin"
    BEAN_VALLEY_WEST_VINE_ROOM_FREESTANDING_FROG_COIN = "Bean Valley West Vine Room Freestanding Frog Coin"
    BEAN_VALLEY_MIDDLE_VINE_ROOM_LOWEST_FREESTANDING_COIN = "Bean Valley Middle Vine Room Lowest Freestanding Coin"
    BEAN_VALLEY_MIDDLE_VINE_ROOM_MIDDLE_FREESTANDING_COIN = "Bean Valley Middle Vine Room Middle Freestanding Coin"
    BEAN_VALLEY_MIDDLE_VINE_ROOM_HIGHEST_FREESTANDING_COIN = "Bean Valley Middle Vine Room Highest Freestanding Coin"
    BEAN_VALLEY_MIDDLE_VINE_ROOM_FREESTANDING_FROG_COIN = "Bean Valley Middle Vine Room Freestanding Frog Coin"
    BEAN_VALLEY_CLOUDS_LOWER_LEFT_CHEST = "Bean Valley Clouds Lower Left Chest"
    BEAN_VALLEY_CLOUDS_LOWER_RIGHT_CHEST = "Bean Valley Clouds Lower Right Chest"
    BEAN_VALLEY_CLOUDS_SOLO_VINE_CHEST = "Bean Valley Clouds Solo Vine Chest"
    BEAN_VALLEY_CLOUDS_UPPER_LEFT_CHEST = "Bean Valley Clouds Upper Left Chest"
    BEAN_VALLEY_CLOUDS_UPPER_RIGHT_CHEST = "Bean Valley Clouds Upper Right Chest"
    MIMIC_CHEST_3_BOSS_FIGHT = "Mimic Chest #3 Boss Fight"
    MIMIC_CHEST_3_STAR_PIECE = "Mimic Chest #3 Star Piece"
    BOOSTER_HILL_FLOWER_1 = "Booster Hill Flower 1"
    BOOSTER_HILL_FLOWER_10 = "Booster Hill Flower 10"
    BOOSTER_HILL_FLOWER_11 = "Booster Hill Flower 11"
    BOOSTER_HILL_FLOWER_12 = "Booster Hill Flower 12"
    BOOSTER_HILL_FLOWER_13 = "Booster Hill Flower 13"
    BOOSTER_HILL_FLOWER_14 = "Booster Hill Flower 14"
    BOOSTER_HILL_FLOWER_15 = "Booster Hill Flower 15"
    BOOSTER_HILL_FLOWER_16 = "Booster Hill Flower 16"
    BOOSTER_HILL_FLOWER_2 = "Booster Hill Flower 2"
    BOOSTER_HILL_FLOWER_3 = "Booster Hill Flower 3"
    BOOSTER_HILL_FLOWER_4 = "Booster Hill Flower 4"
    BOOSTER_HILL_FLOWER_5 = "Booster Hill Flower 5"
    BOOSTER_HILL_FLOWER_6 = "Booster Hill Flower 6"
    BOOSTER_HILL_FLOWER_7 = "Booster Hill Flower 7"
    BOOSTER_HILL_FLOWER_8 = "Booster Hill Flower 8"
    BOOSTER_HILL_FLOWER_9 = "Booster Hill Flower 9"
    BOOSTER_PASS_MAIN_AREA_BUSH_CHECK = "Booster Pass Main Area Bush Check"
    BOOSTER_PASS_MAIN_AREA_LEFT_CHEST = "Booster Pass Main Area Left Chest"
    BOOSTER_PASS_MAIN_AREA_RIGHT_CHEST = "Booster Pass Main Area Right Chest"
    BOOSTER_PASS_FREESTANDING_FLOWER = "Booster Pass Freestanding Flower"
    BOOSTER_PASS_SECRET_LEFT_CHEST = "Booster Pass Secret Left Chest"
    BOOSTER_PASS_SECRET_MIDDLE_CHEST = "Booster Pass Secret Middle Chest"
    BOOSTER_PASS_SECRET_RIGHT_CHEST = "Booster Pass Secret Right Chest"
    BOOSTER_TOWER_BALCONY_BOSS_FIGHT = "Booster Tower Balcony Boss Fight"
    BOOSTER_TOWER_BALCONY_BOSS_STAR_PIECE = "Booster Tower Balcony Boss Star Piece"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_4 = "Booster Tower Checkerboard Room Freestanding Frog Coin 4"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_1 = "Booster Tower Checkerboard Room Freestanding Coin 1"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_2 = "Booster Tower Checkerboard Room Freestanding Coin 2"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_3 = "Booster Tower Checkerboard Room Freestanding Coin 3"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_4 = "Booster Tower Checkerboard Room Freestanding Coin 4"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_5 = "Booster Tower Checkerboard Room Freestanding Coin 5"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_6 = "Booster Tower Checkerboard Room Freestanding Coin 6"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_7 = "Booster Tower Checkerboard Room Freestanding Coin 7"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_8 = "Booster Tower Checkerboard Room Freestanding Coin 8"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_9 = "Booster Tower Checkerboard Room Freestanding Coin 9"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_2 = "Booster Tower Checkerboard Room Freestanding Frog Coin 2"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_ITEM = "Booster Tower Checkerboard Room Item"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_1 = "Booster Tower Checkerboard Room Freestanding Frog Coin 1"
    BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_3 = "Booster Tower Checkerboard Room Freestanding Frog Coin 3"
    BOOSTER_TOWER_UPPER_THWOMP_ROOM_CHEST = "Booster Tower Upper Thwomp Room Chest"
    BOOSTER_TOWER_CURTAIN_PRIZE = "Booster Tower Curtain Prize"
    BOOSTER_TOWER_ELDER_KEY_ROOM = "Booster Tower Elder Key Room"
    BOOSTER_TOWER_MASHER_CHEST = "Booster Tower Masher Chest"
    BOOSTER_TOWER_CURTAIN_ROOM_BOSS_FIGHT = "Booster Tower Curtain Room Boss Fight"
    BOOSTER_TOWER_POSTGAME_BOSS_FIGHT = "Booster Tower Postgame Boss Fight"
    BOOSTER_TOWER_CURTAIN_ROOM_BOSS_STAR_PIECE = "Booster Tower Curtain Room Boss Star Piece"
    BOOSTER_TOWER_POSTGAME_BOSS_STAR_PIECE = "Booster Tower Postgame Boss Star Piece"
    BOOSTER_TOWER_KNIFE_GUY_MAXED_OUT_REWARD = "Booster Tower Knife Guy Maxed Out Reward (if Fixed)"
    BOOSTER_TOWER_KNIFE_GUY_REWARD = "Booster Tower Knife Guy Reward"
    BOOSTER_TOWER_MARIO_DOLL = "Booster Tower Doll Above Curtains"
    BOOSTER_TOWER_PARACHUTE_ROOM_CHEST = "Booster Tower Parachute Room Chest"
    BOOSTER_TOWER_PARACHUTE_ROOM_STAIR_CREVICE = "Booster Tower Parachute Room Stair Crevice"
    BOOSTER_TOWER_PORTRAIT_PRIZE = "Booster Tower Portrait Prize"
    BOOSTER_TOWER_POSTGAME_PRIZE = "Booster Tower Postgame Prize"
    BOOSTER_TOWER_ROOM_KEY_CHEST = "Booster Tower Room Key Chest"
    BOOSTER_TOWER_FIRST_STAIRWAY_CHEST = "Booster Tower First Stairway Chest"
    BOOSTER_TOWER_TOP_FLOOR_CORNER_CHEST = "Booster Tower Top Floor Corner Chest"
    BOOSTER_TOWER_TOP_FLOOR_LOWER_CHEST = "Booster Tower Top Floor Lower Chest"
    BOOSTER_TOWER_TOP_FLOOR_UPPER_CHEST = "Booster Tower Top Floor Upper Chest"
    BOOSTER_TOWER_RAILWAY_ROOM = "Booster Tower Railway Room Crevice"
    BOWSERS_KEEP_MAGIKOOPAS_ROOM_CHEST = "Bowser's Keep Magikoopa's Room Chest"
    BOWSERS_KEEP_FIRST_BOSS_FIGHT = "Bowser's Keep First Boss After Red Doors Fight"
    BOWSERS_KEEP_FIRST_BOSS_STAR_PIECE = "Bowser's Keep First Boss Star Piece"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_1 = "Bowser's Keep Cannonball Room Freestanding Coin 1"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_2 = "Bowser's Keep Cannonball Room Freestanding Coin 2"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_3 = "Bowser's Keep Cannonball Room Freestanding Coin 3"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_4 = "Bowser's Keep Cannonball Room Freestanding Coin 4"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_5 = "Bowser's Keep Cannonball Room Freestanding Coin 5"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_6 = "Bowser's Keep Cannonball Room Freestanding Coin 6"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_7 = "Bowser's Keep Cannonball Room Freestanding Coin 7"
    BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_8 = "Bowser's Keep Cannonball Room Freestanding Coin 8"
    BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_LEFT_CHEST = "Bowser's Keep Cannonball Room Lower Left Chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_LEFT_CHEST = "Bowser's Keep Cannonball Room Upper Left Chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_RIGHT_CHEST = "Bowser's Keep Cannonball Room Upper Right Chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_EXIT_CHEST = "Bowser's Keep Cannonball Room Exit Chest"
    BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_RIGHT_CHEST = "Bowser's Keep Cannonball Room Lower Right Chest"
    BOWSERS_KEEP_SECOND_BOSS_FIGHT = "Bowser's Keep Second Boss After Red Doors Fight"
    BOWSERS_KEEP_SECOND_BOSS_STAR_PIECE = "Bowser's Keep Second Boss Star Piece"
    BOWSERS_KEEP_DARK_ROOM_CHEST = "Bowser's Keep Dark Room Chest"
    BOWSERS_KEEP_DOOR_PRIZE_1 = "Bowser's Keep Door Prize 1"
    BOWSERS_KEEP_DOOR_PRIZE_2 = "Bowser's Keep Door Prize 2"
    BOWSERS_KEEP_DOOR_PRIZE_3 = "Bowser's Keep Door Prize 3"
    BOWSERS_KEEP_DOOR_PRIZE_4 = "Bowser's Keep Door Prize 4"
    BOWSERS_KEEP_DOOR_PRIZE_5 = "Bowser's Keep Door Prize 5"
    BOWSERS_KEEP_DOOR_PRIZE_6 = "Bowser's Keep Door Prize 6"
    BOWSERS_KEEP_6_DOOR_ELEVATOR_PLATFORM_ROOM_CHEST = "Bowser's Keep 6-door Elevator Platform Room Chest"
    BOWSERS_KEEP_THIRD_BOSS_FIGHT = "Bowser's Keep Third Boss After Red Doors Fight"
    BOWSERS_KEEP_THIRD_BOSS_STAR_PIECE = "Bowser's Keep Third Boss Star Piece"
    BOWSERS_KEEP_NEAR_FIRST_SHOP_LEFT_CHEST = "Bowser's Keep Near First Shop Left Chest"
    BOWSERS_KEEP_NEAR_FIRST_SHOP_RIGHT_CHEST = "Bowser's Keep Near First Shop Right Chest"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_CHEST = "Bowser's Keep 6-door Invisble Bridge Top Chest"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_LEFT_COIN = "Bowser's Keep 6-door Invisble Bridge Bottom Left Coin"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_RIGHT_COIN = "Bowser's Keep 6-door Invisble Bridge Bottom Right Coin"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_LEFT_COIN = "Bowser's Keep 6-door Invisble Bridge Top Left Coin"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_RIGHT_COIN = "Bowser's Keep 6-door Invisble Bridge Top Right Coin"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_CHEST = "Bowser's Keep 6-door Invisble Bridge Bottom Chest"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_LEFT_CHEST = "Bowser's Keep 6-door Invisble Bridge Left Chest"
    BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_RIGHT_CHEST = "Bowser's Keep 6-door Invisble Bridge Right Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_EXIT_CHEST = "Bowser's Keep Rotating Platform Exit Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_UPPER_LEFT_CHEST = "Bowser's Keep Rotating Platform Upper Left Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_RIGHT_CHEST = "Bowser's Keep Rotating Platform Right Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_ROOM_ENTRANCE_CHEST = "Bowser's Keep Rotating Platform Room Entrance Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_LOWER_LEFT_CHEST = "Bowser's Keep Rotating Platform Lower Left Chest"
    BOWSERS_KEEP_ROTATING_PLATFORM_CENTER_CHEST = "Bowser's Keep Rotating Platform Center Chest"
    BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_EXIT_CHEST = "Bowser's Keep X-y Platform Room Left Exit Chest"
    BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_EXIT_CHEST = "Bowser's Keep X-y Platform Room Right Exit Chest"
    BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_ENTRANCE_CHEST = "Bowser's Keep X-y Platform Room Left Entrance Chest"
    BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_ENTRANCE_CHEST = "Bowser's Keep X-y Platform Room Right Entrance Chest"
    BOWSERS_KEEP_BATTLE_DOOR_BOSS_FIGHT = "Bowser's Keep Battle Door Final Fight"
    BOWSERS_KEEP_BATTLE_DOOR_STAR_PIECE = "Bowser's Keep Battle Door Star Piece"
    GRATE_GUYS_CASINO_LOTW_PRIZE = "Grate Guy's Casino Lotw Prize"
    FOREST_MAZE_BOSS_FIGHT = "Forest Maze Boss"
    FOREST_MAZE_CHARACTER_RECRUIT = "Forest Maze Character Recruit"
    FOREST_MAZE_1ST_ROOM_CHEST = "Forest Maze 1st Room Chest"
    FOREST_MAZE_FIRST_CHEST_AFTER_UNDERGROUND = "Forest Maze First Chest After Underground"
    FOREST_MAZE_BEFORE_MAZE_CHEST = "Forest Maze Before Maze Chest"
    FOREST_MAZE_SECRET_BOTTOM_MIDDLE_CHEST = "Forest Maze Secret Bottom Middle Chest"
    FOREST_MAZE_SECRET_BOTTOM_RIGHT_CHEST = "Forest Maze Secret Bottom Right Chest"
    FOREST_MAZE_SECRET_LEFT_CHEST = "Forest Maze Secret Left Chest"
    FOREST_MAZE_SECRET_TOP_MIDDLE_CHEST = "Forest Maze Secret Top Middle Chest"
    FOREST_MAZE_SECRET_TOP_RIGHT_CHEST = "Forest Maze Secret Top Right Chest"
    FOREST_MAZE_BOSS_STAR_PIECE = "Forest Maze Boss Star Piece"
    FOREST_MAZE_BOTTOM_RIGHT_STUMP_CHEST = "Forest Maze Bottom Right Stump Chest"
    FOREST_MAZE_MIDDLE_LEFT_STUMP_CHEST = "Forest Maze Middle Left Stump Chest"
    FOREST_MAZE_WIGGLER_CHEST = "Forest Maze Wiggler Chest"
    GENO_SPELL_1 = "Geno Spell 1"
    GENO_SPELL_2 = "Geno Spell 2"
    GENO_SPELL_3 = "Geno Spell 3"
    GENO_SPELL_4 = "Geno Spell 4"
    GENO_SPELL_5 = "Geno Spell 5"
    GENO_SPELL_6 = "Geno Spell 6"
    FACTORY_FINAL_BOSS_FIGHT = "Factory Final Boss Fight"
    FACTORY_FINAL_BOSS_STAR_PIECE = "Factory Final Boss Star Piece"
    INNER_FACTORY_FIRST_BOSS_FIGHT = "Inner Factory First Boss Fight"
    INNER_FACTORY_FIRST_BOSS_STAR_PIECE = "Inner Factory First Boss Star Piece"
    INNER_FACTORY_FOURTH_BOSS_FIGHT = "Inner Factory Fourth Boss Fight"
    INNER_FACTORY_FOURTH_BOSS_STAR_PIECE = "Inner Factory Fourth Boss Star Piece"
    INNER_FACTORY_SECOND_BOSS_FIGHT = "Inner Factory Second Boss Fight"
    INNER_FACTORY_SECOND_BOSS_STAR_PIECE = "Inner Factory Second Boss Star Piece"
    INNER_FACTORY_THIRD_BOSS_FIGHT = "Inner Factory Third Boss Fight"
    INNER_FACTORY_THIRD_BOSS_STAR_PIECE = "Inner Factory Third Boss Star Piece"
    INNER_FACTORY_TOAD_GIFT = "Inner Factory Toad Gift"
    KERO_SEWERS_BEFORE_BOSS_LOWER_CHEST = "Kero Sewers Before Boss Lower Chest"
    KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_AFTER_LANDS_END = "Kero Sewers Before Boss Upper Chest, After Land's End"
    KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_BEFORE_LANDS_END = "Kero Sewers Before Boss Upper Chest, Before Land's End"
    KERO_SEWERS_BOSS_FIGHT = "Kero Sewers Boss"
    KERO_SEWERS_FOUR_RAT_ROOM_CHEST = "Kero Sewers Four Rat Room Chest"
    KERO_SEWERS_STAIRWAY_ROOM_LEFT_CHEST = "Kero Sewers Stairway Room Left Chest"
    KERO_SEWERS_STAIRWAY_ROOM_RIGHT_CHEST = "Kero Sewers Stairway Room Right Chest"
    KERO_SEWERS_BOSS_STAR_PIECE = "Kero Sewers Boss Star Piece"
    MIMIC_CHEST_1_BOSS_FIGHT = "Mimic Chest #1 Boss Fight"
    MIMIC_CHEST_1_FIRST_REWARD = "Mimic Chest #1 Drop Reward"
    MIMIC_CHEST_1_RELOAD_REWARD = "Mimic Chest #1 Reload Reward"
    MIMIC_CHEST_1_STAR_PIECE = "Mimic Chest #1 Star Piece"
    BELOME_TEMPLE_AFTER_FORTUNE_AREA_LOWER_LEFT_CHEST = "Belome Temple After Fortune Area Lower Left Chest"
    BELOME_TEMPLE_AFTER_FORTUNE_AREA_MIDDLE_CHEST = "Belome Temple After Fortune Area Middle Chest"
    BELOME_TEMPLE_AFTER_FORTUNE_AREA_RIGHT_CHEST = "Belome Temple After Fortune Area Right Chest"
    BELOME_TEMPLE_AFTER_FORTUNE_AREA_UPPER_LEFT_CHEST = "Belome Temple After Fortune Area Upper Left Chest"
    BELOME_TEMPLE_FIRST_FORTUNE_TELLING_ROOM_CHEST = "Belome Temple First Fortune-telling Room Chest"
    BELOME_TEMPLE_LEFT_MIDDLE_RIGHT_FORTUNE_CHEST = "Belome Temple Left-middle-right Fortune Chest"
    BELOME_TEMPLE_LEFT_RIGHT_MIDDLE_FORTUNE_CHEST = "Belome Temple Left-right-middle Fortune Chest"
    BELOME_TEMPLE_RIGHT_LEFT_MIDDLE_FORTUNE_CHEST = "Belome Temple Right-left-middle Fortune Chest"
    BELOME_TEMPLE_RIGHT_MIDDLE_LEFT_FORTUNE_CHEST = "Belome Temple Right-middle-left Fortune Chest"
    BELOME_TEMPLE_VAULT_FROG_COIN_3 = "Belome Temple Vault Frog Coin 3"
    BELOME_TEMPLE_VAULT_FROG_COIN_2 = "Belome Temple Vault Frog Coin 2"
    BELOME_TEMPLE_VAULT_LEFT_ITEM_BAG = "Belome Temple Vault Left Item Bag"
    BELOME_TEMPLE_VAULT_FROG_COIN_5 = "Belome Temple Vault Frog Coin 5"
    BELOME_TEMPLE_VAULT_FROG_COIN_7 = "Belome Temple Vault Frog Coin 7"
    BELOME_TEMPLE_VAULT_MIDDLE_ITEM_BAG = "Belome Temple Vault Middle Item Bag"
    BELOME_TEMPLE_VAULT_FROG_COIN_6 = "Belome Temple Vault Frog Coin 6"
    BELOME_TEMPLE_VAULT_FROG_COIN_1 = "Belome Temple Vault Frog Coin 1"
    BELOME_TEMPLE_VAULT_FROG_COIN_4 = "Belome Temple Vault Frog Coin 4"
    BELOME_TEMPLE_VAULT_FROG_COIN_8 = "Belome Temple Vault Frog Coin 8"
    BELOME_TEMPLE_VAULT_FLOWER_4 = "Belome Temple Vault Flower 4"
    BELOME_TEMPLE_VAULT_FLOWER_1 = "Belome Temple Vault Flower 1"
    BELOME_TEMPLE_VAULT_FLOWER_2 = "Belome Temple Vault Flower 2"
    BELOME_TEMPLE_VAULT_FLOWER_3 = "Belome Temple Vault Flower 3"
    BELOME_TEMPLE_VAULT_RIGHT_ITEM_BAG = "Belome Temple Vault Right Item Bag"
    LANDS_END_BEE_ROOM_CHEST = "Land's End Bee Room Chest"
    LANDS_END_SKY_BRIDGE_FREESTANDING_ITEM = "Land's End Sky Bridge Freestanding Item"
    LANDS_END_CHOW_PIT_RIGHT_CHEST = "Land's End Chow Pit Right Chest"
    LANDS_END_CHOW_PIT_LEFT_CHEST = "Land's End Chow Pit Left Chest"
    LANDS_END_BELOME_TEMPLE_CLOUD_BOSS_FIGHT = "Land's End/belome Temple Cloud Boss Fight"
    LANDS_END_BELOME_TEMPLE_CLOUD_STAR_PIECE = "Land's End/belome Temple Cloud Star Piece"
    LANDS_END_1ST_PURCHASE_CHEST = "Land's End Shaman 400 Coin Chest"
    LANDS_END_GROTTO_CORNER_CHEST = "Land's End Grotto Corner Chest"
    LANDS_END_GROTTO_NEAR_SEWER_CHEST = "Land's End Grotto Near Sewer Chest"
    LANDS_END_GROTTO_FIRST_CHEST = "Land's End Grotto First Chest"
    LANDS_END_FIRST_CHEST = "Land's End First Chest"
    LANDS_END_2ND_PURCHASE_CHEST = "Land's End Shaman 800 Coin Chest"
    LANDS_END_WHIRLPOOL_1ST_UNDERGROUND_CHEST = "Land's End Whirlpool 1st Underground Chest"
    BELOME_TEMPLE_BOSS_FIGHT = "Belome Temple Boss Fight"
    BELOME_TEMPLE_POSTGAME_BOSS_FIGHT = "Belome Temple Postgame Boss Fight"
    BELOME_TEMPLE_BOSS_STAR_PIECE = "Belome Temple Boss Star Piece"
    BELOME_TEMPLE_POSTGAME_BOSS_STAR_PIECE = "Belome Temple Postgame Boss Star Piece"
    BELOME_TEMPLE_POSTGAME_PRIZE = "Belome Temple Postgame Prize"
    LANDS_END_TROOPA_CLIMB_SUB_12_SECOND_PRIZE = "Land's End Troopa Climb Sub-12 Second Prize"
    MARIO_SPELL_1 = "Mario Spell 1"
    MARIO_SPELL_2 = "Mario Spell 2"
    MARIO_SPELL_3 = "Mario Spell 3"
    MARIO_SPELL_4 = "Mario Spell 4"
    MARIO_SPELL_5 = "Mario Spell 5"
    MARIO_SPELL_6 = "Mario Spell 6"
    TOADS_POSTGAME_ITEM_GRANT = "Toad's Postgame Item Grant"
    STARTER_CHARACTER_1 = "Starter Character 1"
    STARTER_CHARACTER_2 = "Starter Character 2"
    STARTER_CHARACTER_3 = "Starter Character 3"
    STARTER_CHARACTER_4 = "Starter Character 4"
    STARTER_CHARACTER_5 = "Starter Character 5"
    STARTER_ITEM_1 = "Starter Item 1"
    STARTER_ITEM_2 = "Starter Item 2"
    STARTER_ITEM_3 = "Starter Item 3"
    STARTER_ITEM_4 = "Starter Item 4"
    MARRYMORE_ALTAR_CHAPEL_ITEM = "Marrymore Altar Chapel Item"
    MARRYMORE_INN_ELDERLY_GUESTS_MAJOR_TIP = "Marrymore Inn Elderly Guest Tip (on The Way Out)"
    MARRYMORE_BOSS_FIGHT = "Marrymore Boss Fight"
    MARRYMORE_POSTGAME_BOSS_FIGHT = "Marrymore Postgame Boss Fight"
    MARRYMORE_POSTGAME_PRIZE = "Marrymore Postgame Prize"
    MARRYMORE_BOSS_STAR_PIECE = "Marrymore Boss Star Piece"
    MARRYMORE_POSTGAME_BOSS_STAR_PIECE = "Marrymore Postgame Boss Star Piece"
    MARRYMORE_CHARACTER_RECRUIT = "Marrymore Character Join"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_5 = "Marrymore Suite Total Stays Prize 5"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_1 = "Marrymore Suite Total Stays Prize 1"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_4 = "Marrymore Suite Total Stays Prize 4"
    MARRYMORE_INN_REGULAR_ROOM_CHEST = "Marrymore Inn Regular Room Chest"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_2 = "Marrymore Suite Total Stays Prize 2"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_6 = "Marrymore Suite Total Stays Prize 6"
    MARRYMORE_SNIFIT_1_CHAPEL_ITEM = "Marrymore Snifit 1 Chapel Item"
    MARRYMORE_SNIFIT_2_CHAPEL_ITEM = "Marrymore Snifit 2 Chapel Item"
    MARRYMORE_SNIFIT_3_CHAPEL_ITEM = "Marrymore Snifit 3 Chapel Item"
    MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_3 = "Marrymore Suite Total Stays Prize 3"
    TOADSTOOL_SPELL_1 = "Toadstool Spell 1"
    TOADSTOOL_SPELL_2 = "Toadstool Spell 2"
    TOADSTOOL_SPELL_3 = "Toadstool Spell 3"
    TOADSTOOL_SPELL_4 = "Toadstool Spell 4"
    TOADSTOOL_SPELL_5 = "Toadstool Spell 5"
    TOADSTOOL_SPELL_6 = "Toadstool Spell 6"
    MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_FREESTANDING_FROG_COIN = "Midas River Bottom Left Tunnel Freestanding Frog Coin"
    MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_FREESTANDING_FLOWER = "Midas River Bottom Right Tunnel Freestanding Flower"
    MIDAS_RIVER_FIRST_PLAY_REWARD = "Midas River First Play Reward"
    MIDAS_RIVER_UPPER_LEFT_TUNNEL_FREESTANDING_FROG_COIN = "Midas River Upper Left Tunnel Freestanding Frog Coin"
    BOWSER_SPELL_1 = "Bowser Spell 1"
    BOWSER_SPELL_2 = "Bowser Spell 2"
    BOWSER_SPELL_3 = "Bowser Spell 3"
    BOWSER_SPELL_4 = "Bowser Spell 4"
    BOWSER_SPELL_5 = "Bowser Spell 5"
    BOWSER_SPELL_6 = "Bowser Spell 6"
    MOLEVILLE_BUCKET_GIRL = "Moleville Bucket Girl"
    CARBO_COOKIE_TRADER = "Carbo Cookie Trader"
    MOLEVILLE_FIREWORKS_SHOP_FIRST_ITEM = "Moleville Fireworks Shop Item"
    MOLEVILLE_MINES_SECOND_BOSS_FIGHT = "Moleville Mines Second Boss Fight"
    MOLEVILLE_MINES_NEAR_FINAL_TRAIN_TRACKS_CHEST = "Moleville Mines Near Final Train Tracks Chest"
    MOLEVILLE_MINES_CHARACTER_RECRUIT = "Moleville Mines Character Recruit"
    MOLEVILLE_MINES_BEFORE_BOSS_UPPER_CHEST = "Moleville Mines Before Boss Upper Chest"
    MOLEVILLE_MINES_POSTGAME_BOSS_FIGHT = "Moleville Mines Postgame Boss Fight"
    MOLEVILLE_MINES_POSTGAME_PRIZE = "Moleville Mines Postgame Prize"
    MOLEVILLE_MINES_POSTGAME_BOSS_STAR_PIECE = "Moleville Mines Postgame Boss Star Piece"
    MOLEVILLE_MINES_BEFORE_BOSS_LEFT_CHEST = "Moleville Mines Before Boss Left Chest"
    MOLEVILLE_MINES_SHY_GUY_CART = "Moleville Mines Shy Guy Cart"
    MOLEVILLE_MINES_SECOND_BOSS_STAR_PIECE = "Moleville Mines Second Boss Star Piece"
    MOLEVILLE_MINES_TWO_LEVEL_TRAINTRACK_ROOM_CHEST = "Moleville Mines Two-level Traintrack Room Chest"
    MOLEVILLE_MINES_FIRST_BOSS_FIGHT = "Moleville Mines First Boss Fight"
    MOLEVILLE_MINES_FIRST_BOSS_ITEM = "Moleville Mines First Boss Item"
    MOLEVILLE_MINES_LEFT_BANDIT = "Moleville Mines Left Bandit"
    MOLEVILLE_MINES_RIGHT_BANDIT = "Moleville Mines Right Bandit"
    MOLEVILLE_MINES_FIRST_BOSS_STAR_PIECE = "Moleville Mines First Boss Star Piece"
    MOLEVILLE_MINES_TRAMPOLINE_BANDIT = "Moleville Mines Trampoline Bandit"
    PURTEND_STORE = "Pur-tend Store"
    MOLEVILLE_FIRST_TREASURE_SHOP_ITEM = "Moleville First Treasure Shop Item"
    MOLEVILLE_SECOND_TREASURE_SHOP_ITEM = "Moleville Second Treasure Shop Item"
    MOLEVILLE_THIRD_TREASURE_SHOP_ITEM = "Moleville Third Treasure Shop Item"
    MONSTRO_TOWN_DOJO_POSTGAME_FIGHT = "Monstro Town Dojo Postgame Fight"
    MONSTRO_TOWN_DOJO_POSTGAME_STAR_PIECE = "Monstro Town Dojo Postgame Star Piece"
    MONSTRO_TOWN_DOJO_FIRST_FIGHT = "Monstro Town Dojo First Fight"
    MONSTRO_TOWN_DOJO_FIRST_FIGHT_STAR_PIECE = "Monstro Town Dojo First Fight Star Piece"
    MONSTRO_TOWN_DOJO_FOURTH_FIGHT = "Monstro Town Dojo Fourth Fight"
    MONSTRO_TOWN_DOJO_FOURTH_FIGHT_STAR_PIECE = "Monstro Town Dojo Fourth Fight Star Piece"
    MONSTRO_TOWN_DOJO_SECOND_FIGHT = "Monstro Town Dojo Second Fight"
    MONSTRO_TOWN_DOJO_SECOND_FIGHT_STAR_PIECE = "Monstro Town Dojo Second Fight Star Piece"
    MONSTRO_TOWN_DOJO_THIRD_FIGHT = "Monstro Town Dojo Third Fight"
    MONSTRO_TOWN_DOJO_THIRD_FIGHT_STAR_PIECE = "Monstro Town Dojo Third Fight Star Piece"
    MONSTRO_TOWN_DOJO_PRIZE = "Monstro Town Dojo Prize"
    MONSTRO_TOWN_DOJO_POSTGAME_PRIZE = "Monstro Town Dojo Postgame Prize"
    MONSTRO_TOWN_ENTRANCE_CHEST = "Monstro Town Entrance Chest"
    MONSTRO_TOWN_SUPER_JUMP_FIRST_PRIZE = "Monstro Town Super Jump First Prize"
    MONSTRO_TOWN_FLAG_EXCHANGE_PRIZE = "Monstro Town Flag Exchange Prize"
    MONSTRO_TOWN_SEALED_DOOR_BOSS_FIGHT = "Monstro Town Sealed Door Boss Fight"
    MONSTRO_TOWN_POSTGAME_SEALED_DOOR_BOSS_FIGHT = "Monstro Town Postgame Sealed Door Boss Fight"
    MONSTRO_TOWN_SEALED_DOOR_PRIZE = "Monstro Town Sealed Door Prize"
    MONSTRO_TOWN_POSTGAME_SEALED_DOOR_PRIZE = "Monstro Town Postgame Sealed Door Prize"
    MONSTRO_TOWN_SEALED_DOOR_STAR_PIECE = "Monstro Town Sealed Door Star Piece"
    MONSTRO_TOWN_POSTGAME_SEALED_DOOR_STAR_PIECE = "Monstro Town Postgame Sealed Door Star Piece"
    MONSTRO_TOWN_SUPER_JUMP_SECOND_PRIZE = "Monstro Town Super Jump Second Prize"
    MONSTRO_TOWN_THWOMP_KEY = "Monstro Town Thwomp Key"
    MUSHROOM_KINGDOM_BOSS_FIGHT = "Mushroom Kingdom Boss Fight"
    MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_CHAIR_ITEM = "Mushroom Kingdom Toadstool's Room Chair Item"
    MUSHROOM_KINGDOM_SHOP_FREE_ITEM = "Mushroom Kingdom Shop Free Item"
    MUSHROOM_KINGDOM_GAMEBOY_KID = "Mushroom Kingdom Gameboy Kid"
    MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_LIBERATED = "Mushroom Kingdom Vault Left Chest (liberated)"
    MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_LIBERATED = "Mushroom Kingdom Vault Middle Chest (liberated)"
    MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_LIBERATED = "Mushroom Kingdom Vault Right Chest (liberated)"
    MUSHROOM_KINGDOM_CASTLE_MAIN_HALLWAY_CHEST = "Mushroom Kingdom Castle Main Hallway Chest"
    MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_TOAD_RESCUE_ITEM = "Mushroom Kingdom Toadstool's Room Toad Rescue Item (invasion)"
    MUSHROOM_KINGDOM_INVASION_FAMILY_RESCUE = "Mushroom Kingdom Invasion Family Rescue"
    MUSHROOM_KINGDOM_INVASION_GUEST_ROOM = "Mushroom Kingdom Invasion Guest Room"
    MUSHROOM_KINGDOM_EASTERN_GUARD_RESCUE = "Mushroom Kingdom Eastern Guard Rescue (invasion)"
    MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_OCCUPIED = "Mushroom Kingdom Vault Left Chest (occupied)"
    MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_OCCUPIED = "Mushroom Kingdom Vault Middle Chest (occupied)"
    MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_OCCUPIED = "Mushroom Kingdom Vault Right Chest (occupied)"
    MUSHROOM_KINGDOM_SHOP_BASEMENT_LEFT_CHEST = "Mushroom Kingdom Shop Basement Left Chest"
    MUSHROOM_KINGDOM_SHOP_BASEMENT_RIGHT_CHEST = "Mushroom Kingdom Shop Basement Right Chest"
    MUSHROOM_KINGDOM_INVASION_BOSS_STAR_PIECE = "Mushroom Kingdom Invasion Boss Star Piece"
    MUSHROOM_KINGDOM_SHOP_RARE_FROG_COIN_EXCHANGE = "Mushroom Kingdom Shop Rare Frog Coin Exchange"
    WALLET_REWARD_1 = "Wallet Exchange Reward 1"
    WALLET_REWARD_2 = "Wallet Exchange Reward 2"
    MALLOW_SPELL_1 = "Mallow Spell 1"
    MALLOW_SPELL_2 = "Mallow Spell 2"
    MALLOW_SPELL_3 = "Mallow Spell 3"
    MALLOW_SPELL_4 = "Mallow Spell 4"
    MALLOW_SPELL_5 = "Mallow Spell 5"
    MALLOW_SPELL_6 = "Mallow Spell 6"
    MUSHROOM_WAY_FIRST_CHEST = "Mushroom Way First Chest"
    MUSHROOM_WAY_FIRST_TOAD_REWARD = "Mushroom Way First Toad Reward"
    MUSHROOM_WAY_SECOND_CHEST = "Mushroom Way Second Chest"
    MUSHROOM_WAY_FLOWER_JUMP_LEFT_CHEST = "Mushroom Way Flower Jump Left Chest"
    MUSHROOM_WAY_SECOND_TOAD_REWARD = "Mushroom Way Second Toad Reward"
    MUSHROOM_WAY_BOSS_REWARD = "Mushroom Way Boss Item Reward"
    MUSHROOM_WAY_CHARACTER_RECRUIT = "Mushroom Way Character Join"
    MUSHROOM_WAY_LEFT_FREESTANDING_ITEM = "Mushroom Way Left Freestanding Item"
    MUSHROOM_WAY_SECOND_ROOM_RIGHT_CHEST = "Mushroom Way Second Room Right Chest"
    MUSHROOM_WAY_RIGHT_FREESTANDING_ITEM = "Mushroom Way Right Freestanding Item"
    MUSHROOM_WAY_BOSS_STAR_PIECE = "Mushroom Way Boss Star Piece"
    MUSHROOM_WAY_BOSS_FIGHT = "Mushroom Way Boss Fight"
    NIMBUS_LAND_GARRO_CHECK = "Nimbus Land Garro Check"
    NIMBUS_CASTLE_GIANT_EGG_BOSS_FIGHT = "Nimbus Castle Giant Egg Boss Fight"
    NIMBUS_CASTLE_GIANT_EGG_BOSS_STAR_PIECE = "Nimbus Castle Giant Egg Boss Star Piece"
    NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_RIGHT_CHEST = "Nimbus Castle West Stairway Room Right Chest"
    NIMBUS_CASTLE_POST_THRONE_CHEST_UNOCCUPIED = "Nimbus Castle Post-throne Chest (liberated)"
    NIMBUS_CASTLE_POST_THRONE_CHEST_OCCUPIED = "Nimbus Castle Post-throne Chest (occupied)"
    NIMBUS_CASTLE_5_DOOR_ROOM_CHEST_LIBERATED = "Nimbus Castle 5-exit Room Chest (liberated)"
    NIMBUS_CASTLE_5_DOOR_ROOM_CHEST_OCCUPIED = "Nimbus Castle 5-exit Room Chest (occupied)"
    NIMBUS_CASTLE_BUSINESS_CENTRE_CHEST = "Nimbus Castle Business Centre Chest (occupied)"
    NIMBUS_CASTLE_WEST_TWO_LEVEL_ROOM_CHEST = "Nimbus Castle West Two-level Room Chest"
    NIMBUS_CASTLE_GIANT_EGG_PRIZE = "Nimbus Castle Giant Egg Prize"
    NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_LEFT_CHEST = "Nimbus Castle West Stairway Room Left Chest"
    NIMBUS_CASTLE_WEST_CELLAR_GUARD = "Nimbus Castle West Cellar Guard"
    NIMBUS_CASTLE_WEST_CELLAR_CIVILIAN = "Nimbus Castle West Cellar Civilian"
    NIMBUS_CASTLE_SINGLE_GOLD_BIRD_ROOM_CHEST = "Nimbus Castle Single Gold Bird Room Chest"
    NIMBUS_CASTLE_STATUE_GAME_PRIZE = "Nimbus Castle Statue Game Prize"
    NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_LOWER_CHEST = "Nimbus Castle East Two-level Room Lower Chest"
    NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_UPPER_CHEST = "Nimbus Castle East Two-level Room Upper Chest"
    NIMBUS_LAND_FINAL_BOSS_FIGHT = "Nimbus Land Final Boss Fight"
    NIMBUS_LAND_FINAL_BOSS_STAR_PIECE = "Nimbus Land Final Boss Star Piece"
    NIMBUS_LAND_DREAM_CUSHION_1ST_ITEM = "Nimbus Land Dream Cushion 1st Item"
    NIMBUS_LAND_DREAM_CUSHION_2ND_ITEM = "Nimbus Land Dream Cushion 2nd Item"
    NIMBUS_LAND_POST_INVASION_UPPER_RIGHT_HOUSE = "Nimbus Land Post-invasion Upper Right House"
    NIMBUS_CASTLE_POST_INVASION_NORTH_CELLAR = "Nimbus Castle Post-invasion North Cellar"
    NIMBUS_LAND_POST_INVASION_OFF_CLOUD_ITEM = "Nimbus Land Post-invasion Off-cloud Item"
    NIMBUS_LAND_SHOP_CHEST = "Nimbus Land Shop Chest"
    NIMBUS_CASTLE_STATUE_KEEPER_BOSS_FIGHT = "Nimbus Castle Statue Keeper Boss Fight"
    NIMBUS_CASTLE_STATUE_KEEPER_BOSS_STAR_PIECE = "Nimbus Castle Statue Keeper Boss Star Piece"
    OUTER_FACTORY_FALLING_AXEM_ROOM_CHEST = "Outer Factory Falling Axem Room Chest"
    OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_LEFT_CHEST = "Outer Factory Room Behind Machine Yarid Left Chest"
    OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_RIGHT_CHEST = "Outer Factory Room Behind Machine Yarid Right Chest"
    OUTER_FACTORY_CONVEYOR_ROOM_RIGHT_CHEST = "Outer Factory Conveyor Room Right Chest"
    OUTER_FACTORY_CONVEYOR_ROOM_LEFT_CHEST = "Outer Factory Conveyor Room Left Chest"
    OUTER_FACTORY_BOLT_PLATFORM_CHEST = "Outer Factory Bolt Platform Chest"
    OUTER_FACTORY_FIRST_BOSS_FIGHT = "Outer Factory First Boss Fight"
    OUTER_FACTORY_FIRST_BOSS_STAR_PIECE = "Outer Factory First Boss Star Piece"
    OUTER_FACTORY_SECOND_BOSS_FIGHT = "Outer Factory Second Boss Fight"
    OUTER_FACTORY_SECOND_BOSS_STAR_PIECE = "Outer Factory Second Boss Star Piece"
    OUTER_FACTORY_PIT_BACK_CHEST = "Outer Factory Pit Back Chest"
    OUTER_FACTORY_PIT_FRONT_CHEST = "Outer Factory Pit Front Chest"
    OUTER_FACTORY_EARLY_SAVE_ROOM_CHEST = "Outer Factory Early Save Room Chest"
    PIPE_VAULT_NIPPER_ROOM_SECOND_CHEST = "Pipe Vault Nipper Room Second Chest"
    PIPE_VAULT_GOOMBA_THUMPIN_FIRST_PRIZE = "Pipe Vault Goomba Thumpin First Prize"
    PIPE_VAULT_GOOMBA_THUMPIN_SECOND_PRIZE = "Pipe Vault Goomba Thumpin Second Prize"
    PIPE_VAULT_NIPPER_ROOM_FIRST_CHEST = "Pipe Vault Nipper Room First Chest"
    PIPE_VAULT_SLIDE_ROOM_BACK_CHEST = "Pipe Vault Slide Room Back Chest"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_1 = "Pipe Vault Slide Room Freestanding Coin 1"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_2 = "Pipe Vault Slide Room Freestanding Coin 2"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_3 = "Pipe Vault Slide Room Freestanding Coin 3"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_4 = "Pipe Vault Slide Room Freestanding Coin 4"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_5 = "Pipe Vault Slide Room Freestanding Coin 5"
    PIPE_VAULT_SLIDE_ROOM_FREESTANDING_FROG_COIN = "Pipe Vault Slide Room Freestanding Frog Coin"
    PIPE_VAULT_SLIDE_ROOM_FRONT_CHEST = "Pipe Vault Slide Room Front Chest"
    PIPE_VAULT_SLIDE_ROOM_MIDDLE_CHEST = "Pipe Vault Slide Room Middle Chest"
    ROSE_TOWN_GARDENER_LEFT_CHEST = "Rose Town Gardener Left Chest"
    ROSE_TOWN_GARDENER_RIGHT_CHEST = "Rose Town Gardener Right Chest"
    ROSE_TOWN_GAZ_GIFT = "Rose Town Gaz Gift"
    ROSE_TOWN_INN_TOAD_GIFT = "Rose Town Inn Toad Gift"
    ROSE_TOWN_SHOP_LEFT_CHEST = "Rose Town Shop Left Chest"
    ROSE_TOWN_SHOP_RIGHT_CHEST = "Rose Town Shop Right Chest"
    ROSE_TOWN_UPPER_HOUSE_LEFT_CHEST = "Rose Town Upper House Left Chest"
    ROSE_TOWN_UPPER_HOUSE_MAZE_SECRET_PRIZE = "Rose Town Upper House Maze Secret Prize"
    ROSE_TOWN_UPPER_HOUSE_RIGHT_CHEST = "Rose Town Upper House Right Chest"
    ROSE_TOWN_UPPER_HOUSE_TOP_FLOOR_CHEST = "Rose Town Upper House Top Floor Chest"
    ROSE_WAY_FREESTANDING_COIN_1 = "Rose Way Freestanding Coin 1"
    ROSE_WAY_FREESTANDING_COIN_2 = "Rose Way Freestanding Coin 2"
    ROSE_WAY_FREESTANDING_COIN_3 = "Rose Way Freestanding Coin 3"
    ROSE_WAY_FREESTANDING_COIN_4 = "Rose Way Freestanding Coin 4"
    ROSE_WAY_FREESTANDING_COIN_5 = "Rose Way Freestanding Coin 5"
    ROSE_WAY_FIVE_CHEST_AREA_BOTTOM_LEFT_CHEST = "Rose Way Five-chest Area Bottom Left Chest"
    ROSE_WAY_FIVE_CHEST_BOTTOM_RIGHT_CHEST = "Rose Way Five-chest Bottom Right Chest"
    ROSE_WAY_FIVE_CHEST_TOP_LEFT_CHEST = "Rose Way Five-chest Top Left Chest"
    ROSE_WAY_FIVE_CHEST_TOP_RIGHT_CHEST = "Rose Way Five-chest Top Right Chest"
    ROSE_WAY_FIVE_CHEST_AREA_TOP_MIDDLE_CHEST = "Rose Way Five-chest Area Top Middle Chest"
    ROSE_WAY_FREESTANDING_FLOWER = "Rose Way Freestanding Flower"
    ROSE_WAY_FREESTANDING_MUSHROOM = "Rose Way Freestanding Mushroom"
    ROSE_WAY_SWINGING_SHY_GUY_CHEST = "Rose Way Swinging Shy Guy Chest"
    SEA_SAVE_ROOM_BACK_CHEST = "Sea Save Room Back Chest"
    SEA_SAVE_ROOM_FRONT_CHEST = "Sea Save Room Front Chest"
    SEA_SAVE_ROOM_MIDDLE_CHEST = "Sea Save Room Middle Chest"
    SEA_STARSLAP_ROOM_CHEST = "Sea Starslap Room Chest"
    SEA_WHIRLPOOL_ROOM_CHEST = "Sea Whirlpool Room Chest"
    DISCIPLE_SHOP_FIRST_ITEM = "Disciple Shop First Item"
    DISCIPLE_SHOP_SECOND_ITEM = "Disciple Shop Second Item"
    DISCIPLE_SHOP_THIRD_ITEM = "Disciple Shop Third Item"
    DISCIPLE_SHOP_FOURTH_ITEM = "Disciple Shop Fourth Item"
    DISCIPLE_SHOP_FIFTH_ITEM = "Disciple Shop Fifth Item"
    SEASIDE_TOWN_BOSS_FIGHT = "Seaside Town Boss Fight"
    SEASIDE_TOWN_BOSS_STAR_PIECE = "Seaside Town Boss Star Piece"
    SEASIDE_TOWN_BOSS_PRIZE = "Seaside Town Boss Prize"
    SEASIDE_TOWN_SHED_RESCUE = "Seaside Town Shed Rescue"
    STAR_HILL_FREESTANDING_STAR_PIECE = "Star Hill Freestanding Star Piece"
    SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_LEFT_CHEST = "Sunken Ship Outside Clone Room Left Chest"
    SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_RIGHT_CHEST = "Sunken Ship Outside Clone Room Right Chest"
    SUNKEN_SHIP_NEAR_FINAL_BOSS_CHEST = "Sunken Ship Near Final Boss Chest"
    SUNKEN_SHIP_HIDDEN_BOX_ROOM_CHEST = "Sunken Ship Hidden Box Room Chest"
    SUNKEN_SHIP_CLONE_ROOM_CHEST = "Sunken Ship Clone Room Chest"
    SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_1 = "Sunken Ship Underwater Freestanding Frog Coin 1"
    SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_3 = "Sunken Ship Underwater Freestanding Frog Coin 3"
    SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_4 = "Sunken Ship Underwater Freestanding Frog Coin 4"
    SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_2 = "Sunken Ship Underwater Freestanding Frog Coin 2"
    SUNKEN_SHIP_LARGE_POOL_FREESTANDING_FROG_COIN = "Sunken Ship Large Pool Freestanding Frog Coin"
    SUNKEN_SHIP_HIDONS_ROOM_LEFT_CHEST = "Sunken Ship Hidon's Room Left Chest"
    SUNKEN_SHIP_HIDONS_ROOM_RIGHT_CHEST = "Sunken Ship Hidon's Room Right Chest"
    SUNKEN_SHIP_HIDDEN_UNDERWATER_ROOM_CHEST = "Sunken Ship Hidden Underwater Room Chest"
    MIMIC_CHEST_2_BOSS_FIGHT = "Mimic Chest #2 Boss Fight"
    MIMIC_CHEST_2_FIRST_REWARD = "Mimic Chest #2 Drop Reward"
    MIMIC_CHEST_2_RELOAD_REWARD = "Mimic Chest #2 Reload Reward"
    MIMIC_CHEST_2_STAR_PIECE = "Mimic Chest #2 Star Piece"
    SUNKEN_SHIP_3D_MAZE_PRIZE = "Sunken Ship 3d Maze Prize"
    SUNKEN_SHIP_BARREL_SWITCH_PRIZE = "Sunken Ship Barrel Switch Prize"
    SUNKEN_SHIP_CANNONBALL_PUZZLE_PRIZE = "Sunken Ship Cannonball Puzzle Prize"
    SUNKEN_SHIP_COIN_SNAKE_PUZZLE_PRIZE = "Sunken Ship Coin Snake Puzzle Prize"
    SUNKEN_SHIP_FINAL_BOSS_FIGHT = "Sunken Ship Exit Boss Fight"
    SUNKEN_SHIP_FINAL_BOSS_STAR_PIECE = "Sunken Ship Exit Boss Star Piece"
    SUNKEN_SHIP_PASSWORD_BOSS_FIGHT = "Sunken Ship Password Boss Fight"
    SUNKEN_SHIP_PASSWORD_BOSS_STAR_PIECE = "Sunken Ship Password Boss Star Piece"
    SUNKEN_SHIP_POSTGAME_BOSS_FIGHT = "Sunken Ship Postgame Boss Fight"
    SUNKEN_SHIP_POSTGAME_PRIZE = "Sunken Ship Postgame Prize"
    SUNKEN_SHIP_POSTGAME_BOSS_STAR_PIECE = "Sunken Ship Postgame Boss Star Piece"
    SUNKEN_SHIP_FIRST_STAIRWAY_FREESTANDING_FLOWER = "Sunken Ship First Stairway Freestanding Flower"
    SUNKEN_SHIP_FIRST_STAIRWAY_CHEST = "Sunken Ship First Stairway Chest"
    SUNKEN_SHIP_SHOP_AREA_CHEST = "Sunken Ship Shop Area Chest"
    SUNKEN_SHIP_TRAMPOLINE_PUZZLE_PRIZE = "Sunken Ship Trampoline Puzzle Prize"
    SUNKEN_SHIP_TROOPA_CANNONBALL_PRIZE = "Sunken Ship Troopa Cannonball Prize"
    MELODY_BAY_SONG_1_REWARD = "Melody Bay Song 1 Reward"
    MELODY_BAY_SONG_2_REWARD = "Melody Bay Song 2 Reward"
    MELODY_BAY_SONG_3_REWARD = "Melody Bay Song 3 Reward"
    TADPOLE_POND_CRICKET_JAM_EXCHANGE = "Tadpole Pond Cricket Jam Exchange"
    TADPOLE_POND_CRICKET_PIE_EXCHANGE = "Tadpole Pond Cricket Pie Exchange"
    YOSTER_ISLE_ENTRANCE_CHEST = "Yo'ster Isle Entrance Chest"
    YOSTER_ISLE_RACE_STARTING_COOKIES = "Yo'ster Isle Race-starting Cookies"
    YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_1 = "Yo'ster Isle First Race Prize Item 1"
    YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_3 = "Yo'ster Isle First Race Prize Item 3"
    YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_2 = "Yo'ster Isle First Race Prize Item 2"
    MARIOS_PAD_BED_FLAG = "Mario's Pad Bed Flag"
    ROSE_TOWN_SIGN_FLAG = "Rose Town Sign Flag"
    YOSTER_ISLE_GOAL_FLAG = "Yo'ster Isle Goal Flag"
    MARIOS_PAD_STEAMWHISTLE_FLAG = "Mario's Pad Steamwhistle Flag"
    MARIOS_PAD_LANTERN_FLAG = "Mario's Pad Lantern Flag"
    MARIOS_PAD_HAT_FLAG = "Mario's Pad Hat Flag"
    MUSHROOM_WAY_TREE_FLAG = "Mushroom Way Tree Flag"
    MUSHROOM_KINGDOM_SIGN_FLAG = "Mushroom Kingdom Sign Flag"
    MUSHROOM_KINGDOM_EMPTY_HOUSE_FLAG = "Mushroom Kingdom Empty House Flag"
    CHANCELLOR_THRONE_FLAG = "Chancellor Throne Flag"
    BANDITS_WAY_FLOWER_FLAG = "Bandit's Way Flower Flag"
    KERO_STAIRS_FLAG = "Kero Stairs Flag"
    KERO_GATE_FLAG = "Kero Gate Flag"
    MIDAS_TREES_FLAG = "Midas Trees Flag"
    TADPOLE_CABINET_FLAG = "Tadpole Cabinet Flag"
    ROSE_WAY_DIRT_PATCH_FLAG = "Rose Way Dirt Patch Flag"
    ROSE_TOWN_HYDRANT_FLAG = "Rose Town Hydrant Flag"
    ROSE_TOWN_SINK_FLAG = "Rose Town Sink Flag"
    ROSE_TOWN_BOWSER_FLAG = "Rose Town Bowser Flag"
    ROSE_TOWN_GARDENER_HYDRANT_FLAG = "Rose Town Gardener Hydrant Flag"
    ROSE_TOWN_GARDENER_BUCKET_FLAG = "Rose Town Gardener Bucket Flag"
    ROSE_TOWN_GARDENER_LEAF_FLAG = "Rose Town Gardener Leaf Flag"
    FOREST_MAZE_SECRET_STUMP_FLAG = "Forest Maze Secret Stump Flag"
    FOREST_MAZE_SECRET_MUSHROOMS_FLAG = "Forest Maze Secret Mushrooms Flag"
    FOREST_MAZE_SECRET_WIGGLER_FLAG = "Forest Maze Secret Wiggler Flag"
    PIPE_VAULT_EXTERIOR_FLAG = "Pipe Vault Exterior Flag"
    PIPE_VAULT_RED_PIPE_FLAG = "Pipe Vault Red Pipe Flag"
    YOSTER_ISLE_HUT_FLAG = "Yo'ster Isle Hut Flag"
    MOLEVILLE_HYDRANT_FLAG = "Moleville Hydrant Flag"
    MOLEVILLE_MOUNTAIN_BUSH_FLAG = "Moleville Mountain Bush Flag"
    MOLEVILLE_MOUNTAIN_GO_FLAG = "Moleville Mountain Go Flag"
    MOLEVILLE_BED_FLAG = "Moleville Bed Flag"
    MOLEVILLE_MINES_ARROWS_FLAG = "Moleville Mines Arrows Flag"
    MOLEVILLE_MINES_CEILING_FLAG = "Moleville Mines Ceiling Flag"
    MOLEVILLE_MINES_ENTRY_FLAG = "Moleville Mines Entry Flag"
    BOOSTER_PASS_CORNER_BUSH_FLAG = "Booster Pass Corner Bush Flag"
    BOOSTER_TOWER_EXTERIOR_SIGN_FLAG = "Booster Tower Exterior Sign Flag"
    BOOSTER_TOWER_DESK_FLAG = "Booster Tower Desk Flag"
    BOOSTER_TOWER_MASHER_ROOM_FLAG = "Booster Tower Masher Room Flag"
    BOOSTER_TOWER_CURTAIN_FLAG = "Booster Tower Curtain Flag"
    BOOSTER_TOWER_THWOMP_INVISIBLE_FLAG = "Booster Tower Thwomp Invisible Flag"
    BOOSTER_TOWER_BROKEN_FRAME_FLAG = "Booster Tower Broken Frame Flag"
    BOOSTER_TOWER_BEETLE_CAGE_FLAG = "Booster Tower Beetle Cage Flag"
    BOOSTER_TOWER_TOY_BOX_FLAG = "Booster Tower Toy Box Flag"
    MARRYMORE_OUTSIDE_CRATE_FLAG = "Marrymore Outside Crate Flag"
    MARRYMORE_HALLWAY_FLAG = "Marrymore Hallway Flag"
    MARRYMORE_CURTAINS_FLAG = "Marrymore Curtains"
    MARRYMORE_SUITE_BED_FLAG = "Marrymore Suite Bed Flag"
    MARRYMORE_KITCHEN_FLAG = "Marrymore Kitchen Flag"
    MARRYMORE_FIREPLACE_FLAG = "Marrymore Fireplace Flag"
    MARRYMORE_WINDOW_FLAG = "Marrymore Window Flag"
    MARRYMORE_ORGAN_FLAG = "Marrymore Organ Flag"
    MARRYMORE_ALTAR_FLAG = "Marrymore Altar Flag"
    STAR_HILL_NORTH_STAR_FLAG = "Star Hill North Star Flag"
    SEASIDE_TOWN_ANCHOR_FLAG = "Seaside Town Anchor Flag"
    SEASIDE_TOWN_HYDRANT_FLAG = "Seaside Town Hydrant Flag"
    SEASIDE_TOWN_BUCKET_FLAG = "Seaside Town Bucket Flag"
    SEASIDE_TOWN_FLOWERS_FLAG = "Seaside Town Flowers Flag"
    SEASIDE_TOWN_SHED_BOX_FLAG = "Seaside Town Shed Box Flag"
    SEA_ARROW_FLAG = "Sea Arrow Flag"
    SEA_BOXES_FLAG = "Sea Boxes Flag"
    SEA_STALAGNATE_FLAG = "Sea Stalagnate Flag"
    SEA_UNDERWATER_SAIL_FLAG = "Sea Underwater Sail Flag"
    SHIP_BARREL_PILE_FLAG = "Ship Barrel Pile Flag"
    SHIP_DOOR_MARKER_FLAG = "Ship Door Marker Flag"
    SHIP_BUTTON_FLAG = "Ship Button Flag"
    SHIP_SWITCH_FLAG = "Ship Switch Flag"
    LANDS_END_PLATFORM_FLAG = "Land's End Platform Flag"
    LANDS_END_CANNON_FLAG = "Land's End Cannon Flag"
    LANDS_END_ARROW_FLAG = "Land's End Arrow Flag"
    LANDS_END_HILL_FLAG = "Land's End Hill Flag"
    LANDS_END_TWO_HILL_FLAG = "Land's End Two Hill Flag"
    LANDS_END_STALAGMITE_FLAG = "Land's End Stalagmite Flag"
    LANDS_END_CLIFF_BUSH_FLAG = "Land's End Cliff Bush Flag"
    LANDS_END_SIGN_FLAG = "Land's End Sign Flag"
    TEMPLE_SHAFT_FLAG = "Temple Shaft Flag"
    TEMPLE_SHAFT_SWITCH_FLAG = "Temple Shaft Switch Flag"
    DOJO_BONSAI_FLAG = "Dojo Bonsai Flag"
    MONSTRO_ENTRANCE_SIGN_FLAG = "Monstro Entrance Sign Flag"
    MONSTRO_BAT_FLAG = "Monstro Bat Flag"
    MONSTRO_FAN_FLAG = "Monstro Fan Flag"
    MONSTRO_SHELL_FLAG = "Monstro Shell Flag"
    BEAN_VALLEY_PIPE_FLAG = "Bean Valley Pipe Flag"
    BEAN_VALLEY_BEANSTALK_BLOCK_FLAG = "Bean Valley Beanstalk Block Flag"
    BEAN_VALLEY_CLOUDS_FLAG = "Bean Valley Clouds Flag"
    CASINO_BELL_FLAG = "Casino Bell Flag"
    NIMBUS_GOLD_GOOMBA_FLAG = "Nimbus Gold Goomba Flag"
    NIMBUS_OUTDOOR_FLAG = "Nimbus Outdoor Flag"
    NIMBUS_INN_LOBBY_FLAG = "Nimbus Inn Lobby Flag"
    NIMBUS_PLANT_FLAG = "Nimbus Plant Flag"
    NIMBUS_BIRD_FLAG = "Nimbus Bird Flag"
    NIMBUS_HOT_SPRINGS_FLAG = "Nimbus Hot Springs Flag"
    BARREL_VOLCANO_INN_SIGN_FLAG = "Barrel Volcano Inn Sign Flag"
    BARREL_VOLCANO_STUMPET_FLAG = "Barrel Volcano Stumpet Flag"
    VOLCANO_SHIPS_FLAG = "Volcano Ships Flag"
    VOLCANO_BED_FLAG = "Volcano Bed Flag"
    VOLCANO_LAMP_FLAG = "Volcano Lamp Flag"
    KEEP_POST_OBSTACLE_BOSS_ROOM_FLAG = "Keep Post Obstacle Boss Room Flag"
    KEEP_THWOMP_FLAG = "Keep Thwomp Flag"
    FACTORY_LUGNUT_FLAG = "Factory Lugnut Flag"
    FACTORY_TRAMPOLINE_FLAG = "Factory Trampoline Flag"
    FACTORY_BUTTON_FLAG = "Factory Button Flag"
    INVISIBLE_FLAG_1 = "Invisible Flag 1"
    INVISIBLE_FLAG_2 = "Invisible Flag 2"
    INVISIBLE_FLAG_3 = "Invisible Flag 3"

location_name_lookup = {
    LocationNames.BANDITS_WAY_BOSS_FIGHT: "BanditsWayBossFight",
    LocationNames.BANDITS_WAY_BOSS_REWARD_1: "BanditsWayBossFirstItemDropLocation",
    LocationNames.BANDITS_WAY_BOSS_REWARD_2: "BanditsWayBossSecondItemDropLocation",
    LocationNames.BANDITS_WAY_1ST_COIN: "BanditsWayCoin1Location",
    LocationNames.BANDITS_WAY_2ND_COIN: "BanditsWayCoin2Location",
    LocationNames.BANDITS_WAY_3RD_COIN: "BanditsWayCoin3Location",
    LocationNames.BANDITS_WAY_CROCO_CHASE_CHEST: "BanditsWayDeadEndChestLocation",
    LocationNames.BANDITS_WAY_LONG_ROOM_CHEST: "BanditsWayDogChestLocation",
    LocationNames.BANDITS_WAY_FLOWER_CHEST: "BanditsWayFlowerJumpLocation",
    LocationNames.BANDITS_WAY_STAR_CHEST: "BanditsWayPlatformsLeftChestLocation",
    LocationNames.BANDITS_WAY_DOG_JUMP_CHEST: "BanditsWayPlatformsRightChestLocation",
    LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_FREESTANDING_FROG_COIN: "BeanValley1stRoomFloatingItemLocation",
    LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_LOWER_FREESTANDING_COIN: "BeanValley1stRoomLowerCoinLocation",
    LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN: "BeanValley1stRoomMiddleCoinLocation",
    LocationNames.BEAN_VALLEY_LOWEST_VINE_ROOM_UPPER_FREESTANDING_COIN: "BeanValley1stRoomUpperCoinLocation",
    LocationNames.BEAN_VALLEY_BOSS_REWARD: "BeanValleyBossNoteLocation",
    LocationNames.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE_CHEST: "BeanValleyBottomLeftPiranhaPipeLocation",
    LocationNames.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER_CHEST: "BeanValleyBottomRightPiranhaPipeLowerLocation",
    LocationNames.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER_CHEST: "BeanValleyBottomRightPiranhaPipeUpperLocation",
    LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_LOWEST_FREESTANDING_COIN: "BeanValleyEastBeanstalkCoin1Location",
    LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_LOWER_FREESTANDING_COIN: "BeanValleyEastBeanstalkCoin2Location",
    LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_MIDDLE_FREESTANDING_COIN: "BeanValleyEastBeanstalkCoin3Location",
    LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_HIGHER_FREESTANDING_COIN: "BeanValleyEastBeanstalkCoin4Location",
    LocationNames.BEAN_VALLEY_EAST_VINE_ROOM_HIGHEST_FREESTANDING_COIN: "BeanValleyEastBeanstalkCoin5Location",
    LocationNames.BEAN_VALLEY_SOUTH_UPPER_LEVEL_CHEST: "BeanValleyFirstDeadEndLocation",
    LocationNames.BEAN_VALLEY_NORTH_UPPER_LEVEL_CHEST: "BeanValleyFirstProgressChestLocation",
    LocationNames.BEAN_VALLEY_LEFT_PIRANHA_PIPE_CHEST: "BeanValleyLeftPiranhaPipeLocation",
    LocationNames.BEAN_VALLEY_BOSS_FIGHT: "BeanValleyPlanterBossFight",
    LocationNames.BEAN_VALLEY_CHEST_ABOVE_BOX_BOYS_ROOM: "BeanValleyRightPipeAboveGroundLocation",
    LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_LEFT_CHEST: "BeanValleyRightPipeLeftChestLocation",
    LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_RIGHT_CHEST: "BeanValleyRightPipeRightChestLocation",
    LocationNames.BEAN_VALLEY_RIGHT_PIRANHA_PIPE_HIDDEN_STAIRWAY_ITEM: "BeanValleyRightPipeUnderStairsLocation",
    LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_LOWER_FREESTANDING_COIN: "BeanValleyWestBeanstalkCoin1Location",
    LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_MIDDLE_FREESTANDING_COIN: "BeanValleyWestBeanstalkCoin2Location",
    LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_UPPER_FREESTANDING_COIN: "BeanValleyWestBeanstalkCoin3Location",
    LocationNames.BEAN_VALLEY_WEST_VINE_ROOM_FREESTANDING_FROG_COIN: "BeanValleyWestBeanstalkFloatingItemLocation",
    LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_LOWEST_FREESTANDING_COIN: "Beanstalk2ndRoomCoin1Location",
    LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_MIDDLE_FREESTANDING_COIN: "Beanstalk2ndRoomCoin2Location",
    LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_HIGHEST_FREESTANDING_COIN: "Beanstalk2ndRoomCoin3Location",
    LocationNames.BEAN_VALLEY_MIDDLE_VINE_ROOM_FREESTANDING_FROG_COIN: "Beanstalk2ndRoomFloatingItemLocation",
    LocationNames.BEAN_VALLEY_CLOUDS_LOWER_LEFT_CHEST: "BeanstalkLowerCloudLeftChestLocation",
    LocationNames.BEAN_VALLEY_CLOUDS_LOWER_RIGHT_CHEST: "BeanstalkLowerCloudRightChestLocation",
    LocationNames.BEAN_VALLEY_CLOUDS_SOLO_VINE_CHEST: "BeanstalkLowestChestLocation",
    LocationNames.BEAN_VALLEY_CLOUDS_UPPER_LEFT_CHEST: "BeanstalkUpperCloudLeftChestLocation",
    LocationNames.BEAN_VALLEY_CLOUDS_UPPER_RIGHT_CHEST: "BeanstalkUpperCloudRightChestLocation",
    LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_LOWER_LEFT_CHEST: "BelomeBeforeBossLowerLeftChestLocation",
    LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_MIDDLE_CHEST: "BelomeBeforeBossMiddleChestLocation",
    LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_RIGHT_CHEST: "BelomeBeforeBossRightChestLocation",
    LocationNames.BELOME_TEMPLE_AFTER_FORTUNE_AREA_UPPER_LEFT_CHEST: "BelomeBeforeBossUpperLeftChestLocation",
    LocationNames.BELOME_TEMPLE_FIRST_FORTUNE_TELLING_ROOM_CHEST: "BelomeTempleFortuneTellerLocation",
    LocationNames.BELOME_TEMPLE_LEFT_MIDDLE_RIGHT_FORTUNE_CHEST: "BelomeTempleLMRChestLocation",
    LocationNames.BELOME_TEMPLE_LEFT_RIGHT_MIDDLE_FORTUNE_CHEST: "BelomeTempleLRMChestLocation",
    LocationNames.BELOME_TEMPLE_RIGHT_LEFT_MIDDLE_FORTUNE_CHEST: "BelomeTempleRLMChestLocation",
    LocationNames.BELOME_TEMPLE_RIGHT_MIDDLE_LEFT_FORTUNE_CHEST: "BelomeTempleRMLChestLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_3: "BelomeTempleTreasuryAlmostLeftmostItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_2: "BelomeTempleTreasuryAlmostTopItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_LEFT_ITEM_BAG: "BelomeTempleTreasuryBottomLeftCornerItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_5: "BelomeTempleTreasuryInnerUpperRightItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_7: "BelomeTempleTreasuryLowerOuterBottomRightItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_MIDDLE_ITEM_BAG: "BelomeTempleTreasuryLowestItemsLeftLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_6: "BelomeTempleTreasuryLowestItemsRightLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_1: "BelomeTempleTreasuryMidLeftItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_4: "BelomeTempleTreasuryOuterUpperRightItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FROG_COIN_8: "BelomeTempleTreasuryRightmostItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FLOWER_4: "BelomeTempleTreasuryTopmostItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FLOWER_1: "BelomeTempleTreasuryUpperCornerLeftItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FLOWER_2: "BelomeTempleTreasuryUpperCornerLowerLeftItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_FLOWER_3: "BelomeTempleTreasuryUpperCornerTopItemLocation",
    LocationNames.BELOME_TEMPLE_VAULT_RIGHT_ITEM_BAG: "BelomeTempleTreasuryUpperOuterBottomRightItemLocation",
    LocationNames.BOOSTER_HILL_FLOWER_1: "BoosterHillGuaranteedItem1",
    LocationNames.BOOSTER_HILL_FLOWER_10: "BoosterHillGuaranteedItem10",
    LocationNames.BOOSTER_HILL_FLOWER_11: "BoosterHillGuaranteedItem11",
    LocationNames.BOOSTER_HILL_FLOWER_12: "BoosterHillGuaranteedItem12",
    LocationNames.BOOSTER_HILL_FLOWER_13: "BoosterHillGuaranteedItem13",
    LocationNames.BOOSTER_HILL_FLOWER_14: "BoosterHillGuaranteedItem14",
    LocationNames.BOOSTER_HILL_FLOWER_15: "BoosterHillGuaranteedItem15",
    LocationNames.BOOSTER_HILL_FLOWER_16: "BoosterHillGuaranteedItem16",
    LocationNames.BOOSTER_HILL_FLOWER_2: "BoosterHillGuaranteedItem2",
    LocationNames.BOOSTER_HILL_FLOWER_3: "BoosterHillGuaranteedItem3",
    LocationNames.BOOSTER_HILL_FLOWER_4: "BoosterHillGuaranteedItem4",
    LocationNames.BOOSTER_HILL_FLOWER_5: "BoosterHillGuaranteedItem5",
    LocationNames.BOOSTER_HILL_FLOWER_6: "BoosterHillGuaranteedItem6",
    LocationNames.BOOSTER_HILL_FLOWER_7: "BoosterHillGuaranteedItem7",
    LocationNames.BOOSTER_HILL_FLOWER_8: "BoosterHillGuaranteedItem8",
    LocationNames.BOOSTER_HILL_FLOWER_9: "BoosterHillGuaranteedItem9",
    LocationNames.BOOSTER_PASS_MAIN_AREA_BUSH_CHECK: "BoosterPassBushLocation",
    LocationNames.BOOSTER_PASS_MAIN_AREA_LEFT_CHEST: "BoosterPassFirstRoomLeftChestLocation",
    LocationNames.BOOSTER_PASS_MAIN_AREA_RIGHT_CHEST: "BoosterPassFirstRoomRightChestLocation",
    LocationNames.BOOSTER_PASS_FREESTANDING_FLOWER: "BoosterPassSecondRoomFlowerLocation",
    LocationNames.BOOSTER_PASS_SECRET_LEFT_CHEST: "BoosterPassSecretLeftChestLocation",
    LocationNames.BOOSTER_PASS_SECRET_MIDDLE_CHEST: "BoosterPassSecretMiddleChestLocation",
    LocationNames.BOOSTER_PASS_SECRET_RIGHT_CHEST: "BoosterPassSecretRightChestLocation",
    LocationNames.BOOSTER_TOWER_BALCONY_BOSS_FIGHT: "BoosterTowerBalconyBossFight",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_4: "BoosterTowerCheckerboardBottomItemLocation",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_1: "BoosterTowerCheckerboardCoin1Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_2: "BoosterTowerCheckerboardCoin2Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_3: "BoosterTowerCheckerboardCoin3Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_4: "BoosterTowerCheckerboardCoin4Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_5: "BoosterTowerCheckerboardCoin5Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_6: "BoosterTowerCheckerboardCoin6Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_7: "BoosterTowerCheckerboardCoin7Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_8: "BoosterTowerCheckerboardCoin8Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_COIN_9: "BoosterTowerCheckerboardCoin9Location",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_2: "BoosterTowerCheckerboardLeftmostItemLocation",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_ITEM: "BoosterTowerCheckerboardRightmostItemLocation",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_1: "BoosterTowerCheckerboardTopItemLocation",
    LocationNames.BOOSTER_TOWER_CHECKERBOARD_ROOM_FREESTANDING_FROG_COIN_3: "BoosterTowerCheckerboardUpperRightItemLocation",
    LocationNames.BOOSTER_TOWER_UPPER_THWOMP_ROOM_CHEST: "BoosterTowerChestNearThwompLocation",
    LocationNames.BOOSTER_TOWER_CURTAIN_PRIZE: "BoosterTowerCurtainGamePrizeLocation",
    LocationNames.BOOSTER_TOWER_ELDER_KEY_ROOM: "BoosterTowerElderKeyItemLocation",
    LocationNames.BOOSTER_TOWER_MASHER_CHEST: "BoosterTowerFallingChestLocation",
    LocationNames.BOOSTER_TOWER_CURTAIN_ROOM_BOSS_FIGHT: "BoosterTowerIndoorBossFight",
    LocationNames.BOOSTER_TOWER_POSTGAME_BOSS_FIGHT: "BoosterTowerIndoorBossFightRemake",
    LocationNames.BOOSTER_TOWER_KNIFE_GUY_MAXED_OUT_REWARD: "BoosterTowerKnifeGuy2PrizeLocation",
    LocationNames.BOOSTER_TOWER_KNIFE_GUY_REWARD: "BoosterTowerKnifeGuyPrizeLocation",
    LocationNames.BOOSTER_TOWER_MARIO_DOLL: "BoosterTowerMarioDollLocation",
    LocationNames.BOOSTER_TOWER_PARACHUTE_ROOM_CHEST: "BoosterTowerParachuteRoomChestLocation",
    LocationNames.BOOSTER_TOWER_PARACHUTE_ROOM_STAIR_CREVICE: "BoosterTowerParachuteRoomCreviceLocation",
    LocationNames.BOOSTER_TOWER_PORTRAIT_PRIZE: "BoosterTowerPortraitPrizeLocation",
    LocationNames.BOOSTER_TOWER_POSTGAME_PRIZE: "BoosterTowerRemakeBossFightPrizeLocation",
    LocationNames.BOOSTER_TOWER_ROOM_KEY_CHEST: "BoosterTowerRoomKeyChestLocation",
    LocationNames.BOOSTER_TOWER_FIRST_STAIRWAY_CHEST: "BoosterTowerSpookumStairsLocation",
    LocationNames.BOOSTER_TOWER_TOP_FLOOR_CORNER_CHEST: "BoosterTowerTopFloorCornerChestLocation",
    LocationNames.BOOSTER_TOWER_TOP_FLOOR_LOWER_CHEST: "BoosterTowerTopFloorLowerChestLocation",
    LocationNames.BOOSTER_TOWER_TOP_FLOOR_UPPER_CHEST: "BoosterTowerTopFloorUpperChestLocation",
    LocationNames.BOOSTER_TOWER_RAILWAY_ROOM: "BoosterTowerTrainRoomCreviceLocation",
    LocationNames.MOLEVILLE_BUCKET_GIRL: "BucketGirlRewardLocation",
    LocationNames.GRATE_GUYS_CASINO_LOTW_PRIZE: "CasinoGrateGuyPrizeLocation",
    LocationNames.CARBO_COOKIE_TRADER: "CookieTraderLocation",
    LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_FIGHT: "DojoFifthFight",
    LocationNames.MONSTRO_TOWN_DOJO_FIRST_FIGHT: "DojoFirstFight",
    LocationNames.MONSTRO_TOWN_DOJO_FOURTH_FIGHT: "DojoFourthFight",
    LocationNames.MONSTRO_TOWN_DOJO_SECOND_FIGHT: "DojoSecondFight",
    LocationNames.MONSTRO_TOWN_DOJO_THIRD_FIGHT: "DojoThirdFight",
    LocationNames.SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_LEFT_CHEST: "EarlyInnerShipLeftChestLocation",
    LocationNames.SUNKEN_SHIP_OUTSIDE_CLONE_ROOM_RIGHT_CHEST: "EarlyInnerShipRightChestLocation",
    LocationNames.OUTER_FACTORY_FALLING_AXEM_ROOM_CHEST: "FactoryAxemConveyorsChestLocation",
    LocationNames.OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_LEFT_CHEST: "FactoryBehindNinjasLeftChestLocation",
    LocationNames.OUTER_FACTORY_ROOM_BEHIND_MACHINE_YARID_RIGHT_CHEST: "FactoryBehindNinjasRightChestLocation",
    LocationNames.OUTER_FACTORY_CONVEYOR_ROOM_RIGHT_CHEST: "FactoryBigConveyorRoomFirstChestLocation",
    LocationNames.OUTER_FACTORY_CONVEYOR_ROOM_LEFT_CHEST: "FactoryBigConveyorRoomSecondChestLocation",
    LocationNames.OUTER_FACTORY_BOLT_PLATFORM_CHEST: "FactoryBoltPlatformsChestLocation",
    LocationNames.OUTER_FACTORY_FIRST_BOSS_FIGHT: "FactoryEntranceBossFight",
    LocationNames.OUTER_FACTORY_SECOND_BOSS_FIGHT: "FactoryTransitionBossFight",
    LocationNames.OUTER_FACTORY_PIT_BACK_CHEST: "FactoryTreasurePitBackChestLocation",
    LocationNames.OUTER_FACTORY_PIT_FRONT_CHEST: "FactoryTreasurePitFrontChestLocation",
    LocationNames.FACTORY_FINAL_BOSS_FIGHT: "FinalBossFight",
    LocationNames.FACTORY_FINAL_BOSS_STAR_PIECE: "FinalBossFightStarPiece",
    LocationNames.MOLEVILLE_FIREWORKS_SHOP_FIRST_ITEM: "FireworksShopItemLocation",
    LocationNames.FOREST_MAZE_BOSS_FIGHT: "ForestMazeBossFight",
    LocationNames.FOREST_MAZE_CHARACTER_RECRUIT: "ForestMazeCharacter",
    LocationNames.FOREST_MAZE_1ST_ROOM_CHEST: "ForestMazeFirstRoomLocation",
    LocationNames.FOREST_MAZE_FIRST_CHEST_AFTER_UNDERGROUND: "ForestMazeFirstUndergroundExitLocation",
    LocationNames.FOREST_MAZE_BEFORE_MAZE_CHEST: "ForestMazeInnerMazeEntranceLocation",
    LocationNames.FOREST_MAZE_SECRET_BOTTOM_MIDDLE_CHEST: "ForestMazeSecretBottomMiddleChestLocation",
    LocationNames.FOREST_MAZE_SECRET_BOTTOM_RIGHT_CHEST: "ForestMazeSecretBottomRightChestLocation",
    LocationNames.FOREST_MAZE_SECRET_LEFT_CHEST: "ForestMazeSecretLeftChestLocation",
    LocationNames.FOREST_MAZE_SECRET_TOP_MIDDLE_CHEST: "ForestMazeSecretTopMiddleChestLocation",
    LocationNames.FOREST_MAZE_SECRET_TOP_RIGHT_CHEST: "ForestMazeSecretTopRightChestLocation",
    LocationNames.FOREST_MAZE_BOSS_STAR_PIECE: "ForestMazeStarPiece",
    LocationNames.FOREST_MAZE_BOTTOM_RIGHT_STUMP_CHEST: "ForestMazeUndergroundBottomRightTrunkChestLocation",
    LocationNames.FOREST_MAZE_MIDDLE_LEFT_STUMP_CHEST: "ForestMazeUndergroundMiddleLeftChestLocation",
    LocationNames.FOREST_MAZE_WIGGLER_CHEST: "ForestMazeUndergroundWigglerChestLocation",
    LocationNames.DISCIPLE_SHOP_FIRST_ITEM: "FrogDiscipleLocation1",
    LocationNames.DISCIPLE_SHOP_SECOND_ITEM: "FrogDiscipleLocation2",
    LocationNames.DISCIPLE_SHOP_THIRD_ITEM: "FrogDiscipleLocation3",
    LocationNames.DISCIPLE_SHOP_FOURTH_ITEM: "FrogDiscipleLocation4",
    LocationNames.DISCIPLE_SHOP_FIFTH_ITEM: "FrogDiscipleLocation5",
    LocationNames.NIMBUS_LAND_GARRO_CHECK: "GarroFreeItem",
    LocationNames.NIMBUS_CASTLE_GIANT_EGG_BOSS_FIGHT: "GiantEggBossFight",
    LocationNames.INNER_FACTORY_FIRST_BOSS_FIGHT: "InnerFactoryFirstFight",
    LocationNames.INNER_FACTORY_FOURTH_BOSS_FIGHT: "InnerFactoryFourthFight",
    LocationNames.INNER_FACTORY_SECOND_BOSS_FIGHT: "InnerFactorySecondFight",
    LocationNames.INNER_FACTORY_THIRD_BOSS_FIGHT: "InnerFactoryThirdFight",
    LocationNames.INNER_FACTORY_TOAD_GIFT: "InnerFactoryToadGiftLocation",
    LocationNames.MOLEVILLE_MINES_SECOND_BOSS_FIGHT: "InnerMinesBossFight",
    LocationNames.MOLEVILLE_MINES_NEAR_FINAL_TRAIN_TRACKS_CHEST: "InnerMinesBoxesChestLocation",
    LocationNames.MOLEVILLE_MINES_CHARACTER_RECRUIT: "InnerMinesCharacter",
    LocationNames.MOLEVILLE_MINES_BEFORE_BOSS_UPPER_CHEST: "InnerMinesHighUpChestLocation",
    LocationNames.MOLEVILLE_MINES_POSTGAME_BOSS_FIGHT: "InnerMinesPostgameBossFight",
    LocationNames.MOLEVILLE_MINES_POSTGAME_PRIZE: "InnerMinesPostgameDrop",
    LocationNames.MOLEVILLE_MINES_BEFORE_BOSS_LEFT_CHEST: "InnerMinesSaveBlockChestLocation",
    LocationNames.MOLEVILLE_MINES_SHY_GUY_CART: "InnerMinesShyguyCartLocation",
    LocationNames.MOLEVILLE_MINES_SECOND_BOSS_STAR_PIECE: "InnerMinesStarPiece",
    LocationNames.MOLEVILLE_MINES_TWO_LEVEL_TRAINTRACK_ROOM_CHEST: "InnerMinesTracksChestLocation",
    LocationNames.SUNKEN_SHIP_NEAR_FINAL_BOSS_CHEST: "InnerShipBeforeBossChestLocation",
    LocationNames.SUNKEN_SHIP_HIDDEN_BOX_ROOM_CHEST: "InnerShipBehindBoxesChestLocation",
    LocationNames.SUNKEN_SHIP_CLONE_ROOM_CHEST: "InnerShipCloneRoomChestLocation",
    LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_1: "InnerShipFirstUnderwaterRoomBottomItemLocation",
    LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_3: "InnerShipFirstUnderwaterRoomLeftItemLocation",
    LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_4: "InnerShipFirstUnderwaterRoomMiddleItemLocation",
    LocationNames.SUNKEN_SHIP_UNDERWATER_FREESTANDING_FROG_COIN_2: "InnerShipFirstUnderwaterRoomTopItemLocation",
    LocationNames.SUNKEN_SHIP_LARGE_POOL_FREESTANDING_FROG_COIN: "InnerShipPoolRoomLocation",
    LocationNames.SUNKEN_SHIP_HIDONS_ROOM_LEFT_CHEST: "InnerShipSaveRoomLeftChestLocation",
    LocationNames.SUNKEN_SHIP_HIDONS_ROOM_RIGHT_CHEST: "InnerShipSaveRoomRightChestLocation",
    LocationNames.SUNKEN_SHIP_HIDDEN_UNDERWATER_ROOM_CHEST: "InnerShipSecretRoomChestLocation",
    LocationNames.BOWSERS_KEEP_MAGIKOOPAS_ROOM_CHEST: "KeepAfterObstaclesBossChestLocation",
    LocationNames.BOWSERS_KEEP_FIRST_BOSS_FIGHT: "KeepAfterObstaclesBossFight",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_1: "KeepCannonballCoin1Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_2: "KeepCannonballCoin2Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_3: "KeepCannonballCoin3Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_4: "KeepCannonballCoin4Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_5: "KeepCannonballCoin5Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_6: "KeepCannonballCoin6Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_7: "KeepCannonballCoin7Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_FREESTANDING_COIN_8: "KeepCannonballCoin8Location",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_LEFT_CHEST: "KeepCannonballFrontLeftChestLocation",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_LEFT_CHEST: "KeepCannonballMidLeftChestLocation",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_UPPER_RIGHT_CHEST: "KeepCannonballMidRightChestLocation",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_EXIT_CHEST: "KeepCannonballRoomBackChestLocation",
    LocationNames.BOWSERS_KEEP_CANNONBALL_ROOM_LOWER_RIGHT_CHEST: "KeepCannonballRoomFrontRightChestLocation",
    LocationNames.BOWSERS_KEEP_SECOND_BOSS_FIGHT: "KeepChandelierBossFight",
    LocationNames.BOWSERS_KEEP_DARK_ROOM_CHEST: "KeepDarkRoomChestLocation",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_1: "KeepDoorRewardChest1Location",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_2: "KeepDoorRewardChest2Location",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_3: "KeepDoorRewardChest3Location",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_4: "KeepDoorRewardChest4Location",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_5: "KeepDoorRewardChest5Location",
    LocationNames.BOWSERS_KEEP_DOOR_PRIZE_6: "KeepDoorRewardChest6Location",
    LocationNames.BOWSERS_KEEP_6_DOOR_ELEVATOR_PLATFORM_ROOM_CHEST: "KeepElevatorRoomChestLocation",
    LocationNames.BOWSERS_KEEP_THIRD_BOSS_FIGHT: "KeepFinalBossFight",
    LocationNames.BOWSERS_KEEP_NEAR_FIRST_SHOP_LEFT_CHEST: "KeepFirstCrocoShopLeftChestLocation",
    LocationNames.BOWSERS_KEEP_NEAR_FIRST_SHOP_RIGHT_CHEST: "KeepFirstCrocoShopRightChestLocation",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_CHEST: "KeepInvisibleBridgeBackChestLocation",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_LEFT_COIN: "KeepInvisibleBridgeCoin1Location",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_RIGHT_COIN: "KeepInvisibleBridgeCoin2Location",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_LEFT_COIN: "KeepInvisibleBridgeCoin3Location",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_TOP_RIGHT_COIN: "KeepInvisibleBridgeCoin4Location",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_BOTTOM_CHEST: "KeepInvisibleBridgeFrontChestLocation",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_LEFT_CHEST: "KeepInvisibleBridgeLeftChestLocation",
    LocationNames.BOWSERS_KEEP_6_DOOR_INVISBLE_BRIDGE_RIGHT_CHEST: "KeepInvisibleBridgeRightChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_EXIT_CHEST: "KeepRotatingPlatformsBackChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_UPPER_LEFT_CHEST: "KeepRotatingPlatformsBackMidLeftChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_RIGHT_CHEST: "KeepRotatingPlatformsBackMidRightChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_ROOM_ENTRANCE_CHEST: "KeepRotatingPlatformsFrontChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_LOWER_LEFT_CHEST: "KeepRotatingPlatformsFrontMidLeftChestLocation",
    LocationNames.BOWSERS_KEEP_ROTATING_PLATFORM_CENTER_CHEST: "KeepRotatingPlatformsFrontMidRightChestLocation",
    LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_EXIT_CHEST: "KeepXYPlatformsBackLeftChestLocation",
    LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_EXIT_CHEST: "KeepXYPlatformsBackRightChestLocation",
    LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_LEFT_ENTRANCE_CHEST: "KeepXYPlatformsFrontLeftChestLocation",
    LocationNames.BOWSERS_KEEP_X_Y_PLATFORM_ROOM_RIGHT_ENTRANCE_CHEST: "KeepXYPlatformsFrontRightChestLocation",
    LocationNames.KERO_SEWERS_BEFORE_BOSS_LOWER_CHEST: "KeroSewersBeforeBelomeLowerLocation",
    LocationNames.KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_AFTER_LANDS_END: "KeroSewersBeforeBelomeUpperAfterFlipLocation",
    LocationNames.KERO_SEWERS_BEFORE_BOSS_UPPER_CHEST_BEFORE_LANDS_END: "KeroSewersBeforeBelomeUpperBeforeFlipLocation",
    LocationNames.KERO_SEWERS_BOSS_FIGHT: "KeroSewersBossFight",
    LocationNames.KERO_SEWERS_FOUR_RAT_ROOM_CHEST: "KeroSewersFourRatRoomChestLocation",
    LocationNames.KERO_SEWERS_STAIRWAY_ROOM_LEFT_CHEST: "KeroSewersStairRoomLeftChestLocation",
    LocationNames.KERO_SEWERS_STAIRWAY_ROOM_RIGHT_CHEST: "KeroSewersStairRoomRightChestLocation",
    LocationNames.LANDS_END_BEE_ROOM_CHEST: "LandsEndBeeTowerChestLocation",
    LocationNames.LANDS_END_SKY_BRIDGE_FREESTANDING_ITEM: "LandsEndCaveSideRemake",
    LocationNames.LANDS_END_CHOW_PIT_RIGHT_CHEST: "LandsEndChowPitMovingChestLocation",
    LocationNames.LANDS_END_CHOW_PIT_LEFT_CHEST: "LandsEndChowPitStaticChestLocation",
    LocationNames.LANDS_END_BELOME_TEMPLE_CLOUD_BOSS_FIGHT: "LandsEndCloudBoss",
    LocationNames.LANDS_END_1ST_PURCHASE_CHEST: "LandsEndFirstPurchasableChestLocation",
    LocationNames.LANDS_END_GROTTO_CORNER_CHEST: "LandsEndGrottoCornerChestLocation",
    LocationNames.LANDS_END_GROTTO_NEAR_SEWER_CHEST: "LandsEndGrottoEndChestLocation",
    LocationNames.LANDS_END_GROTTO_FIRST_CHEST: "LandsEndGrottoEntranceChestLocation",
    LocationNames.LANDS_END_FIRST_CHEST: "LandsEndRisingPlatformChestLocation",
    LocationNames.LANDS_END_2ND_PURCHASE_CHEST: "LandsEndSecondPurchasableChestLocation",
    LocationNames.LANDS_END_WHIRLPOOL_1ST_UNDERGROUND_CHEST: "LandsEndUndergroundSaveBoxChestLocation",
    LocationNames.MARRYMORE_ALTAR_CHAPEL_ITEM: "MarrymoreAltarHeadLocation",
    LocationNames.MARRYMORE_INN_ELDERLY_GUESTS_MAJOR_TIP: "MarrymoreBigTipLocation",
    LocationNames.MARRYMORE_BOSS_FIGHT: "MarrymoreBossFight",
    LocationNames.MARRYMORE_POSTGAME_BOSS_FIGHT: "MarrymoreBossFightRemake",
    LocationNames.MARRYMORE_POSTGAME_PRIZE: "MarrymoreBossFightRemakeItemDrop",
    LocationNames.MARRYMORE_CHARACTER_RECRUIT: "MarrymoreCharacter",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_5: "MarrymoreFifthSuitePrizeLocation",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_1: "MarrymoreFirstSuitePrizeLocation",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_4: "MarrymoreFourthSuitePrizeLocation",
    LocationNames.MARRYMORE_INN_REGULAR_ROOM_CHEST: "MarrymoreHotelChestLocation",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_2: "MarrymoreSecondSuitePrizeLocation",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_6: "MarrymoreSixthSuitePrizeLocation",
    LocationNames.MARRYMORE_SNIFIT_1_CHAPEL_ITEM: "MarrymoreSnifit1Location",
    LocationNames.MARRYMORE_SNIFIT_2_CHAPEL_ITEM: "MarrymoreSnifit2Location",
    LocationNames.MARRYMORE_SNIFIT_3_CHAPEL_ITEM: "MarrymoreSnifit3Location",
    LocationNames.MARRYMORE_SUITE_TOTAL_STAYS_PRIZE_3: "MarrymoreThirdSuitePrizeLocation",
    LocationNames.MELODY_BAY_SONG_1_REWARD: "MelodyBayFirstRewardLocation",
    LocationNames.MELODY_BAY_SONG_2_REWARD: "MelodyBaySecondRewardLocation",
    LocationNames.MELODY_BAY_SONG_3_REWARD: "MelodyBayThirdRewardLocation",
    LocationNames.MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_FREESTANDING_FROG_COIN: "MidasRiverBottomLeftCaveLocation",
    LocationNames.MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_FREESTANDING_FLOWER: "MidasRiverBottomRightCaveLocation",
    LocationNames.MIDAS_RIVER_FIRST_PLAY_REWARD: "MidasRiverFirstCompletionRewardLocation",
    LocationNames.MIDAS_RIVER_UPPER_LEFT_TUNNEL_FREESTANDING_FROG_COIN: "MidasRiverLeftCaveLocation",
    LocationNames.MIMIC_CHEST_1_BOSS_FIGHT: "Mimic1BossFight",
    LocationNames.MIMIC_CHEST_1_FIRST_REWARD: "Mimic1DropRewardLocation",
    LocationNames.MIMIC_CHEST_1_RELOAD_REWARD: "Mimic1ReloadRewardLocation",
    LocationNames.MIMIC_CHEST_2_BOSS_FIGHT: "Mimic2BossFight",
    LocationNames.MIMIC_CHEST_2_FIRST_REWARD: "Mimic2DropRewardLocation",
    LocationNames.MIMIC_CHEST_2_RELOAD_REWARD: "Mimic2ReloadRewardLocation",
    LocationNames.MIMIC_CHEST_3_BOSS_FIGHT: "Mimic3BossFight",
    LocationNames.MONSTRO_TOWN_DOJO_PRIZE: "MonstroDojoClearRewardLocation",
    LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_PRIZE: "MonstroDojoPostgameClearRewardLocation",
    LocationNames.MONSTRO_TOWN_ENTRANCE_CHEST: "MonstroEntranceLocation",
    LocationNames.MONSTRO_TOWN_SUPER_JUMP_FIRST_PRIZE: "MonstroFirstSuperJumpRewardLocation",
    LocationNames.MONSTRO_TOWN_FLAG_EXCHANGE_PRIZE: "MonstroFlagExchangeLocation",
    LocationNames.MONSTRO_TOWN_SEALED_DOOR_BOSS_FIGHT: "MonstroSealedDoorBossFight",
    LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_BOSS_FIGHT: "MonstroSealedDoorBossFightPostgame",
    LocationNames.MONSTRO_TOWN_SEALED_DOOR_PRIZE: "MonstroSealedDoorClearRewardLocation",
    LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_PRIZE: "MonstroSealedDoorClearRewardLocationPostgame",
    LocationNames.MONSTRO_TOWN_SUPER_JUMP_SECOND_PRIZE: "MonstroSecondSuperJumpRewardLocation",
    LocationNames.MONSTRO_TOWN_THWOMP_KEY: "MonstroThwompItemLocation",
    LocationNames.MUSHROOM_KINGDOM_BOSS_FIGHT: "MushroomKingdomBossFight",
    LocationNames.MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_CHAIR_ITEM: "MushroomKingdomChair",
    LocationNames.MUSHROOM_KINGDOM_SHOP_FREE_ITEM: "MushroomKingdomFreeShopItem",
    LocationNames.MUSHROOM_KINGDOM_GAMEBOY_KID: "MushroomKingdomInnPurchaseLocation",
    LocationNames.MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_LIBERATED: "MushroomKingdomLiberatedVaultLeft",
    LocationNames.MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_LIBERATED: "MushroomKingdomLiberatedVaultMiddle",
    LocationNames.MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_LIBERATED: "MushroomKingdomLiberatedVaultRight",
    LocationNames.MUSHROOM_KINGDOM_CASTLE_MAIN_HALLWAY_CHEST: "MushroomKingdomMainHall",
    LocationNames.MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_TOAD_RESCUE_ITEM: "MushroomKingdomOccupiedCastleToadRescueLocation",
    LocationNames.MUSHROOM_KINGDOM_INVASION_FAMILY_RESCUE: "MushroomKingdomOccupiedFamilyRescueLocation",
    LocationNames.MUSHROOM_KINGDOM_INVASION_GUEST_ROOM: "MushroomKingdomOccupiedGuestRoomLocation",
    LocationNames.MUSHROOM_KINGDOM_EASTERN_GUARD_RESCUE: "MushroomKingdomOccupiedOutdoorGuardLocation",
    LocationNames.MUSHROOM_KINGDOM_VAULT_LEFT_CHEST_OCCUPIED: "MushroomKingdomOccupiedVaultLeft",
    LocationNames.MUSHROOM_KINGDOM_VAULT_MIDDLE_CHEST_OCCUPIED: "MushroomKingdomOccupiedVaultMiddle",
    LocationNames.MUSHROOM_KINGDOM_VAULT_RIGHT_CHEST_OCCUPIED: "MushroomKingdomOccupiedVaultRight",
    LocationNames.MUSHROOM_KINGDOM_SHOP_BASEMENT_LEFT_CHEST: "MushroomKingdomShopBasementLeft",
    LocationNames.MUSHROOM_KINGDOM_SHOP_BASEMENT_RIGHT_CHEST: "MushroomKingdomShopBasementRight",
    LocationNames.MUSHROOM_KINGDOM_INVASION_BOSS_STAR_PIECE: "MushroomKingdomStarPiece",
    LocationNames.MUSHROOM_KINGDOM_SHOP_RARE_FROG_COIN_EXCHANGE: "MushroomKingdomStoreExchangeLocation",
    LocationNames.WALLET_REWARD_1: "MushroomKingdomWalletGuyFirstRewardLocation",
    LocationNames.WALLET_REWARD_2: "MushroomKingdomWalletGuySecondRewardLocation",
    LocationNames.MUSHROOM_WAY_FIRST_CHEST: "MushroomWay1LowerChest",
    LocationNames.MUSHROOM_WAY_FIRST_TOAD_REWARD: "MushroomWay1ToadRescue",
    LocationNames.MUSHROOM_WAY_SECOND_CHEST: "MushroomWay1UpperChest",
    LocationNames.MUSHROOM_WAY_FLOWER_JUMP_LEFT_CHEST: "MushroomWay2LedgeChest",
    LocationNames.MUSHROOM_WAY_SECOND_TOAD_REWARD: "MushroomWay2ToadRescue",
    LocationNames.MUSHROOM_WAY_BOSS_REWARD: "MushroomWayBossFightRewardItem",
    LocationNames.MUSHROOM_WAY_CHARACTER_RECRUIT: "MushroomWayCharacter",
    LocationNames.MUSHROOM_WAY_LEFT_FREESTANDING_ITEM: "MushroomWayLeftItemRemake",
    LocationNames.MUSHROOM_WAY_SECOND_ROOM_RIGHT_CHEST: "MushroomWayRightGoomba",
    LocationNames.MUSHROOM_WAY_RIGHT_FREESTANDING_ITEM: "MushroomWayRightItemRemake",
    LocationNames.MUSHROOM_WAY_BOSS_FIGHT: "MushrooomWayBossFight",
    LocationNames.NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_RIGHT_CHEST: "NimbusCastleAboveJawfulChestLocation",
    LocationNames.NIMBUS_CASTLE_POST_THRONE_CHEST_UNOCCUPIED: "NimbusCastleBackHallwayLiberatedChestLocation",
    LocationNames.NIMBUS_CASTLE_POST_THRONE_CHEST_OCCUPIED: "NimbusCastleBackHallwayOccupiedChestLocation",
    LocationNames.NIMBUS_CASTLE_5_DOOR_ROOM_CHEST_LIBERATED: "NimbusCastleBusinessCentreLiberatedChestLocation",
    LocationNames.NIMBUS_CASTLE_5_DOOR_ROOM_CHEST_OCCUPIED: "NimbusCastleBusinessCentreOccupiedChestLocation",
    LocationNames.NIMBUS_CASTLE_WEST_TWO_LEVEL_ROOM_CHEST: "NimbusCastleCornerBridgeChestLocation",
    LocationNames.NIMBUS_CASTLE_GIANT_EGG_PRIZE: "NimbusCastleGiantEggRewardLocation",
    LocationNames.NIMBUS_CASTLE_WEST_STAIRWAY_ROOM_LEFT_CHEST: "NimbusCastleOutOfBoundsChestLocation",
    LocationNames.NIMBUS_CASTLE_WEST_CELLAR_GUARD: "NimbusCastleOuterPrisonCellarLeftNPCLocation",
    LocationNames.NIMBUS_CASTLE_WEST_CELLAR_CIVILIAN: "NimbusCastleOuterPrisonCellarRightNPCLocation",
    LocationNames.NIMBUS_CASTLE_SINGLE_GOLD_BIRD_ROOM_CHEST: "NimbusCastleSingleGoldBirdChestLocation",
    LocationNames.NIMBUS_CASTLE_STATUE_GAME_PRIZE: "NimbusCastleStatueGamePrizeLocation",
    LocationNames.NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_LOWER_CHEST: "NimbusCastleTwoLevelLowerChestLocation",
    LocationNames.NIMBUS_CASTLE_EAST_TWO_LEVEL_ROOM_UPPER_CHEST: "NimbusCastleTwoLevelUpperChestLocation",
    LocationNames.NIMBUS_LAND_FINAL_BOSS_FIGHT: "NimbusFinalBossFight",
    LocationNames.NIMBUS_LAND_DREAM_CUSHION_1ST_ITEM: "NimbusInnDreamPrize1Location",
    LocationNames.NIMBUS_LAND_DREAM_CUSHION_2ND_ITEM: "NimbusInnDreamPrize2Location",
    LocationNames.NIMBUS_LAND_POST_INVASION_UPPER_RIGHT_HOUSE: "NimbusLandCrocoItemLocation",
    LocationNames.NIMBUS_CASTLE_POST_INVASION_NORTH_CELLAR: "NimbusLandInnerCellarLocation",
    LocationNames.NIMBUS_LAND_POST_INVASION_OFF_CLOUD_ITEM: "NimbusLandRightSideLocation",
    LocationNames.NIMBUS_LAND_SHOP_CHEST: "NimbusShopChestLocation",
    LocationNames.BOWSERS_KEEP_BATTLE_DOOR_BOSS_FIGHT: "ObstacleCourseFinalFight",
    LocationNames.OUTER_FACTORY_EARLY_SAVE_ROOM_CHEST: "OuterFactorySaveRoomChestLocation",
    LocationNames.MOLEVILLE_MINES_FIRST_BOSS_FIGHT: "OuterMinesBossFight",
    LocationNames.MOLEVILLE_MINES_FIRST_BOSS_ITEM: "OuterMinesBossPrizeLocation",
    LocationNames.MOLEVILLE_MINES_LEFT_BANDIT: "OuterMinesLeftHenchmanLocation",
    LocationNames.MOLEVILLE_MINES_RIGHT_BANDIT: "OuterMinesRightHenchmanLocation",
    LocationNames.MOLEVILLE_MINES_TRAMPOLINE_BANDIT: "OuterMinesTrampolineHenchmanLocation",
    LocationNames.PIPE_VAULT_NIPPER_ROOM_SECOND_CHEST: "PipeVaultChompweedChestLocation",
    LocationNames.PIPE_VAULT_GOOMBA_THUMPIN_FIRST_PRIZE: "PipeVaultGoombaThumpinFirstPrizeLocation",
    LocationNames.PIPE_VAULT_GOOMBA_THUMPIN_SECOND_PRIZE: "PipeVaultGoombaThumpinSecondPrizeLocation",
    LocationNames.PIPE_VAULT_NIPPER_ROOM_FIRST_CHEST: "PipeVaultRisingPlatformChestLocation",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_BACK_CHEST: "PipeVaultSlidingCoinRoomBackChestLocation",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_1: "PipeVaultSlidingCoinRoomCoin1Location",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_2: "PipeVaultSlidingCoinRoomCoin2Location",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_3: "PipeVaultSlidingCoinRoomCoin3Location",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_4: "PipeVaultSlidingCoinRoomCoin4Location",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_COIN_5: "PipeVaultSlidingCoinRoomCoin5Location",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FREESTANDING_FROG_COIN: "PipeVaultSlidingCoinRoomCrouchItemLocation",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_FRONT_CHEST: "PipeVaultSlidingCoinRoomFrontChestLocation",
    LocationNames.PIPE_VAULT_SLIDE_ROOM_MIDDLE_CHEST: "PipeVaultSlidingCoinRoomMiddleChestLocation",
    LocationNames.TOADS_POSTGAME_ITEM_GRANT: "PostgameVoucherLocation",
    LocationNames.PURTEND_STORE: "PurtendStoreLocation",
    LocationNames.ROSE_TOWN_GARDENER_LEFT_CHEST: "RoseTownCloudLeftChestLocation",
    LocationNames.ROSE_TOWN_GARDENER_RIGHT_CHEST: "RoseTownCloudRightChestLocation",
    LocationNames.ROSE_TOWN_GAZ_GIFT: "RoseTownInnGazPrizeLocation",
    LocationNames.ROSE_TOWN_INN_TOAD_GIFT: "RoseTownInnToadPrizeLocation",
    LocationNames.ROSE_TOWN_SHOP_LEFT_CHEST: "RoseTownShopLeftChestLocation",
    LocationNames.ROSE_TOWN_SHOP_RIGHT_CHEST: "RoseTownShopRightChestLocation",
    LocationNames.ROSE_TOWN_UPPER_HOUSE_LEFT_CHEST: "RoseTownTreasureHouseLeftChestLocation",
    LocationNames.ROSE_TOWN_UPPER_HOUSE_MAZE_SECRET_PRIZE: "RoseTownTreasureHouseMazeRewardLocation",
    LocationNames.ROSE_TOWN_UPPER_HOUSE_RIGHT_CHEST: "RoseTownTreasureHouseRightChestLocation",
    LocationNames.ROSE_TOWN_UPPER_HOUSE_TOP_FLOOR_CHEST: "RoseTownTreasureHouseUpperChestLocation",
    LocationNames.ROSE_WAY_FREESTANDING_COIN_1: "RoseWayCoin1Location",
    LocationNames.ROSE_WAY_FREESTANDING_COIN_2: "RoseWayCoin2Location",
    LocationNames.ROSE_WAY_FREESTANDING_COIN_3: "RoseWayCoin3Location",
    LocationNames.ROSE_WAY_FREESTANDING_COIN_4: "RoseWayCoin4Location",
    LocationNames.ROSE_WAY_FREESTANDING_COIN_5: "RoseWayCoin5Location",
    LocationNames.ROSE_WAY_FIVE_CHEST_AREA_BOTTOM_LEFT_CHEST: "RoseWayFiveChestRoomBottomLeftLocation",
    LocationNames.ROSE_WAY_FIVE_CHEST_BOTTOM_RIGHT_CHEST: "RoseWayFiveChestRoomBottomRightLocation",
    LocationNames.ROSE_WAY_FIVE_CHEST_TOP_LEFT_CHEST: "RoseWayFiveChestRoomLeftLocation",
    LocationNames.ROSE_WAY_FIVE_CHEST_TOP_RIGHT_CHEST: "RoseWayFiveChestRoomRightLocation",
    LocationNames.ROSE_WAY_FIVE_CHEST_AREA_TOP_MIDDLE_CHEST: "RoseWayFiveChestRoomTopLocation",
    LocationNames.ROSE_WAY_FREESTANDING_FLOWER: "RoseWayLeftIslandLocation",
    LocationNames.ROSE_WAY_FREESTANDING_MUSHROOM: "RoseWayMiddleIslandLocation",
    LocationNames.ROSE_WAY_SWINGING_SHY_GUY_CHEST: "RoseWaySwingingPlatformRoomLocation",
    LocationNames.SEA_SAVE_ROOM_BACK_CHEST: "SeaSaveRoomBackChestLocation",
    LocationNames.SEA_SAVE_ROOM_FRONT_CHEST: "SeaSaveRoomFrontChestLocation",
    LocationNames.SEA_SAVE_ROOM_MIDDLE_CHEST: "SeaSaveRoomMiddleChestLocation",
    LocationNames.SEA_STARSLAP_ROOM_CHEST: "SeaStarslapRoomChestLocation",
    LocationNames.SEA_WHIRLPOOL_ROOM_CHEST: "SeaWhirlpoolChestLocation",
    LocationNames.SEASIDE_TOWN_BOSS_FIGHT: "SeasideBeachBossFight",
    LocationNames.SEASIDE_TOWN_BOSS_STAR_PIECE: "SeasideBeachStarPiece",
    LocationNames.SEASIDE_TOWN_BOSS_PRIZE: "SeasideTownBossPrizeLocation",
    LocationNames.SEASIDE_TOWN_SHED_RESCUE: "SeasideTownShedRescueLocation",
    LocationNames.SUNKEN_SHIP_3D_MAZE_PRIZE: "Ship3DMazePuzzle",
    LocationNames.SUNKEN_SHIP_BARREL_SWITCH_PRIZE: "ShipBarrelPuzzle",
    LocationNames.SUNKEN_SHIP_CANNONBALL_PUZZLE_PRIZE: "ShipCannonballPuzzle",
    LocationNames.SUNKEN_SHIP_COIN_SNAKE_PUZZLE_PRIZE: "ShipCoinSnakePuzzleLocation",
    LocationNames.SUNKEN_SHIP_FINAL_BOSS_FIGHT: "ShipFinalBossFight",
    LocationNames.SUNKEN_SHIP_PASSWORD_BOSS_FIGHT: "ShipPasswordBossFight",
    LocationNames.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT: "ShipPostgameBossFight",
    LocationNames.SUNKEN_SHIP_POSTGAME_PRIZE: "ShipPostgameFightItemDrop",
    LocationNames.SUNKEN_SHIP_FIRST_STAIRWAY_FREESTANDING_FLOWER: "ShipRatStairsBoxesLocation",
    LocationNames.SUNKEN_SHIP_FIRST_STAIRWAY_CHEST: "ShipRatStairsChestLocation",
    LocationNames.SUNKEN_SHIP_SHOP_AREA_CHEST: "ShipShopChestLocation",
    LocationNames.SUNKEN_SHIP_TRAMPOLINE_PUZZLE_PRIZE: "ShipTrampolinePuzzle",
    LocationNames.SUNKEN_SHIP_TROOPA_CANNONBALL_PRIZE: "ShipTroopaPuzzleLocation",
    LocationNames.STAR_HILL_FREESTANDING_STAR_PIECE: "StarHillStarPiece",
    LocationNames.STARTER_CHARACTER_1: "StartingCharacter1",
    LocationNames.STARTER_ITEM_1: "StartingItem1Location",
    LocationNames.STARTER_ITEM_2: "StartingItem2Location",
    LocationNames.STARTER_ITEM_3: "StartingItem3Location",
    LocationNames.STARTER_ITEM_4: "StartingItem4Location",
    LocationNames.NIMBUS_CASTLE_STATUE_KEEPER_BOSS_FIGHT: "StatueRoomBossFight",
    LocationNames.TADPOLE_POND_CRICKET_JAM_EXCHANGE: "TadpolePondCricketJamExchangeLocation",
    LocationNames.TADPOLE_POND_CRICKET_PIE_EXCHANGE: "TadpolePondCricketPieExchangeLocation",
    LocationNames.BELOME_TEMPLE_BOSS_FIGHT: "TempleBossFight",
    LocationNames.BELOME_TEMPLE_POSTGAME_BOSS_FIGHT: "TempleBossFightPostgame",
    LocationNames.BELOME_TEMPLE_POSTGAME_PRIZE: "TemplePostgameFightItemDrop",
    LocationNames.MOLEVILLE_FIRST_TREASURE_SHOP_ITEM: "TreasureShopItem1",
    LocationNames.MOLEVILLE_SECOND_TREASURE_SHOP_ITEM: "TreasureShopItem2",
    LocationNames.MOLEVILLE_THIRD_TREASURE_SHOP_ITEM: "TreasureShopItem3",
    LocationNames.LANDS_END_TROOPA_CLIMB_SUB_12_SECOND_PRIZE: "TroopaClimbSub12PrizeLocation",
    LocationNames.BARREL_VOLCANO_FIRST_BOSS_FIGHT: "VolcanoBridgeBossFight",
    LocationNames.BARREL_VOLCANO_SECOND_ARROW_SIGN_ROOM_LEFT_CHEST: "VolcanoEarlyProgressChestLeftLocation",
    LocationNames.BARREL_VOLCANO_SECOND_ARROW_SIGN_ROOM_RIGHT_CHEST: "VolcanoEarlyProgressChestRightLocation",
    LocationNames.BARREL_VOLCANO_STAR_CHEST: "VolcanoEarlyProgressThirdChestLocation",
    LocationNames.BARREL_VOLCANO_SECOND_BOSS_FIGHT: "VolcanoExitBossFight",
    LocationNames.BARREL_VOLCANO_SECOND_BOSS_STAR_PIECE: "VolcanoExitStarPiece",
    LocationNames.BARREL_VOLCANO_SECRET_ROOM_LEFT_CHEST: "VolcanoLavaCoveLeftChestLocation",
    LocationNames.BARREL_VOLCANO_SECRET_ROOM_RIGHT_CHEST: "VolcanoLavaCoveRightChestLocation",
    LocationNames.BARREL_VOLCANO_LAVA_POOL_FREESTANDING_FROG_COIN: "VolcanoLavaPoolLocation",
    LocationNames.BARREL_VOLCANO_FIRST_DONUT_LIFT_ROOM_LEFT_FREESTANDING_FROG_COIN: "VolcanoLeftDonutItemLocation",
    LocationNames.BARREL_VOLCANO_REVERSE_LAVA_RECOIL_FROG_COIN: "VolcanoReverseRecoilItemLocation",
    LocationNames.BARREL_VOLCANO_FIRST_DONUT_LIFT_ROOM_RIGHT_FREESTANDING_FROG_COIN: "VolcanoRightDonutItemLocation",
    LocationNames.BARREL_VOLCANO_SAVE_ROOM_LOWER_CHEST: "VolcanoSaveRoomLowerChestLocation",
    LocationNames.BARREL_VOLCANO_SAVE_ROOM_UPPER_CHEST: "VolcanoSaveRoomUpperChestLocation",
    LocationNames.BARREL_VOLCANO_HINOPIO_SHOP_CHEST: "VolcanoShopEntranceChestLocation",
    LocationNames.YOSTER_ISLE_ENTRANCE_CHEST: "YosterEntranceChestLocation",
    LocationNames.YOSTER_ISLE_RACE_STARTING_COOKIES: "YosterRaceCookieYoshiLocation",
    LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_1: "YosterRacePrize1Location",
    LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_3: "YosterRacePrize2Location",
    LocationNames.YOSTER_ISLE_FIRST_RACE_PRIZE_ITEM_2: "YosterRacePrize3Location",
    LocationNames.BANDITS_WAY_FLOWER_FLAG: "BanditsWayFlowerFlag",
    LocationNames.BARREL_VOLCANO_INN_SIGN_FLAG: "BarrelVolcanoInnSignFlag",
    LocationNames.BARREL_VOLCANO_STUMPET_FLAG: "BarrelVolcanoStumpetFlag",
    LocationNames.BEAN_VALLEY_BEANSTALK_BLOCK_FLAG: "BeanValleyBeanstalkBlockFlag",
    LocationNames.BEAN_VALLEY_CLOUDS_FLAG: "BeanValleyCloudsFlag",
    LocationNames.BEAN_VALLEY_PIPE_FLAG: "BeanValleyPipeFlag",
    LocationNames.BOOSTER_PASS_CORNER_BUSH_FLAG: "BoosterPassCornerBushFlag",
    LocationNames.BOOSTER_TOWER_BEETLE_CAGE_FLAG: "BoosterTowerBeetleCageFlag",
    LocationNames.BOOSTER_TOWER_BROKEN_FRAME_FLAG: "BoosterTowerBrokenFrameFlag",
    LocationNames.BOOSTER_TOWER_CURTAIN_FLAG: "BoosterTowerCurtainFlag",
    LocationNames.BOOSTER_TOWER_DESK_FLAG: "BoosterTowerDeskFlag",
    LocationNames.BOOSTER_TOWER_EXTERIOR_SIGN_FLAG: "BoosterTowerExteriorSignFlag",
    LocationNames.BOOSTER_TOWER_MASHER_ROOM_FLAG: "BoosterTowerMasherRoomFlag",
    LocationNames.BOOSTER_TOWER_THWOMP_INVISIBLE_FLAG: "BoosterTowerThwompInvisibleFlag",
    LocationNames.BOOSTER_TOWER_TOY_BOX_FLAG: "BoosterTowerToyBoxFlag",
    LocationNames.CASINO_BELL_FLAG: "CasinoBellFlag",
    LocationNames.CHANCELLOR_THRONE_FLAG: "ChancellorThroneFlag",
    LocationNames.DOJO_BONSAI_FLAG: "DojoBonsaiFlag",
    LocationNames.FACTORY_BUTTON_FLAG: "FactoryButtonFlag",
    LocationNames.FACTORY_LUGNUT_FLAG: "FactoryLugnutFlag",
    LocationNames.FACTORY_TRAMPOLINE_FLAG: "FactoryTrampolineFlag",
    LocationNames.FOREST_MAZE_SECRET_MUSHROOMS_FLAG: "ForestMazeSecretMushroomsFlag",
    LocationNames.FOREST_MAZE_SECRET_STUMP_FLAG: "ForestMazeSecretStumpFlag",
    LocationNames.FOREST_MAZE_SECRET_WIGGLER_FLAG: "ForestMazeSecretWigglerFlag",
    LocationNames.KEEP_POST_OBSTACLE_BOSS_ROOM_FLAG: "KeepPostObstacleBossRoomFlag",
    LocationNames.KEEP_THWOMP_FLAG: "KeepThwompFlag",
    LocationNames.KERO_GATE_FLAG: "KeroGateFlag",
    LocationNames.KERO_STAIRS_FLAG: "KeroStairsFlag",
    LocationNames.LANDS_END_ARROW_FLAG: "LandsEndArrowFlag",
    LocationNames.LANDS_END_CANNON_FLAG: "LandsEndCannonFlag",
    LocationNames.LANDS_END_CLIFF_BUSH_FLAG: "LandsEndCliffBushFlag",
    LocationNames.LANDS_END_HILL_FLAG: "LandsEndHillFlag",
    LocationNames.LANDS_END_PLATFORM_FLAG: "LandsEndPlatformFlag",
    LocationNames.LANDS_END_SIGN_FLAG: "LandsEndSignFlag",
    LocationNames.LANDS_END_STALAGMITE_FLAG: "LandsEndStalagmiteFlag",
    LocationNames.LANDS_END_TWO_HILL_FLAG: "LandsEndTwoHillFlag",
    LocationNames.MARIOS_PAD_BED_FLAG: "MariosPadBedFlag",
    LocationNames.MARIOS_PAD_HAT_FLAG: "MariosPadHatFlag",
    LocationNames.MARIOS_PAD_LANTERN_FLAG: "MariosPadLanternFlag",
    LocationNames.MARIOS_PAD_STEAMWHISTLE_FLAG: "MariosPadSteamwhistleFlag",
    LocationNames.MARRYMORE_ALTAR_FLAG: "MarrymoreAltarFlag",
    LocationNames.MARRYMORE_CURTAINS_FLAG: "MarrymoreCurtains",
    LocationNames.MARRYMORE_FIREPLACE_FLAG: "MarrymoreFireplaceFlag",
    LocationNames.MARRYMORE_HALLWAY_FLAG: "MarrymoreHallwayFlag",
    LocationNames.MARRYMORE_KITCHEN_FLAG: "MarrymoreKitchenFlag",
    LocationNames.MARRYMORE_ORGAN_FLAG: "MarrymoreOrganFlag",
    LocationNames.MARRYMORE_OUTSIDE_CRATE_FLAG: "MarrymoreOutsideCrateFlag",
    LocationNames.MARRYMORE_SUITE_BED_FLAG: "MarrymoreSuiteBedFlag",
    LocationNames.MARRYMORE_WINDOW_FLAG: "MarrymoreWindowFlag",
    LocationNames.MIDAS_TREES_FLAG: "MidasTreesFlag",
    LocationNames.MOLEVILLE_BED_FLAG: "MolevilleBedFlag",
    LocationNames.MOLEVILLE_HYDRANT_FLAG: "MolevilleHydrantFlag",
    LocationNames.MOLEVILLE_MINES_ARROWS_FLAG: "MolevilleMinesArrowsFlag",
    LocationNames.MOLEVILLE_MINES_CEILING_FLAG: "MolevilleMinesCeilingFlag",
    LocationNames.MOLEVILLE_MINES_ENTRY_FLAG: "MolevilleMinesEntryFlag",
    LocationNames.MOLEVILLE_MOUNTAIN_BUSH_FLAG: "MolevilleMountainBushFlag",
    LocationNames.MOLEVILLE_MOUNTAIN_GO_FLAG: "MolevilleMountainGoFlag",
    LocationNames.MONSTRO_BAT_FLAG: "MonstroBatFlag",
    LocationNames.MONSTRO_ENTRANCE_SIGN_FLAG: "MonstroEntranceSignFlag",
    LocationNames.MONSTRO_FAN_FLAG: "MonstroFanFlag",
    LocationNames.MONSTRO_SHELL_FLAG: "MonstroShellFlag",
    LocationNames.MUSHROOM_KINGDOM_EMPTY_HOUSE_FLAG: "MushroomKingdomEmptyHouseFlag",
    LocationNames.MUSHROOM_KINGDOM_SIGN_FLAG: "MushroomKingdomSignFlag",
    LocationNames.MUSHROOM_WAY_TREE_FLAG: "MushroomWayTreeFlag",
    LocationNames.NIMBUS_BIRD_FLAG: "NimbusBirdFlag",
    LocationNames.NIMBUS_GOLD_GOOMBA_FLAG: "NimbusGoldGoombaFlag",
    LocationNames.NIMBUS_HOT_SPRINGS_FLAG: "NimbusHotSpringsFlag",
    LocationNames.NIMBUS_INN_LOBBY_FLAG: "NimbusInnLobbyFlag",
    LocationNames.NIMBUS_OUTDOOR_FLAG: "NimbusOutdoorFlag",
    LocationNames.NIMBUS_PLANT_FLAG: "NimbusPlantFlag",
    LocationNames.PIPE_VAULT_EXTERIOR_FLAG: "PipeVaultExteriorFlag",
    LocationNames.PIPE_VAULT_RED_PIPE_FLAG: "PipeVaultRedPipeFlag",
    LocationNames.ROSE_TOWN_BOWSER_FLAG: "RoseTownBowserFlag",
    LocationNames.ROSE_TOWN_GARDENER_BUCKET_FLAG: "RoseTownGardenerBucketFlag",
    LocationNames.ROSE_TOWN_GARDENER_HYDRANT_FLAG: "RoseTownGardenerHydrantFlag",
    LocationNames.ROSE_TOWN_GARDENER_LEAF_FLAG: "RoseTownGardenerLeafFlag",
    LocationNames.ROSE_TOWN_HYDRANT_FLAG: "RoseTownHydrantFlag",
    LocationNames.ROSE_TOWN_SIGN_FLAG: "RoseTownSignFlag",
    LocationNames.ROSE_TOWN_SINK_FLAG: "RoseTownSinkFlag",
    LocationNames.ROSE_WAY_DIRT_PATCH_FLAG: "RoseWayDirtPatchFlag",
    LocationNames.SEA_ARROW_FLAG: "SeaArrowFlag",
    LocationNames.SEA_BOXES_FLAG: "SeaBoxesFlag",
    LocationNames.SEA_STALAGNATE_FLAG: "SeaStalagnateFlag",
    LocationNames.SEA_UNDERWATER_SAIL_FLAG: "SeaUnderwaterSailFlag",
    LocationNames.SEASIDE_TOWN_ANCHOR_FLAG: "SeasideTownAnchorFlag",
    LocationNames.SEASIDE_TOWN_BUCKET_FLAG: "SeasideTownBucketFlag",
    LocationNames.SEASIDE_TOWN_FLOWERS_FLAG: "SeasideTownFlowersFlag",
    LocationNames.SEASIDE_TOWN_HYDRANT_FLAG: "SeasideTownHydrantFlag",
    LocationNames.SEASIDE_TOWN_SHED_BOX_FLAG: "SeasideTownShedBoxFlag",
    LocationNames.SHIP_BARREL_PILE_FLAG: "ShipBarrelPileFlag",
    LocationNames.SHIP_BUTTON_FLAG: "ShipButtonFlag",
    LocationNames.SHIP_DOOR_MARKER_FLAG: "ShipDoorMarkerFlag",
    LocationNames.SHIP_SWITCH_FLAG: "ShipSwitchFlag",
    LocationNames.STAR_HILL_NORTH_STAR_FLAG: "StarHillNorthStarFlag",
    LocationNames.TADPOLE_CABINET_FLAG: "TadpoleCabinetFlag",
    LocationNames.TEMPLE_SHAFT_FLAG: "TempleShaftFlag",
    LocationNames.TEMPLE_SHAFT_SWITCH_FLAG: "TempleShaftSwitchFlag",
    LocationNames.VOLCANO_BED_FLAG: "VolcanoBedFlag",
    LocationNames.VOLCANO_LAMP_FLAG: "VolcanoLampFlag",
    LocationNames.VOLCANO_SHIPS_FLAG: "VolcanoShipsFlag",
    LocationNames.YOSTER_ISLE_GOAL_FLAG: "YosterIsleGoalFlag",
    LocationNames.YOSTER_ISLE_HUT_FLAG: "YosterIsleHutFlag",
}

# from worlds.smrpg import importer
#
# from randomizer.logic.progression import prizelocations # noqa
# from randomizer.types.prizelocation import PrizeLocation # noqa
# import inspect
# import string
#
# members = inspect.getmembers(prizelocations)
# print("location_name_lookup = {")
# for member in members:
#
#     member_contents = inspect.getmembers(member[1])
#     for content in member_contents:
#         if content[0] == "_clue_text":
#             if content[1] is not None:
#                 words = re.split(r'(?=[A-Z 0-9])', member[0])
#                 words = [word.title() for word in words]
#                 for i, word in enumerate(words):
#                     if word == "Bandits":
#                         words[i] = "Bandit's"
#                     if word == "Marios":
#                         words[i] = "Mario's"
#                     if word == "Yoster":
#                         words[i] = "Yo'ster"
#                     if word == "Bowsers":
#                         words[i] = "Bowser's"
#                     if word == "Lands":
#                         words[i] = "Land's"
#                 id_name = " ".join(words).strip()
#                 #id_name = string.capwords(member[1]._id)
#                 print(f"    LocationNames.{LocationNames(id_name).name}: \"{member[0]}\",")
# print("}")