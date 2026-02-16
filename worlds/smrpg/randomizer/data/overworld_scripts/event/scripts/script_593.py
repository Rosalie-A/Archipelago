# E0593_MINES_BOSS_ROOM_LOADER_AFTER_DEFEAT
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
	JmpIfBitSet(POST_MINES_LEVEL_MODS_COMPLETED, ["mines_postgame_check"]),
	Pause(2),
	FadeOutMusicToVolume(duration=0, volume=1),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	RemoveObjectFromSpecificLevel(NPC_0, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_4, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_5, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_6, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	SetBit(MINES_BOSS_2_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	ApplyTileModToLevel(use_alternate=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=1),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=0),
	FadeInMusic(M0033_MOLEVILLE),
	SetBit(TEMP_7049_6),
	ApplyTileModToLevel(use_alternate=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0),
	SetBit(POST_MINES_LEVEL_MODS_COMPLETED),
	Store01To0248(),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(),
    JmpIfBitSet(MINES_POSTGAME_COMPLETED, ["finish_mines_boss_room_loader"], identifier="mines_postgame_check"),
    JmpIfBitClear(STAY_VOUCHER_USED, ["finish_mines_boss_room_loader"]),
	SummonObjectToCurrentLevel(NPC_0),
	JmpToEvent(E0257_FADE_IN_ASYNC, identifier="finish_mines_boss_room_loader")
])
