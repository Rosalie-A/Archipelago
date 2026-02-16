# R178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS
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
        extra_sprite_buffer_size=2,
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
    music=M0041_SUNKENSHIP,
    entrance_event=E3292_LOWER_SHIP_GENERIC_LOADER,
    events=[
        Event(
            event=E3266_SHIP_LOWER_RAT_STAIRWAY_OPEN_UPPER_DOOR,
            x=14,
            y=83,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=4,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3267_SHIP_LOWER_RAT_STAIRWAY_OPEN_LOWER_DOOR,
            x=9,
            y=91,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            height=4,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=9,
            y=90,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            show_message=False,
            dst_x=11,
            dst_y=124,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
        RoomExit(
            x=14,
            y=82,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS,
            show_message=False,
            dst_x=31,
            dst_y=64,
            dst_z=5,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.ALLEY_RAT_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=74,
            action_script=A0342_SHIP_2ND_STAIRWAY_RATS,
            visible=True,
            x=15,
            y=86,
            z=6,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
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
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0342_SHIP_2ND_STAIRWAY_RATS,
            visible=True,
            x=11,
            y=93,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 2
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0342_SHIP_2ND_STAIRWAY_RATS,
            visible=True,
            x=12,
            y=94,
            z=0,
            z_half=False,
            direction=NORTHEAST),
        BattlePackClone( # 3
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0342_SHIP_2ND_STAIRWAY_RATS,
            visible=True,
            x=15,
            y=87,
            z=6,
            z_half=False,
            direction=NORTHEAST),
    ]
)
