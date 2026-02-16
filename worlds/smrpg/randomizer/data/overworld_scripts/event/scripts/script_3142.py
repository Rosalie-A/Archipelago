# E3142_PIPE_TO_BOSS
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
	SetVarToConst(X_COORD_2, 12),
	SetVarToConst(Y_COORD_2, 108),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	JmpIfBitSet(SEWER_BOSS_DEFEATED, ["EVENT_3142_set_bit_12"]),
	EnterArea(room_id=R302_KERO_SEWERS_AREA_08_BELOMES_ROOM, face_direction=NORTHEAST, x=6, y=40, z=9),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=0, silent=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(6),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(1, identifier="EVENT_3142_pause_9"),
	JmpIfMarioInAir(["EVENT_3142_pause_9"]),
	Return(),
	SetBit(UNKNOWN_MIDAS_RIVER_704D_6, identifier="EVENT_3142_set_bit_12"),
	ClearBit(BUCKET_WARP_BIT),
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=108, z=0, run_entrance_event=True),
	Return()
])
