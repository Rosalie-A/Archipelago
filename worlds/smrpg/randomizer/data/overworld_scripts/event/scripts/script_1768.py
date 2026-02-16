# E1768_TEMPLE_BOSS
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
	SetBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	RemoveObjectFromCurrentLevel(NPC_4),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(target=NPC_0),
	StartLoopNTimes(2),
	Pause(1, identifier="EVENT_1768_pause_13"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1768_pause_13"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	EndLoop(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	RemoveObjectFromSpecificLevel(NPC_1, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN),
	RemoveObjectFromSpecificLevel(NPC_2, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN),
	SetBit(TEMPLE_BOSS_DEFEATED),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	SetBit(MELODY_BAY_SONG_3_UNLOCKED),
	RunEventAsSubroutine(E1211_TEMPLE_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER)
])
