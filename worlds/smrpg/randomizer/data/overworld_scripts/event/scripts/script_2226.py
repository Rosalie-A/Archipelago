# E2226_KEEP_3RD_BOSS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	Pause(10),
	SetVarToConst(PRIMARY_TEMP_7000, 522),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_2226_restore_all_hp_5"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2226_restore_all_hp_5"),
	RestoreAllFP(),
	SetBit(KEEP_BOSS_3_DEFEATED),
	SetBit(BATTLE_DOOR_STAR_PIECE),
	SetVarToConst(PRIMARY_TEMP_7000, 522),
	RunEventAsSubroutine(E1238_KEEP_EXIT_BOSS_UNLOCKS),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	StopSound(),
	JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
	Return()
])
