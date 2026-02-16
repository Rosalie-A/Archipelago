# 220 - CZARDRAGONEnemy
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
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(WaterBlastSpell, FlameWallSpell, FlameWallSpell),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	Attack(Attack1, Attack1, IronMaidenAttack),
	IfTargetAlive(AT_LEAST_ONE_OPPONENT),
	RunBattleEvent(BE0046_CZAR_DRAGON_SUMMONS_HELIOS),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	IfLastMonsterStanding(),
	RunBattleEvent(BE0044_CZAR_DRAGON_DIES),
	CallTarget(MONSTER_2_CALL),
	RunObjectSequence(2),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	RunBattleEvent(BE0044_CZAR_DRAGON_DIES),
	CallTarget(MONSTER_2_CALL),
	RunObjectSequence(2),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(Attack1, DoNothing, DoNothing),
	Wait1TurnandRestartScript()
])