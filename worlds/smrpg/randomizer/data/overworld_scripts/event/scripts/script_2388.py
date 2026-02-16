# E2388_ABYSS_AMEBOID_BUTTON
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
	DisableObjectTrigger(MEM_70A8),
	JmpIfBitSet(ABYSS_GREEN_BUTTON, ["EVENT_2304_ret_0"]),
	SetBit(ABYSS_GREEN_BUTTON),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	Pause(1),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=1),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=2),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=3),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=4),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=5),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=6),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=7),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=8),
	Pause(1),
	SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	ApplySolidityModToLevel(permanent=True, room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS, mod_id=1),
	Return()
])
