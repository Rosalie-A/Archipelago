# 243 - EARTHLINKEnemy
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
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, PoisonAttack, CarniKissAttack),
	ClearVarBits(BV7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_1_SET),
	SetUntargetable(SELF),
	RunBattleEvent(BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	Wait1TurnandRestartScript()
])