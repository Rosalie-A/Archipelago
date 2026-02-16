# R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT
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
    music=M0067_WEAPONSFACTORY,
    entrance_event=E2359_ABYSS_1ST_SAVE_ROOM_LOADER,
    events=[
        Event(
            event=E2380_ABYSS_BOLT_NEAR_SIDE,
            x=5,
            y=74,
            z=10,
            f=EdgeDirection.SOUTHWEST,
            height=7,
            length=4,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E2381_ABYSS_BOLT_FAR_SIDE,
            x=8,
            y=65,
            z=10,
            f=EdgeDirection.SOUTHWEST,
            height=7,
            length=4,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=1,
            y=78,
            z=10,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R350_SMITHY_FACTORY_AREA_01,
            show_message=False,
            dst_x=7,
            dst_y=20,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=16,
            y=53,
            z=10,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS,
            show_message=False,
            dst_x=1,
            dst_y=125,
            dst_z=10,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=16,
            y=55,
            z=10,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS,
            show_message=False,
            dst_x=1,
            dst_y=125,
            dst_z=10,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.FACTORY_HEX_NUT_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E2369_ABYSS_BOLT,
            action_script=A0187_ABYSS_BOLT,
            visible=True,
            x=6,
            y=73,
            z=10,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
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
        RegularClone( # 1
            npc=npcs.FACTORY_HEX_NUT_NPC,
            event_script=E2369_ABYSS_BOLT,
            action_script=A0187_ABYSS_BOLT,
            visible=True,
            x=7,
            y=72,
            z=10,
            z_half=False,
            direction=SOUTHWEST),
        RegularNPC( # 2
            npc=npcs.SAVE_POINT_NPC_3,
            initiator=EventInitiator.JUMP_ON,
            event_script=E2390_ABYSS_1ST_SAVE_POINT,
            action_script=A0120_EMBEDDED_ROUTINE,
            visible=True,
            x=12,
            y=60,
            z=10,
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
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
