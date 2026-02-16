# R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND
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
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[
        Event(
            event=E3765_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_LOWER_CHEST_ROOM,
            x=19,
            y=96,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E3765_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_LOWER_CHEST_ROOM,
            x=19,
            y=97,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E3782_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_WEST_VINE_ROOM,
            x=17,
            y=104,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E3782_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_WEST_VINE_ROOM,
            x=17,
            y=105,
            z=6,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC_3,
            initiator=EventInitiator.NONE,
            event_script=E0346_TOADSTOOLS_ROOM_ITEM,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=27,
            y=67,
            z=4,
            z_half=False,
            direction=NORTHEAST,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        ChestNPC( # 1
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0172_CHEST_1_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=3,
            upper_70a7=0,
            visible=True,
            x=18,
            y=96,
            z=11,
            z_half=True,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=True,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=True,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        ChestNPC( # 2
            npc=npcs.TREASURE_CHEST_NPC_2,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0173_CHEST_2_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=5,
            upper_70a7=0,
            visible=True,
            x=20,
            y=92,
            z=11,
            z_half=True,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=True,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=True,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.EXOR,
    ]
)
