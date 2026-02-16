from __future__ import annotations

from typing import TYPE_CHECKING, Any

from randomizer.data.variables.event_palette_names import (
    EPAL0084_MARIO_ENDING,
    EPAL0085_MALLOW_ENDING,
    EPAL0086_GENO_ENDING,
    EPAL0140_BOWSER_ENDING,
    EPAL0141_TOADSTOOL_ENDING,
    EPAL0142_HOTSPRING,
    EPAL0163_MARIO_ENDING_DARK,
    EPAL0164_TOADSTOOL_ENDING_DARK,
    EPAL0165_BOWSER_ENDING_DARK,
    EPAL0166_MALLOW_ENDING_DARK,
    EPAL0167_GENO_ENDING_DARK,
)
from randomizer.data.variables.sprite_palette_names import (
    SPAL477_OLD_CLASSIC_MARIO,
    SPAL503_RED_MUSHROOM,
    SPAL504_TOADSTOOL_3,
    SPAL505_BOWSER_3,
    SPAL506_MALLOW_3,
    SPAL507_GENO_3,
    SPAL508_MARIO_S_BATTLE_PORTRAIT,
    SPAL510_MARIO_PSN_3,
    SPAL529_MINECART_RIDER,
    SPAL607_MARIO_PSN_4,
    SPAL628_MARIO_WALKING_DOWN_LEFT,
    SPAL630_MARIO_PSN_1,
    SPAL632_MARIO_DARK_1,
    SPAL634_MARIO_DOLL_SURPRISED,
    SPAL636_GENO_DOLL,
    SPAL637_BOWSER_DOLL,
    SPAL638_TOADSTOOL_DOLL,
    SPAL639,
    SPAL644_MARIO_ATTACK_UP_RIGHT,
    SPAL646_MARIO_PSN_2,
    SPAL648_MARIO_DARK_2,
    SPAL654_TOADSTOOL_WALKING_DOWN_LEFT,
    SPAL656_TOADSTOOL_PSN_1,
    SPAL658_TOADSTOOL_DARK_1,
    SPAL659_TOADSTOOL_SLAP_ATTACK,
    SPAL661_TOADSTOOL_PSN_2,
    SPAL663_TOADSTOOL_DARK_2,
    SPAL664_BOWSER_WALKING_DOWN_LEFT,
    SPAL666_BOWSER_PSN_1,
    SPAL668_BOWSER_DARK_1,
    SPAL669_BOWSER_CLAW_ATTACK,
    SPAL671_BOWSER_PSN_2,
    SPAL673_BOWSER_DARK_2,
    SPAL685_GENO_WALKING_DOWN_LEFT,
    SPAL687_GENO_PSN_1,
    SPAL689_GENO_DARK,
    SPAL691_GENO_ELBOW_SHOT,
    SPAL693_GENO_PSN_2,
    SPAL695_GENO_DARK_2,
    SPAL697_MALLOW_WALKING_DOWN_LEFT,
    SPAL699_MALLOW_PSN_1,
    SPAL701_MALLOW_DARK,
    SPAL702_MALLOW_PUNCH,
    SPAL704_MALLOW_PSN_2,
    SPAL706_MALLOW_DARK_2,
    SPAL797_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def color_to_bytes(color: int | str) -> list[int]:
    # Handle both integer colors (0xF8F8F8) and hex strings ("F8F8F8")
    color_int = color if isinstance(color, int) else int(color, 16)
    r = color_int >> 19
    g = (color_int >> 10) & 0x3E
    b = (color_int >> 1) & 0x7C

    byte_1 = r + ((g << 4) & 0xF0)
    byte_2 = b + (g >> 4)
    return [byte_1, byte_2]


def palette_to_bytes(colors) -> list[int]:
    ret = []
    for color in colors:
        ret += color_to_bytes(color)
    return ret

    


MAP_PALETTE_OFFSET = 0x3E99C1


class Palette:
    id: Any | None = None
    colours: list[int] | None = None
    poison_colours: list[int] | None = None
    underwater_colours: list[int] | None = None
    classic_colours: list[int] | None = None
    overworld_map_colours: list[int] | None = None
    original_name = ""
    name = ""
    author = ""
    rename_character = True

    def transform(
        self, base: list[int], colours: list[int], indexes: list[int | None]
    ) -> list[int]:
        output = []
        for i, j in enumerate(indexes):
            output.append(colours[j] if j is not None else base[i])
        return output

    def mutate(self, colours: list[int], indexes: list[int]) -> list[int]:
        output = []
        for i in indexes:
            output.append(colours[i])
        return output

    @property
    def clone_name(self) -> str:
        name = (self.name if self.rename_character else self.original_name).upper()
        if len(name) <= 7:
            return f"{name} CLONE"
        if len(name) <= 8:
            return f"{name} COPY"
        if len(name) <= 11:
            return f"{name} 2"
        return f"{name[0:10]}. 2"

    @property
    def strong_clone_name(self) -> str:
        name = (self.name if self.rename_character else self.original_name).upper()
        if len(name) <= 5:
            return f"{name} CLONE S"
        if len(name) <= 6:
            return f"{name} COPY S"
        if len(name) <= 11:
            return f"{name} 3"
        return f"{name[0:10]}. 3"
    
    def render(self, world: GameWorld) -> dict[int, bytearray]:
        return {}


class MarioPalette(Palette):
    name = "Mario"
    _original_name = "Mario"

    def render(self, world: GameWorld) -> dict[int, bytearray]:
        output = {}
        if self.colours is not None:
            world.sprite_palettes.get_palette(
                SPAL628_MARIO_WALKING_DOWN_LEFT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL644_MARIO_ATTACK_UP_RIGHT).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(
                SPAL508_MARIO_S_BATTLE_PORTRAIT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(EPAL0084_MARIO_ENDING).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL634_MARIO_DOLL_SURPRISED).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL503_RED_MUSHROOM).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL639).set_colors(self.colours)
            world.event_palettes.get_palette(EPAL0084_MARIO_ENDING).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(
                SPAL797_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE
            ).set_colors(
                self.mutate(
                    self.colours, [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14]
                )
            )
            output[0x3EDFFD] = bytearray(palette_to_bytes(self.colours))
            output[0x3EE0FF] = bytearray(palette_to_bytes(self.colours))
            if world.overworld_character.ally.index == 0:
                heated_palette = [*self.colours][0:4]
                heated_palette[1] = 0xF85030
                base_palette = world.event_palettes.get_palette(EPAL0142_HOTSPRING)
                base_palette.set_colors(heated_palette + base_palette.colors[4:])
                if self.overworld_map_colours is None:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                        palette_to_bytes(
                            self.mutate(
                                self.colours,
                                [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14],
                            )
                        )
                    )
                else:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                    palette_to_bytes(self.overworld_map_colours)
                )
                minecart_palette = world.sprite_palettes.get_palette(SPAL529_MINECART_RIDER)
                minecart_palette.set_colors(
                    self.transform(
                        minecart_palette.colors,
                        self.colours,
                        [None, 13, 1, 2, None, 5, 3, 6, 7, 9, 4, 9, 8, 10, 11],
                    )
                )
                classic_palette = world.sprite_palettes.get_palette(
                    SPAL477_OLD_CLASSIC_MARIO
                )
                if self.classic_colours is None:
                    classic_palette.set_colors(
                        self.transform(
                            classic_palette.colors,
                            self.colours,
                            [
                                10,
                                6,
                                1,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                        )
                    )
                else:
                    classic_palette.set_colors(self.classic_colours)
        if self.poison_colours is not None:
            world.sprite_palettes.get_palette(SPAL630_MARIO_PSN_1).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL646_MARIO_PSN_2).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL510_MARIO_PSN_3).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL607_MARIO_PSN_4).set_colors(
                self.poison_colours
            )
        if self.underwater_colours is not None:
            world.sprite_palettes.get_palette(SPAL632_MARIO_DARK_1).set_colors(
                self.underwater_colours
            )
            world.sprite_palettes.get_palette(SPAL648_MARIO_DARK_2).set_colors(
                self.underwater_colours
            )
            world.event_palettes.get_palette(EPAL0163_MARIO_ENDING_DARK).set_colors(
                self.underwater_colours
            )

        return output


