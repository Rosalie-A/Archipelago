"""Equipment randomization logic."""
from __future__ import annotations
import random
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.spells.enums import Element, Status, TempStatBuff
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import PartyCharacter

from ..utils import mutate_normal

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.items.classes import Equipment


def randomize_equipment_properties(world: GameWorld) -> None:
    """Randomize equipment stats and buffs (excluding character allowances)."""
    from ...types.item import Weapon, Armor, Accessory

    EQUIP_STATS = ["speed", "attack", "defense", "magic_attack", "magic_defense"]
    PRIMARY_STATS_BY_TYPE = {
        Weapon: ["attack"],
        Armor: ["defense", "magic_defense"],
        Accessory: ["speed"],
    }

    for item in world.items.items:
        if not isinstance(item, (Weapon, Armor, Accessory)):
            continue

        # Get primary stats for this item type
        primary_stats = []
        for item_type, stats in PRIMARY_STATS_BY_TYPE.items():
            if isinstance(item, item_type):
                primary_stats = stats
                break

        # Calculate stat point value (similar to old logic)
        stat_point_value = 0
        for attr in EQUIP_STATS:
            val = getattr(item, attr, 0)
            if val > 0:
                if attr in primary_stats:
                    stat_point_value += val
                else:
                    stat_point_value += val * 2

        # Randomize number of attributes to go up or down
        # 1/3 chance all non-zero stats go up
        ups: list[str] = []
        if random.randint(1, 3) == 1:
            ups = [attr for attr in EQUIP_STATS if getattr(item, attr, 0) > 0]

        if not ups:
            num_up = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 10, 5, 1])[0]
            while True:
                ups = random.sample(EQUIP_STATS, num_up)
                if set(ups) & set(primary_stats):
                    break

        # Attributes going down (1/3 chance all negative stats go down)
        if random.randint(1, 3) == 1:
            downs = [attr for attr in EQUIP_STATS if getattr(item, attr, 0) < 0]
        else:
            num_down = random.choices(
                [0, 1, 2, 3, 4, 5], weights=[1, 5, 10, 10, 5, 1]
            )[0]
            downs = random.sample(EQUIP_STATS, num_down)

        # Priority to going up
        downs = [d for d in downs if d not in ups]

        # Track increases and decreases
        score = stat_point_value
        up_vals = {u: 0 for u in ups}
        down_vals = {d: 0 for d in downs}

        # Distribute down points
        if downs:
            if score != 0:
                down_points = random.randint(0, random.randint(0, score))
            else:
                down_points = random.randint(
                    0, random.randint(0, random.randint(0, 100))
                )
            score += down_points
            for _ in range(down_points):
                attr = random.choice(downs)
                down_vals[attr] += 1

        # Distribute up points
        while score > 0:
            attr = random.choice(ups)
            up_vals[attr] += 1
            if attr in primary_stats:
                score -= 1
            else:
                score -= 2

        # Zero all stats
        for attr in EQUIP_STATS:
            setter = getattr(item, f"set_{attr}")
            setter(0)

        # Set new positive stats with mutation
        for attr in up_vals:
            val = mutate_normal(up_vals[attr], minimum=1, maximum=127)
            setter = getattr(item, f"set_{attr}")
            setter(val)

        # Set new negative stats with mutation
        for attr in down_vals:
            val = mutate_normal(down_vals[attr], minimum=1, maximum=127)
            setter = getattr(item, f"set_{attr}")
            setter(-val)

        # If weapon with variance, shuffle that too
        if isinstance(item, Weapon) and item.variance > 0:
            new_variance = mutate_normal(
                int(item.variance), minimum=1, maximum=127
            )
            item.set_variance(new_variance)

        # Randomize special properties based on tier
        # Determine tier based on item price (rough approximation)
        price = item.price
        if price <= 50:
            tier = 1
        elif price <= 150:
            tier = 2
        elif price <= 400:
            tier = 3
        elif price <= 1000:
            tier = 4
        else:
            tier = 5

        odds_map = {1: 2 / 3, 2: 1 / 2, 3: 1 / 4, 4: 1 / 8, 5: 3 / 32}
        odds = odds_map.get(tier, 0) / 2  # Halved as per 7.1.3 update

        if odds > 0:
            # Instant KO protection
            ko_odds = odds
            if isinstance(item, Weapon):
                ko_odds /= 2
            item.set_prevent_ko(random.random() < ko_odds)

            # Elemental immunities/resistances
            item.set_elemental_immunities([])
            item.set_elemental_resistances([])
            elements = [Element.ICE, Element.FIRE, Element.THUNDER]
            if random.randint(1, 2) == 1:
                for elem in elements:
                    if random.random() < odds:
                        item.append_elemental_immunity(elem)
                    elif random.random() < odds:
                        item.append_elemental_resistance(elem)
            else:
                for elem in elements:
                    if random.random() < odds:
                        item.append_elemental_resistance(elem)
                    elif random.random() < odds:
                        item.append_elemental_immunity(elem)

            # Safety check: ensure no element is in both immunity and resistance lists
            immunities_set = set(item.elemental_immunities)
            resistances_set = set(item.elemental_resistances)
            overlap = immunities_set & resistances_set
            if overlap:
                # Remove overlapping elements from resistances (immunity takes priority)
                for elem in overlap:
                    item.remove_elemental_resistance(elem)

            # Status immunities
            item.set_status_immunities([])
            status_list = [
                Status.MUTE,
                Status.SLEEP,
                Status.POISON,
                Status.FEAR,
                Status.MUSHROOM,
                Status.SCARECROW,
            ]
            for status in status_list:
                if random.random() < odds:
                    item.append_status_immunity(status)

            # Temp buffs (weighted toward accessories/armor)
            buff_odds = odds
            if isinstance(item, Weapon):
                buff_odds /= 2
            elif isinstance(item, Armor):
                buff_odds /= 5
            item.set_temp_buffs([])
            buffs = [
                TempStatBuff.ATTACK,
                TempStatBuff.DEFENSE,
                TempStatBuff.MAGIC_ATTACK,
                TempStatBuff.MAGIC_DEFENSE,
            ]
            for buff in buffs:
                if random.random() < buff_odds:
                    item.append_temp_buff(buff)

        # Update description based on new stats
        item.set_description(item.build_equipment_description())


