# R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
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
                buffer_type=BufferType.EMPTY_3,
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
    music=M0050_NIMBUSLAND,
    entrance_event=E3761_NIMBUS_MEZZANINE_LOADER,
    events=[
        Event(
            event=E3750_NIMBUS_MEZZANINE_FALL_TO_HOT_SPRINGS,
            x=28,
            y=18,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3750_NIMBUS_MEZZANINE_FALL_TO_HOT_SPRINGS,
            x=28,
            y=19,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3787_NIMBUS_MEZZANINE_FALL_TO_EAST_VINE_ROOM,
            x=24,
            y=26,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3787_NIMBUS_MEZZANINE_FALL_TO_EAST_VINE_ROOM,
            x=24,
            y=27,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.TRAMPOLINE_JUMP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E3749_NIMBUS_MEZZANINE_TRAMPOLINE_TO_TOWN_SQUARE,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=24,
            y=18,
            z=2,
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
        RegularNPC( # 1
            npc=npcs.TRAMPOLINE_WARP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E3760_NIMBUS_MEZZANINE_TRAMPOLINE_TO_WORLD_MAP,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=28,
            y=27,
            z=2,
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
        RegularNPC( # 2
            npc=npcs.YELLOW_LETTER_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0094_OUT_OF_ORDER_NOTE,
            action_script=A0019_NIMBUS_NOTE,
            visible=True,
            x=24,
            y=19,
            z=2,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
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
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,),
    ]
)
