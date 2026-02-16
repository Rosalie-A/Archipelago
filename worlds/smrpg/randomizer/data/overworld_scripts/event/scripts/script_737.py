# E0737_GARROS_HOUSE_LOADER
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
	PaletteSet(palette_set=110, row=1, bit_0=True, bit_1=True, bit_3=True),
	SetVarToRandom(PRIMARY_TEMP_7000, 6),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_737_action_queue_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_737_set_action_script_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_737_action_queue_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_737_set_action_script_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_737_action_queue_12"]),
	Jmp(["EVENT_737_set_action_script_13"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_8"),
	Jmp(["EVENT_737_set_action_script_13"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=2, is_mold=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_10"),
	Jmp(["EVENT_737_set_action_script_13"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_12"),
	SetSyncActionScript(NPC_6, A0119_SLOW_SEQUENCE_LOOP, identifier="EVENT_737_set_action_script_13"),
	RunEventAsSubroutine(E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
