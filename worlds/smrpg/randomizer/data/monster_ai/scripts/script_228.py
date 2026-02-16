# 228 - AXEMPINKEnemy
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
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE00F, 1),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	CastSpell(PetalBlastSpell),
	Wait1TurnandRestartScript(),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(RecoverSpell, RecoverSpell, MegaRecoverSpell),
	SetTarget(RANDOM_OPPONENT),
	StartCounterCommands(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IfVarEqualOrGreaterThan(BV7EE00F, 4),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	SetVarBits(BV7EE003, [0]),
	SetVarBits(BV7EE002, [0]),
	RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IncreaseVarBy1(BV7EE00F),
	SetUntargetable(SELF),
	SetVarBits(BV7EE003, [0]),
	RunBattleEvent(BE0063_UNUSED),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	SetTarget(RANDOM_OPPONENT),
	Attack(DoNothing, Attack3, Attack51),
	Wait1TurnandRestartScript()
])