class MallowPalette(Palette):
    name = "Mallow"
    _original_name = "Mallow"

    def render(self, world: GameWorld) -> dict[int, bytearray]:
        output = {}
        if self.colours is not None:
            world.sprite_palettes.get_palette(
                SPAL697_MALLOW_WALKING_DOWN_LEFT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL702_MALLOW_PUNCH).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL506_MALLOW_3).set_colors(self.colours)
            world.event_palettes.get_palette(EPAL0085_MALLOW_ENDING).set_colors(
                self.colours
            )
            if world.overworld_character.ally.index == 4:
                heated_palette = [*self.colours][0:4]
                heated_palette[0] = 0xF85030
                heated_palette[1] = 0xF85030
                base_palette = world.event_palettes.get_palette(EPAL0142_HOTSPRING)
                base_palette.set_colors(heated_palette + base_palette.colors[4:])
                if self.overworld_map_colours is None:
                    output[MAP_PALETTE_OFFSET] = bytearray(palette_to_bytes(self.colours))
                else:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                        palette_to_bytes(self.overworld_map_colours)
                    )
                world.sprite_palettes.get_palette(SPAL529_MINECART_RIDER).set_colors(
                    self.colours
                )
                if self.classic_colours is None:
                    world.sprite_palettes.get_palette(SPAL477_OLD_CLASSIC_MARIO).set_colors(
                        self.colours
                    )
                else:
                    world.sprite_palettes.get_palette(SPAL477_OLD_CLASSIC_MARIO).set_colors(
                        self.classic_colours
                )

        if self.poison_colours is not None:
            world.sprite_palettes.get_palette(SPAL699_MALLOW_PSN_1).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL704_MALLOW_PSN_2).set_colors(
                self.poison_colours
            )
        if self.underwater_colours is not None:
            world.sprite_palettes.get_palette(SPAL701_MALLOW_DARK).set_colors(
                self.underwater_colours
            )
            world.sprite_palettes.get_palette(SPAL706_MALLOW_DARK_2).set_colors(
                self.underwater_colours
            )
            world.event_palettes.get_palette(EPAL0166_MALLOW_ENDING_DARK).set_colors(
                self.underwater_colours
            )

        return output


