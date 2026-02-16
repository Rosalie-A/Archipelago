# R016_MARIOS_PAD
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
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
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
    music=M0014_MARIO_SPAD,
    entrance_event=E1408_MARIOS_PAD_EXTERIOR_LOADER,
    events=[
        Event(
            event=E1406_MARIOS_PAD_OPEN_DOOR,
            x=12,
            y=34,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=6,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E1407_MARIOS_PAD_CLOSE_DOOR,
            x=11,
            y=34,
            z=1,
            f=EdgeDirection.SOUTHWEST,
            height=6,
            length=3,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E1407_MARIOS_PAD_CLOSE_DOOR,
            x=11,
            y=33,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=6,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E1407_MARIOS_PAD_CLOSE_DOOR,
            x=12,
            y=35,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=6,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=13,
            y=32,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R189_MARIOS_PIPEHOUSE,
            show_message=False,
            dst_x=2,
            dst_y=16,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        MapExit(
            x=10,
            y=51,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=True,
            destination=OW08_MARIOS_PAD,
            show_message=False,
            byte_2_bit_1=False,
            byte_2_bit_0=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SAVE_POINT_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0080_SAVE_BLOCK_SUBROUTINE,
            action_script=A0120_EMBEDDED_ROUTINE,
            visible=True,
            x=5,
            y=34,
            z=0,
            z_half=True,
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
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
