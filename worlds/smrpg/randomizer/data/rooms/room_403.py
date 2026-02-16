# R403_LANDS_END_DESERT_AREA_05
# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.levels.classes import ObjectType, EventInitiator, PostBattleBehaviour, Direction, EdgeDirection, ExitType, BufferType, BufferSpace, VramStore, ShadowSize
from smrpgpatchbuilder.datatypes.levels.classes import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone
from ...types.room import Room
from ...types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from . import npcs
from ..variables.room_names import *
from ..variables.overworld_area_names import *
from ..variables.music_names import *
from ..variables.event_script_names import *
from ..variables.action_script_names import *
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=True,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.COINS,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0013_ROADISFULLOFDANGERS,
    entrance_event=E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE,
    objects=[
        RegularNPC( # 0
            npc=npcs.WHIRLPOOL_DESERT_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E1758_LANDS_END_PENULTIMATE_WHIRLPOOL_1,
            action_script=A0780_LANDS_END_WHIRLPOOLS,
            visible=True,
            x=26,
            y=60,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=True,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.WHIRLPOOL_DESERT_NPC,
            event_script=E1759_LANDS_END_PENULTIMATE_WHIRLPOOL_2,
            action_script=A0780_LANDS_END_WHIRLPOOLS,
            visible=True,
            x=28,
            y=60,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularNPC( # 2
            npc=npcs.SHOGUN_NPC_2,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E1885_WHIRLPOOL_SHOGUN_3,
            action_script=A0713_LANDS_END_SHOGUN,
            visible=True,
            x=26,
            y=60,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 3
            npc=npcs.COIN_NPC,
            initiator=EventInitiator.NONE,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 4
            npc=npcs.FROG_COIN_NPC,
            initiator=EventInitiator.NONE,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            speed=1,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.WHIRL,
    ]
)
