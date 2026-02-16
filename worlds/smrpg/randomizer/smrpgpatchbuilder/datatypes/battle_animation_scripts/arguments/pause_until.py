"""Int subclass instances representing the behaviour of a script pause."""

from .types.classes import PauseUntil

UNKNOWN_PAUSE_1 = PauseUntil(0x01)
UNKNOWN_PAUSE_2 = PauseUntil(0x02)
UNKNOWN_PAUSE_4 = PauseUntil(0x04)
SPRITE_SHIFT_COMPLETE = PauseUntil(6)
UNKNOWN_PAUSE_7 = PauseUntil(0x07)
BUTTON_PRESSED = PauseUntil(8)
FRAMES_ELAPSED = PauseUntil(0x10)
SEQ_4BPP_COMPLETE = bytearray([0x04, 0x00])
SEQ_2BPP_COMPLETE = bytearray([0x08, 0x00])
FADE_IN_COMPLETE = bytearray([0x00, 0x02])
FADE_4BPP_COMPLETE = bytearray([0x00, 0x04])
FADE_2BPP_COMPLETE = bytearray([0x00, 0x08])
