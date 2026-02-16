# E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING
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
	PaletteSet(palette_set=33, row=7, bit_0=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=3, y=9, z=3, direction=EAST),
		A_WalkSouthwestPixels(6),
		A_ShiftZUpPixels(2),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_ShadowOn()
	]),
	SetSyncActionScript(MARIO, A0095_PLAYER_GAME_START),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(2)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4)
	]),
	FadeInFromBlack(sync=False),
	PlayMusicAtDefaultVolume(M0014_MARIO_SPAD),
	Pause(1),
	Set7000ToTappedButton(identifier="EVENT_2497_set_7000_to_tapped_button_12"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_2497_pause_action_script_17"]),
	Jmp(["EVENT_2497_set_7000_to_tapped_button_12"]),
	PauseActionScript(MARIO, identifier="EVENT_2497_pause_action_script_17"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_FaceSoutheast(),
		A_ShadowOff(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(69),
		A_FloatingOn(),
		A_WalkSoutheastSteps(2),
		A_Pause(35),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(1),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_StopSound(),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(30),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	RunEventAsSubroutine(E0181_NPC_QUEST_4_CONTAINER),
	RunEventAsSubroutine(E0182_NPC_QUEST_5_CONTAINER),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0),
	Return()
])
