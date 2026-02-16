# 139 - CHESTEREnemy
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
	RunObjectSequence(7),
	CallTarget(MONSTER_2_CALL),
	RunBattleDialog(216),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(BV7EE004, [0]),
	CastSpell(FlameStoneSpell),
	SetVarBits(BV7EE004, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(SandStormSpell),
	Wait1Turn(),
	CastSpell(MegaRecoverSpell, MegaRecoverSpell, FlameWallSpell),
	Wait1Turn(),
	StartCounterCommands()
])