# 164 - MACHINEMADEBowyerEnemy
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
	RunObjectSequence(0),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE000, 1),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StaticESpell, LightningOrbSpell, BoltSpell),
	IncreaseVarBy1(BV7EE000),
	Wait1TurnandRestartScript(),
	IfVarLessThan(BV7EE000, 1),
	Attack(DUMMYAttack8, DUMMYAttack8, GnightAttack),
	IncreaseVarBy1(BV7EE000),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	ClearVar(BV7EE001),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	EnableCommand([COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]),
	DisableCommand([COMMAND_ATTACK]),
	SetVarBits(BV7EE001, [0]),
	Attack(DUMMYAttack5),
	ClearVar(BV7EE000),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	ClearVar(BV7EE001),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	EnableCommand([COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]),
	DisableCommand([COMMAND_SPECIAL]),
	SetVarBits(BV7EE001, [1]),
	Attack(DUMMYAttack6),
	ClearVar(BV7EE000),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE001),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	EnableCommand([COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]),
	DisableCommand([COMMAND_ITEM]),
	SetVarBits(BV7EE001, [2]),
	Attack(DUMMYAttack7),
	ClearVar(BV7EE000),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([CarboCookieItem]),
	ClearVar(BV7EE000),
	ClearVar(BV7EE001),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	EnableCommand([COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]),
	Wait1TurnandRestartScript()
])