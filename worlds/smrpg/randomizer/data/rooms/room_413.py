# R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR
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
    music=M0000_CURRENT,
    entrance_event=E3811_NIMBUS_INNER_CELLAR_LOADER,
    exits=[
        RoomExit(
            x=29,
            y=57,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            show_message=False,
            dst_x=25,
            dst_y=17,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.NIMBUS_GUARD_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0744_NIMBUS_LAND_LIBERATED_CASTLE_INNER_CELLAR_REWARD,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=27,
            y=51,
            z=0,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=True,
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
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.NIMBUSITE_RED_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3719_NIMBUS_CASTLE_RIGHT_RED_CELLAR_WOMAN,
            action_script=A0810_NIMBUS_NPC_RANDOM_DIRECTIONS,
            visible=True,
            x=27,
            y=57,
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
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 2
            npc=npcs.NIMBUSITE_RED_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3722_NIMBUS_CASTLE_LEFT_CELLAR_WOMAN,
            action_script=A0811_NIMBUS_NPC_RANDOM_DIRECTIONS,
            visible=True,
            x=30,
            y=49,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
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
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
