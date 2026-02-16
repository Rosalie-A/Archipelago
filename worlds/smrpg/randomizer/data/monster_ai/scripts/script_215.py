# 215 - RASPBERRYEnemy
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
	IfVarBitsClear(BV7EE000, [0]),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(SandStormSpell, DrainBeamSpell, SandStormSpell),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack0, Attack31),
	ClearVarBits(BV7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0035_BOOSTER_EATS_CAKE),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])