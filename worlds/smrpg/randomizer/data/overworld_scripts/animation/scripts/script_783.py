#A0783_LANDS_END_CANNON_WHILE_PLAYER_OCCUPIED
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SetBit(TEMP_7043_0),
	A_SetBit(TEMP_7044_6),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_2"),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_SetVarToConst(TEMP_7032, 0),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1280),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1281),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1282),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1283),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_20"]),
	A_JmpIfBitSet(TEMP_7044_2, ["ACTION_783_play_sound_19"]),
	A_PlaySound(sound=SO144_CLICK, channel=4),
	A_Jmp(["ACTION_783_set_sprite_sequence_20"]),
	A_PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=4, identifier="ACTION_783_play_sound_19"),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_20"),
	A_SetVarToConst(TEMP_7032, 5),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1282),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1281),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 1280),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_31"]),
	A_PlaySound(sound=SO144_CLICK, channel=4),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_31"),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_SetVarToConst(TEMP_7032, 0),
	A_SetVarToConst(SECONDARY_TEMP_7024, 256),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 257),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_SetVarToConst(SECONDARY_TEMP_7024, 258),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 259),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_783_clear_bit_61"]),
	A_JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_49"]),
	A_JmpIfBitSet(TEMP_7044_2, ["ACTION_783_play_sound_48"]),
	A_PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=4),
	A_Jmp(["ACTION_783_set_sprite_sequence_49"]),
	A_PlaySound(sound=SO144_CLICK, channel=4, identifier="ACTION_783_play_sound_48"),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_783_set_sprite_sequence_49"),
	A_SetVarToConst(TEMP_7032, 1),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 258),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 257),
	A_Pause(6),
	A_SetVarToConst(SECONDARY_TEMP_7024, 256),
	A_Pause(6),
	A_JmpIfBitClear(TEMP_7044_4, ["ACTION_783_set_sprite_sequence_2"]),
	A_PlaySound(sound=SO144_CLICK, channel=4),
	A_Jmp(["ACTION_783_set_sprite_sequence_2"]),
	A_ClearBit(TEMP_7044_6, identifier="ACTION_783_clear_bit_61"),
	A_ResetProperties(),
	A_ReturnQueue()
])
