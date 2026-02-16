"""Shop class for SMRPG shop data."""

from smrpgpatchbuilder.datatypes.items.classes import Item

# Constants
SHOP_BASE_ADDRESS = 0x3A44DF
TOTAL_SHOPS = 33
ITEMS_PER_SHOP = 15

class Shop:
    """A shop in Super Mario RPG."""

    _index: int
    _buy_frog_coin_one: bool
    _buy_frog_coin: bool
    _buy_only_a: bool
    _buy_only_b: bool
    _discount_6: bool
    _discount_12: bool
    _discount_25: bool
    _discount_50: bool
    _items: list[type[Item] | None]

    @property
    def index(self) -> int:
        """The shop's index (0-32)."""
        return self._index

    def set_index(self, index: int) -> None:
        """Set the shop's index."""
        assert 0 <= index < TOTAL_SHOPS, f"Shop index must be 0-{TOTAL_SHOPS-1}"
        self._index = index

    @property
    def buy_frog_coin_one(self) -> bool:
        """Buy with Frog Coins only once."""
        return self._buy_frog_coin_one

    def set_buy_frog_coin_one(self, value: bool) -> None:
        """Set whether items can be bought with Frog Coins only once."""
        self._buy_frog_coin_one = value

    @property
    def buy_frog_coin(self) -> bool:
        """Buy with Frog Coins."""
        return self._buy_frog_coin

    def set_buy_frog_coin(self, value: bool) -> None:
        """Set whether items can be bought with Frog Coins."""
        self._buy_frog_coin = value

    @property
    def buy_only_a(self) -> bool:
        """Buy only, no selling (flag A)."""
        return self._buy_only_a

    def set_buy_only_a(self, value: bool) -> None:
        """Set buy only flag A."""
        self._buy_only_a = value

    @property
    def buy_only_b(self) -> bool:
        """Buy only, no selling (flag B)."""
        return self._buy_only_b

    def set_buy_only_b(self, value: bool) -> None:
        """Set buy only flag B."""
        self._buy_only_b = value

    @property
    def discount_6(self) -> bool:
        """6% discount."""
        return self._discount_6

    def set_discount_6(self, value: bool) -> None:
        """Set 6% discount."""
        self._discount_6 = value

    @property
    def discount_12(self) -> bool:
        """12% discount."""
        return self._discount_12

    def set_discount_12(self, value: bool) -> None:
        """Set 12% discount."""
        self._discount_12 = value

    @property
    def discount_25(self) -> bool:
        """25% discount."""
        return self._discount_25

    def set_discount_25(self, value: bool) -> None:
        """Set 25% discount."""
        self._discount_25 = value

    @property
    def discount_50(self) -> bool:
        """50% discount."""
        return self._discount_50

    def set_discount_50(self, value: bool) -> None:
        """Set 50% discount."""
        self._discount_50 = value

    @property
    def items(self) -> list[type[Item] | None]:
        """The items sold in this shop (up to 15)."""
        return self._items

    def set_items(self, items: list[type[Item] | None]) -> None:
        """Set the items sold in this shop."""
        assert len(items) <= ITEMS_PER_SHOP, f"Shop can have at most {ITEMS_PER_SHOP} items"
        self._items = items
        # Pad to 15 items with None
        while len(self._items) < ITEMS_PER_SHOP:
            self._items.append(None)

    def __init__(
        self,
        index: int,
        items: list[type[Item] | None],
        buy_frog_coin_one: bool = False,
        buy_frog_coin: bool = False,
        buy_only_a: bool = False,
        buy_only_b: bool = False,
        discount_6: bool = False,
        discount_12: bool = False,
        discount_25: bool = False,
        discount_50: bool = False,
    ) -> None:
        """Initialize a Shop.

        Args:
            index: The shop's index (0-32)
            items: List of item classes sold in this shop (up to 15)
            buy_frog_coin_one: Buy with Frog Coins only once
            buy_frog_coin: Buy with Frog Coins
            buy_only_a: Buy only, no selling (flag A)
            buy_only_b: Buy only, no selling (flag B)
            discount_6: 6% discount
            discount_12: 12% discount
            discount_25: 25% discount
            discount_50: 50% discount
        """
        self.set_index(index)
        self.set_items(items)
        self.set_buy_frog_coin_one(buy_frog_coin_one)
        self.set_buy_frog_coin(buy_frog_coin)
        self.set_buy_only_a(buy_only_a)
        self.set_buy_only_b(buy_only_b)
        self.set_discount_6(discount_6)
        self.set_discount_12(discount_12)
        self.set_discount_25(discount_25)
        self.set_discount_50(discount_50)

    def render(self) -> dict[int, bytearray]:
        """Render the shop data to ROM format.

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching
        """

        assert len(self.items) <= ITEMS_PER_SHOP, f"Shop can have at most {ITEMS_PER_SHOP} items"
        
        offset = SHOP_BASE_ADDRESS + (self.index * 16)
        data = bytearray()

        # Build the flags byte
        flags_byte = 0
        if self.buy_frog_coin_one:
            flags_byte |= 0x01
        if self.buy_frog_coin:
            flags_byte |= 0x02
        if self.buy_only_a:
            flags_byte |= 0x04
        if self.buy_only_b:
            flags_byte |= 0x08
        if self.discount_6:
            flags_byte |= 0x10
        if self.discount_12:
            flags_byte |= 0x20
        if self.discount_25:
            flags_byte |= 0x40
        if self.discount_50:
            flags_byte |= 0x80

        data.append(flags_byte)

        # Add items (15 bytes)
        for item in self.items:
            if item is None:
                data.append(0xFF)  # 0xFF = no item
            else:
                data.append(item().item_id)

        return {offset: data}

class ShopCollection:
    """Collection of all shops in the game."""

    _shops: list[Shop]

    @property
    def shops(self) -> list[Shop]:
        """The list of 33 shops."""
        return self._shops

    def __init__(self, shops: list[Shop]) -> None:
        """Initialize a ShopCollection with exactly 33 shops.

        Args:
            shops: A list of exactly 33 Shop instances

        Raises:
            AssertionError: If not exactly 33 shops are provided
        """
        assert len(shops) == TOTAL_SHOPS, \
            f"ShopCollection requires exactly {TOTAL_SHOPS} shops, got {len(shops)}"
        self._shops = shops

    def render(self) -> dict[int, bytearray]:
        """Render all shops to ROM format.

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching
        """
        patch: dict[int, bytearray] = {}

        for shop in self._shops:
            shop_patch = shop.render()
            patch.update(shop_patch)

        return patch
