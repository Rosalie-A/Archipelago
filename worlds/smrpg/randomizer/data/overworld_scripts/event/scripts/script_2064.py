# E2064_DOJO_LOADER
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
#DOJO_POSTGAME_COMPLETED
script = EventScript([
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastSteps(2),
		A_WalkNorthSteps(1),
		A_WalkNorthPixels(8)
	]),
    JmpIfBitSet(DOJO_POSTGAME_COMPLETED, ["EVENT_2064_action_queue_30_2"]),
	JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2064_action_queue_30"]),
	JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["EVENT_2064_action_queue_25"]),
	JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["EVENT_2064_action_queue_20"]),
	JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["EVENT_2064_action_queue_15"]),
	JmpIfBitSet(INITIAL_DOJO_CUTSCENE_COMPLETED, ["EVENT_2064_action_queue_11"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=13),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_2065_pause_0"]),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	], identifier="EVENT_2064_action_queue_11"),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=9),
		A_FaceSoutheast(),
		A_VisibilityOn()
	], identifier="EVENT_2064_action_queue_15"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=9),
		A_FaceSoutheast(),
		A_VisibilityOn()
	], identifier="EVENT_2064_action_queue_20"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=9),
		A_FaceSoutheast(),
		A_VisibilityOn()
	], identifier="EVENT_2064_action_queue_25"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
    
	JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_2064_action_queue_30_2"], identifier="EVENT_2064_action_queue_30"),
    RemoveObjectFromCurrentLevel(NPC_3),
    SummonObjectToCurrentLevel(NPC_4),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=9),
		A_FaceSoutheast(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),

	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=14),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	], identifier="EVENT_2064_action_queue_30_2"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=6, y=16, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOff(),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	]),
	SetSyncActionScript(NPC_3, A1006_DOJO_PERMA_JUMP),
	SetSyncActionScript(NPC_1, A1006_DOJO_PERMA_JUMP),
	RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
