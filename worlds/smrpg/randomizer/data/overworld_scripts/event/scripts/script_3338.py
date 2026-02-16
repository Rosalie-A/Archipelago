# E3338_VOLCANO_TRAMPOLINE_TO_2ND_BOSS
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
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3338_open_location_16"]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	StopMusicFDA2(),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	JmpIfBitSet(GAME_OVER, ["EVENT_3338_reset_and_choose_game_18"]),
	SetBit(VOLCANO_LIBERATED),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E0208_UNLOCK_KEEP_IF_GATED_BY_VOLCANO_BOSS),
	SetBit(RETURN_TO_OVERWORLD_AFTER_VOLCANO_STAR_PIECE),
	RunEventAsSubroutine(E1234_VOLCANO_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True, identifier="EVENT_3338_open_location_16"),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3338_reset_and_choose_game_18")
])
