# R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E3753_HOT_SPRINGS_LOBBY_LOADER,
    events=[
        Event(
            event=E3751_NIMBUS_LAND_HOT_SPRINGS_LOBBY_EXIT,
            x=20,
            y=57,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC_3,
            initiator=EventInitiator.NONE,
            event_script=E0346_TOADSTOOLS_ROOM_ITEM,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=20,
            y=50,
            z=0,
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
        RegularNPC( # 1
            npc=npcs.NIMBUS_GUARD_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3747_NIMBUS_HOT_SPRING_GUARDS,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=19,
            y=55,
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
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularClone( # 2
            npc=npcs.NIMBUS_GUARD_NPC,
            event_script=E3747_NIMBUS_HOT_SPRING_GUARDS,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=20,
            y=54,
            z=0,
            z_half=False,
            direction=NORTHWEST),
        RegularNPC( # 3
            npc=npcs.TRAMPOLINE_JUMP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E3746_HOT_SPRINGS_TRAMPOLINE_TO_MEZZANINE,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=54,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.SURPRISE_FRAME,
    ]
)
