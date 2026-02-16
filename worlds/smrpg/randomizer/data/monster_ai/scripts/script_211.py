# 211 - AXEMGREENEnemy
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
	IfVarBitsSet(BV7EE003, [4]),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 6),
	CastSpell(MeteorBlastSpell, SolidifySpell, StaticESpell),
	Wait1TurnandRestartScript(),
	Attack(Attack3, Attack3, ElegyAttack),
	StartCounterCommands(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IfVarEqualOrGreaterThan(BV7EE00F, 4),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	SetVarBits(BV7EE003, [4]),
	SetVarBits(BV7EE002, [0]),
	RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(292),
	IfHPBelow(0),
	IncreaseVarBy1(BV7EE00F),
	SetUntargetable(SELF),
	SetVarBits(BV7EE003, [4]),
	RunBattleEvent(BE0066_UNUSED),
	Wait1TurnandRestartScript()
])