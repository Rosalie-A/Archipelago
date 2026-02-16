"""Individual battle animation script command classes.
These are the building blocks of battle animation scripts."""

from smrpgpatchbuilder.datatypes.enemies.classes import Enemy
from smrpgpatchbuilder.datatypes.numbers.classes import (
    Int16,
    Int8,
    UInt16,
    UInt8,
    UInt4,
)
from smrpgpatchbuilder.datatypes.sprites.ids.misc import TOTAL_SPRITES
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    InvalidCommandArgumentException,
    InvalidOpcodeException,
)

from smrpgpatchbuilder.utils.number import bits_to_int, bools_to_int

from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments import (
    BUTTON_PRESSED,
    FADE_2BPP_COMPLETE,
    FADE_4BPP_COMPLETE,
    FADE_IN_COMPLETE,
    FRAMES_ELAPSED,
    SEQ_2BPP_COMPLETE,
    SEQ_4BPP_COMPLETE,
    SPRITE_SHIFT_COMPLETE,
    UNKNOWN_PAUSE_1,
    UNKNOWN_PAUSE_2,
    UNKNOWN_PAUSE_4,
    UNKNOWN_PAUSE_7,
    WAVE_LAYER_BATTLEFIELD,
    WAVE_LAYER_HORIZONTAL,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.types import (
    BattleTarget,
    BonusMessage,
    FlashColour,
    MaskEffect,
    MaskPoint,
    PauseUntil,
    ShiftType,
    MessageType,
    LayerPriorityType,
    WaveEffectDirection,
    WaveEffectLayer,
)
from .types import (
    AnimationScriptAMEM6XSoloCommand,
    AnimationScriptAMEMAnd7E,
    AnimationScriptAMEMAnd7F,
    AnimationScriptAMEMAndAMEM,
    AnimationScriptAMEMAndConst,
    AnimationScriptAMEMAndOMEM,
    AnimationScriptAMEMCommand,
    AnimationScriptCommand,
    AnimationScriptCommandInventory,
    AnimationScriptCommandNoArgs,
    AnimationScriptCommandWithJmps,
    AnimationScriptFadeObject,
    AnimationScriptShakeObject,
    AnimationScriptUnknownJmp2X,
    SetAMEMToXYZCoords,
    UsableAnimationScriptCommand,
)

class NewSpriteAtCoords(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Draws a new sprite by absolute ID at the given coords with the given properties.

    ## Lazy Shell command
        `New object: sprite = {xx}, coords (AMEM $32)`

    ## Opcode
        `0x00`

    ## Size
        9 bytes

    Args:
        sprite_id (int): The ID of the sprite to draw.
        sequence (int): The sprite's specific sequence ID to run when drawn.
        priority (int): The sprite's graphic layer priority.
        vram_address (int): (unknown).
        palette_row (int): The sprite's palette row ID.
        overwrite_vram (bool): (unknown).
        looping (bool): Decides if the sprite sequence should loop.
        param_2_and_0x10 (bool): (unknown).
        overwrite_palette (bool): If drawing over an exiting sprite, decide if the palette should also be overwritten.
        mirror_sprite (bool): If true, the sprite will be drawn horizontally flipped.
        invert_sprite (bool): If true, the sprite will be drawn vertically flipped.
        behind_all_sprites (bool): If true, the sprite will be drawn behind all other sprites.
        overlap_all_sprites (bool): If true, the sprite will be drawn over all other sprites.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x00
    _size: int = 9

    _sprite_id: UInt16 = UInt16(0)
    _sequence: UInt4 = UInt4(0)
    _priority: UInt4 = UInt4(0)
    _vram_address: UInt16 = UInt16(0)
    _palette_row: UInt4 = UInt4(0)
    _overwrite_vram: bool = False
    _looping: bool = False
    _param_2_and_0x10: bool = False
    _overwrite_palette: bool = False
    _mirror_sprite: bool = False
    _invert_sprite: bool = False
    _behind_all_sprites: bool = False
    _overlap_all_sprites: bool = False

    @property
    def sprite_id(self) -> UInt16:
        """The ID of the sprite to draw."""
        return self._sprite_id

    def set_sprite_id(self, sprite_id: int) -> None:
        """Set the ID of the sprite to draw."""
        assert sprite_id < TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

    @property
    def sequence(self) -> UInt4:
        """The sprite's specific sequence ID to run when drawn."""
        return self._sequence

    def set_sequence(self, sequence: int) -> None:
        """Set the sprite's specific sequence ID to run when drawn."""
        self._sequence = UInt4(sequence)

    @property
    def priority(self) -> UInt4:
        """The sprite's graphic layer priority."""
        return self._priority

    def set_priority(self, priority: int) -> None:
        """Set the sprite's graphic layer priority."""
        assert priority <= 3
        self._priority = UInt4(priority)

    @property
    def vram_address(self) -> UInt16:
        """(unknown)."""
        return self._vram_address

    def set_vram_address(self, vram_address: int) -> None:
        """(unknown)."""
        self._vram_address = UInt16(vram_address)

    @property
    def palette_row(self) -> UInt4:
        """The sprite's palette row ID."""
        return self._palette_row

    def set_palette_row(self, palette_row: int) -> None:
        """Set the sprite's palette row ID."""
        self._palette_row = UInt4(palette_row)

    @property
    def overwrite_vram(self) -> bool:
        """(unknown)."""
        return self._overwrite_vram

    def set_overwrite_vram(self, overwrite_vram: bool) -> None:
        """(unknown)."""
        self._overwrite_vram = overwrite_vram

    @property
    def looping(self) -> bool:
        """Decides if the sprite sequence should loop."""
        return self._looping

    def set_looping(self, looping: bool) -> None:
        """Decide if the sprite sequence should loop."""
        self._looping = looping

    @property
    def param_2_and_0x10(self) -> bool:
        """(unknown)."""
        return self._param_2_and_0x10

    def set_param_2_and_0x10(self, param_2_and_0x10: bool) -> None:
        """(unknown)."""
        self._param_2_and_0x10 = param_2_and_0x10

    @property
    def overwrite_palette(self) -> bool:
        """If drawing over an exiting sprite, decide if the palette should also be overwritten."""
        return self._overwrite_palette

    def set_overwrite_palette(self, overwrite_palette: bool) -> None:
        """If drawing over an exiting sprite, decide if the palette should also be overwritten."""
        self._overwrite_palette = overwrite_palette

    @property
    def mirror_sprite(self) -> bool:
        """If true, the sprite will be drawn horizontally flipped."""
        return self._mirror_sprite

    def set_mirror_sprite(self, mirror_sprite: bool) -> None:
        """If true, the sprite will be drawn horizontally flipped."""
        self._mirror_sprite = mirror_sprite

    @property
    def invert_sprite(self) -> bool:
        """If true, the sprite will be drawn vertically flipped."""
        return self._invert_sprite

    def set_invert_sprite(self, invert_sprite: bool) -> None:
        """If true, the sprite will be drawn vertically flipped."""
        self._invert_sprite = invert_sprite

    @property
    def behind_all_sprites(self) -> bool:
        """If true, the sprite will be drawn behind all other sprites."""
        return self._behind_all_sprites

    def set_behind_all_sprites(self, behind_all_sprites: bool) -> None:
        """If true, the sprite will be drawn behind all other sprites."""
        self._behind_all_sprites = behind_all_sprites

    @property
    def overlap_all_sprites(self) -> bool:
        """If true, the sprite will be drawn over all other sprites."""
        return self._overlap_all_sprites

    def set_overlap_all_sprites(self, overlap_all_sprites: bool) -> None:
        """If true, the sprite will be drawn over all other sprites."""
        self._overlap_all_sprites = overlap_all_sprites

    def __init__(
        self,
        sprite_id: int,
        sequence: int,
        priority: int,
        vram_address: int,
        palette_row: int,
        overwrite_vram: bool = False,
        looping: bool = False,
        param_2_and_0x10: bool = False,
        overwrite_palette: bool = False,
        mirror_sprite: bool = False,
        invert_sprite: bool = False,
        behind_all_sprites: bool = False,
        overlap_all_sprites: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sprite_id(sprite_id)
        self.set_sequence(sequence)
        self.set_priority(priority)
        self.set_vram_address(vram_address)
        self.set_palette_row(palette_row)
        self.set_overwrite_vram(overwrite_vram)
        self.set_looping(looping)
        self.set_param_2_and_0x10(param_2_and_0x10)
        self.set_overwrite_palette(overwrite_palette)
        self.set_mirror_sprite(mirror_sprite)
        self.set_invert_sprite(invert_sprite)
        self.set_behind_all_sprites(behind_all_sprites)
        self.set_overlap_all_sprites(overlap_all_sprites)

    def render(self, *args) -> bytearray:
        byte1 = (
            (self.overwrite_vram * 0x01)
            + (self.behind_all_sprites * 0x40)
            + (self.overlap_all_sprites * 0x80)
        )
        byte2 = (
            (self.looping * 0x08)
            + (self.param_2_and_0x10 * 0x10)
            + (self.overwrite_palette * 0x20)
        )
        byte6 = (
            (self.priority << 4)
            + (self.mirror_sprite * 0x40)
            + (self.invert_sprite * 0x80)
            + self.palette_row
        )

        return super().render(
            byte1, byte2, self.sprite_id, self.sequence, byte6, self.vram_address
        )

class SetAMEM32ToXYZCoords(UsableAnimationScriptCommand, SetAMEMToXYZCoords):
    """Store XYZ coords of sprite to AMEM $32.

    ## Lazy Shell command
        `AMEM $32 = coords (x,y,z)`

    ## Opcode
        `0x01`

    ## Size
        8 bytes

    Args:
        origin (Origin): The point at which the x-y-z coords are relative to.
        x (int): Relative X coord (16 bit).
        y (int): Relative Y coord (16 bit).
        z (int): Relative Z coord (16 bit).
        do_set_x (bool): X coord will only be committed to AMEM if this is set to true.
        do_set_y (bool): Y coord will only be committed to AMEM if this is set to true.
        do_set_z (bool): Z coord will only be committed to AMEM if this is set to true.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x01

class DrawSpriteAtAMEM32Coords(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Draw sprite at XYZ coords stored at AMEM 32.

    ## Lazy Shell command
        `Sprite = {xx}, coords (AMEM $32)`

    ## Opcode
        `0x03`

    ## Size
        6 bytes

    Args:
        sprite_id (int): The ID of the sprite to draw.
        sequence (int): The sprite's specific sequence ID to run when drawn.
        store_to_vram (bool): (unknown).
        looping (bool): Decides if the sprite sequence should loop.
        store_palette (bool): (unknown).
        bit_4 (bool): (unknown).
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 6
    _opcode = 0x03

    _sprite_id: UInt16
    _sequence: UInt4
    _store_to_vram: bool
    _looping: bool
    _store_palette: bool
    _behind_all_sprites: bool
    _overlap_all_sprites: bool
    _bit_4: bool
    _bit_7: bool

    @property
    def sprite_id(self) -> UInt16:
        """The ID of the sprite to draw."""
        return self._sprite_id

    def set_sprite_id(self, sprite_id: int) -> None:
        """Sets the ID of the sprite to draw."""
        assert sprite_id < TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

    @property
    def sequence(self) -> UInt4:
        """The sprite's specific sequence ID to run when drawn."""
        return self._sequence

    def set_sequence(self, sequence: int) -> None:
        """Set the sprite's specific sequence ID to run when drawn."""
        self._sequence = UInt4(sequence)

    @property
    def store_to_vram(self) -> bool:
        """(unknown)."""
        return self._store_to_vram

    def set_store_to_vram(self, store_to_vram: bool) -> None:
        """(unknown)."""
        self._store_to_vram = store_to_vram

    @property
    def looping(self) -> bool:
        """Decides if the sprite sequence should loop."""
        return self._looping

    def set_looping(self, looping: bool) -> None:
        """Decide if the sprite sequence should loop."""
        self._looping = looping

    @property
    def behind_all_sprites(self) -> bool:
        """Decides if the sprite sequence should loop."""
        return self._behind_all_sprites

    def set_behind_all_sprites(self, behind_all_sprites: bool) -> None:
        """Decide if the sprite sequence should loop."""
        self._behind_all_sprites = behind_all_sprites

    @property
    def overlap_all_sprites(self) -> bool:
        """Decides if the sprite sequence should loop."""
        return self._overlap_all_sprites

    def set_overlap_all_sprites(self, overlap_all_sprites: bool) -> None:
        """Decide if the sprite sequence should loop."""
        self._overlap_all_sprites = overlap_all_sprites

    @property
    def store_palette(self) -> bool:
        """(unknown)."""
        return self._store_palette

    def set_store_palette(self, store_palette: bool) -> None:
        """(unknown)."""
        self._store_palette = store_palette

    @property
    def bit_4(self) -> bool:
        """(unknown)."""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)."""
        self._bit_4 = bit_4

    @property
    def bit_7(self) -> bool:
        """(unknown)."""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)."""
        self._bit_7 = bit_7

    def __init__(
        self,
        sprite_id: int,
        sequence: int,
        store_to_vram: bool = False,
        looping: bool = False,
        store_palette: bool = False,
        behind_all_sprites: bool = False,
        overlap_all_sprites: bool = False,
        bit_4: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sprite_id(sprite_id)
        self.set_sequence(sequence)
        self.set_store_to_vram(store_to_vram)
        self.set_looping(looping)
        self.set_store_palette(store_palette)
        self.set_behind_all_sprites(behind_all_sprites)
        self.set_overlap_all_sprites(overlap_all_sprites)
        self.set_bit_4(bit_4)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        byte1 = (
            self.store_to_vram * 0x01
            + self.behind_all_sprites * 0x40
            + self.overlap_all_sprites * 0x80
        )
        byte2 = (
            (self.looping * 0x08)
            + (self.store_palette * 0x20)
            + (self.bit_4 * 0x10)
            
        )
        return super().render(byte1, byte2, self.sprite_id, self.sequence + (self.bit_7 * 0x80))

class PauseScriptUntil(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Pause the active script until a certain condition is met.

    ## Lazy Shell command
        `Pause script until...`
        `Pause script until {xx} complete...`

    ## Opcode
        `0x04`
        `0x74`

    ## Size
        4 bytes or 3 bytes depending on the condition

    Args:
        condition (int | PauseUntil | bytearray): The condition that ends the pause.
        frames (int): The number of frames to pause for.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _condition: PauseUntil | bytearray
    _frames: UInt16

    @property
    def condition(self) -> PauseUntil | bytearray:
        """The condition that ends the pause."""
        return self._condition

    def set_condition(self, condition: int | PauseUntil | bytearray) -> None:
        """Set the condition that ends the pause."""
        if isinstance(condition, PauseUntil):
            self._size = 4
            self._opcode = 0x04
            self._condition = condition
        elif isinstance(condition, bytearray):
            self._size = 3
            self._opcode = 0x74
            self._condition = condition
        else:
            raise InvalidCommandArgumentException(
                f"invalid pause condition: {condition}"
            )

    @property
    def frames(self) -> UInt16:
        """The number of frames to pause for.
        Has no use if FRAMES_ELAPSED is not the condition."""
        return self._frames

    def set_frames(self, frames: int) -> None:
        """Set the number of frames to pause for.
        Has no use if FRAMES_ELAPSED is not the condition."""
        self._frames = UInt16(frames)

    def __init__(
        self,
        condition: int | PauseUntil | bytearray,
        frames: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_frames(frames)
        self.set_condition(condition)

    def render(self, *args) -> bytearray:
        if self.opcode == 0x04:
            return super().render(self.condition, self.frames)
        if self.opcode == 0x74:
            return super().render(self.condition)
        raise InvalidOpcodeException(f"invalid opcode {self.opcode}")

class RemoveObject(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Removes the sprite queue target from the scene entirely.

    ## Lazy Shell command
        `Remove object`

    ## Opcode
        `0x05`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x05

class ReturnObjectQueue(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """End object queue script.

    ## Lazy Shell command
        `Return object queue`

    ## Opcode
        `0x07`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x07

class MoveObject(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Move this object along the given axes.

    ## Lazy Shell command
        `Move object: speed = {xx}`

    ## Opcode
        `0x08`

    ## Size
        8 bytes

    Args:
        speed (int): Movement speed.
        start_position (int): Int value indicating start position. Applies to every selected axis.
        end_position (int): Int value indicating end position. Applies to every selected axis.
        apply_to_x (bool): If true, start/end values apply to X axis.
        apply_to_y (bool): If true, start/end values apply to Y axis.
        apply_to_z (bool): If true, start/end values apply to Z axis.
        should_set_start_position (bool): If true, provided start position will be used.
        should_set_end_position (bool): If true, provided end position will be used.
        should_set_speed (bool): Movement speed.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x08
    _size: int = 8

    _speed: Int16
    _start_position: Int16
    _end_position: Int16
    _apply_to_x: bool
    _apply_to_y: bool
    _apply_to_z: bool
    _should_set_start_position: bool
    _should_set_end_position: bool
    _should_set_speed: bool

    @property
    def speed(self) -> Int16:
        """Movement speed."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set movement speed."""
        self._speed = Int16(speed)

    @property
    def start_position(self) -> Int16:
        """Int value indicating start position. Applies to every selected axis."""
        return self._start_position

    def set_start_position(self, start_position: int) -> None:
        """Int value indicating start position. Applies to every selected axis."""
        self._start_position = Int16(start_position)

    @property
    def end_position(self) -> Int16:
        """Int value indicating end position. Applies to every selected axis."""
        return self._end_position

    def set_end_position(self, end_position: int) -> None:
        """Int value indicating end position. Applies to every selected axis."""
        self._end_position = Int16(end_position)

    @property
    def apply_to_x(self) -> bool:
        """If true, start/end values apply to X axis."""
        return self._apply_to_x

    def set_apply_to_x(self, apply_to_x: bool) -> None:
        """If true, start/end values apply to X axis."""
        self._apply_to_x = apply_to_x

    @property
    def apply_to_y(self) -> bool:
        """If true, start/end values apply to Y axis."""
        return self._apply_to_y

    def set_apply_to_y(self, apply_to_y: bool) -> None:
        """If true, start/end values apply to Y axis."""
        self._apply_to_y = apply_to_y

    @property
    def apply_to_z(self) -> bool:
        """If true, start/end values apply to Z axis."""
        return self._apply_to_z

    def set_apply_to_z(self, apply_to_z: bool) -> None:
        """If true, start/end values apply to Z axis."""
        self._apply_to_z = apply_to_z

    @property
    def should_set_start_position(self) -> bool:
        """If true, provided start position will be used."""
        return self._should_set_start_position

    def set_should_set_start_position(self, should_set_start_position: bool) -> None:
        """If true, provided start position will be used."""
        self._should_set_start_position = should_set_start_position

    @property
    def should_set_end_position(self) -> bool:
        """If true, provided end position will be used."""
        return self._should_set_end_position

    def set_should_set_end_position(self, should_set_end_position: bool) -> None:
        """If true, provided end position will be used."""
        self._should_set_end_position = should_set_end_position

    @property
    def should_set_speed(self) -> bool:
        """Movement speed."""
        return self._should_set_speed

    def set_should_set_speed(self, should_set_speed: bool) -> None:
        """Movement speed."""
        self._should_set_speed = should_set_speed

    def __init__(
        self,
        speed: int,
        start_position: int,
        end_position: int,
        apply_to_x: bool = False,
        apply_to_y: bool = False,
        apply_to_z: bool = False,
        should_set_start_position: bool = False,
        should_set_end_position: bool = False,
        should_set_speed: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_speed(speed)
        self.set_start_position(start_position)
        self.set_end_position(end_position)
        self.set_apply_to_x(apply_to_x)
        self.set_apply_to_y(apply_to_y)
        self.set_apply_to_z(apply_to_z)
        self.set_should_set_start_position(should_set_start_position)
        self.set_should_set_end_position(should_set_end_position)
        self.set_should_set_speed(should_set_speed)

    def render(self, *args) -> bytearray:
        byte1 = (
            (self.apply_to_z * 0x01)
            + (self.apply_to_y * 0x02)
            + (self.apply_to_x * 0x04)
            + (self.should_set_start_position * 0x20)
            + (self.should_set_end_position * 0x40)
            + (self.should_set_speed * 0x80)
        )
        return super().render(
            byte1,
            self.start_position,
            self.end_position,
            self.speed,
        )

class Jmp(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """A simple goto with no conditions.

    ## Lazy Shell command
        `Jump to address $xxxx`

    ## Opcode
        `0x09`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x09
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class Pause1Frame(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Pause for exactly one frame.

    ## Lazy Shell command
        `Pause script for 1 frame`

    ## Opcode
        `0x0A`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x0A

class SetAMEM40ToXYZCoords(UsableAnimationScriptCommand, SetAMEMToXYZCoords):
    """Store XYZ coords of sprite to AMEM $40.

    ## Lazy Shell command
        `AMEM $40 = coords (x,y,z)`

    ## Opcode
        `0x0B`

    ## Size
        8 bytes

    Args:
        origin (Origin): The point at which the x-y-z coords are relative to.
        x (int): Relative X coord (16 bit).
        y (int): Relative Y coord (16 bit).
        z (int): Relative Z coord (16 bit).
        do_set_x (bool): X coord will only be committed to AMEM if this is set to true.
        do_set_y (bool): Y coord will only be committed to AMEM if this is set to true.
        do_set_z (bool): Z coord will only be committed to AMEM if this is set to true.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x0B

class MoveSpriteToCoords(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Move sprite to coords stored at AMEM $40.

    ## Lazy Shell command
        `Move sprite to coords (AMEM $40)`

    ## Opcode
        `0x0C`

    ## Size
        6 bytes

    Args:
        shift_type (ShiftType): Describes the movement type (shift, transfer, etc).
        speed (int): Movement speed.
        arch_height (int): Is zero if the movement has no Z axis.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x0C
    _size: int = 6

    _shift_type: ShiftType
    _speed: Int16
    _arch_height: Int16

    @property
    def shift_type(self) -> ShiftType:
        """Describes the movement type (shift, transfer, etc)."""
        return self._shift_type

    def set_shift_type(self, shift_type: ShiftType) -> None:
        """Set the movement type."""
        self._shift_type = shift_type

    @property
    def speed(self) -> Int16:
        """Movement speed."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the movement speed."""
        self._speed = Int16(speed)

    @property
    def arch_height(self) -> Int16:
        """Is zero if the movement has no Z axis.
        Otherwise, this determines the jump height."""
        return self._arch_height

    def set_arch_height(self, arch_height: int) -> None:
        """Set to zero if the movement should have no Z axis.
        Otherwise, this determines the jump height."""
        self._arch_height = Int16(arch_height)

    def __init__(
        self,
        shift_type: ShiftType,
        speed: int,
        arch_height: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_shift_type(shift_type)
        self.set_speed(speed)
        self.set_arch_height(arch_height)

    def render(self, *args) -> bytearray:
        return super().render(self.shift_type, self.speed, self.arch_height)

class ResetTargetMappingMemory(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """(unknown).

    ## Lazy Shell command
        `Reset target mapping memory`

    ## Opcode
        `0x0E`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x0E

class ResetObjectMappingMemory(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """(unknown).

    ## Lazy Shell command
        `Reset object mapping memory`

    ## Opcode
        `0x0F`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x0F

class RunSubroutine(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """Launches the section of code beginning with this goto as a subroutine.

    ## Lazy Shell command
        `Jump to subroutine $xxxx`

    ## Opcode
        `0x10`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command where you want the subroutine to begin.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x10
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class ReturnSubroutine(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Ends code intended to be run as a subroutine.

    ## Lazy Shell command
        `Return subroutine`

    ## Opcode
        `0x11`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x11

class VisibilityOn(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Makes the object visible.

    ## Lazy Shell command
        `Visibility on`

    ## Opcode
        `0x1A`

    ## Size
        2 bytes

    Args:
        unknown_byte (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x1A
    _size: int = 2

    _unknown_byte: UInt8

    @property
    def unknown_byte(self) -> UInt8:
        """(unknown)"""
        return self._unknown_byte

    def set_unknown_byte(self, unknown_byte: int) -> None:
        """(unknown)"""
        self._unknown_byte = UInt8(unknown_byte)

    def __init__(self, unknown_byte: int = 0, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_unknown_byte(unknown_byte)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_byte)

class VisibilityOff(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Makes the object invisible.

    ## Lazy Shell command
        `Visibility off`

    ## Opcode
        `0x1B`

    ## Size
        2 bytes

    Args:
        unknown_byte (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x1B
    _size: int = 2

    _unknown_byte: UInt8

    @property
    def unknown_byte(self) -> UInt8:
        """(unknown)"""
        return self._unknown_byte

    def set_unknown_byte(self, unknown_byte: int) -> None:
        """(unknown)"""
        self._unknown_byte = UInt8(unknown_byte)

    def __init__(self, unknown_byte: int = 0, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_unknown_byte(unknown_byte)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_byte)

class SetAMEM8BitToConst(UsableAnimationScriptCommand, AnimationScriptAMEMAndConst):
    """Set 8bit AMEM $60-6F to the given const value.

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to compare AMEM against
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(self, amem: int, value: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits(), self.value)

class SetAMEM16BitToConst(SetAMEM8BitToConst):
    """Set 16bit AMEM $60-6F to the given const value.

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to perform the AND operation against
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class JmpIfAMEM8BitEqualsConst(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAndConst,
):
    """If 8bit AMEM $60-6F equals the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        value: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits(), self.value, *self.destinations)

class JmpIfAMEM16BitEqualsConst(JmpIfAMEM8BitEqualsConst):
    """If 16bit AMEM $60-6F equals the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEqualsConst(JmpIfAMEM8BitEqualsConst):
    """If 8bit AMEM $60-6F does not equal the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEqualsConst(JmpIfAMEM8BitEqualsConst):
    """If 16bit AMEM $60-6F does not equal the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThanConst(JmpIfAMEM8BitEqualsConst):
    """If 8bit AMEM $60-6F is less than the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThanConst(JmpIfAMEM8BitEqualsConst):
    """If 16bit AMEM $60-6F is less than the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThanConst(JmpIfAMEM8BitEqualsConst):
    """If 8bit AMEM $60-6F is NOT less than the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThanConst(JmpIfAMEM8BitEqualsConst):
    """If 16bit AMEM $60-6F is NOT less than the given const value, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitByConst(UsableAnimationScriptCommand, AnimationScriptAMEMAndConst):
    """Increase 8bit AMEM $60-6F by given const value.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(self, amem: int, value: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits(), self.value)

class IncAMEM16BitByConst(IncAMEM8BitByConst):
    """Increase 16bit AMEM $60-6F by given const value.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitByConst(IncAMEM8BitByConst):
    """Decrease 8bit AMEM $60-6F by given const value.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitByConst(IncAMEM8BitByConst):
    """Decrease 16bit AMEM $60-6F by given const value.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitTo7E1x(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7E):
    """Set 8bit AMEM $60-6F to value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x10 + self._amem_bits(), addr)

class SetAMEM16BitTo7E1x(SetAMEM8BitTo7E1x):
    """Set 16bit AMEM $60-6F to value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class Set7E1xToAMEM8Bit(SetAMEM8BitTo7E1x):
    """Set value stored at given $7Exxxx memory address to value stored at 8bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(
        self, address: int, amem: int, identifier: str | None = None
    ) -> None:
        super().__init__(amem, address, identifier)

class Set7E1xToAMEM16Bit(Set7E1xToAMEM8Bit):
    """Set value stored at given $7Exxxx memory address to value stored at 16bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEquals7E1x(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAnd7E,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        address: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x10 + self._amem_bits(), addr, *self.destinations)

class JmpIfAMEM16BitEquals7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEquals7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEquals7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 16bit AMEM $60-6F does not equal value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThan7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThan7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 16bit AMEM $60-6F is less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThan7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThan7E1x(JmpIfAMEM8BitEquals7E1x):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitBy7E1x(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7E):
    """Increase 8bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x10 + self._amem_bits(), addr)

class IncAMEM16BitBy7E1x(IncAMEM8BitBy7E1x):
    """Increase 16bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitBy7E1x(IncAMEM8BitBy7E1x):
    """Decrease 8bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitBy7E1x(IncAMEM8BitBy7E1x):
    """Decrease 16bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitTo7F(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7F):
    """Set 8bit AMEM $60-6F to value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x20 + self._amem_bits(), addr)

class SetAMEM16BitTo7F(SetAMEM8BitTo7F):
    """Set 16bit AMEM $60-6F to value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class Set7FToAMEM8Bit(SetAMEM8BitTo7F):
    """Set given $7Fxxxx memory address to value at 8bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(
        self, address: int, amem: int, identifier: str | None = None
    ) -> None:
        super().__init__(amem, address, identifier)

class Set7FToAMEM16Bit(Set7FToAMEM8Bit):
    """Set given $7Fxxxx memory address to value at 16bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEquals7F(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAnd7F,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        address: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x20 + self._amem_bits(), addr, *self.destinations)

class JmpIfAMEM16BitEquals7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEquals7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEquals7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 16bit AMEM $60-6F does not equal value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThan7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThan7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 16bit AMEM $60-6F is less than value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThan7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThan7F(JmpIfAMEM8BitEquals7F):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitBy7F(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7F):
    """Increase 8bit AMEM $60-6F by value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x20 + self._amem_bits(), addr)

class IncAMEM16BitBy7F(IncAMEM8BitBy7F):
    """Increase 16bit AMEM $60-6F by value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitBy7F(IncAMEM8BitBy7F):
    """Decrease 8bit AMEM $60-6F by value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitBy7F(IncAMEM8BitBy7F):
    """Decrease 16bit AMEM $60-6F by value stored at given $7Fxxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitToAMEM(UsableAnimationScriptCommand, AnimationScriptAMEMAndAMEM):
    """Copy the value at the source_amem $60-6F address to the amem $60-6F 8bit address. Occasionally the amem can be outside of that range, but I have no idea why or what it does.

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to copy to
        source_amem (int): AMEM target address in range $60-$6F to copy from
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(
        self,
        amem: int,
        source_amem: int,
        upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_source_amem(source_amem)
        self.set_upper(upper)

    def render(self, *args) -> bytearray:
        return super().render(
            0x30 + self._amem_bits(), UInt16((self.source_amem & 0x0F) + self.upper)
        )

class SetAMEM16BitToAMEM(SetAMEM8BitToAMEM):
    """Copy the value at the source_amem $60-6F address to the amem $60-6F 16bit address. Occasionally the amem can be outside of that range, but I have no idea why or what it does.

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to copy to
        source_amem (int): AMEM target address in range $60-$6F to copy from
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class SetAMEMToAMEM8Bit(UsableAnimationScriptCommand, AnimationScriptAMEMAndAMEM):
    """Copy the value of the amem $60-6F 8bit address to the dest_amem $60-6F address. Occasionally the amem can be outside of that range, but I have no idea why or what it does.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        dest_amem (int): AMEM target address in range $60-$6F to copy to
        amem (int): AMEM target address in range $60-$6F to copy from
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(
        self,
        dest_amem: int,
        amem: int,
        upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_source_amem(dest_amem)  # i don't like this naming
        self.set_upper(upper)

    def render(self, *args) -> bytearray:
        return super().render(
            0x30 + self._amem_bits(), UInt16((self.source_amem & 0x0F) + self.upper)
        )

class SetAMEMToAMEM16Bit(SetAMEMToAMEM8Bit):
    """Copy the value of the amem $60-6F 16bit address to the dest_amem $60-6F address. Occasionally the amem can be outside of that range, but I have no idea why or what it does.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        dest_amem (int): AMEM target address in range $60-$6F to copy to
        amem (int): AMEM target address in range $60-$6F to copy from
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEqualsAMEM(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAndAMEM,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        source_amem: int,
        destinations: list[str],
        upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_source_amem(source_amem)
        self.set_upper(upper)

    def render(self, *args) -> bytearray:
        return super().render(
            0x30 + self._amem_bits(),
            UInt16((self.source_amem & 0x0F) + self.upper),
            *self.destinations,
        )

class JmpIfAMEM16BitEqualsAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEqualsAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEqualsAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThanAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThanAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 16bit AMEM $60-6F is less than the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThanAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThanAMEM(JmpIfAMEM8BitEqualsAMEM):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than the value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F controlling the goto
        source_amem (int): AMEM target address in range $60-$6F to compare against
        upper (int): The optional upper bits on the source amem
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitByAMEM(UsableAnimationScriptCommand, AnimationScriptAMEMAndAMEM):
    """Increase 8bit AMEM $60-6F by value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to increase
        source_amem (int): AMEM target address in range $60-$6F to increase it by
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(
        self,
        amem: int,
        source_amem: int,
        upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_source_amem(source_amem)
        self.set_upper(upper)

    def render(self, *args) -> bytearray:
        return super().render(
            0x30 + self._amem_bits(), UInt16((self.source_amem & 0x0F) + self.upper)
        )

class IncAMEM16BitByAMEM(IncAMEM8BitByAMEM):
    """Increase 16bit AMEM $60-6F by value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to increase
        source_amem (int): AMEM target address in range $60-$6F to increase it by
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitByAMEM(IncAMEM8BitByAMEM):
    """Decrease 8bit AMEM $60-6F by value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to decrease
        source_amem (int): AMEM target address in range $60-$6F to decrease it by
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitByAMEM(IncAMEM8BitByAMEM):
    """Decrease 16bit AMEM $60-6F by value stored at source AMEM $60-6F.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F to decrease
        source_amem (int): AMEM target address in range $60-$6F to decrease it by
        upper (int): The optional upper bits on the source amem
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitToOMEMCurrent(
    UsableAnimationScriptCommand, AnimationScriptAMEMAndOMEM
):
    """Set 8bit AMEM $60-6F to value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to set the value of AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(self, amem: int, omem: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(0x40 + self._amem_bits(), UInt16(self.omem))

class SetAMEM16BitToOMEMCurrent(SetAMEM8BitToOMEMCurrent):
    """Set 16bit AMEM $60-6F to value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to set the value of AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class SetOMEMCurrentToAMEM8Bit(SetAMEM8BitToOMEMCurrent):
    """Set OMEM (current) to value of 8bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        omem (int): The OMEM to be set to an AMEM value
        amem (int): The AMEM to set the value of OMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(self, omem: int, amem: int, identifier: str | None = None) -> None:
        super().__init__(amem, omem, identifier)

class SetOMEMCurrentToAMEM16Bit(SetOMEMCurrentToAMEM8Bit):
    """Set OMEM (current) to value of 16bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        omem (int): The OMEM to be set to an AMEM value
        amem (int): The AMEM to set the value of OMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEqualsOMEMCurrent(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAndOMEM,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        omem: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(
            0x40 + self._amem_bits(), UInt16(self.omem), *self.destinations
        )

class JmpIfAMEM16BitEqualsOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEqualsOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEqualsOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 16bit AMEM $60-6F does not equal the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThanOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThanOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent(JmpIfAMEM8BitEqualsOMEMCurrent):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than the value stored at OMEM (current).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitByOMEMCurrent(
    UsableAnimationScriptCommand, AnimationScriptAMEMAndOMEM
):
    """Increase 8bit AMEM $60-6F by value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(self, amem: int, omem: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(0x40 + self._amem_bits(), UInt16(self.omem))

class IncAMEM16BitByOMEMCurrent(IncAMEM8BitByOMEMCurrent):
    """Increase 16bit AMEM $60-6F by value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitByOMEMCurrent(IncAMEM8BitByOMEMCurrent):
    """Decrease 8bit AMEM $60-6F by value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitByOMEMCurrent(IncAMEM8BitByOMEMCurrent):
    """Decrease 16bit AMEM $60-6F by value stored at OMEM (current).

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitTo7E5x(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7E):
    """Set 8bit AMEM $60-6F to value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x50 + self._amem_bits(), addr)

class SetAMEM16BitTo7E5x(SetAMEM8BitTo7E5x):
    """Set 16bit AMEM $60-6F to value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        address (int): The address containing the value to set AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class Set7E5xToAMEM8Bit(SetAMEM8BitTo7E5x):
    """Set value stored at given $7Exxxx memory address to value stored at 8bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(
        self, address: int, amem: int, identifier: str | None = None
    ) -> None:
        super().__init__(amem, address, identifier)

class Set7E5xToAMEM16Bit(Set7E5xToAMEM8Bit):
    """Set value stored at given $7Exxxx memory address to value stored at 16bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        address (int): The address to copy the AMEM value to
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEquals7E5x(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAnd7E,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        address: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x50 + self._amem_bits(), addr, *self.destinations)

class JmpIfAMEM16BitEquals7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEquals7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEquals7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 16bit AMEM $60-6F does not equal value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThan7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThan7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 16bit AMEM $60-6F is less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThan7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThan7E5x(JmpIfAMEM8BitEquals7E5x):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        address (int): The variable holding the value to check AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitBy7E5x(UsableAnimationScriptCommand, AnimationScriptAMEMAnd7E):
    """Increase 8bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(
        self, amem: int, address: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_address(address)

    def render(self, *args) -> bytearray:
        addr = UInt16(self.address & 0xFFFF)
        return super().render(0x50 + self._amem_bits(), addr)

class IncAMEM16BitBy7E5x(IncAMEM8BitBy7E5x):
    """Increase 16bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitBy7E5x(IncAMEM8BitBy7E5x):
    """Decrease 8bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitBy7E5x(IncAMEM8BitBy7E5x):
    """Decrease 16bit AMEM $60-6F by value stored at given $7Exxxx memory address.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitToOMEMMain(UsableAnimationScriptCommand, AnimationScriptAMEMAndOMEM):
    """Set 8bit AMEM $60-6F to value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to set the value of AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20

    def __init__(self, amem: int, omem: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(0x60 + self._amem_bits(), UInt16(self.omem))

class SetAMEM16BitToOMEMMain(SetAMEM8BitToOMEMMain):
    """Set 16bit AMEM $60-6F to value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to set the value of AMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class SetOMEMMainToAMEM8Bit(SetAMEM8BitToOMEMMain):
    """Set OMEM (main) to value of 8bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        omem (int): The OMEM to be set to an AMEM value
        amem (int): The AMEM to set the value of OMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22

    def __init__(self, omem: int, amem: int, identifier: str | None = None) -> None:
        super().__init__(amem, omem, identifier)

class SetOMEMMainToAMEM16Bit(SetOMEMMainToAMEM8Bit):
    """Set OMEM (main) to value of 16bit AMEM $60-6F.

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        omem (int): The OMEM to be set to an AMEM value
        amem (int): The AMEM to set the value of OMEM to
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEqualsOMEMMain(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAndOMEM,
):
    """Goto destination indicated by name if 8bit AMEM $60-6F equals the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6

    def __init__(
        self,
        amem: int,
        omem: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(
            0x60 + self._amem_bits(), UInt16(self.omem), *self.destinations
        )

class JmpIfAMEM16BitEqualsOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 16bit AMEM $60-6F equals the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEqualsOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 8bit AMEM $60-6F does not equal the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEqualsOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 16bit AMEM $60-6F does not equal the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThanOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 8bit AMEM $60-6F is less than the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThanOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 16bit AMEM $60-6F is less than the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThanOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 8bit AMEM $60-6F is not less than the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThanOMEMMain(JmpIfAMEM8BitEqualsOMEMMain):
    """Goto destination indicated by name if 16bit AMEM $60-6F is not less than the value stored at OMEM (main).

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): The AMEM to check
        omem (int): The OMEM to check the AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitByOMEMMain(UsableAnimationScriptCommand, AnimationScriptAMEMAndOMEM):
    """Increase 8bit AMEM $60-6F by value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C

    def __init__(self, amem: int, omem: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_omem(omem)

    def render(self, *args) -> bytearray:
        return super().render(0x60 + self._amem_bits(), UInt16(self.omem))

class IncAMEM16BitByOMEMMain(IncAMEM8BitByOMEMMain):
    """Increase 16bit AMEM $60-6F by value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D

class DecAMEM8BitByOMEMMain(IncAMEM8BitByOMEMMain):
    """Decrease 8bit AMEM $60-6F by value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E

class DecAMEM16BitByOMEMMain(IncAMEM8BitByOMEMMain):
    """Decrease 16bit AMEM $60-6F by value stored at OMEM (main).

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        omem (int): The OMEM to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F

class SetAMEM8BitToUnknownShort(UsableAnimationScriptCommand, AnimationScriptAMEMAndConst):
    """Set 8bit AMEM $60-6F to the given value of the given type

    ## Lazy Shell command
        `AMEM (8-bit) $xx = variable {xx}`

    ## Opcode
        `0x20`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x20
    _type: int

    @property
    def type(self) -> int:
        return self._type

    def set_type(self, type: int) -> None:
        self._type = type

    def __init__(
        self, amem: int, type: int, value: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_value(value)
        self.set_type(type)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits() + (self.type << 4), self.value)

class SetAMEM16BitToUnknownShort(SetAMEM8BitToUnknownShort):
    """Set 16bit AMEM $60-6F to the given value of the given type

    ## Lazy Shell command
        `AMEM (16-bit) $xx = variable {xx}`

    ## Opcode
        `0x21`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x21

class SetUnknownShortToAMEM8Bit(AnimationScriptAMEMAndConst, UsableAnimationScriptCommand):
    """Set variable type 0x7-0xB to AMEM 8 bit

    ## Lazy Shell command
        `Variable {xx} = AMEM (8-bit) $xx`

    ## Opcode
        `0x22`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x22
    _type: int

    @property
    def type(self) -> int:
        return self._type

    def set_type(self, type: int) -> None:
        self._type = type

    def __init__(
        self, amem: int, type: int, value: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_value(value)
        self.set_type(type)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits() + (self.type << 4), self.value)

class SetUnknownShortToAMEM16Bit(SetUnknownShortToAMEM8Bit):
    """Set variable type 0x7-0xB to AMEM 16 bit

    ## Lazy Shell command
        `Variable {xx} = AMEM (16-bit) $xx`

    ## Opcode
        `0x23`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x23

class JmpIfAMEM8BitEqualsUnknownShort(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMAndConst,
):
    """If 8bit AMEM $60-6F equals the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx = {xx} ...`

    ## Opcode
        `0x24`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x24
    _size: int = 6
    _type: int

    @property
    def type(self) -> int:
        return self._type

    def set_type(self, type: int) -> None:
        self._type = type

    def __init__(
        self,
        amem: int,
        type: int,
        value: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_value(value)
        self.set_type(type)

    def render(self, *args) -> bytearray:
        return super().render(
            self._amem_bits() + (self.type << 4), self.value, *self.destinations
        )

class JmpIfAMEM16BitEqualsUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 16bit AMEM $60-6F equals the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx = {xx} ...`

    ## Opcode
        `0x25`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x25

class JmpIfAMEM8BitNotEqualsUnknownShort(JmpIfAMEM16BitEqualsUnknownShort):
    """If 8bit AMEM $60-6F does not equal the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx != {xx} ...`

    ## Opcode
        `0x26`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x26

class JmpIfAMEM16BitNotEqualsUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 16bit AMEM $60-6F does not equal the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx != {xx} ...`

    ## Opcode
        `0x27`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x27

class JmpIfAMEM8BitLessThanUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 8bit AMEM $60-6F is less than the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx < {xx} ...`

    ## Opcode
        `0x28`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x28

class JmpIfAMEM16BitLessThanUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 16bit AMEM $60-6F is less than the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx < {xx} ...`

    ## Opcode
        `0x29`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x29

class JmpIfAMEM8BitGreaterOrEqualThanUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 8bit AMEM $60-6F is greater than or equal to the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (8-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2A`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2A

class JmpIfAMEM16BitGreaterOrEqualThanUnknownShort(JmpIfAMEM8BitEqualsUnknownShort):
    """If 16bit AMEM $60-6F is greater than or equal to the given value of the given type, go to destination indicated by name.

    ## Lazy Shell command
        `If AMEM (16-bit) $xx >= {xx} ...`

    ## Opcode
        `0x2B`

    ## Size
        6 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to compare AMEM against
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2B

class IncAMEM8BitByUnknownShort(
    UsableAnimationScriptCommand, AnimationScriptAMEMAndConst
):
    """Increase 8bit AMEM $60-6F by given value of the given type.

    ## Lazy Shell command
        `AMEM (8-bit) $xx += {xx}`

    ## Opcode
        `0x2C`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2C
    _type: int

    @property
    def type(self) -> int:
        return self._type

    def set_type(self, type: int) -> None:
        self._type = type

    def __init__(
        self, amem: int, type: int, value: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_type(type)
        self.set_value(value)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits() + (self.type << 4), self.value)

class IncAMEM16BitByUnknownShort(IncAMEM8BitByUnknownShort):
    """Increase 26bit AMEM $60-6F by given value of the given type.

    ## Lazy Shell command
        `AMEM (16-bit) $xx += {xx}`

    ## Opcode
        `0x2D`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to increase AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2D
    _type: int

class DecAMEM8BitByUnknownShort(IncAMEM8BitByUnknownShort):
    """Decrease 8bit AMEM $60-6F by given value of the given type.

    ## Lazy Shell command
        `AMEM (8-bit) $xx -= {xx}`

    ## Opcode
        `0x2E`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2E
    _type: int

class DecAMEM16BitByUnknownShort(IncAMEM8BitByUnknownShort):
    """Decrease 16bit AMEM $60-6F by given value of the given type.

    ## Lazy Shell command
        `AMEM (16-bit) $xx -= {xx}`

    ## Opcode
        `0x2F`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        type (int): (unknown)
        value (int): The const value to decrease AMEM by
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x2F
    _type: int

class IncAMEM8Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Increase 8bit AMEM $60-6F by 1.

    ## Lazy Shell command
        `Increment AMEM (8-bit) $xx`

    ## Opcode
        `0x30`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x30

class IncAMEM16Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Increase 16bit AMEM $60-6F by 1.

    ## Lazy Shell command
        `Increment AMEM (16-bit) $xx`

    ## Opcode
        `0x31`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x31

class DecAMEM8Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Decrease 8bit AMEM $60-6F by 1.

    ## Lazy Shell command
        `Decrement AMEM (8-bit) $xx`

    ## Opcode
        `0x32`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x32

class DecAMEM16Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Decrease 16bit AMEM $60-6F by 1.

    ## Lazy Shell command
        `Decrement AMEM (16-bit) $xx`

    ## Opcode
        `0x33`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x33

class ClearAMEM8Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Set specified 8bit AMEM $60-6F to 0.

    ## Lazy Shell command
        `Clear AMEM (8-bit) $xx`

    ## Opcode
        `0x34`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x34

class ClearAMEM16Bit(UsableAnimationScriptCommand, AnimationScriptAMEM6XSoloCommand):
    """Set specified 16bit AMEM $60-6F to 0.

    ## Lazy Shell command
        `Clear AMEM (16-bit) $xx`

    ## Opcode
        `0x35`

    ## Size
        2 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x35

class SetAMEMBits(UsableAnimationScriptCommand, AnimationScriptAMEMCommand):
    """Set the specified bits to high in specified AMEM $60-6F.

    ## Lazy Shell command
        `Set AMEM $xx bits {xx}`

    ## Opcode
        `0x36`

    ## Size
        3 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        bits (list[int]): The bits being set on the specified AMEM.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x36
    _size: int = 3

    @property
    def bits(self) -> set[int]:
        """The bits being set on the specified AMEM."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Set these bits on the specified AMEM."""
        self._bits = set(bits)

    def __init__(
        self, amem: int, bits: list[int], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt8(bits_to_int(list(self.bits)))
        return super().render(self._amem_bits(), flags)

class ClearAMEMBits(SetAMEMBits):
    """Set the specified bits to low in specified AMEM $60-6F.

    ## Lazy Shell command
        `Clear AMEM $xx bits {xx}`

    ## Opcode
        `0x37`

    ## Size
        3 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        bits (list[int]): The bits being set on the specified AMEM.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x37

class JmpIfAMEMBitsSet(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
    AnimationScriptAMEMCommand,
):
    """Goto destination indicated by name if AMEM $60-6F specified bits are all set.

    ## Lazy Shell command
        `If AMEM $xx bits {xx} set...`

    ## Opcode
        `0x38`

    ## Size
        5 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        bits (list[int]): The bits of interest for the goto to happen.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x38
    _size: int = 5

    @property
    def bits(self) -> set[int]:
        """The bits of interest for the goto to happen."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Set the bits of interest for the goto to happen."""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = set(bits)

    def __init__(
        self,
        amem: int,
        bits: list[int],
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_amem(amem)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt8(bits_to_int(list(self.bits)))
        return super().render(self._amem_bits(), flags, *self.destinations)

class JmpIfAMEMBitsClear(JmpIfAMEMBitsSet):
    """Goto destination indicated by name if AMEM $60-6F specified bits are all clear.

    ## Lazy Shell command
        `If AMEM $xx bits {xx} clear...`

    ## Opcode
        `0x39`

    ## Size
        5 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        bits (list[int]): The bits of interest for the goto to happen.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x39

class AttackTimerBegins(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Start the attack timer.

    ## Lazy Shell command
        `Attack timer begins`

    ## Opcode
        `0x3A`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x3A

class PauseScriptUntilAMEMBitsSet(
    UsableAnimationScriptCommand, AnimationScriptAMEMCommand
):
    """Pause the active script until specified bits in AMEM $60-6F are set.

    ## Lazy Shell command
        `Pause script until AMEM $xx bits {xx} set`

    ## Opcode
        `0x40`

    ## Size
        3 bytes

    Args:
        amem (int): Description here to be filled out by me
        bits (list[int]): The bits of interest for the script to resume.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x40
    _size: int = 3

    @property
    def bits(self) -> set[int]:
        """The bits of interest for the script to resume."""
        return self._bits

    def set_bits(self, bits: list[int]) -> None:
        """Set the bits of interest for the script to resume."""
        self._bits = set(bits)

    def __init__(
        self, amem: int, bits: list[int], identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        flags = UInt8(bits_to_int(list(self.bits)))
        return super().render(self._amem_bits(), flags)

class PauseScriptUntilAMEMBitsClear(PauseScriptUntilAMEMBitsSet):
    """Pause the active script until specified bits in AMEM $60-6F are clear.

    ## Lazy Shell command
        `Pause script until AMEM $xx bits {xx} clear`

    ## Opcode
        `0x41`

    ## Size
        3 bytes

    Args:
        amem (int): Description here to be filled out by me
        bits (list[int]): The bits of interest for the script to resume.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x41

class SpriteSequence(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Run a specific sequence for the sprite this command is applied to.

    ## Lazy Shell command
        `Sprite sequence = {xx}`

    ## Opcode
        `0x43`

    ## Size
        2 bytes

    Args:
        sequence (int): The sequence ID being run for this sprite.
        looping_on (bool): If true, the sequence will repeat indefinitely.
        looping_off (bool): If true, the sequence will play only once.
        bit_6 (bool): (unknown)
        mirror (bool): If true, the sprite will be displayed flipped horizontally from default.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x43
    _size: int = 2

    _sequence: UInt4
    _looping_on: bool
    _looping_off: bool
    _bit_6: bool
    _mirror: bool

    @property
    def sequence(self) -> UInt4:
        """The sequence ID being run for this sprite."""
        return self._sequence

    def set_sequence(self, sequence: int) -> None:
        """Set the sequence ID to run for this sprite."""
        self._sequence = UInt4(sequence)

    @property
    def looping_on(self) -> bool:
        """If true, the sequence will repeat indefinitely."""
        return self._looping_on

    def set_looping_on(self, looping_on: bool) -> None:
        """If true, the sequence will repeat indefinitely."""
        self._looping_on = looping_on

    @property
    def looping_off(self) -> bool:
        """If true, the sequence will play only once."""
        return self._looping_off

    def set_looping_off(self, looping_off: bool) -> None:
        """If true, the sequence will play only once."""
        self._looping_off = looping_off

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def mirror(self) -> bool:
        """If true, the sprite will be displayed flipped horizontally from default."""
        return self._mirror

    def set_mirror(self, mirror: bool) -> None:
        """If true, the sprite will be displayed flipped horizontally from default."""
        self._mirror = mirror

    def __init__(
        self,
        sequence: int,
        looping_on: bool = False,
        looping_off: bool = False,
        bit_6: bool = False,
        mirror: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sequence(sequence)
        self.set_looping_on(looping_on)
        self.set_looping_off(looping_off)
        self.set_bit_6(bit_6)
        self.set_mirror(mirror)

    def render(self, *args) -> bytearray:
        byte1 = self.sequence + (
            (
                self.looping_on
                + (self.looping_off << 1)
                + (self.bit_6 << 2)
                + (self.mirror << 3)
            )
            << 4
        )
        return super().render(UInt8(byte1))

class SetAMEM60ToCurrentTarget(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Set AMEM $60 to the ID of the current target.

    ## Lazy Shell command
        `AMEM $60 = current target`

    ## Opcode
        `0x45`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x45

class GameOverIfNoAlliesStanding(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Run the Game Over sequence if all party members are downed.

    ## Lazy Shell command
        `Check ally mortal status, if all allies down set game over`

    ## Opcode
        `0x46`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x46

class PauseScriptUntilSpriteSequenceDone(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Pause the active script until a running sprite sequence has finished.

    ## Lazy Shell command
        `Pause script until sprite sequence don`

    ## Opcode
        `0x4E`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x4E

class JmpIfTargetDisabled(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """Goto destination indicated by name if target is disabled.

    ## Lazy Shell command
        `If target disabled, jump to address $xxxx`

    ## Opcode
        `0x50`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x50
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class JmpIfTargetEnabled(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """Goto destination indicated by name if target is enabled.

    ## Lazy Shell command
        `If target alive, jump to address $xxxx`

    ## Opcode
        `0x51`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x51
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class UseSpriteQueue(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """Perform a set of script commands at the specified address on the specified field target.

    ## Lazy Shell command
        `Sprite queue [$offset] (sprite = {xx})`

    ## Opcode
        `0x5D`

    ## Size
        5 bytes

    Args:
        field_object (int): The ID of the object on the field to target with the script.
        bit_0 (bool): (unknown)
        bit_1 (bool): (unknown)
        bit_2 (bool): (unknown)
        character_slot (bool): (unknown)
        bit_4 (bool): (unknown)
        bit_5 (bool): (unknown)
        current_target (bool): (unknown)
        bit_7 (bool): (unknown)
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to start at.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x5D
    _size: int = 5

    _field_object: UInt4
    _bit_0: bool
    _bit_1: bool
    _bit_2: bool
    _character_slot: bool
    _bit_4: bool
    _bit_5: bool
    _current_target: bool
    _bit_7: bool
    _mirror: bool

    @property
    def field_object(self) -> UInt4:
        """The ID of the object on the field to target with the script."""
        return self._field_object

    def set_field_object(self, field_object: int) -> None:
        """The ID of the object on the field to target with the script."""
        self._field_object = UInt4(field_object)

    @property
    def bit_0(self) -> bool:
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def bit_1(self) -> bool:
        """(unknown)"""
        return self._bit_1

    def set_bit_1(self, bit_1: bool) -> None:
        """(unknown)"""
        self._bit_1 = bit_1

    @property
    def bit_2(self) -> bool:
        """(unknown)"""
        return self._bit_2

    def set_bit_2(self, bit_2: bool) -> None:
        """(unknown)"""
        self._bit_2 = bit_2

    @property
    def character_slot(self) -> bool:
        """(unknown)"""
        return self._character_slot

    def set_character_slot(self, character_slot: bool) -> None:
        """(unknown)"""
        self._character_slot = character_slot

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    @property
    def current_target(self) -> bool:
        """(unknown)"""
        return self._current_target

    def set_current_target(self, current_target: bool) -> None:
        """(unknown)"""
        self._current_target = current_target

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    @property
    def mirror(self) -> bool:
        """If true, the sprite will be displayed flipped horizontally."""
        return self._mirror

    def set_mirror(self, mirror: bool) -> None:
        """Set if the sprite will be displayed flipped horizontally."""
        self._mirror = mirror

    def __init__(
        self,
        field_object: int,
        destinations: list[str],
        bit_0: bool = False,
        bit_1: bool = False,
        bit_2: bool = False,
        character_slot: bool = False,
        bit_4: bool = False,
        bit_5: bool = False,
        current_target: bool = False,
        bit_7: bool = False,
        mirror: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_field_object(field_object)
        self.set_destinations(destinations)
        self.set_bit_0(bit_0)
        self.set_bit_1(bit_1)
        self.set_bit_2(bit_2)
        self.set_character_slot(character_slot)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)
        self.set_current_target(current_target)
        self.set_bit_7(bit_7)
        self.set_mirror(mirror)

    def render(self, *args) -> bytearray:
        byte1 = bools_to_int(
            self.bit_0,
            self.bit_1,
            self.bit_2,
            self.character_slot,
            self.bit_4,
            self.bit_5,
            self.current_target,
            self.bit_7,
        )
        return super().render(byte1, self.field_object, *self.destinations)

class ReturnSpriteQueue(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Terminate a series of commands intended to be run as a animation for a specific object.

    ## Lazy Shell command
        `Return sprite queue`

    ## Opcode
        `0x5E`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x5E

class DisplayMessageAtOMEM60As(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Set the context under which to run the dialog ID corresponding to the current value at AMEM $60.

    ## Lazy Shell command
        `Display {xx} message @ OMEM $60`

    ## Opcode
        `0x63`

    ## Size
        2 bytes

    Args:
        message_type (MessageType): The context in which to display the dialog.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x63
    _size: int = 2

    _message_type: MessageType

    @property
    def message_type(self) -> MessageType:
        """The context in which to display the dialog."""
        return self._message_type

    def set_message_type(self, message_type: MessageType) -> None:
        """Set the context in which to display the dialog."""
        self._message_type = message_type

    def __init__(
        self, message_type: MessageType, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_message_type(message_type)

    def render(self, *args) -> bytearray:
        return super().render(self.message_type)

class UseObjectQueueAtOffsetWithAMEM60Index(
    UsableAnimationScriptCommand, AnimationScriptCommandWithJmps
):
    """Point to an object queue. The starting pointer is chosen by the current value of AMEM $60 (offset + AMEM $60 * 2)

    ## Lazy Shell command
        `Object queue [$offset] index = AMEM $60`

    ## Opcode
        `0x64`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the `CreateObjectQueue` to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x64
    _size: int = 3

    def __init__(
        self,
        destinations: list[str] | None = None,
        identifier: str | None = None,
    ) -> None:
        if not destinations:
            raise InvalidCommandArgumentException(
                "object queue command needs at least one destination label"
            )
        super().__init__(destinations, identifier)

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class UseObjectQueueAtOffsetWithAMEM60PointerOffset(
    UsableAnimationScriptCommand, AnimationScriptCommandWithJmps
):
    """Point to an object queue. The pointer table reference is at (offset + AMEM $60 * 2) and then the starting pointer is at (reference pointer + index).
    Must point to a `ObjectQueueLayeredPointerTable`.

    ## Lazy Shell command
        `Object queue [$offset, AMEM $60] index = {xx}`

    ## Opcode
        `0x68`

    ## Size
        4 bytes

    Args:
        index (int): The index value to be applied on top of the target address.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x68
    _size: int = 4

    _index: UInt8 = UInt8(0)

    @property
    def index(self) -> UInt8:
        """The index value to be applied on top of the target address."""
        return self._index

    def set_index(self, index: int) -> None:
        """Set the index value to be applied on top of the target address."""
        self._index = UInt8(index)

    def __init__(
        self,
        index: int,
        destinations: list[str] | None = None,
        identifier: str | None = None,
    ) -> None:
        if not destinations:
            raise InvalidCommandArgumentException(
                "object queue command needs at least one destination label"
            )
        super().__init__(destinations, identifier)
        self.set_index(index)

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations, self.index)

class DefineObjectQueue(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """This structure should only contain destinations.  
    If destinations point to other object queues, then this should be targeted with `UseObjectQueueAtOffsetWithAMEM60PointerOffset`.

    Args:
        destinations (list[str]): The commands that this queue's indexes should start at, in order of index.
        identifier (str): The label that an `UseObjectQueueAtOffsetWithAMEM60Index` will use to refer to this.
    """

    @property
    def size(self) -> int:
        return len(self.destinations) * 2

    def __init__(self, destinations: list[str], identifier: str) -> None:
        if not destinations:
            raise InvalidCommandArgumentException(
                "object queue needs at least one destination label"
            )
        if not identifier:
            raise InvalidCommandArgumentException("object queues require an identifier")
        super().__init__(destinations, identifier)

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class SetOMEM60To072C(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """(unknown)

    ## Lazy Shell command
        `OMEM $60 = memory $072C`

    ## Opcode
        `0x69`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x69

class SetAMEMToRandomByte(UsableAnimationScriptCommand, AnimationScriptAMEMCommand):
    """Set a specific AMEM $60-6F to a random value between 0 and a specified upper bound. The upper bound can be any unsigned 16 bit value.

    ## Lazy Shell command
        `AMEM $xx = random # between 0 and {xx}`

    ## Opcode
        `0x6A`

    ## Size
        3 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        upper_bound (int): The upper bound for this command's random number generator.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x6A
    _size: int = 3

    _upper_bound: UInt8

    @property
    def upper_bound(self) -> UInt8:
        """The upper bound for this command's random number generator."""
        return self._upper_bound

    def set_upper_bound(self, upper_bound: int) -> None:
        """Set the upper bound that the random number can fall under."""
        self._upper_bound = UInt8(upper_bound)

    def __init__(
        self, amem: int, upper_bound: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_upper_bound(upper_bound)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits(), self.upper_bound)

class SetAMEMToRandomShort(UsableAnimationScriptCommand, AnimationScriptAMEMCommand):
    """Set a specific AMEM $60-6F to a random value between 0 and a specified upper bound. The upper bound can be any unsigned 16 bit value.

    ## Lazy Shell command
        `AMEM $xx = random # between 0 and {xx}`

    ## Opcode
        `0x6B`

    ## Size
        4 bytes

    Args:
        amem (int): AMEM target address in range $60-$6F
        upper_bound (int): The upper bound for this command's random number generator.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x6B
    _size: int = 4

    _upper_bound: UInt16

    @property
    def upper_bound(self) -> UInt16:
        """The upper bound for this command's random number generator."""
        return self._upper_bound

    def set_upper_bound(self, upper_bound: int) -> None:
        """Set the upper bound that the random number can fall under."""
        self._upper_bound = UInt16(upper_bound)

    def __init__(
        self, amem: int, upper_bound: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_amem(amem)
        self.set_upper_bound(upper_bound)

    def render(self, *args) -> bytearray:
        return super().render(self._amem_bits(), self.upper_bound)

class EnableSpritesOnSubscreen(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Subscreen sprites are enabled.

    ## Lazy Shell command
        `Overlap all`

    ## Opcode
        `0x70`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x70

class DisableSpritesOnSubscreen(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Subscreen sprites are disabled.

    ## Lazy Shell command
        `Overlap none`

    ## Opcode
        `0x71`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x71

class NewEffectObject(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Draw a new effect (by ID) on screen. It is recommended to use effect constants for this.

    ## Lazy Shell command
        `New object: effect = ...`

    ## Opcode
        `0x72`

    ## Size
        3 bytes

    Args:
        effect (int): The ID of the effect to draw.
        looping_on (bool): If true, the effect's animation will loop indefinitely.
        playback_off (bool): If true, the effect will be drawn statically with no animation playback.
        looping_off (bool): If true, the effect's animation will play only once.
        bit_3 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x72
    _size: int = 3

    _effect: UInt8
    _looping_on: bool
    _playback_off: bool
    _looping_off: bool
    _bit_3: bool

    @property
    def effect(self) -> UInt8:
        """The ID of the effect to draw."""
        return self._effect

    def set_effect(self, effect: int) -> None:
        """Set the ID of the effect to draw."""
        assert 0 <= effect <= 127
        self._effect = UInt8(effect)

    @property
    def looping_on(self) -> bool:
        """If true, the effect's animation will loop indefinitely."""
        return self._looping_on

    def set_looping_on(self, looping_on: bool) -> None:
        """If true, the effect's animation will loop indefinitely."""
        self._looping_on = looping_on

    @property
    def playback_off(self) -> bool:
        """If true, the effect will be drawn statically with no animation playback."""
        return self._playback_off

    def set_playback_off(self, playback_off: bool) -> None:
        """If true, the effect will be drawn statically with no animation playback."""
        self._playback_off = playback_off

    @property
    def looping_off(self) -> bool:
        """If true, the effect's animation will play only once."""
        return self._looping_off

    def set_looping_off(self, looping_off: bool) -> None:
        """If true, the effect's animation will play only once."""
        self._looping_off = looping_off

    @property
    def bit_3(self) -> bool:
        """(unknown)"""
        return self._bit_3

    def set_bit_3(self, bit_3: bool) -> None:
        """(unknown)"""
        self._bit_3 = bit_3

    def __init__(
        self,
        effect: int,
        looping_on: bool = False,
        playback_off: bool = False,
        looping_off: bool = False,
        bit_3: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_effect(effect)
        self.set_looping_on(looping_on)
        self.set_playback_off(playback_off)
        self.set_looping_off(looping_off)
        self.set_bit_3(bit_3)

    def render(self, *args) -> bytearray:
        byte1 = bools_to_int(
            self.looping_on,
            self.playback_off,
            self.looping_off,
            self.bit_3,
        )
        return super().render(byte1, self.effect)

class Pause2Frames(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Pause the script for exactly 2 frames.

    ## Lazy Shell command
        `Pause script for 2 frames`

    ## Opcode
        `0x73`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x73

class PauseScriptUntilBitsClear(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Pause the active script until specified bits (belonging to unknown var) are clear.

    ## Lazy Shell command
        `Pause script until bits clear...`

    ## Opcode
        `0x75`

    ## Size
        3 bytes

    Args:
        bits (int): The bits of interest.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x75
    _size: int = 3

    _bits: UInt16

    @property
    def bits(self) -> UInt16:
        """The bits of interest."""
        return self._bits

    def set_bits(self, bits: int) -> None:
        """Set the bits of interest."""
        self._bits = UInt16(bits)

    def __init__(self, bits: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_bits(bits)

    def render(self, *args) -> bytearray:
        return super().render(self.bits)

class ClearEffectIndex(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """(unknown, something regarding an active drawn effect)

    ## Lazy Shell command
        `Clear effect index`

    ## Opcode
        `0x76`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x76

class Layer3On(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Turn on layer 3

    ## Lazy Shell command
        `L3 on...`

    ## Opcode
        `0x77`

    ## Size
        2 bytes

    Args:
        property (LayerPriorityType): Description here to be filled out by me
        bit_0 (bool): (unknown)
        bpp4 (bool): bpp4 gfx
        bpp2 (bool): bpp2 gfx
        invisible (bool): Draw invisible if true
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x77
    _size: int = 2

    _prop: LayerPriorityType
    _bit_0: bool
    _bpp4: bool
    _bpp2: bool
    _invisible: bool

    @property
    def prop(self) -> LayerPriorityType:
        """The overlap priority with which to draw the layer"""
        return self._prop

    def set_prop(self, prop: LayerPriorityType) -> None:
        """Set the overlap priority with which to draw the layer"""
        self._prop = prop

    @property
    def bit_0(self) -> bool:
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def bpp4(self) -> bool:
        """bpp4 gfx"""
        return self._bpp4

    def set_bpp4(self, bpp4: bool) -> None:
        """bpp4 gfx"""
        self._bpp4 = bpp4

    @property
    def bpp2(self) -> bool:
        """bpp2 gfx"""
        return self._bpp2

    def set_bpp2(self, bpp2: bool) -> None:
        """bpp2 gfx"""
        self._bpp2 = bpp2

    @property
    def invisible(self) -> bool:
        """Draw invisible if true"""
        return self._invisible

    def set_invisible(self, invisible: bool) -> None:
        """Draw invisible if true"""
        self._invisible = invisible

    def __init__(
        self,
        property: LayerPriorityType,
        bit_0: bool = False,
        bpp4: bool = False,
        bpp2: bool = False,
        invisible: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_prop(property)
        self.set_bit_0(bit_0)
        self.set_bpp4(bpp4)
        self.set_bpp2(bpp2)
        self.set_invisible(invisible)

    def render(self, *args) -> bytearray:
        byte1 = bools_to_int(self.bit_0, self.bpp4, self.bpp2, self.invisible) + (
            self.prop << 4
        )
        return super().render(byte1)

class Layer3Off(Layer3On):
    """Turn off layer 3

    ## Lazy Shell command
        `L3 off...`

    ## Opcode
        `0x78`

    ## Size
        *No `_size` found*

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x78

class DisplayMessage(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Display a dialog in battle with a given context.

    ## Lazy Shell command
        `Display message...`

    ## Opcode
        `0x7A`

    ## Size
        3 bytes

    Args:
        message_type (MessageType): The context in which to display the dialog.
        dialog_id (int): The ID of the dialog to display.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7A
    _size: int = 3

    _type: MessageType
    _dialog_id: UInt8

    @property
    def message_type(self) -> MessageType:
        """The context in which to display the dialog."""
        return self._type

    def set_type(self, message_type: MessageType) -> None:
        """Set the context in which to display the dialog."""
        self._type = message_type

    @property
    def dialog_id(self) -> UInt8:
        """The ID of the dialog to display."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        """Set the ID of the dialog to display."""
        self._dialog_id = UInt8(dialog_id)

    def __init__(
        self,
        message_type: MessageType,
        dialog_id: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_type(message_type)
        self.set_dialog_id(dialog_id)

    def render(self, *args) -> bytearray:
        return super().render(self.message_type, self.dialog_id)

class PauseScriptUntilDialogClosed(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Pause the script until a displayed dialog has closed.

    ## Lazy Shell command
        `Pause script until dialogue closed`

    ## Opcode
        `0x7B`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7B

class FadeOutObject(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Fade out the object on which this queue is running.

    ## Lazy Shell command
        `Fade out object, duration = ...`

    ## Opcode
        `0x7E`

    ## Size
        2 bytes

    Args:
        duration (int): The desired length of the fade animation, in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7E
    _size: int = 2
    _duration: UInt8

    @property
    def duration(self) -> UInt8:
        """The desired length of the fade animation, in frames."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the desired length of the fade animation, in frames."""
        self._duration = UInt8(duration)

    def __init__(self, duration: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_duration(duration)

    def render(self, *args) -> bytearray:
        return super().render(self.duration)

class ResetSpriteSequence(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Reset the active sprite sequence for the object on which this queue is running.

    ## Lazy Shell command
        `Reset sprite sequence`

    ## Opcode
        `0x7F`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x7F

class ShineEffect(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Draw a shine effect on screen.

    ## Lazy Shell command
        `Shine effect...`

    ## Opcode
        `0x80`

    ## Size
        4 bytes

    Args:
        colour_count (int): The number of colours to display during the effect.
        starting_colour_index (int): The number ID of the colour which should start the effect.
        glow_duration (int): The length, in frames, that the effect should last for.
        east (bool): If true, shine direction is eastward.
        west (bool): If true, shine direction is westward.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x80
    _size: int = 4

    _colour_count: UInt4
    _starting_colour_index: UInt4
    _glow_duration: UInt8
    _east: bool
    _west: bool

    @property
    def colour_count(self) -> UInt4:
        """The number of colours to display during the effect."""
        return self._colour_count

    def set_colour_count(self, colour_count: int) -> None:
        """Set the number of colours to display during the effect."""
        self._colour_count = UInt4(colour_count)

    @property
    def starting_colour_index(self) -> UInt4:
        """The number ID of the colour which should start the effect."""
        return self._starting_colour_index

    def set_starting_colour_index(self, starting_colour_index: int) -> None:
        """Set the number ID of the colour which should start the effect."""
        self._starting_colour_index = UInt4(starting_colour_index)

    @property
    def glow_duration(self) -> UInt8:
        """The length, in frames, that the effect should last for."""
        return self._glow_duration

    def set_glow_duration(self, glow_duration: int) -> None:
        """Set the length, in frames, that the effect should last for."""
        self._glow_duration = UInt8(glow_duration)

    @property
    def east(self) -> bool:
        """If true, shine direction is eastward."""
        return self._east

    def _set_east(self, east: bool) -> None:
        self._east = east

    @property
    def west(self) -> bool:
        """If true, shine direction is westward."""
        return self._west

    def _set_west(self, west: bool) -> None:
        self._west = west

    def set_direction(self, east: bool | None, west: bool | None) -> None:
        """Decide if the shine effect will shine eastward or westward.."""
        if east is None:
            east = self.east
        if west is None:
            west = self.west
        if east == west:
            raise InvalidCommandArgumentException(
                "east and west cannot be the same value"
            )
        self._set_east(east)
        self._set_west(west)

    def __init__(
        self,
        colour_count: int,
        starting_colour_index: int,
        glow_duration: int,
        east: bool = False,
        west: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_colour_count(colour_count)
        self.set_starting_colour_index(starting_colour_index)
        self.set_glow_duration(glow_duration)
        self.set_direction(east, west)

    def render(self, *args) -> bytearray:
        return super().render(
            self.west,
            self.colour_count + (self.starting_colour_index << 4),
            self.glow_duration,
        )

class FadeOutEffect(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade out the active effect for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(0, self.duration)

class FadeOutSprite(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade out the active sprite for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(0x10, self.duration)

class FadeOutScreen(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade out the screen for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(0x20, self.duration)

class FadeInEffect(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade in the active effect for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(2, self.duration)

class FadeInSprite(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade in the active sprite for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(0x12, self.duration)

class FadeInScreen(UsableAnimationScriptCommand, AnimationScriptFadeObject):
    """Fade in the screen for a given duration in frames.

    ## Lazy Shell command
        `Fade object {xx}, amount = ...`

    ## Opcode
        `0x85`

    ## Size
        3 bytes

    Args:
        duration (int): Fade duration in frames.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(0x22, self.duration)

class ShakeScreen(UsableAnimationScriptCommand, AnimationScriptShakeObject):
    """Shake the screen for a given number of times at a given speed.

    ## Lazy Shell command
        `Shake object...`

    ## Opcode
        `0x86`

    ## Size
        7 bytes

    Args:
        amount (int): Number of shakes.
        speed (int): Shake speed.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(1)

class ShakeSprites(UsableAnimationScriptCommand, AnimationScriptShakeObject):
    """Shake the visible sprites for a given number of times at a given speed.

    ## Lazy Shell command
        `Shake object...`

    ## Opcode
        `0x86`

    ## Size
        7 bytes

    Args:
        amount (int): Number of shakes.
        speed (int): Shake speed.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(2)

class ShakeScreenAndSprites(UsableAnimationScriptCommand, AnimationScriptShakeObject):
    """Shake the screen AND visible sprites for a given number of times at a given speed.

    ## Lazy Shell command
        `Shake object...`

    ## Opcode
        `0x86`

    ## Size
        7 bytes

    Args:
        amount (int): Number of shakes.
        speed (int): Shake speed.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    def render(self, *args) -> bytearray:
        return super().render(4)

class StopShakingObject(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Halt an active shake command.

    ## Lazy Shell command
        `Stop shaking object`

    ## Opcode
        `0x87`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x87

class ScreenFlashWithDuration(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Flash a colour over the screen for a given duration.

    ## Lazy Shell command
        `Screen flash {xx} color, duration = ...`

    ## Opcode
        `0x8E`

    ## Size
        3 bytes

    Args:
        colour (FlashColour): The screen flash colour.
        duration (int): The duration of the flash, in frames.
        unknown_upper (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x8E
    _size: int = 3

    _colour: FlashColour
    _unknown_upper: UInt8
    _duration: UInt8

    @property
    def colour(self) -> FlashColour:
        """The screen flash colour."""
        return self._colour

    def set_colour(self, colour: FlashColour) -> None:
        """Set the screen flash colour."""
        self._colour = colour

    @property
    def unknown_upper(self) -> UInt8:
        """(unknown)"""
        return self._unknown_upper

    def set_unknown_upper(self, unknown_upper: int) -> None:
        """(unknown)"""
        assert unknown_upper & 0x07 == 0
        self._unknown_upper = UInt8(unknown_upper)

    @property
    def duration(self) -> UInt8:
        """The duration of the flash, in frames."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration of the flash, in frames."""
        self._duration = UInt8(duration)

    def __init__(
        self,
        colour: FlashColour,
        duration: int,
        unknown_upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_colour(colour)
        self.set_duration(duration)
        self.set_unknown_upper(unknown_upper)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_upper + self.colour, self.duration)

class ScreenFlash(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Briefly flash a colour over the screen.

    ## Lazy Shell command
        `Screen flash {xx} color`

    ## Opcode
        `0x8F`

    ## Size
        2 bytes

    Args:
        colour (FlashColour): The screen flash colour.
        unknown_upper (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x8F
    _size: int = 2

    _colour: FlashColour
    _unknown_upper: UInt8

    @property
    def colour(self) -> FlashColour:
        """The screen flash colour."""
        return self._colour

    def set_colour(self, colour: FlashColour) -> None:
        """Set the screen flash colour."""
        self._colour = colour

    @property
    def unknown_upper(self) -> UInt8:
        """(unknown)"""
        return self._unknown_upper

    def set_unknown_upper(self, unknown_upper: int) -> None:
        """(unknown)"""
        assert unknown_upper & 0x07 == 0
        self._unknown_upper = UInt8(unknown_upper)

    def __init__(
        self,
        colour: FlashColour,
        unknown_upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_colour(colour)
        self.set_unknown_upper(unknown_upper)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_upper + self.colour)

class InitializeBonusMessageSequence(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Initialize a bonus message sequence, usually for bonus flowers and certain items.

    ## Lazy Shell command
        `Initialize bonus message sequence`

    ## Opcode
        `0x95`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x95

class DisplayBonusMessage(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Display a pre-set bonus message, usually for bonus flowers and certain items.

    ## Lazy Shell command
        `Display bonus message...`

    ## Opcode
        `0x96`

    ## Size
        5 bytes

    Args:
        message (BonusMessage): The message ID to display.
        x (int): The X coord at which to render the message.
        y (int): The Y coord at which to render the message.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x96
    _size: int = 5

    _message: BonusMessage
    _x: Int8
    _y: Int8

    @property
    def message(self) -> BonusMessage:
        """The message ID to display."""
        return self._message

    def set_message(self, message: BonusMessage) -> None:
        """Set the message ID to display."""
        self._message = message

    @property
    def x(self) -> Int8:
        """The X coord at which to render the message."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coord at which to render the message."""
        self._x = Int8(x)

    @property
    def y(self) -> Int8:
        """The Y coord at which to render the message."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord at which to render the message."""
        self._y = Int8(y)

    def __init__(
        self, message: BonusMessage, x: int, y: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_message(message)
        self.set_x(x)
        self.set_y(y)

    def render(self, *args) -> bytearray:
        return super().render(0, self.message, self.x, self.y)

class PauseScriptUntilBonusMessageComplete(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Pause the script until an aforementioned bonus message (i.e. from a bonus flower) has cleared itself.

    ## Lazy Shell command
        `Pause script until bonus message complete`

    ## Opcode
        `0x97`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x97

class WaveEffect(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Wave effect animation

    ## Lazy Shell command
        `Battlefield wavy effect...`

    ## Opcode
        `0x9C`

    ## Size
        9 bytes

    Args:
        layer (WaveEffectLayer): The layer on which the wave effect is applied.
        direction (WaveEffectDirection): The direction of the wave effect.
        depth (int): The depth of the wave effect.
        intensity (int): The intensity of the wave effect.
        speed (int): The speed of the wave effect.
        bit_3 (bool): The third bit flag for wave effect configuration.
        bit_4 (bool): The fourth bit flag for wave effect configuration.
        bit_5 (bool): The fifth bit flag for wave effect configuration.
        byte_1 (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x9C
    _size: int = 9

    _layer: WaveEffectLayer = WAVE_LAYER_BATTLEFIELD
    _direction: WaveEffectDirection = WAVE_LAYER_HORIZONTAL
    _depth: UInt16 = UInt16(0)
    _intensity: UInt16 = UInt16(0)
    _speed: UInt16 = UInt16(0)
    _bit_3: bool = False
    _bit_4: bool = False
    _bit_5: bool = False
    _byte_1: UInt8 = UInt8(0)

    @property
    def layer(self) -> WaveEffectLayer:
        """The layer on which the wave effect is applied."""
        return self._layer

    def set_layer(self, layer: WaveEffectLayer) -> None:
        """Set the layer on which the wave effect is applied."""
        self._layer = layer

    @property
    def direction(self) -> WaveEffectDirection:
        """The direction of the wave effect."""
        return self._direction

    def set_direction(self, direction: WaveEffectDirection) -> None:
        """Set the direction of the wave effect."""
        self._direction = direction

    @property
    def depth(self) -> UInt16:
        """The depth of the wave effect."""
        return self._depth

    def set_depth(self, depth: int) -> None:
        """Set the depth of the wave effect."""
        self._depth = UInt16(depth)

    @property
    def intensity(self) -> UInt16:
        """The intensity of the wave effect."""
        return self._intensity

    def set_intensity(self, intensity: int) -> None:
        """Set the intensity of the wave effect."""
        self._intensity = UInt16(intensity)

    @property
    def speed(self) -> UInt16:
        """The speed of the wave effect."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed of the wave effect."""
        self._speed = UInt16(speed)

    @property
    def bit_3(self) -> bool:
        """The third bit flag for wave effect configuration."""
        return self._bit_3

    def set_bit_3(self, bit_3: bool) -> None:
        """Set the third bit flag for wave effect configuration."""
        self._bit_3 = bit_3

    @property
    def bit_4(self) -> bool:
        """The fourth bit flag for wave effect configuration."""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """Set the fourth bit flag for wave effect configuration."""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """The fifth bit flag for wave effect configuration."""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """Set the fifth bit flag for wave effect configuration."""
        self._bit_5 = bit_5

    @property
    def byte_1(self) -> UInt8:
        """(unknown)"""
        return self._byte_1

    def set_byte_1(self, byte_1: int) -> None:
        """(unknown)"""
        self._byte_1 = UInt8(byte_1)

    def __init__(
        self,
        layer: WaveEffectLayer,
        direction: WaveEffectDirection,
        depth: int,
        intensity: int,
        speed: int,
        bit_3: bool = False,
        bit_4: bool = False,
        bit_5: bool = False,
        byte_1: int = 0,
        identifier: str | None = None,
    ):
        super().__init__(identifier)
        self.set_layer(layer)
        self.set_direction(direction)
        self.set_depth(depth)
        self.set_intensity(intensity)
        self.set_speed(speed)
        self.set_bit_3(bit_3)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)
        self.set_byte_1(byte_1)

    def render(self, *args) -> bytearray:
        arg_1 = (
            bits_to_int([self.layer])
            + bits_to_int([self.direction + 6])
            + (self.bit_3 << 3)
            + (self.bit_4 << 4)
            + (self.bit_5 << 5)
        )

        return super().render(
            self.byte_1, UInt8(arg_1), self.depth, self.intensity, self.speed
        )

class StopWaveEffect(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Stop an existing wave effect

    ## Lazy Shell command
        `Stop battlefield wavy effect`

    ## Opcode
        `0x9D`

    ## Size
        2 bytes

    Args:
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0x9D
    _size: int = 2

    _bit_7: bool = False

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(self, bit_7: bool = False, identifier: str | None = None):
        super().__init__(identifier)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        return super().render(2 + (self.bit_7 << 7))

class ScreenEffect(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Display a screen effect by ID.

    ## Lazy Shell command
        `Screen effect...`

    ## Opcode
        `0xA3`

    ## Size
        2 bytes

    Args:
        effect (int): The ID of the effect to run
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xA3
    _size: int = 2

    _effect: UInt8

    @property
    def effect(self) -> UInt8:
        """ID of the effect to display"""
        return self._effect

    def set_effect(self, effect: int) -> None:
        """Set the ID of the effect to display"""
        assert 0 <= effect <= 20
        self._effect = UInt8(effect)

    def __init__(self, effect: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_effect(effect)

    def render(self, *args) -> bytearray:
        return super().render(self.effect)

class JmpIfTimedHitSuccess(
    UsableAnimationScriptCommand,
    AnimationScriptCommandWithJmps,
):
    """Goto destination indicated by name if s timed hit was successful.

    ## Lazy Shell command
        `On Successfully Timed-Hit, jump to address $xxxx`

    ## Opcode
        `0xA7`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xA7
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class PlaySound(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Play a sound by ID.

    ## Lazy Shell command
        `Play sound (ch.6,7)...`
        `Play sound (ch.4,5)...`

    ## Opcode
        `0xAB`
        `0xAE`

    ## Size
        2 bytes

    Args:
        sound (int): The sound ID to play.
        channel (int): The channel on which to play the sound. Needs to be 4 or 6
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2

    _sound: UInt8
    _channel: UInt4

    @property
    def sound(self) -> UInt8:
        """The sound ID to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the sound ID to play."""
        assert 0 <= sound <= 210
        self._sound = UInt8(sound)

    @property
    def channel(self) -> UInt4:
        """The channel on which to play the sound."""
        return self._channel

    def set_channel(self, channel: int) -> None:
        """Set the channel on which to play the sound. Valid values are: 4 or 6."""
        assert channel in [4, 6]
        if channel == 4:
            self._opcode = 0xAE
        else:
            self._opcode = 0xAB
        self._channel = UInt4(channel)

    def __init__(
        self, sound: int, channel: int = 6, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_channel(channel)

    def render(self, *args) -> bytearray:
        return super().render(self.sound)

class PlayMusicAtCurrentVolume(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Play a song by ID without changing volume.

    ## Lazy Shell command
        `Play music {xx} (current volume)`

    ## Opcode
        `0xB0`

    ## Size
        2 bytes

    Args:
        music (int): ID of the music to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB0
    _size: int = 2

    _music: UInt8

    @property
    def music(self) -> UInt8:
        """ID of the music to play."""
        return self._music

    def set_music(self, music: int) -> None:
        """Set ID of the music to play. It is recommended to use a music ID constant."""
        assert 0 <= music <= 73
        self._music = UInt8(music)

    def __init__(self, music: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_music(music)

    def render(self, *args) -> bytearray:
        return super().render(self.music)

class PlayMusicAtVolume(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Play a song by ID at specified volume.

    ## Lazy Shell command
        `Play music {xx} (volume = {xx})`

    ## Opcode
        `0xB1`

    ## Size
        4 bytes

    Args:
        music (int): ID of the music to play.
        volume (int): Volume of the music to play.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB1
    _size: int = 4

    _music: UInt8
    _volume: UInt16

    @property
    def music(self) -> UInt8:
        """ID of the music to play."""
        return self._music

    def set_music(self, music: int) -> None:
        """Set ID of the music to play. It is recommended to use a music ID constant."""
        self._music = UInt8(music)

    @property
    def volume(self) -> UInt16:
        """Volume of the music to play."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        "Set the relative volume of the music to play (0 to 65535)."
        self._volume = UInt16(volume)

    def __init__(
        self, music: int, volume: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_music(music)
        self.set_volume(volume)

    def render(self, *args) -> bytearray:
        return super().render(self.music, self.volume)

class StopCurrentSoundEffect(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """If a sound effect is currently playing, cancel it.

    ## Lazy Shell command
        `Stop current sound effect`

    ## Opcode
        `0xB2`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB2

class FadeCurrentMusicToVolume(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Gradually modify the volume of the current music from the current volume to the specified volume.

    ## Lazy Shell command
        `Fade out current music to {xx} volume...`

    ## Opcode
        `0xB6`

    ## Size
        3 bytes

    Args:
        speed (int): The speed at which the volume adjustment should complete.
        volume (int): Volume for the music to reach.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xB6
    _size: int = 3

    _speed: UInt8
    _volume: UInt8

    @property
    def speed(self) -> UInt8:
        """The speed at which the volume adjustment should complete."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed at which the volume adjustment should complete (0 to 255)."""
        self._speed = UInt8(speed)

    @property
    def volume(self) -> UInt8:
        """Volume for the music to reach."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        """Set the volume for the music to reach (0 to 65535)."""
        self._volume = UInt8(volume)

    def __init__(
        self, speed: int, volume: int, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_speed(speed)
        self.set_volume(volume)

    def render(self, *args) -> bytearray:
        return super().render(self.speed, self.volume)

class SetTarget(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Set battle target so a specific object.

    ## Lazy Shell command
        `Set target...`

    ## Opcode
        `0xBB`

    ## Size
        2 bytes

    Args:
        target (BattleTarget): The object ID to target.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBB
    _size: int = 2

    _target: BattleTarget

    @property
    def target(self) -> BattleTarget:
        """The object ID to target."""
        return self._target

    def set_target(self, target: BattleTarget) -> None:
        """Set the object ID to target."""
        self._target = target

    def __init__(self, target: BattleTarget, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self, *args) -> bytearray:
        return super().render(self.target)

class AddItemToStandardInventory(
    UsableAnimationScriptCommand, AnimationScriptCommandInventory
):
    """Add an item by ID to your basic item inventory (inventory denoted by the name "Items").

    ## Lazy Shell command
        `Modify item inventory...`

    ## Opcode
        `0xBC`

    ## Size
        3 bytes

    Args:
        item (type[Item]): The item to store (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBC

    def render(self, *args) -> bytearray:
        return super().render(self.item_id, 0)

class RemoveItemFromStandardInventory(
    UsableAnimationScriptCommand, AnimationScriptCommandInventory
):
    """Remove an item by ID from your basic item inventory (inventory denoted by the name "Items").

    ## Lazy Shell command
        `Modify item inventory...`

    ## Opcode
        `0xBC`

    ## Size
        3 bytes

    Args:
        item (type[Item]): The item to remove (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBC

    def render(self, *args) -> bytearray:
        return super().render(256 - self.item_id, 0xFF)

class AddItemToKeyItemInventory(
    UsableAnimationScriptCommand, AnimationScriptCommandInventory
):
    """Add an item by ID to your basic item inventory (inventory denoted by the name "Special Items").

    ## Lazy Shell command
        `Modify special item inventory...`

    ## Opcode
        `0xBD`

    ## Size
        3 bytes

    Args:
        item (type[Item]): The item to store (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBD

    def render(self, *args) -> bytearray:
        return super().render(self.item_id, 0)

class RemoveItemFromKeyItemInventory(
    UsableAnimationScriptCommand, AnimationScriptCommandInventory
):
    """Remove an item by ID from your basic item inventory (inventory denoted by the name "Special Items").

    ## Lazy Shell command
        `Modify special item inventory...`

    ## Opcode
        `0xBD`

    ## Size
        3 bytes

    Args:
        item (type[Item]): The item to remove (use an item class name from datatypes/items/implementations.py)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xBD

    def render(self, *args) -> bytearray:
        return super().render(256 - self.item_id, 0xFF)

class AddCoins(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Gain coins according to the specified amount.

    ## Lazy Shell command
        `Coins += ...`

    ## Opcode
        `0xBE`

    ## Size
        3 bytes

    Args:
        amount (int): The amount of coins to add.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 3
    _opcode = 0xBE

    _amount: UInt16

    @property
    def amount(self) -> UInt16:
        """The amount of coins to add."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the amount of coins to add."""
        self._amount = UInt16(amount)

    def __init__(self, amount: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self, *args) -> bytearray:
        return super().render(self.amount)

class AddYoshiCookiesToInventory(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Add Yoshi Cookies to your inventory according to the specified amount.

    ## Lazy Shell command
        `Store to item inventory {xx}'s Yoshi Cookie`

    ## Opcode
        `0xBF`

    ## Size
        2 bytes

    Args:
        amount (int): The amount of Yoshi Cookies to add.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _opcode = 0xBF

    _amount: UInt8

    @property
    def amount(self) -> UInt8:
        """The amount of Yoshi Cookies to add."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the amount of Yoshi Cookies to add."""
        self._amount = UInt8(amount)

    def __init__(self, amount: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self, *args) -> bytearray:
        return super().render(self.amount)

class DoMaskEffect(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Draw a specific screen mask effect by ID.

    ## Lazy Shell command
        `Mask effect...`

    ## Opcode
        `0xC3`

    ## Size
        2 bytes

    Args:
        effect (MaskEffect): The effect to draw.
        unknown_upper (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _opcode = 0xC3

    _effect: MaskEffect
    _unknown_upper: UInt8

    @property
    def effect(self) -> MaskEffect:
        """The effect to draw."""
        return self._effect

    def set_effect(self, effect: MaskEffect) -> None:
        """Set the effect to draw."""
        self._effect = effect

    @property
    def unknown_upper(self) -> UInt8:
        """(unknown)"""
        return self._unknown_upper

    def set_unknown_upper(self, unknown_upper: int) -> None:
        """(unknown)"""
        assert unknown_upper & 0x07 == 0
        self._unknown_upper = UInt8(unknown_upper)

    def __init__(
        self,
        effect: MaskEffect,
        unknown_upper: int = 0,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_effect(effect)
        self.set_unknown_upper(unknown_upper)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_upper + self.effect)

class SetMaskCoords(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Set the coords at which to draw a four-pointed mask effect. Not sure if anyone really knows how this works.

    ## Lazy Shell command
        `Mask coords = ...`

    ## Opcode
        `0xC6`

    ## Size
        (varies depending on the number of points)

    Args:
        points (list[tuple[int, int]]): The x,y coords for the 1st point.
        extra_byte (int | None): Description here to be filled out by me
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _count: int = 0
    _opcode = 0xC6

    _points: list[MaskPoint]
    _extra_byte: Int8 | None = None

    @property
    def points(self) -> list[MaskPoint]:
        """The x,y coords for the 1st point."""
        return self._points

    def set_points(self, points: list[tuple[int, int]]) -> None:
        """Set the x,y coords for the 1st point."""
        self._points = [MaskPoint(*point) for point in points]

    @property
    def size(self) -> int:
        return len(self.points) * 2 + 2 + (1 if self.extra_byte is not None else 0)

    @property
    def extra_byte(self) -> Int8 | None:
        return self._extra_byte

    def set_extra_byte(self, extra_byte: int) -> None:
        self._extra_byte = Int8(extra_byte)

    def __init__(
        self,
        points: list[tuple[int, int]],
        extra_byte: int | None = None,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_points(points)
        if extra_byte is not None:
            self.set_extra_byte(extra_byte)

    def render(self, *args) -> bytearray:
        points = [num for tup in self.points for num in tup]
        count = len(self.points) * 2
        if self.extra_byte is not None:
            points.append(self.extra_byte)
            count += 1
        return super().render(
            UInt8(count),
            *points,
        )

class SetSequenceSpeed(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Set the speed at which the sprite animation should run.

    ## Lazy Shell command
        `Sprite sequence speed = ..`

    ## Opcode
        `0xCB`

    ## Size
        2 bytes

    Args:
        speed (int): The speed a numerical value.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _size: int = 2
    _opcode = 0xCB

    _speed: UInt4

    @property
    def speed(self) -> UInt4:
        """The speed a numerical value."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed as a value from 0 to 15."""
        self._speed = UInt4(speed)

    def __init__(self, speed: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_speed(speed)

    def render(self, *args) -> bytearray:
        return super().render(self.speed)

class StartTrackingAllyButtonInputs(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """Begin the frame window for tracking button inputs for a timed hit.

    ## Lazy Shell command
        `Start tracking for Ally Button Timing`

    ## Opcode
        `0xCC`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCC

class EndTrackingAllyButtonInputs(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """End the frame window for tracking button inputs for a timed hit.

    ## Lazy Shell command
        `End tracking for Ally Button Timing`

    ## Opcode
        `0xCD`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCD

class TimingForOneTieredButtonPress(
    UsableAnimationScriptCommand, AnimationScriptCommandWithJmps
):
    """Determine the frame windows for a single timed hit that has partial timing windows. Goto the given destination if timed hit fails.

    ## Lazy Shell command
        `Timing for One Button Press: Just-OK/Perfect range`

    ## Opcode
        `0xCE`

    ## Size
        8 bytes

    Args:
        start_accepting_input (int): The number of frames after initiation at which to begin accepting a timed hit.
        end_accepting_input (int): The number of frames after initiation at which to stop accepting a timed hit.
        partial_start (int): The number of frames after initiation at which to start considering the hit
        perfect_start (int): The number of frames after initiation at which to start considering the hit
        perfect_end (int): The number of frames after initiation at which to no longer consider the hit
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCE
    _size: int = 8

    _start_accepting_input: UInt8
    _end_accepting_input: UInt8
    _partial_start: UInt8
    _perfect_start: UInt8
    _perfect_end: UInt8

    def set_input_windows(
        self,
        start_accepting_input: int | None = None,
        end_accepting_input: int | None = None,
        partial_start: int | None = None,
        perfect_start: int | None = None,
        perfect_end: int | None = None,
    ):
        """Set any and all of the frame window cutoffs for this timed hit."""
        if start_accepting_input is None:
            start_accepting_input = self.start_accepting_input
        if end_accepting_input is None:
            end_accepting_input = self.end_accepting_input
        if partial_start is None:
            partial_start = self.partial_start
        if perfect_start is None:
            perfect_start = self.perfect_start
        if perfect_end is None:
            perfect_end = self.perfect_end

        assert (
            start_accepting_input
            <= partial_start
            <= perfect_start
            <= perfect_end
            <= end_accepting_input
        )

        self._start_accepting_input = UInt8(start_accepting_input)
        self._end_accepting_input = UInt8(end_accepting_input)
        self._partial_start = UInt8(partial_start)
        self._perfect_start = UInt8(perfect_start)
        self._perfect_end = UInt8(perfect_end)

    @property
    def start_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to begin accepting a timed hit."""
        return self._start_accepting_input

    def set_start_accepting_input(self, start_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to begin accepting a timed hit."""
        self.set_input_windows(start_accepting_input=start_accepting_input)

    @property
    def end_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to stop accepting a timed hit."""
        return self._end_accepting_input

    def set_end_accepting_input(self, end_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to stop accepting a timed hit."""
        self.set_input_windows(end_accepting_input=end_accepting_input)

    @property
    def partial_start(self) -> UInt8:
        """The number of frames after initiation at which to start considering the hit
        partially timed."""
        return self._partial_start

    def set_partial_start(self, partial_start: int) -> None:
        """Set the number of frames after initiation at which to start considering the hit
        partially timed."""
        self.set_input_windows(partial_start=partial_start)

    @property
    def perfect_start(self) -> UInt8:
        """The number of frames after initiation at which to start considering the hit
        perfectly timed."""
        return self._perfect_start

    def set_perfect_start(self, perfect_start: int) -> None:
        """Set the number of frames after initiation at which to start considering the hit
        perfectly timed."""
        self.set_input_windows(perfect_start=perfect_start)

    @property
    def perfect_end(self) -> UInt8:
        """The number of frames after initiation at which to no longer consider the hit
        perfectly timed."""
        return self._perfect_end

    def set_perfect_end(self, perfect_end: int) -> None:
        """Set the number of frames after initiation at which to no longer consider the hit
        perfectly timed."""
        self.set_input_windows(perfect_end=perfect_end)

    def __init__(
        self,
        start_accepting_input: int,
        end_accepting_input: int,
        partial_start: int,
        perfect_start: int,
        perfect_end: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_input_windows(
            start_accepting_input,
            end_accepting_input,
            partial_start,
            perfect_start,
            perfect_end,
        )

    def render(self, *args) -> bytearray:
        return super().render(
            self.end_accepting_input,
            self.start_accepting_input,
            self.partial_start,
            self.perfect_start,
            self.perfect_end,
            *self.destinations,
        )

class TimingForOneBinaryButtonPress(
    UsableAnimationScriptCommand, AnimationScriptCommandWithJmps
):
    """Determine the frame windows for a single timed hit that is either hit or not hit, no partial windows. Goto the given destination if timed hit fails.

    ## Lazy Shell command
        `Timing for One Button Press: Any timing range`

    ## Opcode
        `0xCF`

    ## Size
        6 bytes

    Args:
        start_accepting_input (int): The number of frames after initiation at which to begin accepting a timed hit.
        end_accepting_input (int): The number of frames after initiation at which to stop accepting a timed hit.
        timed_hit_ends (int): The number of frames after initiation at which the input no longer registers as
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xCF
    _size: int = 6

    _start_accepting_input: UInt8
    _end_accepting_input: UInt8
    _timed_hit_ends: UInt8

    def set_input_windows(
        self,
        start_accepting_input: int | None = None,
        end_accepting_input: int | None = None,
        timed_hit_ends: int | None = None,
    ):
        """Set any and all of the frame window cutoffs for this timed hit."""
        if start_accepting_input is None:
            start_accepting_input = self.start_accepting_input
        if end_accepting_input is None:
            end_accepting_input = self.end_accepting_input
        if timed_hit_ends is None:
            timed_hit_ends = self.timed_hit_ends
        assert start_accepting_input <= timed_hit_ends <= end_accepting_input
        self._start_accepting_input = UInt8(start_accepting_input)
        self._end_accepting_input = UInt8(end_accepting_input)
        self._timed_hit_ends = UInt8(timed_hit_ends)

    @property
    def start_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to begin accepting a timed hit."""
        return self._start_accepting_input

    def set_start_accepting_input(self, start_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to begin accepting a timed hit."""
        self.set_input_windows(start_accepting_input=start_accepting_input)

    @property
    def end_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to stop accepting a timed hit."""
        return self._end_accepting_input

    def set_end_accepting_input(self, end_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to stop accepting a timed hit."""
        self.set_input_windows(end_accepting_input=end_accepting_input)

    @property
    def timed_hit_ends(self) -> UInt8:
        """The number of frames after initiation at which the input no longer registers as
        a successful timed hit."""
        return self._timed_hit_ends

    def set_timed_hit_ends(self, timed_hit_ends: int) -> None:
        """Set the number of frames after initiation at which the input no longer registers as
        a successful timed hit."""
        self.set_input_windows(timed_hit_ends=timed_hit_ends)

    def __init__(
        self,
        start_accepting_input: int,
        end_accepting_input: int,
        timed_hit_ends: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_input_windows(
            start_accepting_input, end_accepting_input, timed_hit_ends
        )

    def render(self, *args) -> bytearray:
        return super().render(
            self.end_accepting_input,
            self.start_accepting_input,
            self.timed_hit_ends,
            *self.destinations,
        )

class TimingForMultipleButtonPresses(
    UsableAnimationScriptCommand, AnimationScriptCommandWithJmps
):
    """Determine the frame windows for a timed hit that considers multiple A/B/X/Y inputs starting from a certain frame.

    ## Lazy Shell command
        `Timing for Multiple Button Presses: Wait # frames, then jump`

    ## Opcode
        `0xD0`

    ## Size
        4 bytes

    Args:
        start_accepting_input (int): The number of frames after initiation at which to begin accepting input.
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD0
    _size: int = 4

    _start_accepting_input: UInt8

    @property
    def start_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to begin accepting input."""
        return self._start_accepting_input

    def set_start_accepting_input(self, start_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to begin accepting input."""
        self._start_accepting_input = UInt8(start_accepting_input)

    def __init__(
        self,
        start_accepting_input: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_start_accepting_input(start_accepting_input)

    def render(self, *args) -> bytearray:
        return super().render(self.start_accepting_input, *self.destinations)

class TimingForButtonMashUnknown(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """(unknown)

    ## Lazy Shell command
        `Timing for Button Mash: ???`

    ## Opcode
        `0xD1`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD1

class TimingForButtonMashCount(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Determine the cap for a timed hit that counts up to a certain number of A/B/X/Y inputs of an indiscriminate window.

    ## Lazy Shell command
        `Timing for Button Mash: Possible Power-ups range`

    ## Opcode
        `0xD2`

    ## Size
        2 bytes

    Args:
        max_presses (int): The number of button presses at which the timed hit is capped.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD2
    _size: int = 2

    _max_presses: UInt8

    @property
    def max_presses(self) -> UInt8:
        """The number of button presses at which the timed hit is capped."""
        return self._max_presses

    def set_max_presses(self, max_presses: int) -> None:
        """Set the number of button presses at which the timed hit is capped."""
        self._max_presses = UInt8(max_presses)

    def __init__(self, max_presses: int, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_max_presses(max_presses)

    def render(self, *args) -> bytearray:
        return super().render(self.max_presses)

class TimingForRotationCount(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Define a timed hit that counts up to a certain number of D-pad inputs within a specified frame window.

    ## Lazy Shell command
        `Timing for Rotation: Frame range, Possible Power-ups range`

    ## Opcode
        `0xD3`

    ## Size
        4 bytes

    Args:
        start_accepting_input (int): The number of frames after initiation at which inputs can begin
        end_accepting_input (int): The number of frames after initiation at which to no longer accept inputs.
        max_presses (int): The number of button presses at which the timed hit is capped.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD3
    _size: int = 4

    _start_accepting_input: UInt8
    _end_accepting_input: UInt8
    _max_presses: UInt8

    def set_input_windows(
        self,
        start_accepting_input: int | None = None,
        end_accepting_input: int | None = None,
    ):
        """Set any and all of the frame window cutoffs for this timed hit."""
        if start_accepting_input is None:
            start_accepting_input = self.start_accepting_input
        if end_accepting_input is None:
            end_accepting_input = self.end_accepting_input
        assert start_accepting_input <= end_accepting_input
        self._start_accepting_input = UInt8(start_accepting_input)
        self._end_accepting_input = UInt8(end_accepting_input)

    @property
    def start_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which inputs can begin
        being accepted."""
        return self._start_accepting_input

    def set_start_accepting_input(self, start_accepting_input: int) -> None:
        """Set the number of frames after initiation at which inputs can begin
        being accepted."""
        self.set_input_windows(start_accepting_input=start_accepting_input)

    @property
    def end_accepting_input(self) -> UInt8:
        """The number of frames after initiation at which to no longer accept inputs."""
        return self._end_accepting_input

    def set_end_accepting_input(self, end_accepting_input: int) -> None:
        """Set the number of frames after initiation at which to no longer accept inputs."""
        self.set_input_windows(end_accepting_input=end_accepting_input)

    @property
    def max_presses(self) -> UInt8:
        """The number of button presses at which the timed hit is capped."""
        return self._max_presses

    def set_max_presses(self, max_presses: int) -> None:
        """Set the number of button presses at which the timed hit is capped."""
        self._max_presses = UInt8(max_presses)

    def __init__(
        self,
        start_accepting_input: int,
        end_accepting_input: int,
        max_presses: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_input_windows(start_accepting_input, end_accepting_input)
        self.set_max_presses(max_presses)

    def render(self, *args) -> bytearray:
        return super().render(
            self.end_accepting_input, self.start_accepting_input, self.max_presses
        )

class TimingForChargePress(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Define a timed hit that requires you to hold down one of A/B/X/Y for a continuous interval, with results differing based on how long it is held.

    ## Lazy Shell command
        `Timing for Held Button: Hold for frame range`

    ## Opcode
        `0xD4`

    ## Size
        6 bytes

    Args:
        charge_level_1_end (int): The number of frames after initiation at which the button can be released
        charge_level_2_end (int): The number of frames after initiation at which the button can be released
        charge_level_3_end (int): The number of frames after initiation at which the button can be released
        charge_level_4_end (int): The number of frames after initiation at which the button can be released
        overcharge_end (int): The number of frames after initiation at which the button can be released, having
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD4
    _size: int = 6

    _charge_level_1_end: UInt8
    _charge_level_2_end: UInt8
    _charge_level_3_end: UInt8
    _charge_level_4_end: UInt8
    _overcharge_end: UInt8

    def set_input_windows(
        self,
        charge_level_1_end: int | None = None,
        charge_level_2_end: int | None = None,
        charge_level_3_end: int | None = None,
        charge_level_4_end: int | None = None,
        overcharge_end: int | None = None,
    ):
        """Set any and all of the charge window cutoffs for this timed hit."""
        if charge_level_1_end is None:
            charge_level_1_end = self.charge_level_1_end
        if charge_level_2_end is None:
            charge_level_2_end = self.charge_level_2_end
        if charge_level_3_end is None:
            charge_level_3_end = self.charge_level_3_end
        if charge_level_4_end is None:
            charge_level_4_end = self.charge_level_4_end
        if overcharge_end is None:
            overcharge_end = self.overcharge_end

        assert (
            charge_level_1_end
            <= charge_level_2_end
            <= charge_level_3_end
            <= charge_level_4_end
            <= overcharge_end
        )
        self._charge_level_1_end = UInt8(charge_level_1_end)
        self._charge_level_2_end = UInt8(charge_level_2_end)
        self._charge_level_3_end = UInt8(charge_level_3_end)
        self._charge_level_4_end = UInt8(charge_level_4_end)
        self._overcharge_end = UInt8(overcharge_end)

    @property
    def charge_level_1_end(self) -> UInt8:
        """The number of frames after initiation at which the button can be released
        for the lowest partially-charged damage output."""
        return self._charge_level_1_end

    def set_charge_level_1_end(self, charge_level_1_end: int) -> None:
        """Set the number of frames after initiation at which the button can be released
        for the lowest partially-charged damage output."""
        self.set_input_windows(charge_level_1_end=charge_level_1_end)

    @property
    def charge_level_2_end(self) -> UInt8:
        """The number of frames after initiation at which the button can be released
        for the middle range of damage output."""
        return self._charge_level_2_end

    def set_charge_level_2_end(self, charge_level_2_end: int) -> None:
        """Set the number of frames after initiation at which the button can be released
        for the middle range of damage output."""
        self.set_input_windows(charge_level_2_end=charge_level_2_end)

    @property
    def charge_level_3_end(self) -> UInt8:
        """The number of frames after initiation at which the button can be released
        for the highest partially-charged damage output."""
        return self._charge_level_3_end

    def set_charge_level_3_end(self, charge_level_3_end: int) -> None:
        """Set the number of frames after initiation at which the button can be released
        for the highest partially-charged damage output."""
        self.set_input_windows(charge_level_3_end=charge_level_3_end)

    @property
    def charge_level_4_end(self) -> UInt8:
        """The number of frames after initiation at which the button can be released
        for the maximum possible damage output."""
        return self._charge_level_4_end

    def set_charge_level_4_end(self, charge_level_4_end: int) -> None:
        """Set the number of frames after initiation at which the button can be released
        for the maximum possible damage output."""
        self.set_input_windows(charge_level_4_end=charge_level_4_end)

    @property
    def overcharge_end(self) -> UInt8:
        """The number of frames after initiation at which the button can be released, having
        been charged so long that the output resets to the lowest possible amount."""
        return self._overcharge_end

    def set_overcharge_end(self, overcharge_end: int) -> None:
        """Set the number of frames after initiation at which the button can be released, having
        been charged so long that the output resets to the lowest possible amount."""
        self.set_input_windows(overcharge_end=overcharge_end)

    def __init__(
        self,
        charge_level_1_end: int,
        charge_level_2_end: int,
        charge_level_3_end: int,
        charge_level_4_end: int,
        overcharge_end: int,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_input_windows(
            charge_level_1_end,
            charge_level_2_end,
            charge_level_3_end,
            charge_level_4_end,
            overcharge_end,
        )

    def render(self, *args) -> bytearray:
        return super().render(
            self.charge_level_1_end,
            self.charge_level_2_end,
            self.charge_level_3_end,
            self.charge_level_4_end,
            self.overcharge_end,
        )

class SummonMonster(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Summon a monster of a specified enemy class.

    ## Lazy Shell command
        `Summon monster...`

    ## Opcode
        `0xD5`

    ## Size
        4 bytes

    Args:
        monster (type['Enemy']): The class of the monster type to summon.
        position (int): The formation position to summon the monster to.
        bit_0 (bool): (unknown)
        bit_1 (bool): (unknown)
        bit_2 (bool): (unknown)
        bit_3 (bool): (unknown)
        bit_4 (bool): (unknown)
        bit_5 (bool): (unknown)
        bit_6 (bool): (unknown)
        bit_7 (bool): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD5
    _size: int = 4

    _monster: type["Enemy"]
    _position: UInt4
    _bit_0: bool
    _bit_1: bool
    _bit_2: bool
    _bit_3: bool
    _bit_4: bool
    _bit_5: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def monster(self) -> type["Enemy"]:
        """The class of the monster type to summon."""
        return self._monster

    def set_monster(self, monster: type["Enemy"]) -> None:
        """Set the class of the monster type to summon."""
        self._monster = monster

    @property
    def position(self) -> UInt4:
        """The formation position to summon the monster to."""
        return self._position

    def set_position(self, position: int) -> None:
        """Set the formation position to summon the monster to."""
        assert 0 <= position <= 7
        self._position = UInt4(position)

    @property
    def bit_0(self) -> bool:
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def bit_1(self) -> bool:
        """(unknown)"""
        return self._bit_1

    def set_bit_1(self, bit_1: bool) -> None:
        """(unknown)"""
        self._bit_1 = bit_1

    @property
    def bit_2(self) -> bool:
        """(unknown)"""
        return self._bit_2

    def set_bit_2(self, bit_2: bool) -> None:
        """(unknown)"""
        self._bit_2 = bit_2

    @property
    def bit_3(self) -> bool:
        """(unknown)"""
        return self._bit_3

    def set_bit_3(self, bit_3: bool) -> None:
        """(unknown)"""
        self._bit_3 = bit_3

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        monster: type["Enemy"],
        position: int,
        bit_0: bool = False,
        bit_1: bool = False,
        bit_2: bool = False,
        bit_3: bool = False,
        bit_4: bool = False,
        bit_5: bool = False,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: str | None = None,
    ) -> None:
        super().__init__(identifier)
        self.set_monster(monster)
        self.set_position(position)
        self.set_bit_0(bit_0)
        self.set_bit_1(bit_1)
        self.set_bit_2(bit_2)
        self.set_bit_3(bit_3)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self, *args) -> bytearray:
        byte1: int = bools_to_int(
            self.bit_0,
            self.bit_1,
            self.bit_2,
            self.bit_3,
            self.bit_4,
            self.bit_5,
            self.bit_6,
            self.bit_7,
        )
        return super().render(byte1, self.monster().monster_id, self.position)

class MuteTimingJmp(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """(unknown, related somehow to Mute attack timing)

    ## Lazy Shell command
        `Timing for Mute: ??? then jump`

    ## Opcode
        `0xD8`

    ## Size
        3 bytes

    Args:
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to jump to.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD8
    _size: int = 3

    def render(self, *args) -> bytearray:
        return super().render(*self.destinations)

class DisplayCantRunDialog(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Display the "Can't Run" dialog

    ## Lazy Shell command
        `Display "Can't run" dialogue`

    ## Opcode
        `0xD9`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xD9

class StoreOMEM60ToItemInventory(
    UsableAnimationScriptCommand, AnimationScriptCommandNoArgs
):
    """An item with its ID matching the value at OMEM $60 is added to inventoy.

    ## Lazy Shell command
        `Store OMEM $60 to item inventory`

    ## Opcode
        `0xE0`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE0

class RunBattleEvent(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Run a battle event (battle animation script type) by ID.

    ## Lazy Shell command
        `Run battle event...`

    ## Opcode
        `0xE1`

    ## Size
        4 bytes

    Args:
        script_id (int): The ID of the battle event to run.
        offset (int): (unknown)
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _opcode = 0xE1
    _size: int = 4

    _script_id: UInt16
    _offset: UInt8

    @property
    def script_id(self) -> UInt16:
        """The ID of the battle event to run."""
        return self._script_id

    def set_script_id(self, script_id: int) -> None:
        """Set the ID of the battle event to run.
        It is recommended to use battle event ID constants for this."""
        self._script_id = UInt16(script_id)

    @property
    def offset(self) -> UInt8:
        """(unknown)"""
        return self._offset

    def set_offset(self, offset: int) -> None:
        """(unknown)"""
        self._offset = UInt8(offset)

    def __init__(
        self, script_id: int, offset: int = 0, identifier: str | None = None
    ) -> None:
        super().__init__(identifier)
        self.set_script_id(script_id)
        self.set_offset(offset)

    def render(self, *args) -> bytearray:
        return super().render(self.script_id, self.offset)

class UnknownCommand(UsableAnimationScriptCommand, AnimationScriptCommand):
    """Catch-all command class representing any command not represented by other AnimationScriptCommand subclasses.
    Use this sparingly as there are no safety checks to make sure that the number of arguments in the command are correct.

    ## Lazy Shell command
        Any that don't have a name

    ## Opcode
        Any that aren't used by other classes

    ## Size
        Variable

    Args:
        contents (bytearray): The whole contents of the command as bytes, including the opcode.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """

    _contents: bytearray

    @property
    def contents(self) -> bytearray:
        """The whole contents of the command as bytes, including the opcode."""
        return self._contents

    def set_contents(self, contents: bytearray) -> None:
        """Set the whole contents of the command as bytes, including the opcode."""
        self._contents = contents

    @property
    def size(self) -> int:
        return len(self.contents)

    def __init__(self, contents: bytearray, identifier: str | None = None) -> None:
        super().__init__(identifier)
        self.set_contents(contents)

    def render(self, *args) -> bytearray:
        return super().render(self.contents)

class ActorExitBattleEXPERIMENTAL(UsableAnimationScriptCommand, AnimationScriptCommandNoArgs):
    """Run opcode 0x02, which is only used in animations where an actor is leaving the battle (escape, deaths, etc).
    Unsure what this actually does. Treating it as a terminating byte to see if it solves any animation code mysteries.

    ## Opcode
        `0x02`

    ## Size
        1 byte

    Args:
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """
    
    _opcode = 0x02

class SpriteQueueReferenceEXPERIMENTAL(UsableAnimationScriptCommand, AnimationScriptCommandWithJmps):
    """Run opcode 0x47. Treating it as a sprite queue pointer to see if it solves any animation code mysteries.

    ## Opcode
        `0x47`

    ## Size
        4 bytes

    Args:   
        unknown_byte (int): (unknown)
        destinations (list[str]): This should be a list of exactly one `str`. The `str` should be the label of the command to start at.
        identifier (str | None): Give this command a label if you want another command to jump to it.
    """
    
    _opcode = 0x47
    _size: int = 4

    _unknown_byte: UInt8

    @property
    def unknown_byte(self) -> UInt8:
        """(unknown)"""
        return self._unknown_byte

    def set_unknown_byte(self, unknown_byte: int) -> None:
        """(unknown)"""
        self._unknown_byte = UInt8(unknown_byte)

    def __init__(
        self,
        unknown_byte: int,
        destinations: list[str],
        identifier: str | None = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_destinations(destinations)
        self.set_unknown_byte(unknown_byte)

    def render(self, *args) -> bytearray:
        return super().render(self.unknown_byte, *self.destinations)

commands = [
    NewSpriteAtCoords,
    SetAMEM32ToXYZCoords,
    DrawSpriteAtAMEM32Coords,
    PauseScriptUntil,
    RemoveObject,
    ReturnObjectQueue,
    MoveObject,
    Jmp,
    Pause1Frame,
    SetAMEM40ToXYZCoords,
    MoveSpriteToCoords,
    ResetTargetMappingMemory,
    ResetObjectMappingMemory,
    RunSubroutine,
    ReturnSubroutine,
    VisibilityOn,
    VisibilityOff,
    SetAMEM8BitToConst,
    SetAMEM16BitToConst,
    JmpIfAMEM8BitEqualsConst,
    JmpIfAMEM16BitEqualsConst,
    JmpIfAMEM8BitNotEqualsConst,
    JmpIfAMEM16BitNotEqualsConst,
    JmpIfAMEM8BitLessThanConst,
    JmpIfAMEM16BitLessThanConst,
    JmpIfAMEM8BitGreaterOrEqualThanConst,
    JmpIfAMEM16BitGreaterOrEqualThanConst,
    SetAMEM8BitToUnknownShort,
    SetAMEM16BitToUnknownShort,
    SetAMEM8BitTo7E1x,
    SetAMEM16BitTo7E1x,
    Set7E1xToAMEM8Bit,
    Set7E1xToAMEM16Bit,
    JmpIfAMEM8BitEquals7E1x,
    JmpIfAMEM16BitEquals7E1x,
    JmpIfAMEM8BitNotEquals7E1x,
    JmpIfAMEM16BitNotEquals7E1x,
    JmpIfAMEM8BitLessThan7E1x,
    JmpIfAMEM16BitLessThan7E1x,
    JmpIfAMEM8BitGreaterOrEqualThan7E1x,
    JmpIfAMEM16BitGreaterOrEqualThan7E1x,
    SetAMEM8BitTo7F,
    SetAMEM16BitTo7F,
    Set7FToAMEM8Bit,
    Set7FToAMEM16Bit,
    JmpIfAMEM8BitEquals7F,
    JmpIfAMEM16BitEquals7F,
    JmpIfAMEM8BitNotEquals7F,
    JmpIfAMEM16BitNotEquals7F,
    JmpIfAMEM8BitLessThan7F,
    JmpIfAMEM16BitLessThan7F,
    JmpIfAMEM8BitGreaterOrEqualThan7F,
    JmpIfAMEM16BitGreaterOrEqualThan7F,
    SetAMEM8BitToAMEM,
    SetAMEM16BitToAMEM,
    SetAMEMToAMEM8Bit,
    SetAMEMToAMEM16Bit,
    JmpIfAMEM8BitEqualsAMEM,
    JmpIfAMEM16BitEqualsAMEM,
    JmpIfAMEM8BitNotEqualsAMEM,
    JmpIfAMEM16BitNotEqualsAMEM,
    JmpIfAMEM8BitLessThanAMEM,
    JmpIfAMEM16BitLessThanAMEM,
    JmpIfAMEM8BitGreaterOrEqualThanAMEM,
    JmpIfAMEM16BitGreaterOrEqualThanAMEM,
    SetAMEM8BitToOMEMCurrent,
    SetAMEM16BitToOMEMCurrent,
    SetOMEMCurrentToAMEM8Bit,
    SetOMEMCurrentToAMEM16Bit,
    JmpIfAMEM8BitEqualsOMEMCurrent,
    JmpIfAMEM16BitEqualsOMEMCurrent,
    JmpIfAMEM8BitNotEqualsOMEMCurrent,
    JmpIfAMEM16BitNotEqualsOMEMCurrent,
    JmpIfAMEM8BitLessThanOMEMCurrent,
    JmpIfAMEM16BitLessThanOMEMCurrent,
    JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent,
    JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent,
    SetAMEM8BitTo7E5x,
    SetAMEM16BitTo7E5x,
    Set7E5xToAMEM8Bit,
    Set7E5xToAMEM16Bit,
    JmpIfAMEM8BitEquals7E5x,
    JmpIfAMEM16BitEquals7E5x,
    JmpIfAMEM8BitNotEquals7E5x,
    JmpIfAMEM16BitNotEquals7E5x,
    JmpIfAMEM8BitLessThan7E5x,
    JmpIfAMEM16BitLessThan7E5x,
    JmpIfAMEM8BitGreaterOrEqualThan7E5x,
    JmpIfAMEM16BitGreaterOrEqualThan7E5x,
    SetAMEM8BitToOMEMMain,
    SetAMEM16BitToOMEMMain,
    SetOMEMMainToAMEM8Bit,
    SetOMEMMainToAMEM16Bit,
    JmpIfAMEM8BitEqualsOMEMMain,
    JmpIfAMEM16BitEqualsOMEMMain,
    JmpIfAMEM8BitNotEqualsOMEMMain,
    JmpIfAMEM16BitNotEqualsOMEMMain,
    JmpIfAMEM8BitLessThanOMEMMain,
    JmpIfAMEM16BitLessThanOMEMMain,
    JmpIfAMEM8BitGreaterOrEqualThanOMEMMain,
    JmpIfAMEM16BitGreaterOrEqualThanOMEMMain,
    SetUnknownShortToAMEM8Bit,
    SetUnknownShortToAMEM16Bit,
    JmpIfAMEM8BitEqualsUnknownShort,
    JmpIfAMEM16BitEqualsUnknownShort,
    JmpIfAMEM8BitNotEqualsUnknownShort,
    JmpIfAMEM16BitNotEqualsUnknownShort,
    JmpIfAMEM8BitLessThanUnknownShort,
    JmpIfAMEM16BitLessThanUnknownShort,
    JmpIfAMEM8BitGreaterOrEqualThanUnknownShort,
    JmpIfAMEM16BitGreaterOrEqualThanUnknownShort,
    IncAMEM8BitByConst,
    IncAMEM8BitBy7E1x,
    IncAMEM8BitBy7F,
    IncAMEM8BitByAMEM,
    IncAMEM8BitByOMEMCurrent,
    IncAMEM8BitBy7E5x,
    IncAMEM8BitByOMEMMain,
    IncAMEM16BitByConst,
    IncAMEM16BitBy7E1x,
    IncAMEM16BitBy7F,
    IncAMEM16BitByAMEM,
    IncAMEM16BitByOMEMCurrent,
    IncAMEM16BitBy7E5x,
    IncAMEM16BitByOMEMMain,
    DecAMEM8BitByConst,
    DecAMEM8BitBy7E1x,
    DecAMEM8BitBy7F,
    DecAMEM8BitByAMEM,
    DecAMEM8BitByOMEMCurrent,
    DecAMEM8BitBy7E5x,
    DecAMEM8BitByOMEMMain,
    DecAMEM16BitByConst,
    DecAMEM16BitBy7E1x,
    DecAMEM16BitBy7F,
    DecAMEM16BitByAMEM,
    DecAMEM16BitByOMEMCurrent,
    DecAMEM16BitBy7E5x,
    DecAMEM16BitByOMEMMain,
    IncAMEM8BitByUnknownShort,
    IncAMEM16BitByUnknownShort,
    DecAMEM8BitByUnknownShort,
    DecAMEM16BitByUnknownShort,
    IncAMEM8Bit,
    IncAMEM16Bit,
    DecAMEM8Bit,
    DecAMEM16Bit,
    ClearAMEM8Bit,
    ClearAMEM16Bit,
    SetAMEMBits,
    ClearAMEMBits,
    JmpIfAMEMBitsSet,
    JmpIfAMEMBitsClear,
    AttackTimerBegins,
    PauseScriptUntilAMEMBitsSet,
    PauseScriptUntilAMEMBitsClear,
    SpriteSequence,
    SetAMEM60ToCurrentTarget,
    PauseScriptUntilSpriteSequenceDone,
    JmpIfTargetDisabled,
    JmpIfTargetEnabled,
    UseSpriteQueue,
    ReturnSpriteQueue,
    DisplayMessageAtOMEM60As,
    UseObjectQueueAtOffsetWithAMEM60Index,
    UseObjectQueueAtOffsetWithAMEM60PointerOffset,
    SetOMEM60To072C,
    SetAMEMToRandomByte,
    SetAMEMToRandomShort,
    EnableSpritesOnSubscreen,
    DisableSpritesOnSubscreen,
    NewEffectObject,
    Pause2Frames,
    PauseScriptUntilBitsClear,
    ClearEffectIndex,
    Layer3On,
    Layer3Off,
    DisplayMessage,
    PauseScriptUntilDialogClosed,
    FadeOutObject,
    ResetSpriteSequence,
    ShineEffect,
    FadeOutEffect,
    FadeOutSprite,
    FadeOutScreen,
    FadeInEffect,
    FadeInSprite,
    FadeInScreen,
    ShakeScreen,
    ShakeSprites,
    ShakeScreenAndSprites,
    StopShakingObject,
    ScreenFlashWithDuration,
    ScreenFlash,
    InitializeBonusMessageSequence,
    DisplayBonusMessage,
    PauseScriptUntilBonusMessageComplete,
    ScreenEffect,
    PlaySound,
    PlayMusicAtCurrentVolume,
    PlayMusicAtVolume,
    StopCurrentSoundEffect,
    FadeCurrentMusicToVolume,
    SetTarget,
    AddItemToStandardInventory,
    RemoveItemFromStandardInventory,
    AddItemToKeyItemInventory,
    RemoveItemFromKeyItemInventory,
    AddCoins,
    AddYoshiCookiesToInventory,
    DoMaskEffect,
    SetMaskCoords,
    SetSequenceSpeed,
    StartTrackingAllyButtonInputs,
    EndTrackingAllyButtonInputs,
    TimingForOneTieredButtonPress,
    TimingForOneBinaryButtonPress,
    TimingForMultipleButtonPresses,
    TimingForButtonMashUnknown,
    TimingForButtonMashCount,
    TimingForOneBinaryButtonPress,
    TimingForChargePress,
    SummonMonster,
    DisplayCantRunDialog,
    StoreOMEM60ToItemInventory,
    RunBattleEvent,
    WaveEffect,
    StopWaveEffect,
    JmpIfTimedHitSuccess,
    UnknownCommand,
    ActorExitBattleEXPERIMENTAL,
    SpriteQueueReferenceEXPERIMENTAL
]
