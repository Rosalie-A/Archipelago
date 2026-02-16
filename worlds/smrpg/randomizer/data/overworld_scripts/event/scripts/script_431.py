# E0431_PIPE_VAULT_GOOMBA_THUMPIN_ENTRANCE_PIPE
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
	SetBit(TEMP_7044_6),
	SetVarToConst(X_COORD_2, 13),
	SetVarToConst(Y_COORD_2, 38),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R143_PIPE_VAULT_GOOMBATHUMPING_ROOM, face_direction=NORTHEAST, x=2, y=123, z=1, run_entrance_event=True),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x00')),
		A_AddConstToVar(Z_COORD_2, 2304),
		A_UnknownCommand(bytearray(b'\x99')),
		A_TransferXYZFPixels(x=16, y=0, z=0, direction=EAST),
		A_JumpToHeight(height=0, silent=True)
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_431_pause_8"),
	JmpIfMarioInAir(["EVENT_431_pause_8"]),
	Return()
])
