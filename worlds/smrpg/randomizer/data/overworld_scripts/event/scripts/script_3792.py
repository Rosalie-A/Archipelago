# E3792_FACTORY_FINAL_BOSS_ROOM_LOADER
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
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferXYZFPixels(x=0, y=4, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferXYZFPixels(x=246, y=2, z=30, direction=NORTHEAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=3, y=23, z=0, direction=SOUTHEAST),
		A_FloatingOff()
	]),
	FreezeCamera(),
	RememberLastObject(),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2])
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2])
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1])
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1])
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[])
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetPriority(3),
		A_TransferXYZFPixels(x=0, y=8, z=0, direction=EAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=0, y=8, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetPriority(3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=0, y=24, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetPriority(3),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=0, y=24, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetPriority(3),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=234, y=19, z=0, direction=EAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	RememberLastObject(),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_8),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_5),
	RunEventAsSubroutine(E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	RunEventAtReturn(E3794_FACTORY_FINAL_BOSS_FIGHT),
	Return()
])
