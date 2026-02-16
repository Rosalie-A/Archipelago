# 188 - YARIDOVICHMirageEnemy
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
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	CastSpell(MeteorBlastSpell, StaticESpell, BoltSpell),
	IncreaseVarBy1(BV7EE002),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(Attack1),
	IncreaseVarBy1(BV7EE002),
	StartCounterCommands(),
	IfHPBelow(0),
	ClearVar(BV7EE002),
	RunBattleEvent(BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM),
	ClearVarBits(BV7EE000, [0]),
	ClearVarBits(BV7EE003, [0]),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])