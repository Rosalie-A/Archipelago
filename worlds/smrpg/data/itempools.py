from collections import Counter

from worlds.smrpg import SMRPGOptions
from worlds.smrpg.data.ItemNames import ItemNames
from worlds.smrpg.data.items import unique_item_data, key_item_data, character_item_data, spell_item_data, ItemData, \
    remake_unique_item_data, remake_key_item_data

def get_vanilla_pool(options: SMRPGOptions):
    vanilla_dict = {
        ItemNames.MUSHROOM: 6,
        ItemNames.COINS_5: 5,
        ItemNames.FLOWER: 69,
        ItemNames.FLOWER_TAB: 11,
        ItemNames.RECOVERY_MUSHROOM: 26,
        ItemNames.NOTHING: 34,
        ItemNames.FROG_COIN: 65,
        ItemNames.COINS_10: 34,
        ItemNames.PICK_ME_UP: 3,
        ItemNames.STAR_PIECE: 7,
        ItemNames.KEROKERO_COLA: 9,
        ItemNames.EXP_STAR: 8,
        ItemNames.COINS_50: 2,
        ItemNames.PROGRESSIVE_CARD: 3,
        ItemNames.RED_ESSENCE: 6,
        ItemNames.FLOWER_JAR: 4,
        ItemNames.YOSHI_COOKIE: 4,
        ItemNames.PROGRESSIVE_EGG: 3,
        ItemNames.COINS_150: 4,
        ItemNames.ROCK_CANDY: 6,
        ItemNames.FLOWER_BOX: 2,
        ItemNames.MAX_MUSHROOM: 5,
        ItemNames.COINS_100: 8,
        ItemNames.ROYAL_SYRUP: 5,
        ItemNames.FIRE_BOMB: 3,
        ItemNames.SLOTS: 3,
        ItemNames.ALTO_CARD: 0,
        ItemNames.TENOR_CARD: 0,
        ItemNames.SOPRANO_CARD: 0,
        ItemNames.MYSTERY_EGG: 0,
        ItemNames.SHEEP_ATTACK: 0,
        ItemNames.LAMBS_LURE: 0,
        ItemNames.REGULAR_FIREWORKS: 0,
        ItemNames.BEETLEMANIA: 1,
        ItemNames.FIRST_MIMIC_LAUNCHER: 1,
        ItemNames.SECOND_MIMIC_LAUNCHER: 1,
        ItemNames.THIRD_MIMIC_LAUNCHER: 1,
        ItemNames.INFINITE_COINS: 1,
        ItemNames.FROG_COIN_2: 1,
        ItemNames.FROG_COIN_10: 1,
        ItemNames.FROG_COIN_20: 1,
    }
    vanilla_pool = Counter(vanilla_dict)
    return_pool = vanilla_pool.copy()
    singleton_items: list[ItemData] = [*unique_item_data, *key_item_data]

    if options.spells_anywhere:
        singleton_items.extend(spell_item_data)
    else:
        # I'm not sure precisely what I'm missing for vanilla pool right now, so this is
        # an ad hoc adustment.
        return_pool.update({ItemNames.FLOWER: 10, ItemNames.RECOVERY_MUSHROOM: 10, ItemNames.COINS_10: 7})

    # Similar to the above else clause, not sure what I'm missing, but not fussing about the details.
    return_pool[ItemNames.RECOVERY_MUSHROOM] -= 2

    for item in singleton_items:
        return_pool[item.name] = 1

    remake_items: list[ItemData] = [*remake_unique_item_data, *remake_key_item_data]

    remake_pool = dict()
    for item in remake_items:
        remake_pool[item] = 1
    if options.enable_remake_content:
        return_pool.update(remake_pool)
    return return_pool

# from worlds.smrpg import importer
#
# from randomizer.logic.progression import prizelocations # noqa
# from randomizer.types.prizelocation import PrizeLocation # noqa
# import inspect
#
# members = inspect.getmembers(prizelocations)
# for member in members:
#     member_contents = inspect.getmembers(member[1])
#     for content in member_contents:
#         if content[0] == "_originally_held":
#             if content[1] is not None:
#                 print(content[1].__name__)