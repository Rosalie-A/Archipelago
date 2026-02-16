"""Enum of all music tracks in SMRPG with their IDs and display names."""

from enum import Enum


class MusicTrack(Enum):
    """Music tracks available for shuffling.

    Each entry has a display name (_name) and music ID (_value).
    """

    DODOS_COMING = (1, "Dodo's Coming")
    MUSHROOM_KINGDOM = (2, "Mushroom Kingdom")
    FIGHT_STRONGER_MONSTER = (3, "Fight Against Stronger Monster")
    YOSTER_ISLAND = (4, "Yo'ster Island")
    SEASIDE_TOWN = (5, "Seaside Town")
    FIGHT_MONSTERS = (6, "Fight Against Monsters")
    PIPE_VAULT = (7, "Pipe Vault")
    INVINCIBLE_STAR = (8, "Invincible Star")
    #VICTORY = (9, "Victory")
    FLOWER_GARDEN = (10, "In The Flower Garden")
    BOWSERS_CASTLE_1ST = (11, "Bowser's Castle (1st time)")
    FIGHT_BOWSER = (12, "Fight Against Bowser")
    ROAD_FULL_DANGERS = (13, "Road Is Full Of Dangers")
    MARIOS_PAD = (14, "Mario's Pad")
    HERES_SOME_WEAPONS = (15, "Here's Some Weapons")
    LETS_RACE = (16, "Let's Race")
    TADPOLE_POND = (17, "Tadpole Pond")
    ROSE_TOWN = (18, "Rose Town")
    RACE_TRAINING = (19, "Race Training")
    #SHOCK = (20, "Shock!")
    SAD_SONG = (21, "Sad Song")
    MIDAS_RIVER = (22, "Midas River")
    #STAR_PIECE_1 = (23, "Got A Star Piece (part 1)")
    #STAR_PIECE_2 = (24, "Got A Star Piece (part 2)")
    FIGHT_ARMED_BOSS = (25, "Fight Against An Armed Boss")
    FOREST_MAZE = (26, "Forest Maze")
    DUNGEON_MONSTERS = (27, "Dungeon Is Full Of Monsters")
    LETS_PLAY_GENO = (28, "Let's Play Geno")
    START_SLOT_MENU = (29, "Start Slot Menu")
    LONG_LONG_AGO = (30, "Long Long Ago")
    BOOSTERS_TOWER = (31, "Booster's Tower")
    MY_NAMES_BOOSTER = (32, "And My Name's Booster")
    MOLEVILLE = (33, "Moleville")
    STAR_HILL = (34, "Star Hill")
    MOUNTAIN_RAILROAD = (35, "Mountain Railroad")
    EXPLANATION = (36, "Explanation")
    BOOSTER_HILL_START = (37, "Booster Hill (start)")
    BOOSTER_HILL = (38, "Booster Hill")
    MARRYMORE = (39, "Marrymore")
    #NEW_PARTNER = (40, "New Partner")
    SUNKEN_SHIP = (41, "Sunken Ship")
    STILL_ROAD_MONSTERS = (42, "Still The Road Is Full Of Monsters")
    SEA = (44, "Sea")
    HEART_BEATING_1 = (45, "Heart Beating A Little Faster (part 1)")
    HEART_BEATING_2 = (46, "Heart Beating A Little Faster (part 2)")
    GRATE_GUYS_CASINO = (47, "Grate Guy's Casino")
    GENO_AWAKENS = (48, "Geno Awakens")
    #CELEBRATIONAL = (49, "Celebrational")
    NIMBUS_LAND = (50, "Nimbus Land")
    MONSTRO_TOWN = (51, "Monstro Town")
    TOADOFSKY = (52, "Toadofsky")
    HAPPY_ADVENTURE = (54, "Happy Adventure, Delightful Adventure")
    WORLD_MAP = (55, "World Map")
    FACTORY = (56, "Factory")
    SWORD_CRASHES = (57, "Sword Crashes And Stars Scatter")
    CONVERSATION_CULEX = (58, "Conversation With Culex")
    FIGHT_CULEX = (59, "Fight Against Culex")
    #VICTORY_CULEX = (60, "Victory Against Culex")
    VALENTINA = (61, "Valentina")
    BARREL_VOLCANO = (62, "Barrel Volcano")
    AXEM_RANGERS = (63, "Axem Rangers Drop In")
    THE_END = (64, "The End")
    GATE = (65, "Gate")
    BOWSERS_CASTLE_2ND = (66, "Bowser's Castle (2nd time)")
    WEAPONS_FACTORY = (67, "Weapons Factory")
    FIGHT_SMITHY_1 = (68, "Fight Against Smithy 1")
    FIGHT_SMITHY_2 = (69, "Fight Against Smithy 2")
    #ENDING_1 = (70, "Ending Part 1")
    ENDING_2 = (71, "Ending Part 2")
    #ENDING_3 = (72, "Ending Part 3")
    #ENDING_4 = (73, "Ending Part 4")

    def __init__(self, music_id: int, display_name: str):
        self._music_id = music_id
        self._display_name = display_name

    @property
    def music_id(self) -> int:
        """The music ID to write to the ROM."""
        return self._music_id

    @property
    def display_name(self) -> str:
        """Display name for the UI."""
        return self._display_name
