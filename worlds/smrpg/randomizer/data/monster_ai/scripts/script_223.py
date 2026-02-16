# 223 - MADADDEREnemy
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
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 5),
	CastSpell(SandStormSpell, StormSpell, WaterBlastSpell),
	Wait1TurnandRestartScript(),
	CastSpell(DoNothing, BoulderSpell, BoulderSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_2_SET),
	SetUntargetable(SELF),
	RunBattleEvent(BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	Wait1TurnandRestartScript()
])