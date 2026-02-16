from ..variables.dialog_names import *
import random

option_1_correct = [
    DI1842_QUIZ_QUESTION_1,
    DI1843_QUIZ_QUESTION_2,
    DI1844_QUIZ_QUESTION_3,
    DI1845_QUIZ_QUESTION_4,
    DI1846_QUIZ_QUESTION_5,
    DI1847_QUIZ_QUESTION_6,
    DI1848_QUIZ_QUESTION_7,
    DI1849_QUIZ_QUESTION_8,
    DI1850_QUIZ_QUESTION_9,
    DI1851_QUIZ_QUESTION_10,
    DI1852_QUIZ_QUESTION_11,
    DI1853_QUIZ_QUESTION_12,
    DI1854_QUIZ_QUESTION_13,
    DI1855_QUIZ_QUESTION_14,
    DI1856_QUIZ_QUESTION_15,
    DI1857_QUIZ_QUESTION_16,
]
option_2_correct = [
    DI1858_QUIZ_QUESTION_17,
    DI1859_QUIZ_QUESTION_18,
    DI1860_QUIZ_QUESTION_19,
    DI1861_QUIZ_QUESTION_20,
    DI1862_QUIZ_QUESTION_21,
    DI1863_QUIZ_QUESTION_22,
    DI1864_QUIZ_QUESTION_23,
    DI1865_QUIZ_QUESTION_24,
    DI1866_QUIZ_QUESTION_25,
    DI1867_QUIZ_QUESTION_26,
    DI1868_QUIZ_QUESTION_27,
    DI1869_QUIZ_QUESTION_28,
    DI1870_QUIZ_QUESTION_29,
    DI1871_QUIZ_QUESTION_30,
    DI1872_QUIZ_QUESTION_31,
    DI1873_QUIZ_QUESTION_32,
]
option_3_correct = [
    DI1874_QUIZ_QUESTION_33,
    DI1875_QUIZ_QUESTION_34,
    DI1876_QUIZ_QUESTION_35,
    DI1877_QUIZ_QUESTION_36,
    DI1878_QUIZ_QUESTION_37,
    DI1879_QUIZ_QUESTION_38,
    DI1880_QUIZ_QUESTION_39,
    DI1881_QUIZ_QUESTION_40,
]

wrong_indexes = {
    0: (1, 2),
    1: (0, 2),
    2: (0, 1),
}


class Question:
    def __init__(self, question, correct, wrong_1, wrong_2):
        self.question = question
        self.correct_answer = correct
        self.wrong_answers = [wrong_1, wrong_2]

    def get_string(self, dialog_id: int) -> str:
        if dialog_id in option_1_correct:
            correct_index = 0
        elif dialog_id in option_2_correct:
            correct_index = 1
        elif dialog_id in option_3_correct:
            correct_index = 2
        else:
            raise ValueError(f"Dialog ID {dialog_id} is not a valid quiz question ID.")
        answers = [""] * 3
        answers[correct_index] = " [select]  (" + self.correct_answer + ")\n"
        index_1, index_2 = wrong_indexes[correct_index]
        answers[index_1] = " [select]  (" + self.wrong_answers[0] + ")\n"
        answers[index_2] = " [select]  (" + self.wrong_answers[1] + ")\n"
        final_string = self.question + "[await][page]\n" + "".join(answers)
        final_string = final_string[:-1]  # Remove trailing newline from final answer.
        return final_string


