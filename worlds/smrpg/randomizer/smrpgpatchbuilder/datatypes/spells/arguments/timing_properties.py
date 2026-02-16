"""Int subclass instances representing the different timed hit functionality presets."""

from .types.classes import TimingProperties

ONE_TIMING_FOR_125_OR_15X_DMG = TimingProperties(0xCB0E)
MULTIPLE_BUTTON_PRESSES = TimingProperties(0xCBD8)
ONE_PLUS_MORE_TARGETS_WITH_PRESSES = TimingProperties(0xCC44)
ONE_TIMING_FOR_125_DMG_ONLY = TimingProperties(0xCD1E)
ROTATE_1_TARGET_IF_TIMED_ALL = TimingProperties(0xCD3F)
TIMED_HEALS_ALL_HP_TO_FIRST_TARGET = TimingProperties(0xCDA2)
BUTTON_MASH = TimingProperties(0xCDE1)
ROTATE_ONLY = TimingProperties(0xCE75)
CHARGE_ONLY = TimingProperties(0xCE85)
TIMED_GIVES_TARGET_DEFENSE_UP_BUFF = TimingProperties(0xCF22)
TIMED_FOR_9999_SET_ENEMY_HP_0 = TimingProperties(0xCF63)
TIME_TO_ACTIVATE_HP_READ = TimingProperties(0xCFC2)
TIMED_JUMPS = TimingProperties(0xCFDF)
