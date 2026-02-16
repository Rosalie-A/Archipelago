# E1674_LANDS_END_ENTER_GROTTO
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
	SetSyncActionScript(MARIO, A0161_SEQUENCE_LOOPING_OFF),
	PlaySound(sound=SO032_UNDERGROUND_WARP, channel=6),
	StartAsyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_FloatingOff(),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_sequence=True, looping=True),
		A_StartLoopNTimes(7),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_ShiftZUpPixels(1),
		A_EndLoop()
	]),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=8, duration=4, bit_6=True, bit_7=True),
	EnterArea(room_id=R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, face_direction=NORTHWEST, x=17, y=103, z=11),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	PauseScriptUntilEffectDone(),
	Jmp(["EVENT_1676_set_var_to_const_1"])
])
