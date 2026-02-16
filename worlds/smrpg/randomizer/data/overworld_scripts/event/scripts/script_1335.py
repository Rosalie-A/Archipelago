# E1335_PORTRAIT_GAME_4
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
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1335_ret_50"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 5, ["EVENT_1335_remove_from_current_level_10"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=49),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	Pause(30),
	StartBattleAtBattlefield(PACK046_SPOOKUM_WITH_OTHER_MONSTERS, BF12_BOOSTER_TOWER),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_1338_pause_0"]),
	RemoveObjectFromCurrentLevel(NPC_3, identifier="EVENT_1335_remove_from_current_level_10"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=18, y=25),
		A_WalkNorthwestPixels(5),
		A_VisibilityOn(),
		A_FaceSoutheast(),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=49),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=17, y=27),
		A_FixedFCoordOff()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True, identifier="tower_toss")
	], identifier="tower_toss_aqueue"),
	Pause(10, identifier="tower_toss_contact_frame"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOn(),
		A_PlaySound(sound=SO078_CLICK, channel=6),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(21),
		A_FloatingOn(),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	PlaySound(sound=SO106_OFF_BALANCE, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=47),
	Pause(5),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=48),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastPixels(8),
		A_Pause(15),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(45)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(8),
		A_VisibilityOff()
	]),
	RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	SetBit(PORTRAIT_GAME_COMPLETED),
	Return(identifier="EVENT_1335_ret_50")
])
