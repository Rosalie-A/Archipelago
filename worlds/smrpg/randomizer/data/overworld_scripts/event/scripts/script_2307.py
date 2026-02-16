# E2307_TOWER_BUTTON
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
	DisableObjectTrigger(NPC_0),
	JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["EVENT_2307_ret_12"]),
	SetBit(BOOSTER_PASS_SECRET_OPEN),
	SetVarToConst(APPRENTICE_LOSS_COUNTER, 4),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_OverwriteSolidity()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=0),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	RunDialog(dialog_id=DI3154_BOOSTER_PASS_OPENED, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return(identifier="EVENT_2307_ret_12")
])
