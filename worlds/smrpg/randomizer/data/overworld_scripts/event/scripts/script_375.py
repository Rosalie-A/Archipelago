# E0375_TALK_TO_CHANCELLOR_AFTER_MUSHROOM_KINGDOM_BOSS
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
	PlayMusicAtDefaultVolume(M0002_MUSHROOMKINGDOM, identifier="EVENT_375_play_music_default_volume_0"),
	EnterArea(room_id=R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, face_direction=NORTHEAST, x=16, y=30, z=2),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(16)
	]),
	FadeInFromBlack(sync=True, duration=200),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(8),
		A_FaceSouthwest(),
		A_Pause(20),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest(),
		A_Pause(20),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_Pause(20),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	PauseScriptUntilEffectDone(),
	SetBit(UNKNOWN_7065_5),
	SetBit(UNKNOWN_7065_6),
	SetBit(UNKNOWN_7065_7),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_KERO_SEWERS),
	SetBit(TEMP_7042_0),
	SetBit(MUSHROOM_KINGDOM_LIBERATED),
    RunEventAsSubroutine(E1196_MUSHROOM_KINGDOM_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
