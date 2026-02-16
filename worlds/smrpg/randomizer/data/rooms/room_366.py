# R366_VOLCANO_AREA_13_WSAVE_POINT
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
    music=M0062_BARRELVOLCANO,
    entrance_event=E3923_VOLCANO_SAVE_ROOM_LOADER,
    exits=[
        RoomExit(
            x=12,
            y=67,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R386_VOLCANO_AREA_12_ERUPTING_STUMPET,
            show_message=False,
            dst_x=19,
            dst_y=123,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=15,
            y=71,
            z=5,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R386_VOLCANO_AREA_12_ERUPTING_STUMPET,
            show_message=False,
            dst_x=20,
            dst_y=110,
            dst_z=4,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        ChestNPC( # 0
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E3391_VOLCANO_1ST_SAVE_ROOM_LOWER_CHEST,
            action_script=A0435_FLOATING_CHEST,
            lower_70a7=2,
            upper_70a7=0,
            visible=True,
            x=10,
            y=67,
            z=4,
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
        ChestNPC( # 1
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E3392_VOLCANO_1ST_SAVE_ROOM_UPPER_CHEST,
            action_script=A0435_FLOATING_CHEST,
            lower_70a7=3,
            upper_70a7=0,
            visible=True,
            x=11,
            y=61,
            z=8,
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
        RegularNPC( # 2
            npc=npcs.SAVE_POINT_NPC_3,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0080_SAVE_BLOCK_SUBROUTINE,
            action_script=A0120_EMBEDDED_ROUTINE,
            visible=True,
            x=13,
            y=65,
            z=5,
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
    ]
)
