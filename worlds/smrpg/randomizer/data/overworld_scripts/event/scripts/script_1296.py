# E1296_TOWER_CHECKERBOARD_ROOM_FIREBALL_LAUNCHER
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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1296_ret_11"], identifier="EVENT_1296_jmp_if_bit_set_0"),
	Pause(1),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=MARIO, destinations=["EVENT_1296_jmp_if_bit_set_0"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=20, y=23, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_Pause(10),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(3),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(30)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=80, silent=True),
		A_Pause(40)
	]),
	StartBattleAtBattlefield(PACK143_TOWER_FIREBALLS, BF12_BOOSTER_TOWER),
	JmpIfBitClear(GAME_OVER, ["EVENT_1296_set_bit_8"]),
	ResetAndChooseGame(),
	SetBit(TEMP_7043_0, identifier="EVENT_1296_set_bit_8"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_1296_ret_11")
])
