# E3746_HOT_SPRINGS_TRAMPOLINE_TO_MEZZANINE
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
	JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_3746_run_event_as_subroutine_9"]),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	EnterArea(room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE, face_direction=SOUTHWEST, x=28, y=17, z=0),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=132, silent=True),
		A_WalkSouthwestSteps(2),
		A_FloatingOn(),
		A_WalkSouthwestPixels(20)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
	PauseScriptUntilEffectDone(),
	Return(),
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE, identifier="EVENT_3746_run_event_as_subroutine_9"),
	Return()
])
