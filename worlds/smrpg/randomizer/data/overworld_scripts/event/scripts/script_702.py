# E0702_MARRYMORE_TAKE_PHOTO
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
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_5),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_WalkToXYCoords(x=22, y=68),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FaceSoutheast()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2164_MARRYMORE_PHOTO, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_702_action_queue_6_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_702_action_queue_6_SUBSCRIPT_pause_2"]),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2165_MARRYMORE_PHOTO, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2202_MARRYMORE_PHOTO, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	CircleMaskShrinkToObject(target=NPC_3, width=0, speed=10, static=True),
	PauseScriptUntilEffectDone(),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	CircleMaskShrinkToObject(target=NPC_3, width=255, speed=10, static=True),
	PauseScriptUntilEffectDone(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
