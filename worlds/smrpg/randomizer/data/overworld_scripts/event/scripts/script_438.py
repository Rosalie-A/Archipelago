# E0438_PIPE_VAULT_FIREBALL_3
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
	StopAllBackgroundEvents(),
	StartBattleAtBattlefield(PACK031_MULTIPLE_SPARKY_WITH_SHYRANGER, BF21_KERO_SEWERS),
	RunEventAsSubroutine(E0440_PIPE_VAULT_FIREBALL_BACKGROUND),
	JmpIfBitSet(RUN_AWAY, ["EVENT_438_action_queue_7"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=8, y=13, z=4, direction=EAST)
	]),
	Jmp(["EVENT_438_set_bit_8"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=7, y=16, z=2, direction=EAST)
	], identifier="EVENT_438_action_queue_7"),
	SetBit(TEMP_7049_6, identifier="EVENT_438_set_bit_8"),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	JmpIfBitClear(RUN_AWAY, ["EVENT_438_fade_in_from_black_async_12"]),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False, identifier="EVENT_438_fade_in_from_black_async_12"),
	Jmp(["EVENT_436_action_queue_13"])
])
