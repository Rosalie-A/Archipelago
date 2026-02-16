"""Base classes shared across type modules to avoid circular imports."""

from enum import StrEnum, Enum


class CategorizationOption(StrEnum):
    """Base class for categorization options used in flags.

    Use this for options that are simple string choices (e.g., SelectOneFlag).
    """
    pass


class ClassCategorizationOption(Enum):
    """Base class for categorization options that reference class types.

    Use this when you need to access class properties from enabled options.
    The enum values should be class types, not strings.
    """
    pass
