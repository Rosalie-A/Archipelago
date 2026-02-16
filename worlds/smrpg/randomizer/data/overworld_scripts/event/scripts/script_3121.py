# E3121_SEWER_BOSS_FIGHT
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
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_3121_set_bit_3"]),
	ResetAndChooseGame(),
	SetBit(TEMP_707C_5, identifier="EVENT_3121_set_bit_3"),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	Pause(10),
	SetBit(SEWER_BOSS_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(MARIO),
	SetBit(UNKNOWN_MIDAS_RIVER_704D_6),
	ClearBit(BUCKET_WARP_BIT),
	Pause(1),
	EnterArea(room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, face_direction=SOUTH, x=12, y=108, z=11),
	RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=144, silent=True)
	]),
    RunEventAsSubroutine(E1197_KERO_SEWER_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
