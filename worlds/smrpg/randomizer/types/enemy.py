from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status


class Enemy(EnemyBase):
    _remake_name: str | None = None

    # Stat scaling ratios - define what percentage of the stat pool this enemy should receive
    # These can be overridden in subclasses for bosses with specific scaling needs
    _ratio_hp: float = 1.0
    _ratio_attack: float = 1.0
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 1.0
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 1.0

    @property
    def ratio_hp(self) -> float:
        return self._ratio_hp

    @property
    def ratio_attack(self) -> float:
        return self._ratio_attack

    @property
    def ratio_defense(self) -> float:
        return self._ratio_defense

    @property
    def ratio_magic_attack(self) -> float:
        return self._ratio_magic_attack

    @property
    def ratio_magic_defense(self) -> float:
        return self._ratio_magic_defense

    @property
    def ratio_evade(self) -> float:
        return self._ratio_evade

    @property
    def ratio_magic_evade(self) -> float:
        return self._ratio_magic_evade

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name

    @property
    def boss(self) -> bool:
        """Returns True if this enemy is a boss (uses ohko_immune as indicator)."""
        return self._ohko_immune

    def build_psychopath_text(self) -> str:
        """Generate Psychopath text showing elemental weaknesses/immunities and status vulnerabilities.

        Uses ~empty~ (character 141) as invisible placeholder for missing elements/statuses.
        The encoder trims trailing ~empty~ characters before terminating.

        Format: [resist_icon elements] [weak_icon elements] [V statuses ohko]

        Returns:
            Psychopath message string with special characters for game display.
        """
        EMPTY = '~empty~'  # Invisible placeholder (character 141)

        # Element tokens map to their byte values via BATTLE_CHAR_MAP in encoder
        ELEMENT_TOKENS = {
            Element.ICE: '~ice~',       # 125
            Element.FIRE: '~fire~',     # 126
            Element.THUNDER: '~thunder~',  # 127
            Element.JUMP: '~jump~',     # 133
        }

        # Status tokens - using raw bytes since they're not in BATTLE_CHAR_MAP
        STATUS_CHARS = {
            Status.SLEEP: '\x80',    # 128
            Status.FEAR: '\x81',     # 129
            Status.MUTE: '\x82',     # 130
            Status.POISON: '\x83',   # 131
        }

        desc = ''

        # Elemental resistances - collect present elements, then pad with empty
        element_order = [Element.FIRE, Element.ICE, Element.THUNDER, Element.JUMP]
        resist_elements = [e for e in element_order if e in self.resistances]
        if resist_elements:
            desc += '|'  # Resistance icon (124)
            for element in resist_elements:
                desc += ELEMENT_TOKENS[element]
            desc += EMPTY 

        # Elemental weaknesses - collect present elements, then pad with empty
        weak_elements = [e for e in element_order if e in self.weaknesses]
        if weak_elements:
            desc += '{'  # Weakness icon (123)
            for element in weak_elements:
                desc += ELEMENT_TOKENS[element]
            desc += EMPTY 

        # Status vulnerabilities (inverse of immunities) - collect present, then pad
        status_order = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
        vulnerabilities = [s for s in status_order if s not in self.status_immunities]

        # Check if there are any vulnerabilities (status or OHKO)
        has_status_vulns = len(vulnerabilities) > 0
        has_ohko_vuln = not self.ohko_immune

        if has_status_vulns or has_ohko_vuln:
            # Add "V" prefix for vulnerabilities section
            desc += 'V'
            for status in vulnerabilities:
                desc += STATUS_CHARS[status]
            # Pad to 4 statuses
            # OHKO vulnerability
            if has_ohko_vuln:
                desc += '~ohko~~ohko~'  # Two OHKO symbols (132, 132)
        # Strip trailing EMPTY placeholders (must strip full substring, not individual chars)
        while desc.endswith(EMPTY):
            desc = desc[:-len(EMPTY)]
        if desc == '':
            desc = "(none)"

        return desc
