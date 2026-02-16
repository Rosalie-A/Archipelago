# R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
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
    entrance_event=E3226_SHIP_GENERIC_LOADER,
    events=[
        Event(
            event=E3158_ITEM_BEHIND_SHIP_UPPER_STAIRS_TILE,
            x=18,
            y=22,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=16,
            y=27,
            z=6,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES,
            show_message=False,
            dst_x=9,
            dst_y=71,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=17,
            y=41,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY,
            show_message=False,
            dst_x=22,
            dst_y=67,
            dst_z=5,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        ChestNPC( # 0
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0172_CHEST_1_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=10,
            upper_70a7=0,
            visible=True,
            x=19,
            y=36,
            z=6,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackNPC( # 1
            npc=npcs.ALLEY_RAT_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=74,
            action_script=A0341_SHIP_1ST_STAIRWAY_RATS,
            visible=True,
            x=18,
            y=27,
            z=6,
            z_half=False,
            direction=SOUTHEAST,
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
        BattlePackClone( # 2
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0341_SHIP_1ST_STAIRWAY_RATS,
            visible=True,
            x=21,
            y=32,
            z=2,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 3
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0341_SHIP_1ST_STAIRWAY_RATS,
            visible=True,
            x=20,
            y=38,
            z=0,
            z_half=False,
            direction=NORTHEAST),
        BattlePackClone( # 4
            npc=npcs.ALLEY_RAT_NPC,
            battle_pack=74,
            action_script=A0341_SHIP_1ST_STAIRWAY_RATS,
            visible=True,
            x=21,
            y=31,
            z=2,
            z_half=False,
            direction=NORTHWEST),
    ]
)