class GenoPalette(Palette):
    name = "Geno"
    _original_name = "Geno"

    def render(self, world: GameWorld) -> dict[int, bytearray]:
        output = {}
        if self.colours is not None:
            world.sprite_palettes.get_palette(
                SPAL685_GENO_WALKING_DOWN_LEFT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL691_GENO_ELBOW_SHOT).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL507_GENO_3).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL636_GENO_DOLL).set_colors(
                self.colours
            )
            world.event_palettes.get_palette(EPAL0086_GENO_ENDING).set_colors(
                self.colours
            )

            if world.overworld_character.ally.index == 3:
                heated_palette = [*self.colours][0:4]
                heated_palette[1] = 0xF85030
                base_palette = world.event_palettes.get_palette(EPAL0142_HOTSPRING)
                base_palette.set_colors(heated_palette + base_palette.colors[4:])
                world.sprite_palettes.get_palette(SPAL529_MINECART_RIDER).set_colors(
                    self.colours
                )
                if self.overworld_map_colours is None:
                    output[MAP_PALETTE_OFFSET] = bytearray(palette_to_bytes(self.colours))
                else:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                        palette_to_bytes(self.overworld_map_colours)
                    )
                classic_palette = world.sprite_palettes.get_palette(
                    SPAL477_OLD_CLASSIC_MARIO
                )
                if self.classic_colours is None:
                    classic_palette.set_colors(
                        self.transform(
                            classic_palette.colors,
                            self.colours,
                            [
                                3,
                                6,
                                1,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                        )
                    )
                else:
                    classic_palette.set_colors(self.classic_colours)

        if self.poison_colours is not None:
            world.sprite_palettes.get_palette(SPAL687_GENO_PSN_1).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL693_GENO_PSN_2).set_colors(
                self.poison_colours
            )
        if self.underwater_colours is not None:
            world.sprite_palettes.get_palette(SPAL689_GENO_DARK).set_colors(
                self.underwater_colours
            )
            world.sprite_palettes.get_palette(SPAL695_GENO_DARK_2).set_colors(
                self.underwater_colours
            )
            world.event_palettes.get_palette(EPAL0167_GENO_ENDING_DARK).set_colors(
                self.underwater_colours
            )

        return output


