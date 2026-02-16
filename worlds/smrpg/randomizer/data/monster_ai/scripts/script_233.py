# 233 - EXOREnemy
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
	IfVarBitsClear(BV7EE000, [0, 1, 2]),
	IfTargetAlive(MONSTER_3_SET),
	IfTargetAlive(MONSTER_4_SET),
	SetVarBits(BV7EE000, [2]),
	RunBattleDialog(218),
	MakeInvulnerable(MONSTER_1_SET, identifier="exor_vulnerability_3"),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetVarBits(BV7EE008, [0]),
	SetUntargetable(MONSTER_2_SET),
	SetUntargetable(MONSTER_3_SET),
	SetUntargetable(MONSTER_4_SET),
	RunBattleEvent(BE0081_EXOR_IS_DEFEATED_CRIES_AND_OPENS_MOUTH),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])