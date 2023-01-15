import typing

from BaseClasses import ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification
    event: bool = False


# Filler items that we can freely toss multiples of in the pool
consumables = [
    "Mushroom", "Mid Mushroom", "Max Mushroom", "Honey Syrup", "Maple Syrup", "Royal Syrup", "Pick Me Up",
    "Able Juice", "Bracer", "Energizer", "Yoshi Ade", "Red Essence", "Kerokero Cola", "Yoshi Cookie",
    "Pure Water", "Sleepy Bomb", "Bad Mushroom", "Fire Bomb", "Ice Bomb", "Flower Tab", "Flower Jar",
    "Flower Box", "Yoshi Candy", "Froggie Drink", "Muku Cookie", "Elixir", "Megalixir", "Freshen Up",
    "Rock Candy", "Sheep Attack", "Carbo Cookie", "Fright Bomb", "Crystalline", "Power Blast",
    "Wilt Shroom", "Rotten Mush", "Moldy Mush", "Mushroom 2", "Lucky Jewel"
]

chest_rewards = [
    "Five Coins", "Eight Coins", "Ten Coins", "Fifty Coins", "One Hundred Coins", "One Hundred Fifty Coins",
    "Flower", "Recovery Mushroom", "Frog Coin", "You Missed!"
]

filler = [*consumables, *chest_rewards]

# Not key items, but stuff that doesn't make sense to have in the pool multiple times
singleton_items = [
    "Wallet", "Goodie Bag", "See Ya", "Earlier Times", "Shiny Stone", "Lamb's Lure", "Mystery Egg", "Star Egg"
]

weapons = [
    "Hammer", "Froggie Stick", "Nok Nok Shell", "Punch Glove", "Finger Shot", "Cymbals",
    "Chomp", "Masher", "Chomp Shell", "Super Hammer", "Hand Gun", "Whomp Glove", "Slap Glove",
    "Troopa Shell", "Parasol", "Hurly Gloves", "Double Punch", "Ribbit Stick", "Spiked Link", "Mega Glove",
    "War Fan", "Hand Cannon", "Sticky Glove", "Ultra Hammer", "Super Slap", "Drill Claw", "Star Gun",
    "Sonic Cymbal", "Lazy Shell Weapon", "Frying Pan", "Lucky Hammer"
]

armor = [
    "Shirt", "Pants", "Thick Shirt",
    "Thick Pants", "Mega Shirt", "Mega Pants", "Work Pants", "Mega Cape", "Happy Shirt", "Happy Pants",
    "Happy Cape", "Happy Shell", "Polka Dress", "Sailor Shirt", "Sailor Pants", "Sailor Cape", "Nautica Dress",
    "Courage Shell", "Fuzzy Shirt", "Fuzzy Pants", "Fuzzy Cape", "Fuzzy Dress", "Fire Shirt", "Fire Pants",
    "Fire Cape", "Fire Shell", "Fire Dress", "Hero Shirt", "Prince Pants", "Star Cape", "Heal Shell",
    "Royal Dress", "Super Suit", "Lazy Shell Armor"
]

accessories = [
    "Zoom Shoes", "Safety Badge", "Jump Shoes",
    "Safety Ring", "Amulet", "Scrooge Ring", "Exp Booster", "Attack Scarf", "Rare Scarf",
    "B'tub Ring", "Antidote Pin", "Wake Up Pin", "Fearless Pin", "Trueform Pin", "Coin Trick",
    "Ghost Medal", "Jinx Belt", "Feather", "Troopa Pin", "Signal Ring", "Quartz Charm"
]

equipment = [*weapons, *armor, *accessories]

all_mundane_items = [*filler, *equipment]

key_items = [
    "Temple Key", "Rare Frog Coin", "Cricket Pie", "Castle Key 1", "Castle Key 2", "Bambino Bomb",
    "Room Key", "Elder Key", "Shed Key", "Soprano Card", "Alto Card", "Tenor Card", "Seed", "Fertilizer",
    "Big Boo Flag", "Dry Bones Flag", "Greaper Flag", "Cricket Jam", "Bright Card"
]

boss_items = [
    "Star Piece", "Defeated!", "Star Road Restored!"
]
id = 0

item_table = dict()

for item in consumables:
    new_item = ItemData(id, ItemClassification.filler, False)
    item_table[item] = new_item
    id += 1

for item in chest_rewards:
    new_item = ItemData(id, ItemClassification.filler, False)
    item_table[item] = new_item
    id += 1

for item in weapons:
    new_item = ItemData(id, ItemClassification.useful, False)
    item_table[item] = new_item
    id += 1

for item in armor:
    new_item = ItemData(id, ItemClassification.useful, False)
    item_table[item] = new_item
    id += 1

for item in accessories:
    new_item = ItemData(id, ItemClassification.useful, False)
    item_table[item] = new_item
    id += 1

for item in key_items:
    new_item = ItemData(id, ItemClassification.progression, False)
    item_table[item] = new_item
    id += 1

for item in boss_items:
    new_item = ItemData(id, ItemClassification.progression, False)
    item_table[item] = new_item
    id += 1
