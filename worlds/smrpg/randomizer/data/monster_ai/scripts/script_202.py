# 202 - SMILAXEnemy
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
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack0, PollenNapAttack),
	ClearVarBits(BV7EE00F, [0]),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	CastSpell(DrainSpell, DrainSpell, FlameSpell),
	StartCounterCommands(),
	IfLastMonsterStanding(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE003, [0]),
	SetVarBits(BV7EE003, [0]),
	RunObjectSequence(3),
	RunBattleEvent(BE0055_SHY_AWAY_WATERS_SMILAX_PART_1),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE003, [1]),
	SetVarBits(BV7EE003, [1]),
	RunObjectSequence(3),
	RunBattleEvent(BE0056_SHY_AWAY_WATERS_SMILAX_PART_2),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE003, [2]),
	SetVarBits(BV7EE003, [2]),
	RunObjectSequence(3),
	RunBattleEvent(BE0057_SHY_AWAY_WATERS_SMILAX_PART_3),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(3),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, DoNothing, DoNothing),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript()
])