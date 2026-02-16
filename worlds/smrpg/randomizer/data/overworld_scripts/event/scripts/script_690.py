# E0690_MARRYMORE_RED_TOAD_1
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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_690_fade_out_music_FDA3_8"]),
	JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_690_run_dialog_5"]),
	RunDialog(dialog_id=DI2332_MARRYMORE_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2114_MARRYMORE_BOSS_NAMES, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_690_run_dialog_5"),
	RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
	Return(),
	FadeOutMusicFDA3(identifier="EVENT_690_fade_out_music_FDA3_8"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceNortheast()
	]),
	PlayMusicAtDefaultVolume(M0049_CELEBRATIONAL),
	Pause(30),
	RunDialog(dialog_id=DI2331_MARRYMORE_COMPOSER, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	Pause(170),
	Pause(180),
	Pause(10),
	PlayMusicAtDefaultVolume(M0039_MARRYMORE),
	CloseDialog(),
	Return()
])
