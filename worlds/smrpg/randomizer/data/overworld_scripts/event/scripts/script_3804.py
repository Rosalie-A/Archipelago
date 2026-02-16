# E3804_ENDING_CREDITS_CORONATION_NPCS
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
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	SetTempSyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
	SetTempSyncActionScript(NPC_3, A0807_INC_PALETTE_ROW_2),
	SetTempSyncActionScript(NPC_7, A0804_INC_PALETTE_ROW_15),
	SetTempSyncActionScript(NPC_9, A0803_INC_PALETTE_ROW),
	SetTempSyncActionScript(NPC_5, A0807_INC_PALETTE_ROW_2),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	StarMaskExpandFromScreenCenter(),
	Pause(60),
	SetTempSyncActionScript(NPC_8, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_1, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_3, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_11, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_9, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_2, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_7, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_5, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_10, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_6, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_4, A0238_CHEERING_NIMBITES),
	Pause(28),
	SetTempSyncActionScript(NPC_4, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_10, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_6, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_2, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_7, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_5, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_11, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_9, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_1, A0238_CHEERING_NIMBITES),
	SetTempSyncActionScript(NPC_3, A0238_CHEERING_NIMBITES),
	Pause(18),
	SetTempSyncActionScript(NPC_8, A0238_CHEERING_NIMBITES),
	Pause(65),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=15, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=14, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=14, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SetSpriteSequence(index=17, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(95),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(18),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(18),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(18),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkSouthwestPixels(8),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkSouthwestPixels(8),
		A_BPL262728()
	]),
	Pause(45),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkNorthwestSteps(5)
	]),
	Pause(160),
	StarMaskShrinkToScreenCenter(),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E3803_ENDING_CREDITS_GREEN_STAR)
])
