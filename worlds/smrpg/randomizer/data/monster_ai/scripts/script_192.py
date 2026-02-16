# 192 - KNIFEGUYEnemy
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
	IfVarEqualOrGreaterThan(BV7EE002, 3),
	IfVarBitsClear(BV7EE000, [0]),
	IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
	ClearVar(BV7EE001),
	SetVarBits(BV7EE000, [0]),
	RunBattleEvent(BE0018_KNIFE_GUY_GRATE_GUY_PAIR_UP_PIGGY_BACK),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE000, [0]),
	CastSpell(BlizzardSpell, CrystalSpell, CrystalSpell),
	IncreaseVarBy1(BV7EE002),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, Attack20),
	IncreaseVarBy1(BV7EE002),
	StartCounterCommands(),
	IfHPBelow(0),
	IfLastMonsterStanding(),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IfVarBitsSet(BV7EE000, [0]),
	ClearVarBits(BV7EE000, [0]),
	RunBattleEvent(BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IncreaseVarBy1(BV7EE001),
	IfVarBitsSet(BV7EE000, [0]),
	IfVarEqualOrGreaterThan(BV7EE001, 5),
	ClearVarBits(BV7EE000, [0]),
	ClearVar(BV7EE002),
	RunBattleEvent(BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH),
	Wait1TurnandRestartScript()
])