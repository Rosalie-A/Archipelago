# E0468_MUSHROOM_DERBY_USE_YOSHI_COOKIE
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
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SequenceLoopingOn()
	]),
	CopyVarToVar(from_var=UNKNOWN_70EB, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_468_pause_5"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	RunDialog(dialog_id=DI0523_NEW_PAGE_NUM_OF_COOKIES_AWAIT_TERMINATE, above_object=NPC_14, closable=False, sync=False, multiline=False, use_background=False),
	Pause(1, identifier="EVENT_468_pause_5"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[6], destinations=["EVENT_468_jmp_if_bit_set_9"]),
	Jmp(["EVENT_468_pause_5"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_468_pause_5"], identifier="EVENT_468_jmp_if_bit_set_9"),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_468_pause_5"]),
	Dec(SECONDARY_TEMP_7024),
	Inc(UNKNOWN_70EE),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_468_close_dialog_16"]),
	RunDialog(dialog_id=DI0523_NEW_PAGE_NUM_OF_COOKIES_AWAIT_TERMINATE, above_object=NPC_14, closable=False, sync=False, multiline=False, use_background=False),
	Jmp(["EVENT_468_set_bit_17"]),
	CloseDialog(identifier="EVENT_468_close_dialog_16"),
	SetBit(TEMP_7043_4, identifier="EVENT_468_set_bit_17"),
	PauseActionScript(MARIO),
	PauseActionScript(NPC_9),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_TransferToObjectXY(MARIO),
		A_TransferXYZFPixels(x=0, y=0, z=16, direction=EAST),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_JumpToHeight(height=110, silent=True),
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(14),
		A_SetSpriteSequence(index=6, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=11, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=12, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=14, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=16, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=17, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=18, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=19, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=20, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_ResetProperties(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(4)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_9, A0430_YOSHI_FINISH_RACE),
	SetSyncActionScript(MARIO, A0503_MUSHROOM_DERBY_PLAYER_WHEN_COOKIE_USED),
	Jmp(["EVENT_468_pause_5"])
])
