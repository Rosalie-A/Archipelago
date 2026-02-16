# 214 - fancy bundt

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
	IfVarLessThan(BV7EE007, 1),
	CastSpell(CakerBeamSpell),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack31, LullaByeAttack),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(BlizzardSpell, PetalBlastSpell, DiamondSawSpell),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_2_SET),
	SetTargetable(MONSTER_5_SET),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarLessThan(BV7EE007, 6),
	SetTarget(SELF),
	Attack(ATKMATKneg5Attack),
	IncreaseVarBy1(BV7EE007),
	Wait1TurnandRestartScript()
])