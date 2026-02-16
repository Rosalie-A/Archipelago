# E2081_MUSTY_FEARS_LAMP
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
	MoveScriptToMainThread(),
	SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(2),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=112, green=104, blue=16, speed=0),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB]),
	FadeOutMusicToVolume(duration=8, volume=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkToXYCoords(x=5, y=49),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(120),
		A_WalkNorthwestPixels(32)
	]),
	Pause(5),
	CircleMaskShrinkToObject(target=NPC_5, width=0, speed=3, static=True),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(120),
	ApplyTileModToLevel(use_alternate=True, room_id=R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, mod_id=32),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(16),
		A_WalkSouthPixels(2),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	Pause(5),
	FadeInFromBlack(sync=False, duration=120),
	Pause(150),
	SetSyncActionScript(NPC_2, A0568_MUSTY_FEARS_1),
	JmpIfBitSet(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_2081_pause_0"]),
	SetBit(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED),
    RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER),
	Pause(60, identifier="EVENT_2081_pause_0"),
	RunDialog(dialog_id=DI1105_MUSTY_FEARS_EXPLANATION, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
    
	JmpIfBitSet(INVISIBLE_FLAG_1_FOUND, ["EVENT_2081_dialog_97"]),
	RunDialog(dialog_id=DI1109_RESERVED_FOR_GREAPERFLAG_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
    Jmp(["EVENT_2081_pause_97"]),
	RunDialog(dialog_id=DI3748_GREAPER_FLAG_FOUND, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2081_dialog_97"),
	
	Pause(20, identifier="EVENT_2081_pause_97"),
	SetSyncActionScript(NPC_3, A0568_MUSTY_FEARS_1),
	Pause(60),
    
	JmpIfBitSet(INVISIBLE_FLAG_2_FOUND, ["EVENT_2081_dialog_99"]),
	RunDialog(dialog_id=DI1107_RESERVED_FOR_BIGBOOFLAG_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
    Jmp(["EVENT_2081_pause_99"]),
	RunDialog(dialog_id=DI3750_BIGBOO_FLAG_FOUND, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2081_dialog_99"),
	
	Pause(20, identifier="EVENT_2081_pause_99"),
	SetSyncActionScript(NPC_4, A0568_MUSTY_FEARS_1),
	Pause(60),
    
	JmpIfBitSet(INVISIBLE_FLAG_3_FOUND, ["EVENT_2081_dialog_100"]),
	RunDialog(dialog_id=DI1108_RESERVED_FOR_DRYBONESFLAG_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
    Jmp(["EVENT_2081_pause_100"]),
	RunDialog(dialog_id=DI3749_DRYBONES_FLAG_FOUND, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2081_dialog_100"),
	
	Pause(60, identifier="EVENT_2081_pause_100"),
    
	StoreItemAmountTo7000(DryBonesFlagItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_set_7000_to_tapped_button_98"]),
	StoreItemAmountTo7000(GreaperFlagItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_set_7000_to_tapped_button_98"]),
	StoreItemAmountTo7000(BigBooFlagItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_set_7000_to_tapped_button_98"]),
	RunDialog(dialog_id=DI2232_FLAGS_FOUND, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
    RemoveOneOfItemFromInventory(DryBonesFlagItem),
	RemoveOneOfItemFromInventory(GreaperFlagItem),
	RemoveOneOfItemFromInventory(BigBooFlagItem),

	SetSyncActionScript(NPC_2, A0569_MUSTY_FEARS_2, identifier="EVENT_2081_set_7000_to_tapped_button_98"),
	SetSyncActionScript(NPC_3, A0569_MUSTY_FEARS_2),
	SetSyncActionScript(NPC_4, A0569_MUSTY_FEARS_2),
	Pause(60),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=0, green=0, blue=0, speed=0),
	ResetPrioritySet(),
	FadeOutMusicToVolume(duration=0, volume=100),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL)
	]),
	FadeOutMusicToVolume(duration=6, volume=100),
	Set7000ToTappedButton(identifier="EVENT_2081_set_7000_to_tapped_button_99"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_2081_apply_tile_mod_103"]),
	Jmp(["EVENT_2081_set_7000_to_tapped_button_99"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, mod_id=32, identifier="EVENT_2081_apply_tile_mod_103"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(120),
		A_WalkSouthPixels(32),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(1),
	PlaySound(sound=SO058_INSERT, channel=6),
	ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	Return()
])