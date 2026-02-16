# 116 - POUNDEREnemy2
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing
from ...variables.battle_event_names import *
from ...variables.battle_variable_names import *
from ...items.items import *
from ...spells.spells import *
from ...enemies.enemies import *
from ...enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *

script = MonsterScript([
	IfTurnCounterEquals(6),
	CastSpell(LightningOrbSpell),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	Attack(Attack1),
	Wait1Turn(),
	Attack(Attack1),
	Wait1Turn(),
	UnknownCommand(bytearray(b'\x82')),
	Wait1Turn(),
	StartCounterCommands()
])