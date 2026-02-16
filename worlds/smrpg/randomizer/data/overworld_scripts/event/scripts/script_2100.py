# E2100_HINOPIO
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
	JmpIfBitSet(TEMP_7043_2, ["EVENT_2100_run_dialog_3"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2100_jmp_to_event_41"]),
	JmpToEvent(E1183_VOLCANO_ITEM_SHOP),
	RunDialog(dialog_id=DI2576_VOLCANO_INN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2100_run_dialog_3"),
	JmpIfDialogOptionBSelected(["EVENT_2100_ret_40"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2100_set_var_to_const_10"]),
	RunDialog(dialog_id=DI2578_VOLCANO_INN_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 30, identifier="EVENT_2100_set_var_to_const_10"),
	Dec7000FromCoins(),
	FadeOutMusicToVolume(duration=2, volume=0),
	CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
	Pause(10),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=8, y=56, z=2, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=41, height=0)
	]),
	Pause(30),
	CircleMaskShrinkToObject(target=MARIO, width=40, speed=3, static=True),
	Pause(10),
	FadeOutMusicToVolume(duration=6, volume=100),
	Pause(10),
	Set7000ToTappedButton(identifier="EVENT_2100_set_7000_to_tapped_button_29"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_2100_circle_mask_static_34"]),
	Jmp(["EVENT_2100_set_7000_to_tapped_button_29"]),
	CircleMaskShrinkToObject(target=MARIO, width=255, speed=5, static=True, identifier="EVENT_2100_circle_mask_static_34"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(120),
		A_Pause(60),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	Pause(20),
	RestoreAllHP(),
	RestoreAllFP(),
	Return(identifier="EVENT_2100_ret_40"),
	JmpToEvent(E1184_VOLCANO_ARMOR_SHOP, identifier="EVENT_2100_jmp_to_event_41")
])
