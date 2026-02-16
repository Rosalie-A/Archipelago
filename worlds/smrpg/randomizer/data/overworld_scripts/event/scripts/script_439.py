# E0439_PIPE_VAULT_FIREBALL_4
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
	StartBattleAtBattlefield(PACK030_SPARKY_WITH_SHYRANGER, BF21_KERO_SEWERS),
	RunEventAsSubroutine(E0440_PIPE_VAULT_FIREBALL_BACKGROUND),
	JmpIfBitSet(RUN_AWAY, ["EVENT_439_action_queue_7"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=10, y=10, z=2, direction=EAST)
	]),
	Jmp(["EVENT_439_jmp_if_bit_clear_8"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=8, y=13, z=4, direction=EAST)
	], identifier="EVENT_439_action_queue_7"),
	JmpIfBitClear(RUN_AWAY, ["EVENT_439_fade_in_from_black_async_10"], identifier="EVENT_439_jmp_if_bit_clear_8"),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False, identifier="EVENT_439_fade_in_from_black_async_10"),
	Jmp(["EVENT_436_action_queue_13"])
])
