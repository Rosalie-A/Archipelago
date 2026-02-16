# E3590_ROSE_TOWN_CHIMNEY
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
	SetVarToConst(X_COORD_2, 23),
	SetVarToConst(Y_COORD_2, 47),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R087_ROSE_TOWN_ITEM_SHOP, face_direction=SOUTH, x=7, y=69, z=3),
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_3590_set_bit_7"]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_VisibilityOn()
	]),
	SetBit(TEMP_709C_3, identifier="EVENT_3590_set_bit_7"),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	RunEventAsSubroutine(E0282_UNKNOWN_PIPE_VAULT),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3590_pause_11"),
	JmpIfMarioInAir(["EVENT_3590_pause_11"]),
	StopSound(),
	PlaySound(sound=SO058_INSERT, channel=6),
	ClearBit(DIRECTIONAL_7049_0),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
