# E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE
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
	FadeOutMusicFDA3(),
	PlayMusicAtDefaultVolume(M0053_SILENCE),
	SetBit(UNKNOWN_BOWSERS_KEEP_707F_0),
	EnterArea(room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, face_direction=NORTHEAST, x=5, y=36, z=0, run_entrance_event=True),
	Return(),
	ClearBit(UNKNOWN_BOWSERS_KEEP_707F_0, identifier="EVENT_3356_clear_bit_5"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Pause(1, identifier="EVENT_3356_pause_8"),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[5, 7], destinations=["EVENT_3356_pause_8"]),
	FadeInMusic(M0066_BOWSER_SCASTLE_2NDTIME),
	SetVarToConst(TEMP_70AE, 20),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
