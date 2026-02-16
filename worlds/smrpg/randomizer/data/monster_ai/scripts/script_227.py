# 227 - DRILLBITEnemy
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
	Attack(DoNothing, Attack1, SkewerAttack),
	IncreaseVarBy1(BV7EE003),
	Wait1Turn(),
	Attack(DoNothing, Attack1, Attack1),
	IncreaseVarBy1(BV7EE003),
	Wait1Turn(),
	StartCounterCommands()
])