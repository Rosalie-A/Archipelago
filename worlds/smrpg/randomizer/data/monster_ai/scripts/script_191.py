# 191 - LEFTEYEEnemy
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
	IfVarEqualOrGreaterThan(BV7EE004, 2),
	SetTargetable(SELF),
	ClearVar(BV7EE004),
	ClearVar(BV7EE003),
	RunObjectSequence(13),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE003, [0]),
	IncreaseVarBy1(BV7EE004),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, GunkBallAttack, Attack0),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript(),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, VenomDroolAttack, ScrowBellAttack),
	ClearVarBits(BV7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE008, [0]),
	SetVarBits(BV7EE003, [0]),
	SetVarBits(BV7EE000, [1]),
	ClearVarBits(BV7EE000, [2]),
	SetUntargetable(SELF),
	MakeVulnerable(MONSTER_1_SET, identifier="exor_vulnerability_2"),
	RunObjectSequence(12),
	RunBattleDialog(219),
	Wait1TurnandRestartScript()
])