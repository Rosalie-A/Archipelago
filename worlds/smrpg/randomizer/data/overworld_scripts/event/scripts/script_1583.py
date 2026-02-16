# E1583_LANDS_END_UNDERGROUND_TRAMPOLINE_TO_DESERT
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
	JmpIfBitSet(TEMP_7076_0, ["EVENT_1583_action_queue_6"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=SOUTH, x=8, y=110, z=0),
	SetVarToConst(ACTIVE_NPC, 20),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, looping=False),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(36),
		A_SetSequenceSpeed(FAST),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_Pause(5),
		A_SequenceLoopingOff()
	], identifier="EVENT_1583_action_queue_6"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(3),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(1),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(2),
		A_Pause(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(1),
		A_Pause(9),
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOn(),
		A_JumpToHeight(height=108, silent=True),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_1583_action_queue_7_SUBSCRIPT_pause_21"),
		A_JmpIfMarioInAir(["EVENT_1583_action_queue_7_SUBSCRIPT_pause_21"])
	]),
	Return()
])
