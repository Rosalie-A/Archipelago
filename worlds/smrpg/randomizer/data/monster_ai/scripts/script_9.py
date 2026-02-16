# 9 - GOBYEnemy
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
	IfVarBitsSet(BV7EE003, [0]),
	ClearVarBits(BV7EE003, [0]),
	RunBattleDialog(128),
	Wait1TurnandRestartScript(),
	Attack(Attack9, Attack9, Attack9),
	StartCounterCommands(),
	IfTargetedByElement([Element.THUNDER]),
	SetVarBits(BV7EE003, [0]),
	Wait1TurnandRestartScript()
])