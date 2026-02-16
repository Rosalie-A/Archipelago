# 249 - JOHNNYEnemy
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
	IfVarBitsSet(BV7EE004, [0]),
	IfVarBitsClear(BV7EE004, [1]),
	IfLastMonsterStanding(),
	IfTargetAlive(SLOT_3),
	SetVarBits(BV7EE004, [1]),
	SetTarget(RANDOM_OPPONENT),
	RunBattleEvent(BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE),
	SetUntargetable(MONSTER_2_SET),
	SetUntargetable(MONSTER_3_SET),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Attack(Attack1, SkewerAttack, SkewerAttack),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	CastSpell(DoNothing, DiamondSawSpell, MegaDrainSpell),
	Wait1TurnandRestartScript(),
	Attack(Attack1),
	StartCounterCommands(),
	IfHPBelow(0),
	IncreaseVarBy1(BV7EE003),
	RunObjectSequence(3),
	RemoveTarget(ALL_ALLIES_AND_SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(400),
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	SetTarget(SELF),
	Attack(GetToughAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript()
])