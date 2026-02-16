# E3504_BOOSTER_HILL_HENCHMAN_INTERACTION
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
	StopBackgroundEvent(TIMER_701C),
	ClearBit(TEMP_7043_5),
	EnableControlsUntilReturn([]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_3504_reset_coords_15', 'EVENT_3504_set_7000_to_object_coord_4']),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, identifier="EVENT_3504_set_7000_to_object_coord_4"),
	CompareVarToConst(PRIMARY_TEMP_7000, 288),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3504_reset_coords_15"]),
	DisableObjectTrigger(MEM_70A8),
	ResumeActionScript(MEM_70A8),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(height=112, silent=True),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_VisibilityOff(identifier="EVENT_3504_action_queue_9_SUBSCRIPT_visibility_off_7"),
		A_Pause(1),
		A_VisibilityOn(),
		A_CompareVarToConst(SECONDARY_TEMP_7024, 65475),
		A_JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3504_action_queue_9_SUBSCRIPT_pause_15"]),
		A_WalkSoutheastPixels(2),
		A_AddConstToVar(SECONDARY_TEMP_7024, 65534),
		A_Jmp(["EVENT_3504_action_queue_9_SUBSCRIPT_visibility_off_7"]),
		A_Pause(1, identifier="EVENT_3504_action_queue_9_SUBSCRIPT_pause_15"),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	EnableControlsUntilReturn([B]),
	EnableObjectTrigger(MEM_70A8),
	SetVarToConst(TIMER_701C, 2),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	Return(),
	ResetCoords(MEM_70A8, identifier="EVENT_3504_reset_coords_15"),
	SetSyncActionScript(MEM_70A8, A0711_BOOSTER_HILL_HENCHMAN_BOUNCE),
	SetVarToConst(TEMP_7028, 48),
	Jmp(["EVENT_3501_action_queue_19"])
])
