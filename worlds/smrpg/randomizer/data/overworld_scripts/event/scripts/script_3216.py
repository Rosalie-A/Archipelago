# E3216_SHIP_COIN_SNAKE_PUZZLE_TAIL_COIN
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
	PlaySound(sound=SO013_COIN, channel=6),
	PauseActionScript(MEM_70A8),
	DisableObjectTrigger(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_ShiftZUpSteps(2),
		A_VisibilityOff()
	]),
	Inc(TEMP_70AF),
	JmpIfVarEqualsConst(TEMP_70AF, 16, ["EVENT_3216_set_action_script_7"]),
	Return(),
	SetSyncActionScript(NPC_17, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL, identifier="EVENT_3216_set_action_script_7"),
	JmpIfBitSet(SHIP_COIN_PRIZE, ["EVENT_3216_ret_11"]),
	SetBit(SHIP_COIN_PRIZE),
	JmpToEvent(E0241_FREESTANDING_1_GRANT),
	Return(identifier="EVENT_3216_ret_11")
])
