# R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
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
    music=M0000_CURRENT,
    entrance_event=E2335_TOWER_FIRST_STAIRCASE_LOADER,
    exits=[
        RoomExit(
            x=17,
            y=76,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            show_message=False,
            dst_x=29,
            dst_y=115,
            dst_z=5,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=14,
            y=70,
            z=8,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
            show_message=False,
            dst_x=4,
            dst_y=111,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.SPOOKUM_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=46,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
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
        BattlePackClone( # 1
            npc=npcs.SPOOKUM_NPC,
            battle_pack=47,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 2
            npc=npcs.SPOOKUM_NPC,
            battle_pack=46,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 3
            npc=npcs.SPOOKUM_NPC,
            battle_pack=47,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 4
            npc=npcs.SPOOKUM_NPC,
            battle_pack=46,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackClone( # 5
            npc=npcs.SPOOKUM_NPC,
            battle_pack=47,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        ChestNPC( # 6
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E2574_TOWER_FIRST_STAIRCASE_CHEST,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=3,
            upper_70a7=0,
            visible=True,
            x=16,
            y=66,
            z=11,
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
