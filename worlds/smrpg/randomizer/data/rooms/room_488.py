# R488_MUSHROOM_KINGDOM_JUMPING_KIDS_HOUSE_1F
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0002_MUSHROOMKINGDOM,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=[
        Event(
            event=E0304_UNKNOWN,
            x=7,
            y=15,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0305_UNKNOWN,
            x=6,
            y=21,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3102_EXIT_JUMPING_KIDS_HOUSE,
            x=6,
            y=26,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False
        ),
    ],
    exits=[
        RoomExit(
            x=3,
            y=19,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R489_MUSHROOM_KINGDOM_JUMPING_KIDS_HOUSE_2F,
            show_message=False,
            dst_x=1,
            dst_y=45,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.WALLET_GUY_ALSO_CASINO_ASSISTANTS_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0302_MUSHROOM_KINGDOM_DAD,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=7,
            y=22,
            z=2,
            z_half=False,
            direction=NORTHWEST,
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
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.RAINI_NPC,
            event_script=E0301_MUSHROOM_KINGDOM_MOM,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=7,
            y=16,
            z=2,
            z_half=False,
            direction=NORTHEAST),
        RegularNPC( # 2
            npc=npcs.MARRYMORE_KID_PURPLE_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0306_MUSHROOM_KINGDOM_BROTHER,
            action_script=A0128_WALK_RANDOM_DIRECTIONS,
            visible=True,
            x=5,
            y=18,
            z=2,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
