# 234 - SMITHY1Enemy
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
	RunBattleEvent(BE0096_NOTHING),
	CastSpell(SledgeSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE003, [0]),
	ClearVarBits(BV7EE003, [0]),
	CastSpell(SledgeSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(MeteorSwarmSpell, MeteorSwarmSpell, MegaDrainSpell),
	Wait1TurnandRestartScript(),
	Attack(Attack90),
	StartCounterCommands(),
	IfHPBelow(0),
	IfTargetAlive(MONSTER_4_SET),
	RunBattleEvent(BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC),
	RemoveTarget(MONSTER_4_SET),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunBattleEvent(BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])