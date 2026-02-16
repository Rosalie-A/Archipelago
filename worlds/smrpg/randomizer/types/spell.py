from smrpgpatchbuilder.datatypes.spells.classes import Spell as SpellBase, CharacterSpell as CharacterSpellBase, EnemySpell as EnemySpellBase
class Spell(SpellBase):
    _remake_name: str | None = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._title


class CharacterSpell(CharacterSpellBase, Spell):
    @property
    def palette_patch(self) -> dict[int, bytearray]:
        return {}


class EnemySpell(EnemySpellBase, Spell):
    _remake_only: bool = False

def _colour_bytes(colour: int) -> bytearray:
    red = colour >> 19
    green = (colour >> 10) & 0x3E
    blue = (colour >> 1) & 0x7C

    byte_1 = red + ((green << 4) & 0xF0)
    byte_2 = blue + (green >> 4)
    return bytearray([byte_1, byte_2])

def palette_to_bytes(palette: list[int]) -> bytearray:
    output = bytearray()
    for colour in palette:
        output += _colour_bytes(colour)
    #assert len(output) == 30
    return output