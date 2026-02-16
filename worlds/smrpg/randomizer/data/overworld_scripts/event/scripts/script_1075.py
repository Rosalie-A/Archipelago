# E1075_TOADOFSKY
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
	RunDialog(dialog_id=DI2719_MUSIC_TUTORIAL_PROMPT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_1075_run_dialog_22"]),
	SetBit(TEMP_7044_6),
	JmpToSubroutine(["EVENT_1078_jmp_if_bit_clear_0"]),
	RunDialog(dialog_id=DI2720_MUSIC_TUTORIAL, above_object=NPC_12, closable=False, sync=True, multiline=True, use_background=False),
	Pause(1),
	PauseScriptResumeOnNextDialogPageB(),
	Pause(1),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=14, y=32, z=0, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_WalkSouthwestPixels(4),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_7, A0081_MELODY_BAY_TUTORIAL),
	PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6),
	Pause(1),
	PauseScriptResumeOnNextDialogPageB(),
	Pause(1),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkNorthwestSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkNorthwestSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO042_TADPOLE_POND_STAFF_TI, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(50)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_Pause(45),
		A_WalkSoutheastSteps(2),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkSoutheastSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO039_TADPOLE_POND_STAFF_FA, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkSoutheastSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO038_TADPOLE_POND_STAFF_MI, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkSoutheastSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO037_TADPOLE_POND_STAFF_RE, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(25),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOff(),
		A_WalkSoutheastSteps(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(7),
		A_PlaySound(sound=SO036_TADPOLE_POND_STAFF_DO, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(50),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(10),
		A_VisibilityOff()
	]),
	CloseDialog(),
	RunDialog(dialog_id=DI2717_SONGS_FINISHED, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ClearBit(TEMP_7044_6),
	Return(),
	RunDialog(dialog_id=DI2721_MUSIC_TUTORIAL_DECLINE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1075_run_dialog_22"),
	Return(),
	RunDialog(dialog_id=DI2721_MUSIC_TUTORIAL_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
