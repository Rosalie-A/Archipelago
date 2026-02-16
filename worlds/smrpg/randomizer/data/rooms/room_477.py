# R477_BOWSERS_KEEP_2ND_TIME_AREA_02
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
    music=M0000_CURRENT,
    entrance_event=E2144_KEEP_2ND_ROOM_LOADER,
    exits=[
        RoomExit(
            x=3,
            y=96,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=3,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R476_BOWSERS_KEEP_2ND_TIME_AREA_01,
            show_message=False,
            dst_x=10,
            dst_y=23,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=17,
            y=67,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            show_message=False,
            dst_x=4,
            dst_y=66,
            dst_z=5,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.TERRA_COTTA_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=110,
            action_script=A0547_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=7,
            y=85,
            z=0,
            z_half=False,
            direction=SOUTHEAST,
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
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackClone( # 1
            npc=npcs.TERRA_COTTA_NPC,
            battle_pack=110,
            action_script=A0548_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=10,
            y=87,
            z=0,
            z_half=False,
            direction=NORTHWEST),
        BattlePackClone( # 2
            npc=npcs.TERRA_COTTA_NPC,
            battle_pack=110,
            action_script=A0547_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=9,
            y=81,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 3
            npc=npcs.TERRA_COTTA_NPC,
            battle_pack=110,
            action_script=A0548_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=12,
            y=83,
            z=0,
            z_half=False,
            direction=NORTHWEST),
        BattlePackClone( # 4
            npc=npcs.TERRA_COTTA_NPC,
            battle_pack=110,
            action_script=A0547_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=11,
            y=77,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 5
            npc=npcs.TERRA_COTTA_NPC,
            battle_pack=110,
            action_script=A0548_KEEP_CROSSING_TERRA_COTTAS,
            visible=True,
            x=14,
            y=79,
            z=0,
            z_half=False,
            direction=NORTHWEST),
    ]
)
