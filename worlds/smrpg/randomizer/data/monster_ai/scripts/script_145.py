# 145 - MACHINEMADEBodyguardEnemy
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
	Attack(Attack13),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	CastSpell(DoNothing, DrainSpell, DrainSpell),
	StartCounterCommands(),
	IfTargetKOed(AT_LEAST_ONE_ALLY),
	IncreaseVarBy1(BV7EE000),
	IfVarEqualOrGreaterThan(BV7EE000, 4),
	ClearVarBits(BV7EE003, [0]),
	IfVarBitsSet(BV7EE003, [7]),
	ClearVarBits(BV7EE003, [7]),
	SetTargetable(MONSTER_1_SET),
	RunBattleEvent(BE0005_MACK_RETURNS_TO_BATTLE),
	Wait1TurnandRestartScript()
])