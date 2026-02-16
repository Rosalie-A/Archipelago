# E2067_DOJO_FIGHT_1_FINISHED
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
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, identifier="jagger_looks_around"),
		A_Pause(45),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(45),
		A_SetAllSpeeds(FASTER),
		A_WalkToXYCoords(x=5, y=9),
		A_FaceNortheast()
	], identifier="EVENT_2067_action_queue_0"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(80),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(15),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(NORMAL),
		A_ShadowOff(),
		A_JumpToHeight(48),
		A_WalkSoutheastSteps(1)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(5),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(2),
		A_ShadowOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestSteps(1),
		A_Pause(15),
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(height=48, silent=True),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkSoutheastPixels(4),
		A_VisibilityOff(),
		A_WalkSoutheastPixels(8),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(4),
		A_Pause(1),
		A_FixedFCoordOff(),
		A_Pause(1),
		A_FaceNorthwest(),
		A_Pause(1),
		A_FixedFCoordOn(),
		A_Pause(1),
		A_JumpToHeight(height=48, silent=True),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
		A_WalkSouthwestPixels(4),
		A_VisibilityOff(),
		A_WalkSouthwestPixels(32)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_WalkSouthwestPixels(4),
		A_Pause(1),
		A_FixedFCoordOff(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(1),
		A_FixedFCoordOn(),
		A_Pause(1),
		A_JumpToHeight(height=48, silent=True),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
		A_WalkNorthwestPixels(4),
		A_VisibilityOff(),
		A_WalkNorthwestPixels(10),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(4),
		A_Pause(1),
		A_FixedFCoordOff(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(5)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(25),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
		A_WalkNorthwestPixels(4),
		A_VisibilityOff(),
		A_WalkNorthwestPixels(10),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(4),
		A_Pause(1),
		A_FixedFCoordOff(),
		A_Pause(1),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(1),
		A_FixedFCoordOn(),
		A_Pause(1),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
		A_WalkNortheastPixels(4),
		A_VisibilityOff(),
		A_WalkNortheastPixels(16),
		A_VisibilityOn(),
		A_WalkNortheastPixels(4),
		A_Pause(1),
		A_FixedFCoordOff(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_Pause(1),
		A_FixedFCoordOn(),
		A_Pause(1),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
		A_WalkSoutheastPixels(4),
		A_VisibilityOff(),
		A_WalkSoutheastPixels(10),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(4),
		A_Pause(1),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(10)
	]),
	SetBit(DOJO_BOSS_1_DEFEATED),
	RunEventAsSubroutine(E1213_DOJO_1_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
