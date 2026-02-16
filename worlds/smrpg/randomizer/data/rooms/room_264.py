# R264_LANDS_END_UNDERGROUND_AREA_02
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
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
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
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E1791_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER,
    exits=[
        RoomExit(
            x=22,
            y=26,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R263_LANDS_END_UNDERGROUND_AREA_01,
            show_message=False,
            dst_x=10,
            dst_y=92,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=30,
            y=10,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R265_LANDS_END_UNDERGROUND_AREA_03,
            show_message=False,
            dst_x=15,
            dst_y=109,
            dst_z=4,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.GECKIT_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=91,
            action_script=A0768_LANDS_END_UNDERGROUND_GECKO,
            visible=True,
            x=24,
            y=23,
            z=0,
            z_half=False,
            direction=NORTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackClone( # 1
            npc=npcs.GECKIT_NPC,
            battle_pack=91,
            action_script=A0768_LANDS_END_UNDERGROUND_GECKO,
            visible=True,
            x=26,
            y=21,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 2
            npc=npcs.GECKIT_NPC,
            battle_pack=91,
            action_script=A0768_LANDS_END_UNDERGROUND_GECKO,
            visible=True,
            x=29,
            y=18,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        BattlePackNPC( # 3
            npc=npcs.CHOW_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=83,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=28,
            y=13,
            z=0,
            z_half=False,
            direction=NORTHEAST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackClone( # 4
            npc=npcs.CHOW_NPC,
            battle_pack=83,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=29,
            y=14,
            z=0,
            z_half=False,
            direction=NORTHEAST),
        BattlePackClone( # 5
            npc=npcs.CHOW_NPC,
            battle_pack=83,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=28,
            y=13,
            z=2,
            z_half=False,
            direction=NORTHEAST),
        BattlePackClone( # 6
            npc=npcs.CHOW_NPC,
            battle_pack=83,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=29,
            y=14,
            z=2,
            z_half=False,
            direction=NORTHEAST),
    ]
)
