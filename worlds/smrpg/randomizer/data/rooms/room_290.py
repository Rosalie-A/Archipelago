# R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING
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
        extra_sprite_buffer_size=1,
        buffers = [
            Buffer(
                buffer_type=BufferType.TREASURE_CHEST,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E3182_MINECART_PAID_LOBBY_ROOM_LOADER,
    events=[
        Event(
            event=E3189_FALL_TO_MINECART_ROOM_FROM_LOBBY,
            x=21,
            y=22,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=2,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3189_FALL_TO_MINECART_ROOM_FROM_LOBBY,
            x=21,
            y=21,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=2,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=21,
            y=21,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            show_message=False,
            dst_x=4,
            dst_y=55,
            dst_z=2,
            dst_z_half=False,
            dst_f=SOUTH,
            x_bit_7=False),
        RoomExit(
            x=21,
            y=22,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            show_message=False,
            dst_x=4,
            dst_y=55,
            dst_z=2,
            dst_z_half=False,
            dst_f=SOUTH,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.TRAMPOLINE_WARP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E3183_MINECART_PAID_LOBBY_TRAMPOLINE_TO_EXTERIOR,
            action_script=A0000_DO_NOTHING,
            visible=True,
            x=19,
            y=27,
            z=3,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
