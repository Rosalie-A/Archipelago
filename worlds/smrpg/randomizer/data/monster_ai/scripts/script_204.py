# 204 - MEGASMILAXEnemy
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
	IfVarBitsClear(BV7EE00A, [0]),
	SetVarBits(BV7EE00A, [0]),
	CastSpell(PetalBlastSpell),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(4),
	CastSpell(PetalBlastSpell),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack0, ScrowDustAttack),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(DrainSpell, FlameWallSpell, FlameWallSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, DoNothing, DoNothing),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript()
])