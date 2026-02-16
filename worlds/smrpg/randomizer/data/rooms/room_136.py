# R136_SEA_AREA_07_SMALL_UNDERWATER_ROOM
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
        full_palette_buffer=False
    ),
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[
        Event(
            event=E3298_SEA_REVERSE_WHIRLPOOL_TO_LONE_CHEST,
            x=25,
            y=120,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=7,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=26,
            y=125,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
            show_message=False,
            dst_x=26,
            dst_y=37,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.WHIRLPOOL_WATER_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0256_RETURN,
            action_script=A0926_SEA_ESCAPE_BUBBLE,
            visible=True,
            x=25,
            y=120,
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
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.WHIRLPOOL_WATER_NPC_2,
            event_script=E0256_RETURN,
            action_script=A0927_SEA_ESCAPE_BUBBLE,
            visible=True,
            x=24,
            y=119,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.WHIRL,
    ]
)
