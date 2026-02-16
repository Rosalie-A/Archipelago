"""Shop shuffling logic."""

from __future__ import annotations
import random
from typing import TYPE_CHECKING, cast

from ...data.variables.dialog_names import *
from ...types.item import Item
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import SetVarToConst

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.items.classes import Item as BaseItem


def shuffle_shops(world: GameWorld) -> None:
    """Shuffle the contents of all shops based on settings."""
    from smrpgpatchbuilder.datatypes.items.classes import Weapon, Armor, Accessory
    from ...data.items.items import (
        GoodieBagItem,
        PickMeUpItem,
        MushroomItem,
        MidMushroomItem,
        MaxMushroomItem,
        HoneySyrupItem,
        MapleSyrupItem,
        AbleJuiceItem,
        BracerItem,
        EnergizerItem,
        YoshiCookieItem,
        PureWaterItem,
        YoshiCandyItem,
        FroggieDrinkItem,
        MukuCookieItem,
        ElixirItem,
        FreshenUpItem,
        MushroomItem2,
        YoshiAdeItem,
        RedEssenceItem,
        KerokeroColaItem,
        MegalixirItem,
        RockCandyItem,
        CrystallineItem,
        PowerBlastItem,
        RoyalSyrupItem,
        IceBombItem,
        FireBombItem,
        SleepyBombItem,
        FrightBombItem,
        BadMushroomItem,
        # Original Frog Disciple items
        SeeYaItem,
        EarlierTimesItem,
        ExpBoosterItem,
        CoinTrickItem,
        ScroogeRingItem,
    )
    from ...types.flags import (
        ShopQuality,
        ShopQualities,
        BiasShopShuffle,
        NoPickMeUps,
        FreeShops,
        SeaGate,
        SeaGating,
        MonstroTownGate,
        MonstroTownGating,
        BarrelVolcanoGate,
        BarrelVolcanoGating,
        NimbusGate,
        NimbusGating,
        BowsersKeepGate,
        BowsersKeepGating,
    )
    from ...data.shops.shops import (
        SH03_FROG_DISCIPLE,
        SH06_FROG_COIN_EMPORIUM,
        SH07_SEA_AND_SHIP_SHAMAN,
        SH08_SEASIDE_TOWN_MINION,
        SH09_JUICE_BAR_BASE,
        SH10_JUICE_BAR_ALTO,
        SH11_JUICE_BAR_TENOR,
        SH12_JUICE_BAR_SOPRANO,
        SH13_SEASIDE_WEAPON,
        SH14_SEASIDE_ARMOR,
        SH15_SEASIDE_ACCESSORY,
        SH16_SEASIDE_HEALTH_FOOD,
        SH17_MONSTRO,
        SH18_VOLCANO_ITEM,
        SH19_VOLCANO_ARMOR,
        SH20_GOOMBETTE,
        SH21_NIMBUS_LAND,
        SH22_KEEP_1,
        SH23_KEEP_2,
        SH24_FACTORY_TOAD,
    )
    from ...progression.prizelocations import (
        FrogDiscipleLocation1,
        FrogDiscipleLocation2,
        FrogDiscipleLocation3,
        FrogDiscipleLocation4,
        FrogDiscipleLocation5,
    )

    quality = world.settings.get_flag(ShopQuality).selected
    bias_enabled = world.settings.isflag_enabled(BiasShopShuffle)
    no_pickmeups = world.settings.isflag_enabled(NoPickMeUps)
    free_shops = world.settings.isflag_enabled(FreeShops)

    # Define shop indices for special handling
    FROG_DISCIPLE_SHOP = SH03_FROG_DISCIPLE
    FROG_COIN_EMPORIUM = SH06_FROG_COIN_EMPORIUM
    JUICE_BAR_BASE = SH09_JUICE_BAR_BASE
    JUICE_BAR_ALTO = SH10_JUICE_BAR_ALTO
    JUICE_BAR_TENOR = SH11_JUICE_BAR_TENOR
    JUICE_BAR_SOPRANO = SH12_JUICE_BAR_SOPRANO

    # Original frog coin shop items (vanilla items sold in frog coin shops)
    # Used for price adjustment logic
    ORIGINAL_FROG_COIN_ITEMS: set[type[BaseItem]] = {
        # Frog Disciple (buy_frog_coin_one=True)
        SeeYaItem,
        EarlierTimesItem,
        ExpBoosterItem,
        CoinTrickItem,
        ScroogeRingItem,
        # Frog Coin Emporium (buy_frog_coin=True)
        SleepyBombItem,
        BracerItem,
        EnergizerItem,
        CrystallineItem,
        PowerBlastItem,
    }

    # Get the items from Frog Disciple prize locations (already shuffled)
    frog_disciple_items: list[type[BaseItem] | None] = []
    frog_disciple_locations = [
        FrogDiscipleLocation1,
        FrogDiscipleLocation2,
        FrogDiscipleLocation3,
        FrogDiscipleLocation4,
        FrogDiscipleLocation5,
    ]
    for loc_type in frog_disciple_locations:
        loc = world.locations.get(loc_type)
        if loc and loc.prize:
            # Get the item type from the prize
            from ...types.prize import ItemPrize

            if isinstance(loc.prize, ItemPrize):
                prize_item = loc.prize.item
                if prize_item:
                    frog_disciple_items.append(prize_item)

    # Set Frog Disciple shop contents (don't shuffle into it)
    world.shops.shops[FROG_DISCIPLE_SHOP].set_items(frog_disciple_items)

    # Define should_get_better_items shops
    should_get_better_items = [
        SH06_FROG_COIN_EMPORIUM,
        SH08_SEASIDE_TOWN_MINION,
        SH11_JUICE_BAR_TENOR,
        SH12_JUICE_BAR_SOPRANO,
        SH13_SEASIDE_WEAPON,
        SH14_SEASIDE_ARMOR,
        SH15_SEASIDE_ACCESSORY,
        SH16_SEASIDE_HEALTH_FOOD,
        SH23_KEEP_2,
        SH24_FACTORY_TOAD,
    ]
    if not world.settings.is_flag_value(SeaGate, SeaGating.OPEN):
        should_get_better_items.append(SH07_SEA_AND_SHIP_SHAMAN)
    if not world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
        should_get_better_items.extend([SH17_MONSTRO, SH20_GOOMBETTE])
    if not world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
        should_get_better_items.extend([SH18_VOLCANO_ITEM, SH19_VOLCANO_ARMOR])
    if world.settings.is_flag_value(NimbusGate, NimbusGating.MEGASMILAX):
        should_get_better_items.append(SH21_NIMBUS_LAND)
    if not world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
        should_get_better_items.extend([SH22_KEEP_1])

    # Use class-level item impact categories (built by build_item_impact_categories)
    low_impact_items = world.low_impact_items
    high_impact_items = world.high_impact_items
    highest_impact_items = world.highest_impact_items
    low_impact_equip = world.low_impact_equip
    high_impact_equip = world.high_impact_equip
    highest_impact_equip = world.highest_impact_equip

    # Get original shop item types for each shop (for type restrictions)
    original_shop_data: dict[int, dict] = {}
    # Track how many shops each item originally appeared in (for ORIGINAL mode)
    original_item_shop_count: dict[type[BaseItem], int] = {}
    for shop in world.shops.shops:
        if shop is None:
            continue
        orig_items = [i for i in shop.items if i is not None]
        original_shop_data[shop.index] = {
            "has_weapon": any(issubclass(i, Weapon) for i in orig_items),
            "has_armor": any(issubclass(i, Armor) for i in orig_items),
            "has_accessory": any(issubclass(i, Accessory) for i in orig_items),
            "has_consumable": any(
                not issubclass(i, (Weapon, Armor, Accessory)) for i in orig_items
            ),
            "original_items": orig_items,
            "original_count": len(orig_items),
        }
        # Count shops per item (excluding Frog Disciple as those are handled separately)
        if shop.index != FROG_DISCIPLE_SHOP:
            for item in orig_items:
                original_item_shop_count[item] = (
                    original_item_shop_count.get(item, 0) + 1
                )

    # Track how many shops each item has been placed in during shuffling
    current_item_shop_count: dict[type[BaseItem], int] = {}

    # Handle EMPTY mode: only GoodieBag in every shop
    if quality == ShopQualities.EMPTY:
        for shop in world.shops.shops:
            if shop is None:
                continue
            shop.set_items([GoodieBagItem])
        return

    # Build item pools based on quality setting
    def get_item_pool(
        quality: ShopQualities, is_equipment: bool = False
    ) -> tuple[list, list, list]:
        """Returns (low, high, highest) pools based on quality."""
        if is_equipment:
            if quality == ShopQualities.ORIGINAL:
                # Only equipment that was originally in shops
                orig_equip_in_shops: set = set()
                for shop in world.shops.shops:
                    if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                        continue
                    for item in shop.items:
                        if item and issubclass(item, (Weapon, Armor, Accessory)):
                            orig_equip_in_shops.add(item)
                return (
                    [e for e in low_impact_equip if e in orig_equip_in_shops],
                    [e for e in high_impact_equip if e in orig_equip_in_shops],
                    [e for e in highest_impact_equip if e in orig_equip_in_shops],
                )
            elif quality == ShopQualities.MOSTLY_RANDOM:
                return (low_impact_equip, high_impact_equip, [])
            else:  # COMPLETELY_RANDOM
                return (low_impact_equip, high_impact_equip, highest_impact_equip)
        else:
            if quality == ShopQualities.ORIGINAL:
                # Only consumables that were originally in shops
                orig_in_shops: set = set()
                for shop in world.shops.shops:
                    if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                        continue
                    for item in shop.items:
                        if item and not issubclass(item, (Weapon, Armor, Accessory)):
                            orig_in_shops.add(item)
                return (
                    [i for i in low_impact_items if i in orig_in_shops],
                    [i for i in high_impact_items if i in orig_in_shops],
                    [i for i in highest_impact_items if i in orig_in_shops],
                )
            elif quality == ShopQualities.MOSTLY_RANDOM:
                return (low_impact_items, high_impact_items, [])
            else:  # COMPLETELY_RANDOM
                return (low_impact_items, high_impact_items, highest_impact_items)

    low_consumables, high_consumables, highest_consumables = get_item_pool(
        quality, is_equipment=False
    )
    low_equip, high_equip, highest_equip = get_item_pool(quality, is_equipment=True)

    # Remove Pick Me Ups if setting enabled
    if no_pickmeups:
        low_consumables = [i for i in low_consumables if i != PickMeUpItem]
        high_consumables = [i for i in high_consumables if i != PickMeUpItem]
        highest_consumables = [i for i in highest_consumables if i != PickMeUpItem]

    # Track items placed in Frog Coin Emporium (cannot appear elsewhere)
    frog_emporium_items: set = set()
    # Track items placed in Frog Disciple (can only also appear in Frog Coin Emporium)
    frog_disciple_set = set(frog_disciple_items)

    def can_place_item(
        item_type: type[BaseItem] | None, shop_idx: int, current_items: list
    ) -> bool:
        """Check if an item can be placed in a shop."""
        if item_type is None:
            return False
        # No duplicates in same shop
        if item_type in current_items:
            return False
        # Items in Frog Coin Emporium can't appear elsewhere
        if item_type in frog_emporium_items and shop_idx != FROG_COIN_EMPORIUM:
            return False
        # Items in Frog Disciple can only also appear in Frog Coin Emporium
        if item_type in frog_disciple_set and shop_idx not in [
            FROG_DISCIPLE_SHOP,
            FROG_COIN_EMPORIUM,
        ]:
            return False
        # In ORIGINAL mode, items can't appear in more shops than they originally did
        if quality == ShopQualities.ORIGINAL:
            max_shops = original_item_shop_count.get(item_type, 0)
            current_shops = current_item_shop_count.get(item_type, 0)
            if current_shops >= max_shops:
                return False
        # Check type restrictions
        shop_data = original_shop_data.get(shop_idx, {})
        if issubclass(item_type, Weapon) and not shop_data.get("has_weapon", False):
            return False
        if issubclass(item_type, Armor) and not shop_data.get("has_armor", False):
            return False
        if issubclass(item_type, Accessory) and not shop_data.get(
            "has_accessory", False
        ):
            return False
        if not issubclass(item_type, (Weapon, Armor, Accessory)) and not shop_data.get(
            "has_consumable", False
        ):
            return False
        return True

    def select_item(
        shop_idx: int, current_items: list, prefer_high: bool = False
    ) -> type[BaseItem] | None:
        """Select an item for a shop based on bias and availability."""
        is_better_shop = shop_idx in should_get_better_items

        # Build weighted pool
        candidates = []
        weights = []

        # Combine consumables and equipment pools
        all_low = low_consumables + low_equip
        all_high = high_consumables + high_equip
        all_highest = highest_consumables + highest_equip

        if bias_enabled:
            if is_better_shop:
                # Better shops: favor high/highest impact
                for item in all_highest:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(5)
                for item in all_high:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(3)
                for item in all_low:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(1)
            else:
                # Other shops: favor low impact
                for item in all_low:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(5)
                for item in all_high:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(1)
                # Significantly less likely for highest
                for item in all_highest:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(0.2)
        else:
            # No bias: equal weights
            for item in all_low + all_high + all_highest:
                if can_place_item(item, shop_idx, current_items):
                    candidates.append(item)
                    weights.append(1)

        if not candidates:
            return None

        return random.choices(candidates, weights=weights, k=1)[0]

    # Process each shop (except Frog Disciple which is already set)
    shops_to_process = [
        s for s in world.shops.shops if s is not None and s.index != FROG_DISCIPLE_SHOP
    ]

    # Process Frog Coin Emporium first (its items are exclusive)
    frog_emporium_shop = world.shops.shops[FROG_COIN_EMPORIUM]
    if frog_emporium_shop:
        shop_data = original_shop_data.get(FROG_COIN_EMPORIUM, {})
        target_count = min(15, max(1, shop_data.get("original_count", 5)))
        emporium_new_items: list[type[BaseItem] | None] = []

        for _ in range(target_count):
            item = select_item(FROG_COIN_EMPORIUM, emporium_new_items, prefer_high=True)
            if item:
                emporium_new_items.append(item)
                frog_emporium_items.add(item)
                # Track shop count for ORIGINAL mode
                current_item_shop_count[item] = current_item_shop_count.get(item, 0) + 1

        frog_emporium_shop.set_items(emporium_new_items)

    # Handle Juice Bar hierarchy (BASE < ALTO < TENOR < SOPRANO)
    # Items cascade upward: BASE items appear in all, ALTO items appear in ALTO+TENOR+SOPRANO, etc.
    juice_bars = [
        JUICE_BAR_BASE,
        JUICE_BAR_ALTO,
        JUICE_BAR_TENOR,
        JUICE_BAR_SOPRANO,
    ]
    juice_bar_max_items = {
        JUICE_BAR_BASE: 12,
        JUICE_BAR_ALTO: 13,
        JUICE_BAR_TENOR: 14,
        JUICE_BAR_SOPRANO: 15,
    }
    juice_bar_items: dict[int, list[type[BaseItem] | None]] = {
        bar: [] for bar in juice_bars
    }

    def add_to_juice_bar_cascade(item: type[BaseItem], starting_tier: int) -> bool:
        """Add item to starting_tier and all higher tiers (if they have room).
        Returns True if item was added to at least the starting tier."""
        # In ORIGINAL mode, check if adding to cascade would exceed the limit
        if quality == ShopQualities.ORIGINAL:
            # Count how many juice bar tiers we would add this item to
            shops_to_add = 0
            for i in range(starting_tier, len(juice_bars)):
                bar_idx = juice_bars[i]
                max_items = juice_bar_max_items[bar_idx]
                items_list = juice_bar_items[bar_idx]
                if len(items_list) < max_items and item not in items_list:
                    shops_to_add += 1

            # Check if adding would exceed the original limit
            max_shops = original_item_shop_count.get(item, 0)
            current_shops = current_item_shop_count.get(item, 0)
            if current_shops + shops_to_add > max_shops:
                return False

        added_to_start = False
        shops_added = 0
        for i in range(starting_tier, len(juice_bars)):
            bar_idx = juice_bars[i]
            max_items = juice_bar_max_items[bar_idx]
            items_list = juice_bar_items[bar_idx]
            if len(items_list) < max_items and item not in items_list:
                items_list.append(item)
                shops_added += 1
                if i == starting_tier:
                    added_to_start = True

        # Track shop count for ORIGINAL mode
        if shops_added > 0:
            current_item_shop_count[item] = (
                current_item_shop_count.get(item, 0) + shops_added
            )

        return added_to_start

    # Fill each tier, cascading items to higher tiers
    for tier_idx, bar_idx in enumerate(juice_bars):
        shop = world.shops.shops[bar_idx]
        if shop is None:
            continue

        max_items = juice_bar_max_items[bar_idx]
        current_items = juice_bar_items[bar_idx]

        # Try to add items until we reach max capacity for this tier
        attempts = 0
        while len(current_items) < max_items and attempts < 100:
            item = select_item(bar_idx, current_items)
            if item and item not in current_items:
                add_to_juice_bar_cascade(item, tier_idx)
            attempts += 1

    # Set items for each juice bar shop
    for bar_idx in juice_bars:
        shop = world.shops.shops[bar_idx]
        if shop is not None:
            shop.set_items(juice_bar_items[bar_idx])

    # Process remaining shops
    processed = {FROG_DISCIPLE_SHOP, FROG_COIN_EMPORIUM} | set(juice_bars)
    for shop in shops_to_process:
        if shop.index in processed:
            continue

        shop_data = original_shop_data.get(shop.index, {})
        target_count = min(15, max(1, shop_data.get("original_count", 5)))
        shop_new_items: list[type[BaseItem] | None] = []

        for _ in range(target_count):
            item = select_item(shop.index, shop_new_items)
            if item:
                shop_new_items.append(item)
                # Track shop count for ORIGINAL mode
                current_item_shop_count[item] = current_item_shop_count.get(item, 0) + 1

        if shop_new_items:
            shop.set_items(shop_new_items)
        elif quality == ShopQualities.ORIGINAL:
            # If no items could be placed in ORIGINAL mode, discard
            shop.set_items([])

    # Guarantee Pick Me Ups appear in at least one shop if not disabled
    # In ORIGINAL mode, only guarantee if Pick Me Up was originally in at least one shop
    # and we haven't exceeded the original shop count
    can_guarantee_pickmeup = not no_pickmeups
    if can_guarantee_pickmeup and quality == ShopQualities.ORIGINAL:
        original_pickmeup_shops = original_item_shop_count.get(PickMeUpItem, 0)
        current_pickmeup_shops = current_item_shop_count.get(PickMeUpItem, 0)
        if (
            original_pickmeup_shops == 0
            or current_pickmeup_shops >= original_pickmeup_shops
        ):
            can_guarantee_pickmeup = False

    if can_guarantee_pickmeup:
        # Check if any shop contains Pick Me Up
        has_pickmeup = False
        for shop in world.shops.shops:
            if shop is not None and PickMeUpItem in (shop.items or []):
                has_pickmeup = True
                break

        if not has_pickmeup:
            # Find shops that can have consumables and have room
            eligible_shops = []
            for shop in world.shops.shops:
                if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                    continue
                shop_data = original_shop_data.get(shop.index, {})
                if shop_data.get("has_consumable", False):
                    current_items = shop.items or []
                    if len(current_items) < 15 and PickMeUpItem not in current_items:
                        eligible_shops.append(shop)

            if eligible_shops:
                target_shop = random.choice(eligible_shops)
                current_items: list[type[BaseItem] | None] = list(
                    target_shop.items or []
                )
                current_items.append(PickMeUpItem)
                target_shop.set_items(current_items)

    # Apply FreeShops: set all non-zero prices to 1
    if free_shops:
        for item in world.items.items:
            if item.price > 0:
                item.set_price(1)

    # Apply Frog Coin shop price adjustments (skip if FreeShops is enabled)
    if not free_shops:
        # Items that end up in frog coin shops (after shuffling)
        frog_coin_items = frog_disciple_set | frog_emporium_items

        # Case 1 & 2: Handle items currently in frog coin shops
        for item_type in frog_coin_items:
            if item_type is None:
                continue
            # If item was originally a frog coin item, don't reduce price (it's already frog-coin-priced)
            if item_type in ORIGINAL_FROG_COIN_ITEMS:
                continue
            # Non-original item going to frog coin shop: divide by 10
            item = world.items.get_by_type(item_type)
            if item and item.price > 0:
                item.set_price(max(1, item.price // 10))

        # Case 3: Handle original frog coin items that are NOT in frog coin shops anymore
        # These need their price multiplied (inverse operation) since they now cost coins
        for item_type in ORIGINAL_FROG_COIN_ITEMS:
            if item_type in frog_coin_items:
                # Still in a frog coin shop, no change needed
                continue
            # Original frog coin item moved to a regular shop: multiply by 10
            item = world.items.get_by_type(item_type)
            if item and item.price > 0:
                item.set_price(min(9999, item.price * 10))

    # Sort items in all shops: non-equippables (ID >= 96) first, then equippables, each group sorted by ID
    for shop in world.shops.shops:
        if shop is None:
            continue
        # Get current items, filter out None values
        current_items = [item for item in (shop.items or []) if item is not None]
        # Sort by: (0 if non-equippable else 1, item_id) - puts consumables/specials at top
        sorted_items = sorted(
            current_items,
            key=lambda item_type: (0 if item_type().item_id >= 96 else 1, item_type().item_id)  # type: ignore
        )
        # Set the sorted items back to the shop
        shop.set_items(sorted_items)

    # Room service menu
    lower_tier_items = [
        MushroomItem,
        MidMushroomItem,
        HoneySyrupItem,
        MapleSyrupItem,
        AbleJuiceItem,
        BracerItem,
        EnergizerItem,
        YoshiCookieItem,
        PureWaterItem,
        YoshiCandyItem,
        FroggieDrinkItem,
        MukuCookieItem,
        ElixirItem,
        FreshenUpItem,
        MushroomItem2,
    ]
    if not no_pickmeups:
        lower_tier_items.append(PickMeUpItem)
    higher_tier_items = [
        MaxMushroomItem,
        RoyalSyrupItem,
        YoshiAdeItem,
        RedEssenceItem,
        KerokeroColaItem,
        MegalixirItem,
        RockCandyItem,
        CrystallineItem,
        PowerBlastItem,
    ]

    low_item = cast(Item, world.get_item(random.choice(lower_tier_items)))
    high_item = cast(Item, world.get_item(random.choice(higher_tier_items)))

    # Store for spoiler log and cosmetic dialog updates
    world.room_service_items = [type(low_item), type(high_item)]

    # Update event script variables for room service prices and item IDs
    updates = zip(
        ["room_service_price_1_a", "room_service_price_1_b", "room_service_item_id_1",
         "room_service_price_2_a", "room_service_price_2_b", "room_service_item_id_2"],
        [low_item.room_service_price, low_item.room_service_price, type(low_item),
         high_item.room_service_price, high_item.room_service_price, type(high_item)]
    )
    for id, val in updates:
        cmd = world.event_scripts.get_command_by_identifier(id, SetVarToConst)
        var = cmd.address
        cmd.set_value_and_address(var, val)

    # Bomb trade shop
    bomb_pool = [
        IceBombItem,
        FireBombItem,
        SleepyBombItem,
        FrightBombItem,
        RockCandyItem,
        BadMushroomItem
    ]

    bi = [cast(Item, world.get_item(b)) for b in random.sample(bomb_pool, 3)]

    # Store for spoiler log and cosmetic dialog updates
    world.bomb_shop_items = [type(b) for b in bi]

    # Update event script variables for bomb shop item IDs
    bomb_updates = zip(
        ["bomb_shop_item_1", "bomb_shop_item_2", "bomb_shop_item_3"],
        [type(b) for b in bi]
    )
    for id, val in bomb_updates:
        cmd = world.event_scripts.get_command_by_identifier(id, SetVarToConst)
        var = cmd.address
        cmd.set_value_and_address(var, val)
    
    