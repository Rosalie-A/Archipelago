# E2596_ABYSS_1ST_BOSS_FIGHT
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
	JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["EVENT_2596_ret_18"]),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_EndLoop()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=4, y=69)
	]),
	Pause(30),
	SetSyncActionScript(MARIO, A0861_ABYSS_1ST_BOSS_FIGHT_SHOCKED),
	SetSyncActionScript(SCREEN_FOCUS, A0862_ABYSS_1ST_BOSS_FIGHT_CAMERA),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetSyncActionScript(MARIO, A0015_DO_NOTHING),
	SetSyncActionScript(SCREEN_FOCUS, A0015_DO_NOTHING),
	JmpIfBitClear(GAME_OVER, ["EVENT_2596_restore_all_hp_13"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2596_restore_all_hp_13"),
	RestoreAllFP(),
	SetBit(ABYSS_BOSS_1_DEFEATED),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	EnterArea(room_id=R433_SMITHY_FACTORY_AREA_01_DUMMY, face_direction=NORTHEAST, x=7, y=106, z=10, run_entrance_event=True),
	Return(identifier="EVENT_2596_ret_18")
])
