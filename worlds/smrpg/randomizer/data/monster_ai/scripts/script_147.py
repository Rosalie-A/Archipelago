# 147 - FORMLESSEnemy
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
	CastSpell(BoltSpell, StaticESpell, ElectroshockSpell),
	Wait1Turn(),
	CastSpell(BoltSpell, CrystalSpell, SolidifySpell),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	RunBattleDialog(214),
	RunBattleEvent(BE0075_FORMLESS_CHANGES_INTO_MOKURA),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])