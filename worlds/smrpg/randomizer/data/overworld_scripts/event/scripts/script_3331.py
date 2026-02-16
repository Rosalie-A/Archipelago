# E3331_VOLCANO_1ST_BOSS_FIGHT
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
	JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["EVENT_3331_ret_24"]),
	Pause(700),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(VOLCANO_MIDBOSS_DEFEATED),
	SetSyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_5, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_6, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_7, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_8, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_9, A1023_ERUPTED_MAGMITES),
	ApplyTileModToLevel(use_alternate=True, room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, mod_id=33),
	UnknownCommand(bytearray(b'\xfdD')),
	ResetPrioritySet(),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E1233_VOLCANO_MID_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_3331_ret_24")
])
