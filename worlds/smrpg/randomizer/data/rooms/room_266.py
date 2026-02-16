# R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM
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
    music=M0066_BOWSER_SCASTLE_2NDTIME,
    entrance_event=E2208_KEEP_1ST_BOSS_ROOM_LOADER,
    exits=[
        RoomExit(
            x=23,
            y=106,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=3,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT,
            show_message=False,
            dst_x=4,
            dst_y=42,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=28,
            y=97,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM,
            show_message=False,
            dst_x=4,
            dst_y=77,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=26,
            y=93,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R450_BOWSERS_KEEP_AREA_12_CROCOS_SHOP_2_AFTER_MAGIKOOPAS_ROOM,
            show_message=False,
            dst_x=4,
            dst_y=29,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        ChestNPC( # 0
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0172_CHEST_1_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=15,
            upper_70a7=0,
            visible=False,
            x=27,
            y=104,
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
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.RED_MAGIKOOPA_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E2210_KEEP_1ST_BOSS_HEALS_YOU,
            action_script=A0015_DO_NOTHING,
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
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
