# 210 - AXEMREDEnemy
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
	IfVarBitsSet(BV7EE003, [2]),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(BV7EE00F, 2),
	IfVarBitsClear(BV7EE004, [1]),
	SetVarBits(BV7EE004, [1]),
	SetTarget(SELF),
	Attack(VigorupAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, Attack31),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarEqualOrGreaterThan(BV7EE00F, 4),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	SetVarBits(BV7EE003, [2]),
	SetVarBits(BV7EE002, [0]),
	RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IncreaseVarBy1(BV7EE00F),
	SetUntargetable(SELF),
	SetVarBits(BV7EE003, [2]),
	RunBattleEvent(BE0068_PUNCHINELLO_2_SUMMONS_BOMBS),
	Wait1TurnandRestartScript()
])