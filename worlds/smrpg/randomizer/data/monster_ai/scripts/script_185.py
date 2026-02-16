# 130 - WATERCRYS3DEnemy
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
	IfTargetKOed(MONSTER_1_CALL),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	CallTarget(MONSTER_1_CALL),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(1),
	IfVarBitsClear(BV7EE002, [0]),
	Set7EE005ToRandomNumber(upper_bound=4),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 1),
	RunBattleDialog(146),
	DisableCommand([COMMAND_SPECIAL]),
	SetVarBits(BV7EE002, [0]),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 1),
	CastSpell(DiamondSawSpell),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	CastSpell(BlizzardSpell),
	Wait1TurnandRestartScript(),
	CastSpell(CrystalSpell, SolidifySpell, IceRockSpell),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTarget(MONSTER_1_SET),
	SetTarget(ALL_ALLIES_EXCLUDING_SELF),
	Attack(MagicForceAttack),
	RunObjectSequence(3),
	RemoveTarget(SELF)
])