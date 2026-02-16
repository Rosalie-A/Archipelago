# E2392_GARDENER
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
	SetVarToConst(TEMP_70AE, 23),
	StoreItemAmountTo7000(SeedItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2392_jmp_if_bit_set_11"]),
	StoreItemAmountTo7000(FertilizerItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2392_jmp_if_bit_set_144"]),
	JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["EVENT_2392_run_dialog_9"]),
	SetBit(UNKNOWN_GARDENER_708E_2),
	RunDialog(dialog_id=DI3216_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3103_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_9"),
	Return(),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_2, ["EVENT_2392_jmp_if_bit_set_14"], identifier="EVENT_2392_jmp_if_bit_set_11"),
	SetBit(UNKNOWN_GARDENER_708E_2),
	RunDialog(dialog_id=DI3216_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_3, ["EVENT_2392_run_dialog_40"], identifier="EVENT_2392_jmp_if_bit_set_14"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(108),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_Pause(22),
		A_SetSequenceSpeed(VERY_FAST)
	]),
	Pause(22),
	SlowDownMusicTempoBy(duration=0, change=32),
	Pause(2),
	RunDialog(dialog_id=DI3217_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FreezeCamera(),
	Pause(2),
	SlowDownMusicTempoBy(duration=0, change=0),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0855_PLAYER_DIZZY_FROM_GARDENER),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(32),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_4, ["EVENT_2392_run_dialog_30"]),
	RunDialog(dialog_id=DI3214_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2392_pause_31"]),
	RunDialog(dialog_id=DI3215_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_30"),
	Pause(16, identifier="EVENT_2392_pause_31"),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_3, ["EVENT_2392_run_dialog_40"]),
	SetBit(UNKNOWN_GARDENER_708E_3),
	RunDialog(dialog_id=DI3219_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2392_jmp_if_dialog_option_b_41"]),
	RunDialog(dialog_id=DI3221_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_40"),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_93"], identifier="EVENT_2392_jmp_if_dialog_option_b_41"),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(SeedItem),
	RunDialog(dialog_id=DI3223_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(GAVE_SEED),
	JmpIfBitSet(GAVE_FERTILIZER, ["EVENT_2392_freeze_camera_191"]),
	StoreItemAmountTo7000(FertilizerItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2392_jmp_if_bit_set_52"]),
	UnfreezeCamera(),
	Return(),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_4, ["EVENT_2392_run_dialog_85"], identifier="EVENT_2392_jmp_if_bit_set_52"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(108),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_Pause(22),
		A_SetSequenceSpeed(VERY_FAST)
	]),
	Pause(22),
	SlowDownMusicTempoBy(duration=0, change=32),
	Pause(2),
	RunDialog(dialog_id=DI3218_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FreezeCamera(),
	Pause(2),
	SlowDownMusicTempoBy(duration=0, change=0),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0855_PLAYER_DIZZY_FROM_GARDENER),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(32),
	RunDialog(dialog_id=DI3215_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(16),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetBit(UNKNOWN_GARDENER_708E_4),
	RunDialog(dialog_id=DI3220_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	Jmp(["EVENT_2392_freeze_camera_191"]),
	Pause(10, identifier="EVENT_2392_pause_80"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI3225_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	RunDialog(dialog_id=DI3224_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_85"),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	Jmp(["EVENT_2392_freeze_camera_191"]),
	Pause(10, identifier="EVENT_2392_pause_93"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI3230_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StoreItemAmountTo7000(FertilizerItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2392_jmp_if_bit_set_101"]),
	RunDialog(dialog_id=DI3225_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_4, ["EVENT_2392_jmp_if_bit_set_131"], identifier="EVENT_2392_jmp_if_bit_set_101"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(108),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_Pause(22),
		A_SetSequenceSpeed(VERY_FAST)
	]),
	Pause(22),
	SlowDownMusicTempoBy(duration=0, change=32),
	Pause(2),
	RunDialog(dialog_id=DI3218_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FreezeCamera(),
	Pause(2),
	SlowDownMusicTempoBy(duration=0, change=0),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0855_PLAYER_DIZZY_FROM_GARDENER),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(32),
	RunDialog(dialog_id=DI3215_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(16),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetBit(UNKNOWN_GARDENER_708E_4),
	RunDialog(dialog_id=DI3220_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	RunDialog(dialog_id=DI3227_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_run_dialog_134"], identifier="EVENT_2392_jmp_if_bit_set_131"),
	RunDialog(dialog_id=DI3224_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2392_jmp_if_dialog_option_b_135"]),
	RunDialog(dialog_id=DI3229_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_134"),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"], identifier="EVENT_2392_jmp_if_dialog_option_b_135"),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	RunDialog(dialog_id=DI3227_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_4, ["EVENT_2392_run_dialog_183"], identifier="EVENT_2392_jmp_if_bit_set_144"),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_2, ["EVENT_2392_action_queue_148"]),
	SetBit(UNKNOWN_GARDENER_708E_2),
	RunDialog(dialog_id=DI3216_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(108),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_Pause(22),
		A_SetSequenceSpeed(VERY_FAST)
	], identifier="EVENT_2392_action_queue_148"),
	Pause(24),
	SlowDownMusicTempoBy(duration=0, change=32),
	Pause(2),
	RunDialog(dialog_id=DI3218_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FreezeCamera(),
	Pause(2),
	SlowDownMusicTempoBy(duration=0, change=0),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0855_PLAYER_DIZZY_FROM_GARDENER),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(32),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_3, ["EVENT_2392_run_dialog_163"]),
	RunDialog(dialog_id=DI3214_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2392_pause_164"]),
	RunDialog(dialog_id=DI3215_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_163"),
	Pause(16, identifier="EVENT_2392_pause_164"),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	JmpIfBitSet(UNKNOWN_GARDENER_708E_4, ["EVENT_2392_run_dialog_173"]),
	SetBit(UNKNOWN_GARDENER_708E_4),
	RunDialog(dialog_id=DI3220_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2392_jmp_if_dialog_option_b_174"]),
	RunDialog(dialog_id=DI3222_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_173"),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"], identifier="EVENT_2392_jmp_if_dialog_option_b_174"),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	RunDialog(dialog_id=DI3228_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	RunDialog(dialog_id=DI3222_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2392_run_dialog_183"),
	JmpIfDialogOptionBSelected(["EVENT_2392_pause_80"]),
	RemoveOneOfItemFromInventory(FertilizerItem),
	SetBit(GAVE_FERTILIZER),
	JmpIfBitSet(GAVE_SEED, ["EVENT_2392_freeze_camera_191"]),
	RunDialog(dialog_id=DI3228_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnfreezeCamera(),
	Return(),
	FreezeCamera(identifier="EVENT_2392_freeze_camera_191"),
	RunDialog(dialog_id=DI3226_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(GAVE_SEED_AND_FERTILIZER),
	SummonObjectToSpecificLevel(NPC_0, R417_GARDENERS_HOUSE_OUTSIDE),
	SummonObjectToSpecificLevel(NPC_1, R417_GARDENERS_HOUSE_OUTSIDE),
	SummonObjectToSpecificLevel(NPC_0, R418_GARDENERS_HOUSE),
	SummonObjectToSpecificLevel(NPC_1, R418_GARDENERS_HOUSE),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSoutheastSteps(2),
		A_FaceNortheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(10),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_Pause(32),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_OverwriteSolidity(),
		A_SequenceLoopingOn(),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$ \x01\xa0\xff')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(25),
		A_BPL262728(),
		A_Pause(10),
		A_SequenceLoopingOff(),
		A_Pause(48),
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
		A_SetSequenceSpeed(FASTER),
		A_SequenceLoopingOn(),
		A_Pause(64),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_PlaySound(sound=SO000_SILENCE, channel=4)
	]),
	RunDialog(dialog_id=DI3075_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=25, y=14),
		A_FaceSoutheast()
	]),
	Pause(16),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
		A_SetSequenceSpeed(FASTER),
		A_SequenceLoopingOn(),
		A_Pause(64),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_PlaySound(sound=SO000_SILENCE, channel=4)
	]),
	RunDialog(dialog_id=DI3076_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(16),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=22, y=0)
	]),
	Pause(96),
	RunDialog(dialog_id=DI3085_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(32),
	PlaySound(sound=SO127_LIGHT_RATTLE, channel=6),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xe0\xfe`\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(32),
		A_BPL262728()
	]),
	SetAsyncActionScript(NPC_3, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(24),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(32),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO128_FLOATING_HOVERING, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(64),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(40),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(64),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Pause(48),
	RunDialog(dialog_id=DI3098_GARDENER_CUTSCENE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(160)
	]),
	RunDialog(dialog_id=DI3099_GARDENER_CUTSCENE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(24),
	SetSyncActionScript(NPC_3, A0856_GARDENER_RUNS_IN_CIRCLES),
	SlowDownMusicTempoBy(duration=0, change=32),
	Pause(2),
	RunDialog(dialog_id=DI2993_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_0),
	Pause(1, identifier="EVENT_2392_pause_236"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2392_pause_239"]),
	Jmp(["EVENT_2392_pause_236"]),
	Pause(4, identifier="EVENT_2392_pause_239"),
	SlowDownMusicTempoBy(duration=0, change=0),
	Pause(32),
	RunDialog(dialog_id=DI3101_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(8),
	RunDialog(dialog_id=DI3102_GARDENER_CUTSCENE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(8),
	SetAsyncActionScript(MARIO, A0857_PLAYER_DENIES_GARDENER),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return()
])
