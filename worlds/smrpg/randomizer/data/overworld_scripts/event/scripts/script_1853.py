# E1853_SKY_BRIDGE_RIDE_SHAMAN
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1853_stop_all_background_events_5', 'EVENT_1853_run_dialog_3']),
	RunDialog(dialog_id=DI1313_ELEVATOR_SHAMAN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1853_run_dialog_3"),
	Return(),
	StopAllBackgroundEvents(identifier="EVENT_1853_stop_all_background_events_5"),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_3),
	ClearBit(TEMP_7043_2),
	SetBit(SKY_BRIDGE_COURSE_CHOICE),
	SetBit(SKY_BRIDGE_COURSE_1_CHOSEN),
	SetVarToConst(TEMP_702E, 48),
	SetVarToConst(TEMP_702C, 70),
	ActionQueueSync(target=NPC_17, subscript=[
		A_TransferToXYZF(x=20, y=104, z=18, direction=EAST)
	]),
	Set7016701BToObjectXYZ(target=MEM_70A8, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_WalkTo70167018(),
		A_FloatingOn()
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceNorthwest(),
		A_ShiftZUpSteps(10),
		A_WalkNorthSteps(3),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO161_GHOST, channel=4),
		A_JumpToHeight(128),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True),
		A_TransferToXYZF(x=20, y=112, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	Return()
])
