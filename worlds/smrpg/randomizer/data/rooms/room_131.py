# R131_SEA_AREA_04_BUNCH_OF_ZEOSTARS
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
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    exits=[
        RoomExit(
            x=14,
            y=61,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R134_SEA_AREA_03_SUPER_STAR_ROOM,
            show_message=False,
            dst_x=18,
            dst_y=97,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=4,
            y=57,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT,
            show_message=False,
            dst_x=1,
            dst_y=120,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
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
            destination=R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
            show_message=False,
            dst_x=26,
            dst_y=36,
            dst_z=5,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.ZEOSTAR_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=62,
            action_script=A0924_SEA_ZEOSTAR,
            visible=True,
            x=13,
            y=66,
            z=0,
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
        BattlePackClone( # 1
            npc=npcs.ZEOSTAR_NPC,
            battle_pack=62,
            action_script=A0924_SEA_ZEOSTAR,
            visible=True,
            x=8,
            y=71,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 2
            npc=npcs.ZEOSTAR_NPC,
            battle_pack=62,
            action_script=A0924_SEA_ZEOSTAR,
            visible=True,
            x=5,
            y=65,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 3
            npc=npcs.ZEOSTAR_NPC,
            battle_pack=62,
            action_script=A0924_SEA_ZEOSTAR,
            visible=True,
            x=2,
            y=65,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 4
            npc=npcs.ZEOSTAR_NPC,
            battle_pack=62,
            action_script=A0924_SEA_ZEOSTAR,
            visible=True,
            x=7,
            y=74,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
    ]
)