def randomize_equipment_characters(
    world: GameWorld,
    setting,  # EquipmentCharactersOptions
) -> None:
    """Randomize which characters can equip each piece of equipment."""
    from smrpgpatchbuilder.datatypes.items.classes import Weapon, Armor, Accessory
    from ...types.flags import EquipmentCharactersOptions

    ALL_CHARS = [
        PartyCharacter(i) for i in range(5)
    ]  # Mario=0, Mallow=1, Geno=2, Bowser=3, Peach=4

    for item in world.items.items:
        if not isinstance(item, (Weapon, Armor, Accessory)):
            continue

        if setting == EquipmentCharactersOptions.EQUIP_ALL:
            # Anyone can equip anything
            item.set_equip_chars(list(ALL_CHARS))

        elif setting == EquipmentCharactersOptions.VANILLA_ACCESSORIES_ALL:
            # Only accessories get all chars
            if isinstance(item, Accessory):
                item.set_equip_chars(list(ALL_CHARS))
            # Weapons and armor keep vanilla (no change needed)

        elif setting == EquipmentCharactersOptions.RANDOM_ACCESSORIES_ALL:
            if isinstance(item, Accessory):
                # All accessories can be equipped by anyone
                item.set_equip_chars(list(ALL_CHARS))
            else:
                # Weapons and armor get randomized
                _randomize_single_equip_chars(item, ALL_CHARS)

        elif setting == EquipmentCharactersOptions.RANDOM:
            # Everything gets randomized
            _randomize_single_equip_chars(item, ALL_CHARS)


def _randomize_single_equip_chars(
    item: Equipment, all_chars: list[PartyCharacter]
) -> None:
    """Randomize equippable characters for a single item."""
    # Pick random number of characters with lower numbers weighted heavier
    num_equippable = random.randint(1, random.randint(1, 5))
    new_chars: set[PartyCharacter] = set()

    for _ in range(num_equippable):
        char_choices = set(all_chars) - new_chars
        if not char_choices:
            break
        new_chars.add(random.choice(list(char_choices)))

    item.set_equip_chars(list(new_chars))


