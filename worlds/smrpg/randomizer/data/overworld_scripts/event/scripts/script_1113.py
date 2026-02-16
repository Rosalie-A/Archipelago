# E1113_SONG_HINT_TADPOLE
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
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1113_run_dialog_21"]),
	JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1113_jmp_if_bit_clear_8"]),
	JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1113_jmp_if_bit_clear_5"]),
	RunDialog(dialog_id=DI2664_TADPOLE_SONG_1_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1113_run_dialog_17"], identifier="EVENT_1113_jmp_if_bit_clear_5"),
	RunDialog(dialog_id=DI2665_TADPOLE_SONG_2_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_1113_run_dialog_19"], identifier="EVENT_1113_jmp_if_bit_clear_8"),
	RunDialog(dialog_id=DI2663_TADPOLE_FAVOURITE_SONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2668_TADPOLE_SONG_3_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FadeOutMusicToVolume(duration=1, volume=0),
	Pause(30),
	RunEventAsSubroutine(E1088_MELODY_BAY_THIRD_SONG_HINT),
	RunDialog(dialog_id=DI2673_TADPOLE_SONG_3_HINT_END, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	FadeOutMusicToVolume(duration=3, volume=100),
	Return(),
	RunDialog(dialog_id=DI2660_TADPOLE_PROMPTS_YOU_TO_FIND_2ND_SONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1113_run_dialog_17"),
	Return(),
	RunDialog(dialog_id=DI2662_TADPOLE_PROMPTS_YOU_TO_FIND_3RD_SONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1113_run_dialog_19"),
	Return(),
	RunDialog(dialog_id=DI2674_TADPOLE_AFTER_FINAL_SONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1113_run_dialog_21"),
	Return()
])
