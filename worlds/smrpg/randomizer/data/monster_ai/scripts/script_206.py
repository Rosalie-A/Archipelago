# 206 - EGGBERTEnemy
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
	IfCurrentlyInFormationID(285),
	Wait1TurnandRestartScript(),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfCurrentlyInFormationID(285),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE004, [0]),
	ClearVarBits(BV7EE007, [0]),
	SetTarget(MONSTER_1_SET),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(285),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE004, [1]),
	ClearVarBits(BV7EE007, [1]),
	SetTarget(MONSTER_1_SET),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(285),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE004, [2]),
	ClearVarBits(BV7EE007, [2]),
	SetTarget(MONSTER_1_SET),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(285),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE004, [3]),
	ClearVarBits(BV7EE007, [3]),
	SetTarget(MONSTER_1_SET),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(285),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(DUMMYAttack16),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])