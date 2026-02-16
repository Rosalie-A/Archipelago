# E0433_PIPE_VAULT_CHOMPWEED
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
	JmpIfMarioInAir(["EVENT_256_ret_0"]),
	StoreCoinCountTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_433_action_queue_10"]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_4),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOff(),
		A_TransferXYZFPixels(x=0, y=0, z=24, direction=EAST),
		A_SetVarToRandom(PRIMARY_TEMP_700C, 8),
		A_FaceEast7C(),
		A_JumpToHeight(height=108, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkFDirectionPixels(12),
		A_FloatingOn(),
		A_WalkFDirectionPixels(12),
		A_VisibilityOff()
	]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_5),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FloatingOff(),
		A_TransferXYZFPixels(x=0, y=0, z=24, direction=EAST),
		A_SetVarToRandom(PRIMARY_TEMP_700C, 8),
		A_FaceEast7C(),
		A_JumpToHeight(height=108, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkFDirectionPixels(12),
		A_FloatingOn(),
		A_WalkFDirectionPixels(12),
		A_VisibilityOff()
	]),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 2),
	Dec7000FromCoins(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(10),
		A_ResetProperties()
	], identifier="EVENT_433_action_queue_10"),
	Pause(1, identifier="EVENT_433_pause_11"),
	JmpIfObjectInAir(MEM_70A8, ["EVENT_433_pause_11"]),
	Return()
])