def get_smrpg_questions():
    """Get SMRPG-related quiz questions.

    Returns:
        list[Question]: List of SMRPG questions.

    """
    return [
        Question(
            "What game gives\nyou the Star Egg?",
            "Look The Other Way",
            "Blackjack",
            "Pokemon",
        ),
        Question("Who is Yoshi's nemesis?", "Boshi", "Broshi", "Raz"),
        Question(
            "What can you trade\nthe Shiny Stone for?",
            "Carbo Cookie",
            "Fireworks",
            "A Frog Coin",
        ),
        Question(
            "Which isn't a setting\non Monstro Town's Pinwheel?",
            "Blow",
            "Gust",
            "Blast",
        ),
        Question(
            "How does Mario taste?",
            "Ack! Sour!",
            "YES! THIS is YUMMY!",
            "Mmm, tastes peachy...",
        ),
        Question(
            "How does Mallow taste?",
            "YES! THIS is YUMMY!",
            "Mmm, tastes peachy...",
            "Ack! Sour!",
        ),
        Question(
            "How does Geno taste?",
            "Bitter, but not bad...",
            "Ack! Sour!",
            "Yuck! How repulsive!",
        ),
        Question(
            "How does Bowser taste?",
            "Yuck! How repulsive!",
            "Bitter, but not bad...",
            "YES! THIS is YUMMY!",
        ),
        Question(
            "How does Toadstool taste?",
            "Mmm, tastes peachy...",
            "YES! THIS is YUMMY!",
            "Bitter, but not bad...",
        ),
        Question(
            "Like the moon over\nthe day, my genius and brawn...",
            "are lost on these fools.",
            "are hollow echoes.",
            "are without equal.",
        ),
        Question(
            "Which of these is NOT\na card for the Juice Bar?",
            "Baritone Card",
            "Tenor Card",
            "Soprano Card",
        ),
        Question(
            "What type of clothes\nare normally sold\nin Nimbus Land?",
            "Fuzzy",
            "Happy",
            "Thick",
        ),
        Question(
            "Where did Samus Aran\nstay the night?",
            "Mushroom Kingdom",
            "Rose Town",
            "Nimbus Land",
        ),
        Question(
            "Where did Link\nstay the night?",
            "Rose Town",
            "Mushroom Kingdom",
            "Nimbus Land",
        ),
        Question(
            "Which enemy uses Blast?", "Earth Crystal", "Wind Crystal", "Fire Crystal"
        ),
        Question(
            "Which enemy uses Drain?", "Fire Crystal", "Wind Crystal", "Earth Crystal"
        ),
        Question(
            "Which enemy uses Light Beam?",
            "Wind Crystal",
            "Water Crystal",
            "Earth Crystal",
        ),
        Question(
            "Which enemy uses Crystal?", "Water Crystal", "Wind Crystal", "Fire Crystal"
        ),
        Question(
            "Which equip allows you to\njump through enemy defenses?",
            "Jump Shoes",
            "Zoom Shoes",
            "Spring Shoes",
        ),
        Question(
            "How many wishes\ncan you interact with\non Star Hill?", "12", "10", "15"
        ),
        Question("Jawful is...?", "Sleeping", "Enraptured", "Ready to launch!"),
        Question("Valentina's hair is\nmade of a...?", "Parrot", "Plant", "Octopus"),
        Question("Who knocks out Mario?", "Gaz", "Raz", "Garro"),
        Question(
            "What does Dyna get\ninto the business of?",
            "Trading",
            "Selling items",
            "Giving hints",
        ),
        Question("Who summons Bahamutt?", "Magikoopa", "Belome", "Box Boy"),
        Question(
            "The Gardener wants to hit\nthe lottery without what?",
            "Paying taxes",
            "Skiing",
            "Getting his picture taken",
        ),
        Question("Who is the cloud enemy\nin Land's End?", "Mokura", "Bokura", "Goku"),
        Question(
            "Who gets mad if you\nstand on their head?", "Johnny", "Frogfucius", "Jinx"
        ),
        Question(
            "What does Bowser love\nthe scent of?",
            "Boiling lava",
            "Flower beds",
            "Green donkeys",
        ),
        Question(
            "How many bolts hold together\nthe inner factory battlefield?",
            "4",
            "3",
            "5",
        ),
        Question(
            "How much damage does a\nboosted Ice Bomb normally do\nagainst Czar Dragon?",
            "420",
            "210",
            "69",
        ),
        Question(
            "What snake boss does\nDomino join up with?",
            "Mad Adder",
            "Earthlink",
            "Culex",
        ),
        Question("Who is NOT a hidden\nchest boss?", "Fautso", "Box Boy", "Chester"),
        Question(
            "What is Geno's move\nthat knocks out Mario?",
            "Shooting Star Shot",
            "Special Beam Cannon",
            "Spirit Gun",
        ),
        Question(
            "Vat ist zee name of\nzee cake you fight\nin Marrymore?",
            "Bundt",
            "German Chocolate",
            "Pound",
        ),
        Question(
            "How many more points in\nGoomba Thumping are needed\nto win another reward?",
            "2",
            "4",
            "6",
        ),
        Question(
            "How many hidden treasure\nchests are in the\nvanilla game?",
            "39",
            "38",
            "40",
        ),
        Question(
            "Which accessory does NOT\nprovide an attack boost\nto the equipped character?",
            "Ghost Medal",
            "Troopa Pin ",
            "Quartz Charm",
        ),
        Question(
            "What is Johnny looking\nat in the end credits?",
            "Sunset",
            "Mario",
            "His ship",
        ),
        Question(
            "How many citizens are at\nMallow's coronation ceremony?", "12", "9", "5"
        ),
        Question(
            "Who is flying Bowser's\nclown car in the\nending cutscene?",
            "Shy Guy",
            "Terrapin",
            "Magikoopa",
        ),
        Question(
            "Who does Yoshi race against\nin the ending cutscene?",
            "Croco",
            "Boshi",
            "Mario",
        ),
        Question("How many Toads are in\nToadofsky's choir?", "7", "4", "10"),
        Question(
            "Who does Booster\nend up marrying?", "Valentina", "Toadstool", "Raini"
        ),
        Question(
            "How many Toads immediately\nfollow Luigi in the parade?", "5", "3", "2"
        ),
        Question(
            "What makes a sound when\na hidden chest is near?",
            "Signal Ring",
            "B'tub Ring",
            "Safety Ring",
        ),
        Question(
            "Which type of armor\nis normally only usable\nby Bowser?",
            "Courage",
            "Fire",
            "Sailor",
        ),
        Question(
            "What happens when a\nYoshi Cookie fails?",
            "Get Yoshi Candy instead",
            "Enemy bites Yoshi's tongue",
            "Yoshi lays an egg",
        ),
        Question(
            "What is the travelling\nToad looking for?",
            "Grate Guy's Casino",
            "Best inn to stay at",
            "Star pieces",
        ),
        Question(
            "Which does NOT normally\ngive immunity to\ninstant death attacks?",
            "Super Suit",
            "Attack Scarf",
            "Quartz Charm",
        ),
        Question(
            "Which enemy is NOT found\nin the same location\nas the others?",
            "Wiggler",
            "Mukumuku",
            "Mastadoom",
        ),
        Question("How many tentacles does\nKing Calimari have?", "8", "6", "10"),
        Question("Which is NOT one of the\nAxem Rangers?", "Blue", "Pink", "Red"),
        Question(
            "Which is NOT one of\nCountdown's attacks?",
            "Boulder",
            "Mega Recover",
            "Aurora Flash",
        ),
        Question(
            "Which attack does Mack\nuse on you?",
            "Flame Wall",
            "S'Crow Dust",
            "Static E!",
        ),
        Question(
            "Who do you attack\ninstead of Bowser\nin the prologue?",
            "Kinklink",
            "Throne",
            "Support",
        ),
        Question(
            "Where is the Goomba\nthumping game located?",
            "Pipe Vault",
            "Moleville",
            "Monstro Town",
        ),
        Question(
            "Which is NOT normally\none of Mallow's\nspecial attacks?",
            "Mute",
            "Psychopath",
            "Snowy",
        ),
        Question(
            "What special attack does\nMario normally start with?",
            "Jump",
            "Fire Orb",
            "Crusher",
        ),
        Question("Who does Toadstool\nalmost marry?", "Booster", "Bowser", "Mario"),
        Question(
            "What menu option appears\nwhen your fourth\nparty member joins?",
            "Switch",
            "Team",
            "Power",
        ),
        Question(
            "What did Croco steal\nfrom Mallow?", "Frog Coin", "Wallet", "Kerokerocola"
        ),
        Question(
            "What does Hammer Bro use\nwhen one is defeated?",
            "Valor Up",
            "Vigor Up",
            "Versatility Up",
        ),
        Question(
            "What is the name of\nMario's house?",
            "The Pipehouse",
            "Mario Manor",
            "The Goomba Hole",
        ),
        Question(
            "Where do you fight\nBowser in the prologue?",
            "On chandeliers",
            "Over a lava pit",
            "A large arena",
        ),
        Question(
            "How much...does a\nfemale beetle cost?",
            "1 coin",
            "50 coins",
            "A frog coin",
        ),
        Question(
            "What does Belome\nreally like to turn people into?",
            "Scarecrows",
            "Ice cream cones",
            "Mushrooms",
        ),
        Question("What is Raini's\nhusband's name?", "Raz", "Romeo", "Gaz"),
        Question(
            "What's the name of\nthe boss at the Sunken Ship?",
            "Johnny",
            "Jimmy",
            "Jackson",
        ),
        Question("Booster is what\ngeneration?", "7th", "8th", "78th"),
        Question(
            "Where is the 3rd\nStar Piece normally found?",
            "Moleville",
            "Forest Maze",
            "Star Hill",
        ),
        Question(
            "Johnny loves WHICH\nbeverage?...",
            "Currant juice",
            "Grape juice",
            "Boysenberry smoothie",
        ),
        Question(
            "In the Moleville blues,\nit's said that the moles are\ncovered in what?",
            "Soil",
            "Dirt",
            "Slugs",
        ),
        Question(
            "What color are the\ncurtains in Mario's house?", "Blue", "Green", "Red"
        ),
        Question(
            "Yaridovich is what?", "A boss", "A new breed of cattle", "A special attack"
        ),
        Question(
            "The boy at the inn in\nMushroom Kingdom was playing\nwith...What?",
            "Game Boy",
            "Super NES",
            "Virtual Boy",
        ),
        Question("What did Carroboscis\nturn into?", "A carrot", "A beet", "A radish"),
        Question("Who is the famous\nsculptor in Nimbus Land?", "Garro", "Gaz", "Goya"),
        Question(
            "What is Hinopio in\ncharge of at the middle counter?",
            "The inn",
            "Weapons",
            "Items",
        ),
        Question(
            "Who is the ultimate\nenemy in this adventure?",
            "Smithy",
            "Bowser",
            "Goomba",
        ),
        Question("Who is the leader of\nThe Axem Rangers?", "Red", "Black", "Green"),
        Question("What's the name of\nJagger's \"sensei#?", "Jinx", "Dinky", "Johnny"),
        Question("How many underlings\ndoes Croco have?", "3", "2", "4"),
        Question(
            "What was Toadstool\ndoing when she was kidnapped by\nBowser?",
            "She was looking at flowers",
            "She was playing cards",
            "She was digging for worms",
        ),
        Question(
            "Who is the famous\ncomposer at Tadpole Pond?",
            "Toadofsky",
            "Toadoskfy",
            "Frogfucius",
        ),
        Question(
            "Which monster does\nnot appear in Booster Tower?",
            "Terrapin",
            "Jester",
            "Bob-omb",
        ),
        Question(
            "The boy getting his\npicture taken at Marrymore\ncan't wait 'til which season?",
            "Skiing",
            "Hunting",
            "Baseball",
        ),
        Question(
            "What technique does Bowser\nnormally learn at Level 15?",
            "Crusher",
            "Bowser Crush",
            "Terrorize",
        ),
        Question(
            "What words does\nShy Away use when he sings?",
            "La dee dah:",
            "Dum dee dah:",
            "Dum lee lah:",
        ),
        Question(
            "What does Birdo\ncome out of?", "An eggshell", "A barrel", "A basket"
        ),
        Question(
            "What's the first\nmonster you see in the Pipe Vault?",
            "Sparky",
            "Goomba",
            "Chompweed",
        ),
        Question(
            "What's the password\nin the Sunken Ship?", "Pearls", "Corals", "Oyster"
        ),
        Question(
            "What was Mallow \nasked to get for Frogfucius?",
            "Cricket Pie",
            "Honey Syrup",
            "Carbo Cookie",
        ),
        Question(
            "Mite is Dyna's...\nWHAT?", "Little brother", "Big sister", "Second cousin"
        ),
        Question(
            "What does the Red\nEssence do?",
            "Gives you strength",
            "Makes you sleepy",
            "Relieves back pain",
        ),
        Question(
            "How long have the\ncouple inside the chapel been\nwaiting for their wedding?",
            "30 minutes",
            "1 hour",
            "45 minutes",
        ),
        Question(
            "What do Culex, Jinx,\nand Goomba have in common?",
            "They live in Monstro Town",
            "They are immortal",
            "They all like bratwurst",
        ),
        Question(
            "What is the 4th\nselection on the Menu screen?",
            "Equip",
            "Important Items",
            "Special Items",
        ),
        Question(
            "The man getting his\npicture taken at Marrymore\nhates what?",
            "Getting his picture taken",
            "Getting married",
            "Mowing the lawn on Sundays",
        ),
        Question(
            "Where is the 1st\nStar Piece normally found?",
            "Mushroom Kingdom",
            "Bowser's Keep",
            "Mario's Pad",
        ),
        Question("How many legs does\nWiggler have?", "6", "10", "8"),
        Question(
            "What's the full name\nof the boss at the Sunken Ship?",
            "Jonathan Jones",
            "Johnny Jones",
            "Jesse James Jones",
        ),
        Question(
            "Who helped you up the\ncliff at Land's End?",
            "Sky Troopas",
            "Sky Troops",
            "Flying Troopa",
        ),
        Question("What color is the\nend of Dodo's beak?", "Red", "Yellow", "Orange"),
        Question("What's the chef's\nname at Marrymore?", "Torte", "Blintz", "Gateau"),
        Question(
            "DR. TOPPER: What status\n condition can BOWYER give you?",
            "Sleep",
            "Mute",
            "Fear",
        ),
        Question(
            "DR. TOPPER: The mitochondria is...",
            "The powerhouse of the cell",
            "A rare species of insect",
            "An iconic Italian pasta",
        ),
    ]


def get_non_smrpg_questions():
    """Get non-SMRPG-related quiz questions.

    Returns:
        list[Question]: List of non-SMRPG questions.

    """
    return [
        Question(
            "DR. TOPPER: Name That Move: The\n player jumps off a Switch Palace\n button in Super Mario World?",
            "Yump!",
            "Frame Perfect Button Bounce!",
            "No name, it's just cool",
        )
    ]


def get_quiz_questions(include_non_smrpg: bool = False):
    """Get new list of potential quiz questions for the randomizer.

    Args:
        include_non_smrpg: If True, include non-SMRPG questions in the pool.

    Returns:
        list[Question]: List of questions.

    """
    questions = get_smrpg_questions()
    if include_non_smrpg:
        questions = questions + get_non_smrpg_questions()
    return random.sample(questions, 40)
