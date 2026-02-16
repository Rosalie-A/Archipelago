# R161_SUNKEN_SHIP_AREA_03_GREAPERS
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
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
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
    music=M0041_SUNKENSHIP,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[
        Event(
            event=E3250_SHIP_1ST_GREAPER_ROOM_OPEN_UPPER_DOOR,
            x=10,
            y=42,
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
            x=4,
            y=52,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R160_SUNKEN_SHIP_AREA_01,
            show_message=False,
            dst_x=2,
            dst_y=13,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
        RoomExit(
            x=10,
            y=41,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES,
            show_message=False,
            dst_x=4,
            dst_y=82,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.GREAPER_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=76,
            action_script=A0309_SHIP_EARLY_GREAPERS,
            visible=True,
            x=8,
            y=42,
            z=2,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackClone( # 1
            npc=npcs.GREAPER_NPC,
            battle_pack=76,
            action_script=A0309_SHIP_EARLY_GREAPERS,
            visible=True,
            x=5,
            y=46,
            z=2,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 2
            npc=npcs.GREAPER_NPC,
            battle_pack=76,
            action_script=A0309_SHIP_EARLY_GREAPERS,
            visible=True,
            x=9,
            y=46,
            z=2,
            z_half=False,
            direction=NORTHWEST),
        RegularNPC( # 3
            npc=npcs.YELLOW_LETTER_NPC,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E3304_SHIP_1ST_GREAPER_ROOM_HINT_NOTE,
            action_script=A0728_SET_SEQ_1,
            visible=True,
            x=6,
            y=46,
            z=0,
            z_half=True,
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
    ]
)
