# 64 - TERRACOTTAEnemy
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
	IfTargetAlive(BOWSER),
	RunBattleDialog(130),
	SetTarget(SELF),
	CastSpell(EscapeSpell),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarBitsClear(BV7EE004, [0]),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 2),
	SetVarBits(BV7EE004, [0]),
	RunBattleDialog(129),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [0]),
	IfLastMonsterStanding(),
	SetTarget(SELF),
	CastSpell(EscapeSpell),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [0]),
	SetTarget(RANDOM_ALLY_EXCLUDING_SELF_OPPONENT_IF_SOLO),
	Attack(Attack0),
	Wait1TurnandRestartScript(),
	Attack(Attack6, Attack6, TerrapunchAttack),
	StartCounterCommands()
])