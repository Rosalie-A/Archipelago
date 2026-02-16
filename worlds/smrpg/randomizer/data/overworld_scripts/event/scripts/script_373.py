# E0373_MUSHROOM_KINGDOM_BOSS_FIGHT
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
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_375_play_music_default_volume_0"]),
	Pause(1, identifier="EVENT_373_pause_1"),
	JmpIfMarioInAir(["EVENT_373_pause_1"]),
	JmpIfObjectInSpecificLevel(NPC_1, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, ["EVENT_373_run_event_as_subroutine_93"]),
	Set7016701BToObjectXYZ(target=MARIO, bit_7=True),
	JmpIfVarNotEqualsConst(Z_COORD_2, 4, ["EVENT_256_ret_0"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=16, y=29, height=4),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_373_action_queue_6"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=12, y=9)
	]),
	SetBit(TEMP_7043_5),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO086_BIG_BOUNCE, channel=6),
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\n\xe0\xff')),
		A_Walk1StepSouthwest(),
		A_BPL262728(),
		A_TransferToXYZF(x=18, y=26, z=20, direction=EAST),
		A_Pause(120),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestPixels(3),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(13)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(150),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True)
	]),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(180),
	SetBit(TEMP_7043_5),
	PauseActionScript(NPC_10),
	SetSyncActionScript(NPC_10, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_4, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_5, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_6, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_7, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	JmpIfBitClear(UNKNOWN_7082_4, ["EVENT_373_action_queue_33"]),
	SetSyncActionScript(NPC_8, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_9, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	Jmp(["EVENT_373_play_sound_35"]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_WalkNorthwestPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(8),
		A_FixedFCoordOff()
	], identifier="EVENT_373_action_queue_33"),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_WalkSoutheastPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(8),
		A_FixedFCoordOff()
	]),
	PlaySound(sound=SO021_RUMBLING, channel=6, identifier="EVENT_373_play_sound_35"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_Walk1StepNorth(),
		A_WalkSouthPixels(12),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(6),
		A_WalkNorthPixels(4),
		A_StopSound(),
		A_WalkSouthPixels(3),
		A_WalkNorthPixels(1)
	]),
	Pause(60),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_10, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	SetAsyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
	Pause(20),
	SetBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(40),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(40),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ClearBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(80),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(80),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(80),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(80),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(80),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(80),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=72, silent=True),
		A_Walk1StepSoutheast()
	]),
	SetVarToConst(TEMP_70A9, 24),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(4)
	]),
	SetVarToConst(TEMP_70A9, 25),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceNorthwest(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(4)
	]),
	SetVarToConst(TEMP_70A9, 26),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	Pause(20),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=72, silent=True),
		A_Walk1StepNorthwest()
	]),
	SetVarToConst(TEMP_70A9, 26),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSoutheast()
	]),
	Pause(20),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNortheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
	ReturnFD(),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_Pause(20),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%@\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_BPL262728()
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	RememberLastObject(),
	FadeOutMusicToVolume(duration=0, volume=1),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER, identifier="EVENT_373_run_event_as_subroutine_93"),
	ReturnFD(),
	RestoreAllHP(),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromSpecificLevel(NPC_8, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM),
	RemoveObjectFromSpecificLevel(NPC_9, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	Pause(30),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	JmpToEvent(E0375_TALK_TO_CHANCELLOR_AFTER_MUSHROOM_KINGDOM_BOSS),
	Return()
])
