# 198 - DINGALINGEnemy
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
	Set7EE005ToRandomNumber(upper_bound=9),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 3),
	Attack(Attack0),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	RunObjectSequence(14),
	RunBattleDialog(220),
	IncreaseVarBy1(BV7EE000),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 6),
	RunObjectSequence(16),
	SetVarBits(BV7EE00F, [1]),
	Attack(ScrowBellAttack, DoomReverbAttack, SporeChimesAttack),
	ClearVarBits(BV7EE00F, [1]),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 8),
	RunObjectSequence(17),
	CastSpell(DarkStarSpell),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	IfVarEqualOrGreaterThan(BV7EE00A, 3),
	IfTargetAlive(SLOT_1),
	RunObjectSequence(15),
	SetTarget(SLOT_1),
	Attack(FearRouletteAttack),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	IfVarEqualOrGreaterThan(BV7EE00A, 3),
	IfTargetAlive(SLOT_2),
	RunObjectSequence(15),
	SetTarget(SLOT_2),
	SetVarBits(BV7EE00E, [0]),
	Attack(FearRouletteAttack),
	ClearVarBits(BV7EE00E, [0]),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE00A, 3),
	IfTargetAlive(SLOT_3),
	RunObjectSequence(15),
	SetTarget(SLOT_3),
	SetVarBits(BV7EE00E, [1]),
	Attack(FearRouletteAttack),
	ClearVarBits(BV7EE00E, [1]),
	Wait1TurnandRestartScript(),
	CastSpell(DarkStarSpell),
	StartCounterCommands()
])