def build_item_impact_categories(world: GameWorld) -> None:
    """Build item impact categories for use in shop shuffling and other systems.

    Categorizes consumables and equipment into low/high/highest impact tiers.
    Equipment is ranked based on stats, immunities, and special properties.
    """
    from smrpgpatchbuilder.datatypes.items.classes import Weapon, Armor, Accessory, Equipment
    from ...data.items.items import (
        PickMeUpItem,
        MushroomItem,
        HoneySyrupItem,
        AbleJuiceItem,
        BracerItem,
        EnergizerItem,
        YoshiCookieItem,
        PureWaterItem,
        SleepyBombItem,
        BadMushroomItem,
        FlowerTabItem,
        FroggieDrinkItem,
        MukuCookieItem,
        FreshenUpItem,
        FrightBombItem,
        WiltShroomItem,
        RottenMushItem,
        MoldyMushItem,
        MushroomItem2,
        MidMushroomItem,
        MaxMushroomItem,
        MapleSyrupItem,
        RoyalSyrupItem,
        YoshiAdeItem,
        FireBombItem,
        IceBombItem,
        YoshiCandyItem,
        ElixirItem,
        MegalixirItem,
        CrystallineItem,
        PowerBlastItem,
        RedEssenceItem,
        KerokeroColaItem,
        RockCandyItem,
    )
    from ...types.flags import NoPickMeUps, RestrictSpecialEquips, Remake

    no_pickmeups = world.settings.isflag_enabled(NoPickMeUps)

    # Define consumable item pools
    world.low_impact_items = [
        MushroomItem,
        HoneySyrupItem,
        AbleJuiceItem,
        BracerItem,
        EnergizerItem,
        YoshiCookieItem,
        PureWaterItem,
        SleepyBombItem,
        BadMushroomItem,
        FlowerTabItem,
        FroggieDrinkItem,
        MukuCookieItem,
        FreshenUpItem,
        FrightBombItem,
        WiltShroomItem,
        RottenMushItem,
        MoldyMushItem,
        MushroomItem2,
    ]
    if not no_pickmeups:
        world.low_impact_items.append(PickMeUpItem)

    world.high_impact_items = [
        MidMushroomItem,
        MaxMushroomItem,
        MapleSyrupItem,
        RoyalSyrupItem,
        YoshiAdeItem,
        FireBombItem,
        IceBombItem,
        YoshiCandyItem,
        ElixirItem,
        MegalixirItem,
        CrystallineItem,
        PowerBlastItem,
    ]

    world.highest_impact_items = [
        RedEssenceItem,
        KerokeroColaItem,
        RockCandyItem,
    ]

    # Calculate equipment rank values and categorize them
    def calc_equip_rank(item: Equipment) -> float:
        variance = int(item.variance) if isinstance(item, Weapon) else 0
        attack = item.attack
        attack_base = attack - variance if attack - variance != 0 else 1
        attack_variance_factor = (
            min(2, (attack + variance) / attack_base) if attack > 0 else 0
        )

        rank = (
            attack * max(0, attack_variance_factor)
            + max(
                0,
                (item.magic_attack / (2 if item.magic_attack < 0 else 1))
                + (item.magic_defense / (2 if item.magic_defense < 0 else 1))
                + (item.defense / (2 if item.defense < 0 else 1))
                + min(20, item.speed / 2),
            )
            + 10 * len(item.status_immunities)
            + 15 * len(item.elemental_immunities)
            + 7.5 * len(item.elemental_resistances)
            + 50 * (1 if item.prevent_ko else 0)
            + 30 * len(item.temp_buffs)
        )
        return rank

    # Get all equipment and sort by rank
    all_equipment = [
        i for i in world.items.items if isinstance(i, (Weapon, Armor, Accessory))
    ]
    world.equipment_ranks = [(type(e), calc_equip_rank(e)) for e in all_equipment]
    world.equipment_ranks.sort(key=lambda x: x[1], reverse=True)

    # Categorize equipment: top 20% = highest, next 30% = high, bottom 50% = low
    total_equip = len(world.equipment_ranks)
    highest_cutoff = int(total_equip * 0.2)
    high_cutoff = int(total_equip * 0.5)

    from ...types.gameworld import GameWorld as GW

    world.highest_impact_equip = [
        e[0]
        for e in world.equipment_ranks[:highest_cutoff]
        if not (
            world.settings.isflag_enabled(RestrictSpecialEquips)
            and GW.is_monstro_item(e[0])
        )
        and not (
            GW.is_remake_item(e[0])
            and not world.settings.isflag_enabled(Remake)
        )
    ]
    world.high_impact_equip = [
        e[0]
        for e in world.equipment_ranks[highest_cutoff:high_cutoff]
        if not (
            world.settings.isflag_enabled(RestrictSpecialEquips)
            and GW.is_monstro_item(e[0])
        )
        and not (
            GW.is_remake_item(e[0])
            and not world.settings.isflag_enabled(Remake)
        )
    ]
    world.low_impact_equip = [
        e[0]
        for e in world.equipment_ranks[high_cutoff:]
        if not (
            world.settings.isflag_enabled(RestrictSpecialEquips)
            and GW.is_monstro_item(e[0])
        )
        and not (
            GW.is_remake_item(e[0])
            and not world.settings.isflag_enabled(Remake)
        )
    ]


def build_item_to_prize_mapping(world: GameWorld) -> None:
    """Build a mapping from item classes to their corresponding prize classes.

    Iterates through all ItemPrize subclasses and creates a reverse mapping
    from their `item` attribute to the prize class itself.
    """
    from ...types.prize import ItemPrize

    world.item_to_prize = {}

    def get_all_subclasses(cls: type) -> list[type]:
        """Recursively get all subclasses of a class."""
        subclasses = []
        for subclass in cls.__subclasses__():
            subclasses.append(subclass)
            subclasses.extend(get_all_subclasses(subclass))
        return subclasses

    for prize_class in get_all_subclasses(ItemPrize):
        if hasattr(prize_class, "item") and prize_class.item is not None:
            world.item_to_prize[prize_class.item] = prize_class
