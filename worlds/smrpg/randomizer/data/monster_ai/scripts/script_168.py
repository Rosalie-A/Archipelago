# 168 - MACHINEMADEAxemRedEnemy
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
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	SetTarget(SELF),
	Attack(ValorUpAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE004, [1]),
	SetVarBits(BV7EE004, [1]),
	SetTarget(SELF),
	Attack(VigorupAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, Attack31),
	StartCounterCommands()
])