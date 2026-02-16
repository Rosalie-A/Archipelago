from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from .contents.dialog_pointers import pointers
from .contents.compression_table import compression_table
from .contents.dialog_table_0x22 import dialog_data as data_0
from .contents.dialog_table_0x23 import dialog_data as data_1
from .contents.dialog_table_0x24 import dialog_data as data_2

data = DialogCollection(pointers, [data_0, data_1, data_2], compression_table=compression_table)