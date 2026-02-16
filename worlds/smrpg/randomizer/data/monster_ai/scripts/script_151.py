# 151 - EARTHCRYSTALEnemy
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
	IfCurrentlyInFormationID(322),
	IfTargetKOed(MONSTER_1_CALL),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(BlastSpell, BlastSpell, StormSpell),
	Wait1TurnandRestartScript(),
	CastSpell(SandStormSpell, WaterBlastSpell, BoulderSpell),
	StartCounterCommands()
])