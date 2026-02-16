# E0476_INITIATE_MUSHROOM_DERBY_FROM_TALKING_TO_BOSHI
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
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_9),
	PauseActionScript(NPC_10),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=16, y=77, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	]),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=11, y=83, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=11, y=75, z=0, direction=EAST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=20, y=69, z=0, direction=EAST),
		A_FaceNorthwest()
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=15, y=67, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=19, y=60, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_13),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_476_action_queue_23"]),
	SummonObjectToCurrentLevel(NPC_13),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNorthwest(),
		A_VisibilityOn()
	], identifier="EVENT_476_action_queue_23"),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True),
	PauseScriptUntilEffectDone(),
	Pause(30),
	PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	Pause(60),
	JmpToSubroutine(["EVENT_457_action_queue_0"]),
	RunBackgroundEvent(event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC, return_on_level_exit=True, run_as_second_script=True),
	EnableControls([]),
	Return()
])
