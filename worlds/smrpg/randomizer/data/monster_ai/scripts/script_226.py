# 226 - YARIDOVICHEnemy
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
	IfVarBitsClear(BV7EE003, [0]),
	CastSpell(WaterBlastSpell),
	SetVarBits(BV7EE003, [0]),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE002, 3),
	IfVarBitsSet(BV7EE000, [0]),
	ClearVarBits(BV7EE000, [0]),
	ClearVar(BV7EE002),
	ClearVarBits(BV7EE003, [0]),
	RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
	RemoveTarget(MONSTER_2_SET),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE000, [0]),
	Attack(Attack1, PierceAttack, Attack31),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE001, 2),
	CastSpell(FlameStoneSpell, WillyWispSpell, WaterBlastSpell),
	IncreaseVarBy1(BV7EE001),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE001),
	SetVarBits(BV7EE000, [0]),
	RunBattleDialog(133),
	RunBattleEvent(BE0022_YARIDOVICH_MIRAGE_ATTACK),
	StartCounterCommands(),
	IfHPBelow(0),
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
	RemoveTarget(MONSTER_2_SET),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])