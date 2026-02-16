# E0409_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_LOADER
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
	RunEventAsSubroutine(E0771_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_SHUFFLED_NPC_ANIMATION_LOADER),
	RemoveObjectFromCurrentLevel(NPC_2),
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED, ["EVENT_409_jmp_if_object_not_in_level_5"]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_261_fade_out_music_to_volume_0"], identifier="EVENT_409_jmp_if_object_not_in_level_5"),
	SummonObjectToCurrentLevel(NPC_2),
	PauseActionScript(NPC_2),
	SetSyncActionScript(NPC_2, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	FadeInFromBlack(sync=False),
	Return()
])
