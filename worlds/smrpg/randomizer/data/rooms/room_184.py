# R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT
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
        ally_sprite_buffer_size=2,
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
    music=M0041_SUNKENSHIP,
    entrance_event=E3284_SHIP_SAVE_ROOMS_LOADER,
    events=[
        Event(
            event=E3271_SHIP_FINAL_SAVE_ROOM_OPEN_EXIT_DOOR,
            x=31,
            y=112,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=4,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=26,
            y=115,
            z=3,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES,
            show_message=False,
            dst_x=23,
            dst_y=97,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=31,
            y=111,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            show_message=False,
            dst_x=1,
            dst_y=32,
            dst_z=5,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SAVE_POINT_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0080_SAVE_BLOCK_SUBROUTINE,
            action_script=A0120_EMBEDDED_ROUTINE,
            visible=True,
            x=27,
            y=121,
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
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        ChestNPC( # 1
            npc=npcs.TREASURE_CHEST_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0172_CHEST_1_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=0,
            upper_70a7=0,
            visible=True,
            x=24,
            y=120,
            z=3,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        ChestNPC( # 2
            npc=npcs.TREASURE_CHEST_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0173_CHEST_2_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=10,
            upper_70a7=0,
            visible=True,
            x=30,
            y=116,
            z=3,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
