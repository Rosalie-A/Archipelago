# 240 - CROCO1Enemy
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
	RunBattleDialog(131),
	Wait1TurnandRestartScript(),
	IfHPBelow(100),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	SetTarget(SELF),
	CastSpell(WeirdMushroomSpell),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(Attack14, Attack14, Attack25),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE003, [0, 1]),
	IfTargetedByElement([Element.FIRE]),
	SetVarBits(BV7EE003, [0, 1]),
	RunBattleDialog(1),
	Wait1TurnandRestartScript()
])