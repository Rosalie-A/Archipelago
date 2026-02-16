# R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM
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
    music=M0066_BOWSER_SCASTLE_2NDTIME,
    entrance_event=E2224_KEEP_FINAL_BOSS_ROOM_LOADER,
    events=[
        Event(
            event=E2225_KEEP_2ND_BOSS,
            x=11,
            y=48,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=6,
            length=3,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT,
            x=13,
            y=43,
            z=1,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=1,
            y=67,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM,
            show_message=False,
            dst_x=27,
            dst_y=32,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.BOOMER_RED_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0000_EMPTY,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=8,
            y=39,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
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
        RegularNPC( # 1
            npc=npcs.HANGIN_XX_SHY_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0000_EMPTY,
            action_script=A0590_KEEP_FINAL_ROOM_CHANDELIER_STRING,
            visible=True,
            x=3,
            y=41,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
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
        RegularClone( # 2
            npc=npcs.HANGIN_XX_SHY_NPC,
            event_script=E0000_EMPTY,
            action_script=A0590_KEEP_FINAL_ROOM_CHANDELIER_STRING,
            visible=True,
            x=7,
            y=30,
            z=0,
            z_half=False,
            direction=NORTHWEST),
        RegularNPC( # 3
            npc=npcs.EMPTY_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0000_EMPTY,
            action_script=A0015_DO_NOTHING,
            speed=3,
            visible=True,
            x=12,
            y=45,
            z=3,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 4
            npc=npcs.EMPTY_NPC_2,
            event_script=E0000_EMPTY,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=13,
            y=44,
            z=3,
            z_half=False,
            direction=SOUTHWEST),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.RECOIL,
        SpriteAnimationState.WOBBLE,
    ]
)
