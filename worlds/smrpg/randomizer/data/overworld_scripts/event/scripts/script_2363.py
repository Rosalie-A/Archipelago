# E2363_ABYSS_1ST_BOSS_ROOM_LOADER
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
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	FreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_WalkNorthPixels(4),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_WalkWestPixels(11),
		A_WalkSouthPixels(2),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_WalkWestPixels(4),
		A_WalkSouthPixels(2),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(16)
	]),
	RunEventAsSubroutine(E0854_ABYSS_1ST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=1, is_sequence=True, looping=True),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_2363_action_queue_8_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_2363_action_queue_8_SUBSCRIPT_pause_2"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return()
])
