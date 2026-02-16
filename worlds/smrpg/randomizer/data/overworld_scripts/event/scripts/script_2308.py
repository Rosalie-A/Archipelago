# E2308_BOOSTER_PASS_1ST_ROOM_LOADER
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
	RemoveObjectFromSpecificLevel(NPC_0, R100_BOOSTER_PASS_AREA_01),
	RemoveObjectFromSpecificLevel(NPC_1, R100_BOOSTER_PASS_AREA_01),
	RemoveObjectFromSpecificLevel(NPC_2, R100_BOOSTER_PASS_AREA_01),
	RunBackgroundEvent(event_id=E2309_BOOSTER_PASS_LAKITU_TOSSES_SPINY, return_on_level_exit=True),
	JmpIfBitClear(DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING, ["EVENT_2308_fade_in_from_black_async_15"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff()
	]),
	RemoveObjectFromCurrentLevel(MARIO),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0397_PLAYER_TUMBLES_DOWN_BOOSTER_PASS),
	Pause(64),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ClearBit(TEMP_7043_0),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_2308_fade_in_from_black_async_15"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2308_ret_20"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2308_ret_20"]),
	RunEventAsSubroutine(E3898_BOOSTER_PASS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2308_ret_20")
])
