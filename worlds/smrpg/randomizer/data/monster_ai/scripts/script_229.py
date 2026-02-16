# 229 - AXEMBLACKEnemy
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
	IfVarBitsSet(BV7EE003, [1]),
	Wait1TurnandRestartScript(),
	Attack(Attack5, Attack5, Attack25),
	IfTargetAlive(AT_LEAST_ONE_OPPONENT),
	Attack(Attack5, Attack5, Attack25),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IfVarEqualOrGreaterThan(BV7EE00F, 4),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	SetVarBits(BV7EE003, [1]),
	SetVarBits(BV7EE002, [0]),
	RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IncreaseVarBy1(BV7EE00F),
	SetUntargetable(SELF),
	SetVarBits(BV7EE003, [1]),
	RunBattleEvent(BE0064_UNUSED),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	Attack(SpritzBombAttack),
	Wait1TurnandRestartScript()
])