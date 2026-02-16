import os
import shutil
from django.core.management.base import BaseCommand
from copy import deepcopy
import importlib.util
from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from datetime import datetime

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("-t", "--text", action='store_true', dest="text", help="use -t if you want to output your assembled bytes as plain text files.")
		parser.add_argument("-b", "--bin", action='store_true', dest="bin", help="use -b if you want to output your assembled bytes as flexhex-compatible img files.")
		parser.add_argument("-r", "--rom", dest="rom", help="specify a path to a mario rpg rom if you want to output your assembled bytes as a bps patch.")

	def handle(self, *args, **options):
		module_path = "disassembler_output.monster_ai.monster_scripts"
		
		outputToText = options["text"] or False
		outputToBin = options["bin"] or False
		romPath = options["rom"]
		outputToPatch = romPath is not None 
		
		if not (outputToText or outputToBin or outputToPatch):
			print("you need to specify at least one output format. options are --text, --bin, --rom")
			exit(1)

		if outputToText:
			shutil.rmtree("./src/assembler_output/monster_ai/txt", ignore_errors=True)
			os.makedirs("./src/assembler_output/monster_ai/txt", exist_ok=True)
		if outputToBin:
			shutil.rmtree("./src/assembler_output/monster_ai/bin", ignore_errors=True)
			os.makedirs("./src/assembler_output/monster_ai/bin", exist_ok=True)
		if outputToPatch:
			os.makedirs("./src/assembler_output/monster_ai/bps", exist_ok=True)
		
		rom = bytearray()
		if outputToPatch:
			original_rom = bytearray(open(romPath, "rb").read())
			rom = deepcopy(original_rom)

		module = importlib.import_module(module_path)
		bank = module.monster_scripts
		if bank:
			output = bank.render()
			if outputToBin:
				with open(f'./src/assembler_output/monster_ai/bin/write_to_0x3930AA.img', 'wb') as f:
					f.write(output[0])
				with open(f'./src/assembler_output/monster_ai/bin/write_to_0x39F400.img', 'wb') as f:
					f.write(output[1])
			if outputToText:
				with open(f'./src/assembler_output/monster_ai/txt/write_to_0x3930AA.txt', 'w') as f:
					f.write(" ".join([f'{b:02X}' for b in output[0]]))
				with open(f'./src/assembler_output/monster_ai/txt/write_to_0x39F400.txt', 'w') as f:
					f.write(" ".join([f'{b:02X}' for b in output[1]]))
			if outputToPatch:
				end1 = 0x3930AA + len(output[0])
				if end1 > len(rom):
					raise ValueError(f"change at {0x3930AA:#X} exceeds file size (end = {end1:#X})")
				end2 = 0x39F400 + len(output[1])
				if end2 > len(rom):
					raise ValueError(f"change at {0x39F400:#X} exceeds file size (end = {end2:#X})")
				rom[0x3930AA:end1] = output[0]
				rom[0x39F400:end2] = output[1]

		if outputToPatch:
			blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
			iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
			with open(f'./src/assembler_output/monster_ai/bps/smrpg-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps', 'wb') as f:
				write_bps(bps_progress(iterable), f)

		self.stdout.write(self.style.SUCCESS("successfully assembled monster ai battle scripts"))
