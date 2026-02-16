# 18 - THEBIGBOOEnemy
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
	Attack(Attack12, Attack12, ScreamAttack),
	Wait1Turn(),
	CastSpell(LightningOrbSpell, LightningOrbSpell, BoltSpell),
	Wait1Turn(),
	StartCounterCommands(),
	IfTargetedByItem([PureWaterItem]),
	IfTargetAlive(SELF),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])