class BowserPalette(Palette):
    name = "Bowser"
    _original_name = "Bowser"

    def render(self, world: GameWorld) -> dict[int, bytearray]:
        output = {}
        if self.colours is not None:
            world.sprite_palettes.get_palette(
                SPAL664_BOWSER_WALKING_DOWN_LEFT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL669_BOWSER_CLAW_ATTACK).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL505_BOWSER_3).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL637_BOWSER_DOLL).set_colors(
                self.colours
            )
            world.event_palettes.get_palette(EPAL0140_BOWSER_ENDING).set_colors(
                self.colours
            )

            if world.overworld_character.ally.index == 2:
                world.sprite_palettes.get_palette(SPAL529_MINECART_RIDER).set_colors(
                    self.colours
                )
                world.sprite_palettes.get_palette(SPAL477_OLD_CLASSIC_MARIO).set_colors(
                    self.colours
                )
                heated_palette = [*self.colours][0:4]
                base_palette = world.event_palettes.get_palette(EPAL0142_HOTSPRING)
                base_palette.set_colors(heated_palette + base_palette.colors[4:])
                if self.overworld_map_colours is None:
                    output[MAP_PALETTE_OFFSET] = bytearray(palette_to_bytes(self.colours))
                else:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                        palette_to_bytes(self.overworld_map_colours)
                    )
        if self.poison_colours is not None:
            world.sprite_palettes.get_palette(SPAL666_BOWSER_PSN_1).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL671_BOWSER_PSN_2).set_colors(
                self.poison_colours
            )
        if self.underwater_colours is not None:
            world.sprite_palettes.get_palette(SPAL668_BOWSER_DARK_1).set_colors(
                self.underwater_colours
            )
            world.sprite_palettes.get_palette(SPAL673_BOWSER_DARK_2).set_colors(
                self.underwater_colours
            )
            world.event_palettes.get_palette(EPAL0165_BOWSER_ENDING_DARK).set_colors(
                self.underwater_colours
            )

        return output


class ToadstoolPalette(Palette):
    name = "Toadstool"
    _original_name = "Toadstool"

    def render(self, world: GameWorld) -> dict[int, bytearray]:
        output = {}
        if self.colours is not None:
            world.sprite_palettes.get_palette(
                SPAL654_TOADSTOOL_WALKING_DOWN_LEFT
            ).set_colors(self.colours)
            world.sprite_palettes.get_palette(SPAL659_TOADSTOOL_SLAP_ATTACK).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL504_TOADSTOOL_3).set_colors(
                self.colours
            )
            world.sprite_palettes.get_palette(SPAL638_TOADSTOOL_DOLL).set_colors(
                self.colours
            )
            world.event_palettes.get_palette(EPAL0141_TOADSTOOL_ENDING).set_colors(
                self.colours
            )
            if world.overworld_character.ally.index == 1:
                world.sprite_palettes.get_palette(SPAL529_MINECART_RIDER).set_colors(
                    self.colours
                )
                classic_palette = world.sprite_palettes.get_palette(
                    SPAL477_OLD_CLASSIC_MARIO
                )
                if self.classic_colours is None:
                    classic_palette.set_colors(
                        self.transform(
                            classic_palette.colors,
                            self.colours,
                            [
                                6,
                                3,
                                1,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                        )
                    )
                else:
                    classic_palette.set_colors(self.classic_colours)
                heated_palette = [*self.colours][0:4]
                heated_palette[1] = 0xF85030
                base_palette = world.event_palettes.get_palette(EPAL0142_HOTSPRING)
                base_palette.set_colors(heated_palette + base_palette.colors[4:])
                if self.overworld_map_colours is None:
                    output[MAP_PALETTE_OFFSET] = bytearray(palette_to_bytes(self.colours))
                else:
                    output[MAP_PALETTE_OFFSET] = bytearray(
                        palette_to_bytes(self.overworld_map_colours)
                    )
        if self.poison_colours is not None:
            world.sprite_palettes.get_palette(SPAL656_TOADSTOOL_PSN_1).set_colors(
                self.poison_colours
            )
            world.sprite_palettes.get_palette(SPAL661_TOADSTOOL_PSN_2).set_colors(
                self.poison_colours
            )
        if self.underwater_colours is not None:
            world.sprite_palettes.get_palette(SPAL658_TOADSTOOL_DARK_1).set_colors(
                self.underwater_colours
            )
            world.sprite_palettes.get_palette(SPAL663_TOADSTOOL_DARK_2).set_colors(
                self.underwater_colours
            )
            world.event_palettes.get_palette(EPAL0164_TOADSTOOL_ENDING_DARK).set_colors(
                self.underwater_colours
            )

        return output
