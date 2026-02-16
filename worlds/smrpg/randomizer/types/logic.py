from .prize import Prize


class Inventory(list[Prize]):
    """A list of items, boss fights, spells, and characters the player is assumed
    to have collected."""

    # Lazy type cache - built on demand, invalidated when inventory changes
    _type_cache: set[type] | None

    def __init__(self, items=None):
        """Initialize inventory with optional items."""
        super().__init__(items or [])
        self._type_cache = None  # Instance-level cache

    def _get_type_cache(self) -> set[type]:
        """Get or build the type cache for O(1) has_item checks."""
        if self._type_cache is None:
            self._type_cache = set()
            for item in self:
                # Add item's type and all parent types for isinstance compatibility
                for cls in type(item).__mro__:
                    if cls is object:
                        break
                    self._type_cache.add(cls)
        return self._type_cache

    def _invalidate_cache(self):
        """Mark type cache as dirty."""
        self._type_cache = None

    def extend(self, items) -> None:
        """Extend list and invalidate cache."""
        super().extend(items)
        self._invalidate_cache()

    def append(self, item) -> None:
        """Append item and invalidate cache."""
        super().append(item)
        self._invalidate_cache()

    def remove(self, item) -> None:
        """Remove item and invalidate cache."""
        super().remove(item)
        self._invalidate_cache()

    def has_item_count(self, item_type: type[Prize], value=1):
        """The amount of a given item class collected."""
        # Quick check: if type not in cache, count is 0
        if item_type not in self._get_type_cache():
            return value <= 0
        count = sum(1 for item in self if isinstance(item, item_type))
        return count >= value

    def has_item(self, item_type: type[Prize]):
        """Returns true if at least one of the given class is collected."""
        return item_type in self._get_type_cache()

    def has_one_of(self, item_types: list[type[Prize]]):
        """Returns true of at least one of any of the given classes is collected."""
        cache = self._get_type_cache()
        return any(t in cache for t in item_types)

    def get_items_of_type(self, item_type: type[Prize]) -> list[Prize]:
        """Returns a list of all items of the given type in the inventory."""
        # Quick check: if type not in cache, return empty
        if item_type not in self._get_type_cache():
            return []
        return [item for item in self if isinstance(item, item_type)]

    def get_item(self, item_type: type[Prize]) -> Prize | None:
        """Returns the first item of the given type in the inventory, or None if not found."""
        # Quick check: if type not in cache, return None
        if item_type not in self._get_type_cache():
            return None
        return next((item for item in self if isinstance(item, item_type)), None)