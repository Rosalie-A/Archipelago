# E3093_OPEN_ABYSS_IF_STAR_PIECE_THRESHOLD_MET
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
	JmpIfBitClear(FACTORY_GATED_BY_STAR_PIECES, ["EVENT_3093_jmp_2"]),
	JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 6, ["EVENT_3093_set_bit_3"]),
	Jmp(["EVENT_3093_jmp_to_event_7"], identifier="EVENT_3093_jmp_2"),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, identifier="EVENT_3093_set_bit_3"),
	SetBit(MAP_GATE),
	JmpIfBitClear(KEEP_BOSS_3_DEFEATED, ["EVENT_3093_jmp_to_event_7"]),
	JmpToEvent(E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE, identifier="EVENT_3093_jmp_to_event_7")
])
