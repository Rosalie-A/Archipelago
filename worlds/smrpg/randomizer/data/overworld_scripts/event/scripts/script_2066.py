# E2066_DOJO_BOSS_1
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
	JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2066_run_dialog_29"]),
	JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["EVENT_2066_run_dialog_27"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=16),
		A_FaceNortheast()
	]),
	Pause(30),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkSouthwestSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(15),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(30)
	]),
	RunEventAsSubroutine(E0861_DOJO_1ST_BOSS_CHALLENGE_SUBROUTINE),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	RestoreAllHP(),
	RestoreAllFP(),
	JmpIfBitSet(GAME_OVER, ["EVENT_2066_fade_in_from_black_async_14"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2066_fade_in_from_black_async_14"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=8, z=3, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_2066_fade_in_from_black_async_14"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(1),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	Pause(30),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2066_stop_music_FDA2_21"]),
	JmpIfBitClear(GAME_OVER, ["EVENT_2066_jmp_25"]),
	StopMusicFDA2(identifier="EVENT_2066_stop_music_FDA2_21"),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	Return(),
	Jmp(["EVENT_2067_action_queue_0"], identifier="EVENT_2066_jmp_25"),
	Return(),
	RunDialog(dialog_id=DI3044_DOJO_BOSS_1_AFTER_DEFEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_27"),
	Return(),
	RunDialog(dialog_id=DI3352_DOJO_BOSS_1_FULLY_DEFEATED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_29"),
	Return()
])
