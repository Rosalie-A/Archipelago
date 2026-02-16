# R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[
        Event(
            event=E3230_CANCEL_STAR_IN_SEA,
            x=6,
            y=21,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=6,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3230_CANCEL_STAR_IN_SEA,
            x=7,
            y=21,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=6,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=5,
            y=40,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R134_SEA_AREA_03_SUPER_STAR_ROOM,
            show_message=False,
            dst_x=22,
            dst_y=81,
            dst_z=5,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=1,
            y=32,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT,
            show_message=False,
            dst_x=12,
            dst_y=102,
            dst_z=4,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=8,
            y=18,
            z=5,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R135_SEA_AREA_01_ENTRANCE,
            show_message=False,
            dst_x=16,
            dst_y=123,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SHAMAN_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3297_SEA_SHOP,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=3,
            y=30,
            z=0,
            z_half=True,
            direction=SOUTHEAST,
            face_on_trigger=True,
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
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.EMPTY_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E3297_SEA_SHOP,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=3,
            y=31,
            z=0,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=True,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
