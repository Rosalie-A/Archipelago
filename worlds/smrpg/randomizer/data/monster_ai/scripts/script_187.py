# 187 - NEOSQUIDEnemy
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
	IfVarBitsSet(BV7EE001, [0]),
	IfVarEqualOrGreaterThan(BV7EE004, 3),
	SetTargetable(SELF),
	ClearVar(BV7EE004),
	ClearVar(BV7EE001),
	RunObjectSequence(13),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE001, [0]),
	IncreaseVarBy1(BV7EE004),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(SolidifySpell, AuroraFlashSpell, CoronaSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StaticESpell, FlameWallSpell, WaterBlastSpell),
	Wait1TurnandRestartScript(),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, CarniKissAttack, LullaByeAttack),
	ClearVarBits(BV7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	SetVarBits(BV7EE001, [0]),
	SetUntargetable(SELF),
	RunObjectSequence(10),
	Wait1TurnandRestartScript()
])