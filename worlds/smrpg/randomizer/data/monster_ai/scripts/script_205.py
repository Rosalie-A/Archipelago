# 205 - BIRDETTAEnemy
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
	IfVarEqualOrGreaterThan(BV7EE000, 3),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	Attack(DUMMYAttack14),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [0]),
	Attack(DUMMYAttack13, DUMMYAttack14, DUMMYAttack14),
	Wait1TurnandRestartScript(),
	Attack(DUMMYAttack13),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	SetVarBits(BV7EE00F, [0]),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IncreaseVarBy1(BV7EE000),
	Wait1TurnandRestartScript()
])