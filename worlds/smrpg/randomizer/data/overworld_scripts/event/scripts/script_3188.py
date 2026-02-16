# E3188_MOUNT_MINECART
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_ShadowOn(),
		A_FloatingOff(),
		A_TransferToObjectXY(MEM_70A8),
		A_TransferXYZFPixels(x=0, y=0, z=26, direction=NORTHEAST),
		A_FaceSouthwest(),
		A_SequencePlaybackOff(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(8),
		A_UnknownCommand(bytearray(b' \x03')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_PlaySound(sound=SO048_MINECART_START, channel=4),
		A_Pause(200)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_UnknownCommand(bytearray(b' \x07')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x10\x00\x00\x01\x00\x00\x00\x04\x80')),
		A_Pause(200),
		A_SetBit(TEMP_7043_0),
		A_ObjectMemoryClearBit(arg_1=0x0B, bits=[3])
	]),
	Pause(1, identifier="EVENT_3188_pause_5"),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3188_pause_5"]),
	FadeOutToBlack(sync=False),
	Set7000ToMinecartTimer(),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
	RunMolevilleMountainSequence(),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1648_MINECART_ENDING)
])
