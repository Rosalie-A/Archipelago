from enum import Enum
from smrpgpatchbuilder.datatypes.allies.ally import Ally as AllyBase, LevelUp, AllyCoordinate


class SpriteAnimationState(str, Enum):
    """Enum of sprite animation states for playable characters.

    These represent specific animation frames/sequences that can be used
    in overworld event scripts.
    """

    SOUTH = "south"
    DEFEND = "defend"
    FACE_NORTH = "face_north"
    FACE_SOUTH = "face_south"
    SHOCKED_LOOP = "shocked_loop"
    SHOCKED_LOOP_BACKWARDS = "shocked_loop_backwards"
    SHOCKED_BACKWARDS_SEQUENCE = "shocked_backwards_sequence"
    SHOCKED_SHADOW = "shocked_shadow"
    SHOCKED_SHADOW_BACKWARDS = "shocked_shadow_backwards"
    CRYING = "crying"
    CRYING_BACKWARDS = "crying_backwards"
    LOOKING_DOWN_STATIC = "looking_down_static"
    LOOKING_DOWN = "looking_down"
    LOOKING_DOWN_AWAY = "looking_down_away"
    FLOORED = "floored"
    HURT = "hurt"
    SHAKING_HEAD = "shaking_head"
    SHAKING_HEAD_BACKWARD = "shaking_head_backward"
    SLEEPING = "sleeping"
    SALUTE = "salute"
    JOY = "joy"
    JOY_BEHIND = "joy_behind"
    JOY_JUMP = "joy_jump"
    JOY_JUMP_BEHIND = "joy_jump_behind"
    LAUGHING = "laughing"
    LAUGHING_BACKWARDS = "laughing_backwards"
    DISTRACTED = "distracted"
    DISPLEASED = "displeased"
    CHALLENGE = "challenge"
    LOOK_TO_SIDE = "look_to_side"
    LOOK_TO_DOWN = "look_to_down"
    LOOK_TO_SIDE_BEHIND = "look_to_side_behind"
    CAST_FRAME_1 = "cast_frame_1"
    CAST_FRAME_2 = "cast_frame_2"
    CAST_FRAME_3 = "cast_frame_3"
    CAST_FRAME_4 = "cast_frame_4"
    LOOK_UP_SLIGHTLY = "look_up_slightly"
    LOOK_WAY_UP = "look_way_up"
    VICTORY_POSE = "victory_pose"
    VICTORY_STATIC = "victory_static"
    PRINCE_NEUTRAL = "prince_neutral"
    PRINCE_DOWN = "prince_down"
    PRINCE_LEFT = "prince_left"
    PRINCE_JOY = "prince_joy"
    HAMMER = "hammer"
    HAMMER_STATIC = "hammer_static"
    # Extra sprite actions (merged from ExtraSpriteActions)
    SWIM = "swim"
    WHIRL = "whirl"
    RECOIL = "recoil"
    SURPRISE_FRAME = "surprise_frame"
    SURPRISE_FRAME_BACK = "surprise_frame_back"
    STANDING_SLEEP = "standing_sleep"
    LEAN_BACK = "lean_back"
    LEAN_BACK_2 = "lean_back_2"
    LEAN_FORWARD = "lean_forward"
    DOWN_PIPE = "down_pipe"
    PRAISE_FRONT = "praise_front"
    PRAISE_BACK = "praise_back"
    DISPLEASED_FRONT = "displeased_front"
    DISPLEASED_BACK = "displeased_back"
    TUMBLE_FRONT = "tumble_front"
    TUMBLE_BACK = "tumble_back"
    EXOR = "exor"
    CHALLENGE_NIMBUS = "challenge_nimbus"
    CROUCH = "crouch"
    YOSHI = "yoshi"
    CLIMB = "climb"
    CLIMB_FRAME = "climb_frame"
    BLACKJACK = "blackjack"
    FLOP = "flop"
    DIZZY = "dizzy"
    WOBBLE = "wobble"
    SLEEP = "sleep"
    HOLD_STAR = "hold_star"
    LOOK_AT_DOLL = "look_at_doll"
    MUTE = "mute"


class Ally(AllyBase):
    """Extended Ally class with _sprites_primary and _sprites_secondary support."""

    def __init__(
        self,
        *args,
        _sprites_primary: dict[SpriteAnimationState, tuple[int, int, bool]] | None = None,
        _sprites_secondary: dict[SpriteAnimationState, tuple[int, int, bool]] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._sprites_primary = _sprites_primary or {}
        self._sprites_secondary = _sprites_secondary or {}