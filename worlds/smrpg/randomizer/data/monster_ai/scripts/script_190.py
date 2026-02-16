# 190 - RIGHTEYEEnemy
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
	IfVarBitsSet(BV7EE002, [0]),
	IfVarEqualOrGreaterThan(BV7EE004, 3),
	SetTargetable(SELF),
	ClearVar(BV7EE004),
	ClearVar(BV7EE002),
	RunObjectSequence(13),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE002, [0]),
	IncreaseVarBy1(BV7EE004),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(BoltSpell, DiamondSawSpell, MegaDrainSpell),
	Wait1TurnandRestartScript(),
	CastSpell(FlameStoneSpell, DarkStarSpell, BlastSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsClear(BV7EE008, [0]),
	SetVarBits(BV7EE002, [0]),
	SetVarBits(BV7EE000, [0]),
	ClearVarBits(BV7EE000, [2]),
	SetUntargetable(SELF),
	MakeVulnerable(MONSTER_1_SET, identifier="exor_vulnerability_1"),
	RunObjectSequence(11),
	RunBattleDialog(219),
	Wait1TurnandRestartScript()
])