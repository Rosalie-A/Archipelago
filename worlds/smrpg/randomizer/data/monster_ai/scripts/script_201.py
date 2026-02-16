# 201 - BELOMEEnemy3
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
	IfVarBitsClear(BV7EE004, [7]),
	IfVarBitsSet(BV7EE004, [0]),
	SetVarBits(BV7EE004, [7]),
	SetVarBits(BV7EE002, [0]),
	RunBattleDialog(181),
	RunBattleEvent(BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS),
	RunBattleEvent(BE0099_BELOME_3_SUMMONS_CLONES),
	IncreaseVarBy1(BV7EE000),
	ClearVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [0]),
	RunBattleEvent(BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS),
	RunBattleEvent(BE0099_BELOME_3_SUMMONS_CLONES),
	IncreaseVarBy1(BV7EE000),
	ClearVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(AuroraFlashSpell, LightBeamSpell, LightBeamSpell),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, LullaByeAttack),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarLessThan(BV7EE000, 2),
	SetVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript()
])