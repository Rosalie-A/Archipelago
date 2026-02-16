# E1771_TEMPLE_BOSS_ROOM_LOADER
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
	JmpIfObjectInSpecificLevel(NPC_4, R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, ["EVENT_1771_jmp_if_bit_clear_2"]),
    JmpIfBitSet(TEMPLE_POSTGAME_BOSS_DEFEATED, ["do_not_load_postgame_boss"]),
	JmpIfBitClear(TEMPLE_BOSS_BUTTON_PRESSED, ["do_not_load_postgame_boss"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["do_not_load_postgame_boss"]),
    SummonObjectToCurrentLevel(NPC_5),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	], identifier="do_not_load_postgame_boss"),
	JmpIfBitClear(TEMPLE_BOSS_BUTTON_PRESSED, ["EVENT_1771_fade_in_from_black_async_80"], identifier="EVENT_1771_jmp_if_bit_clear_2"),
	ApplySolidityModToLevel(permanent=True, room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, mod_id=0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthSteps(3),
		A_SetWalkingSpeed(NORMAL)
	]),
	RunEventAsSubroutine(E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False, identifier="EVENT_1771_fade_in_from_black_async_80"),
	Return()
])