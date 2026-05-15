from .MapMFIData import MapMFIData
from .Sector import Sector


class BATTLEBin:
    start_sector = 1000
    start_sector_location = start_sector * Sector.sector_size
    sector_count = 682
    end_location = start_sector_location + (sector_count * Sector.sector_size)
    map_mfi_data_offset = 0x8EE74
    map_count = 128
    map_mfi_data_length = 16
    map_mfi_total_length = map_count * map_mfi_data_length
    map_mfi_datas: list[MapMFIData] = []
    all_data: bytearray

    def __init__(self, all_data: bytearray):
        self.all_data = all_data
        map_mfi_data = all_data[self.map_mfi_data_offset:self.map_mfi_data_offset + self.map_mfi_total_length]
        for i in range(self.map_count):
            self.map_mfi_datas.append(
                MapMFIData(map_mfi_data[i * self.map_mfi_data_length:(i + 1) * self.map_mfi_data_length], i))

    def apply_data(self):
        for map_mfi_data in self.map_mfi_datas:
            map_mfi_data.apply_data()
            map_mfi_data_start = self.map_mfi_data_offset + (map_mfi_data.index * 16)
            map_mfi_data_end = map_mfi_data_start + 16
            self.all_data[map_mfi_data_start:map_mfi_data_end] = map_mfi_data.raw_data