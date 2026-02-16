# R259_BOOSTER_TOWER_3F_AREA_01_GREEN_SWITCH_FOR_BP_SECRET
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
    music=M0032_ANDMYNAME_SBOOSTER,
    entrance_event=E2338_TOWER_BUTTON_ROOM_LOADER,
    exits=[
        RoomExit(
            x=28,
            y=116,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            show_message=False,
            dst_x=2,
            dst_y=77,
            dst_z=9,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
        RoomExit(
            x=30,
            y=125,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM,
            show_message=False,
            dst_x=20,
            dst_y=65,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.GREEN_SWITCH_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E2307_TOWER_BUTTON,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=29,
            y=121,
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
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
