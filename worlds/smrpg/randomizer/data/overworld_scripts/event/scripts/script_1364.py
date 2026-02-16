# E1364_CURTAIN_ROOM_EXIT_TO_BALCONY
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
	JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_1364_jmp_if_bit_set_27"]),
	JmpIfBitSet(TOWER_BOSS_1_DEFEATED, ["EVENT_1364_jmp_if_bit_set_27"]),
	SetVarToConst(TEMP_7026, 0, identifier="EVENT_1364_set_var_to_const_2"),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=2),
	FreezeCamera(),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=3),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=0, y=3, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=3, y=26),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(15),
		A_FaceNortheast(),
		A_Pause(15),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(8),
		A_Pause(7),
		A_SetSpriteSequence(index=10, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(7),
		A_SetSpriteSequence(index=11, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_SetSpriteSequence(index=9, is_mold=True, looping=True),
		A_Pause(7),
		A_SetSpriteSequence(index=8, is_mold=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(7)
	]),
	Pause(20),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	Pause(2),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNorthwestPixels(20),
		A_SetPriority(2),
		A_Pause(15),
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(NORMAL)
	]),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	Pause(2),
	JmpToEvent(E1358_CURTAIN_GAME_BEGINS_NPCS_WALK_INTO_ROOM),
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_1364_jmp_if_bit_set_30"], identifier="EVENT_1364_jmp_if_bit_set_27"),
	EnterArea(room_id=R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, face_direction=NORTHEAST, x=4, y=19, z=0, run_entrance_event=True, identifier="EVENT_1364_enter_area_28"),
	Return(),
	JmpIfBitSet(FAST_TRAVEL_ENABLED, ["EVENT_1364_enter_area_28"], identifier="EVENT_1364_jmp_if_bit_set_30"),
	Return()
])
