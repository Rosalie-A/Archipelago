# 231 - RASPBERRY2Enemy
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
	IfVarLessThan(BV7EE007, 4),
	Attack(Attack0, Attack31, ScrowBellAttack),
	Wait1TurnandRestartScript(),
	CastSpell(SandStormSpell, LightBeamSpell, WaterBlastSpell),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])