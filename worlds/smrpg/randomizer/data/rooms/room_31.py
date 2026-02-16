# R031_MUSHROOM_KINGDOM_CASTLE_VAULT
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
    music=M0002_MUSHROOMKINGDOM,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    exits=[
        RoomExit(
            x=6,
            y=89,
            z=3,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R021_MUSHROOM_KINGDOM_CASTLE_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
            show_message=False,
            dst_x=13,
            dst_y=69,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        ChestNPC( # 0
            npc=npcs.TREASURE_CHEST_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0172_CHEST_1_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=10,
            upper_70a7=0,
            visible=True,
            x=2,
            y=91,
            z=4,
            z_half=False,
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
        ChestNPC( # 1
            npc=npcs.TREASURE_CHEST_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0173_CHEST_2_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=0,
            upper_70a7=0,
            visible=True,
            x=5,
            y=97,
            z=4,
            z_half=False,
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
            npc=npcs.TREASURE_CHEST_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E0174_CHEST_3_CONTAINER,
            action_script=A0014_FLOATING_CHEST,
            lower_70a7=2,
            upper_70a7=0,
            visible=True,
            x=4,
            y=94,
            z=4,
            z_half=False,
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
    ]
)
