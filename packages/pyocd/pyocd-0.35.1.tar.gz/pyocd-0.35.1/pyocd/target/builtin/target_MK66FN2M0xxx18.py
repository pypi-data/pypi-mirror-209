# pyOCD debugger
# Copyright (c) 2016,2018 Arm Limited
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..family.target_kinetis import Kinetis
from ..family.flash_kinetis import Flash_Kinetis
from ...core.memory_map import (FlashRegion, RamRegion, MemoryMap)
from ...debug.svd.loader import SVDFile

FLASH_ALGO = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xb510482e, 0x5120f24c, 0xf64d81c1, 0x81c11128, 0xf0218801, 0x80010101, 0x44484829, 0xf856f000,
    0xbf182800, 0xbd102001, 0x47702000, 0xb5104824, 0x44484924, 0xf926f000, 0x4821b920, 0x44482100,
    0xf9daf000, 0x684a4920, 0x0270f442, 0xbd10604a, 0x4c1bb570, 0x444c4605, 0x4b1a4601, 0x68e24620,
    0xf88ef000, 0x2300b928, 0x46204629, 0xf00068e2, 0x4915f91f, 0xf442684a, 0x604a0270, 0xb570bd70,
    0x460b460c, 0x46014606, 0xb084480d, 0x44484615, 0xf8b8f000, 0x2000b958, 0xe9cd2101, 0x90021000,
    0x462b4807, 0x46314622, 0xf0004448, 0x4906f963, 0xf442684a, 0x604a0270, 0xbd70b004, 0x40052000,
    0x00000004, 0x6b65666b, 0x4001f000, 0xbf042800, 0x47702004, 0x6cc94926, 0x0e094a26, 0xf832447a,
    0x03091011, 0x2064bf04, 0x22004770, 0x2100e9c0, 0x60812104, 0x60c10289, 0x780b491f, 0x7c80f44f,
    0xf303fa0c, 0x78c96103, 0x1205e9c0, 0x47704610, 0xbf0e2800, 0x61812004, 0x47702000, 0xbf042800,
    0x47702004, 0x42191e5b, 0x421abf0e, 0x47702065, 0x428b6803, 0x6840d806, 0x44184411, 0xbf244288,
    0x47702000, 0x47702066, 0x4288490c, 0x206bbf14, 0x47702000, 0x290fb140, 0x2a04d802, 0xe005d104,
    0xbf982913, 0xd0012a08, 0x47702004, 0x47702000, 0x40048000, 0x0000036c, 0x40020028, 0x6b65666b,
    0x4df0e92d, 0x46154606, 0x4618460c, 0xffdcf7ff, 0xbf182800, 0x8df0e8bd, 0x462a2310, 0x46304621,
    0xffbcf7ff, 0xbf180007, 0x8df0e8bd, 0x1e451960, 0xfbb568f0, 0xfb00f1f0, 0xb1125211, 0x43481c49,
    0x42ac1e45, 0xf8dfd817, 0x44f88034, 0xb030f8df, 0x0a09f04f, 0x0000f8d8, 0xf88b6004, 0xf000a007,
    0x4607f917, 0x280069b0, 0x4780bf18, 0x68f0b91f, 0x42ac4404, 0x4638d9ee, 0x8df0e8bd, 0x0000027a,
    0x40020000, 0xbf042a00, 0x47702004, 0x4df0e92d, 0x4614461d, 0x4607460e, 0x462a2308, 0xff7ef7ff,
    0x0b00ea5f, 0xe8bdbf18, 0x2d008df0, 0xf8dfbf1e, 0x44f8804c, 0x0a07f04f, 0xf8d8d01c, 0x60060000,
    0x1000f8d8, 0x0b04f854, 0xf8d86048, 0xf8541000, 0x60880b04, 0xf880480a, 0xf000a007, 0x4683f8d9,
    0x280069b8, 0x4780bf18, 0x0f00f1bb, 0x3608d102, 0xd1e23d08, 0xe8bd4658, 0x00008df0, 0x00000212,
    0x40020000, 0x4604b510, 0xf7ff4608, 0x2800ff5d, 0xbd10bf18, 0xbf042c00, 0xbd102004, 0x49032044,
    0xe8bd71c8, 0xf0004010, 0x0000b8b3, 0x40020000, 0x4df0e92d, 0x4614469a, 0x4605460e, 0xf7ff2310,
    0x2800ff2d, 0xe8bdbf18, 0xe9d58df0, 0xfbb00101, 0x4270f8f1, 0x0100f1c8, 0x42474008, 0xbf0842b7,
    0x2c004447, 0xf8dfbf18, 0xd01cb044, 0x42a51bbd, 0x4625bf88, 0x490e0928, 0x68094479, 0x2101600e,
    0x1007f88b, 0xf88b0a01, 0xf88b100b, 0xf88b000a, 0xf000a009, 0x2800f87d, 0xe8bdbf18, 0x1b648df0,
    0x4447442e, 0x2000d1e2, 0x8df0e8bd, 0x40020000, 0x0000014c, 0xbf122800, 0x20042a00, 0x29084770,
    0xe8dfd215, 0x0604f001, 0x0c0a0806, 0x68c0100e, 0x6840e00a, 0x6880e008, 0x6800e006, 0x2001e004,
    0x6900e002, 0x6940e000, 0x20006010, 0x206a4770, 0x00004770, 0xbf042b00, 0x47702004, 0x4df0e92d,
    0xe9dd461c, 0x46158709, 0x2304460e, 0xa020f8dd, 0xfec4f7ff, 0xbf182800, 0x8df0e8bd, 0xbf1a2d00,
    0xb04cf8df, 0xe8bd44fb, 0xf8db8df0, 0x60060000, 0x21024810, 0xf88071c1, 0xf8dba00b, 0x68201000,
    0xf0006088, 0xb150f825, 0x0f00f1b8, 0xf8c8bf18, 0x2f006000, 0x2100bf1c, 0xe8bd6039, 0x1f2d8df0,
    0x0404f104, 0x0604f106, 0xe8bdd1df, 0x00008df0, 0x000000a0, 0x40020000, 0xbf042800, 0x47702004,
    0x48022240, 0x718171c2, 0xb802f000, 0x40020000, 0x2170480c, 0x21807001, 0x78017001, 0x0f80f011,
    0x7800d0fb, 0x0f20f010, 0x2067bf1c, 0xf0104770, 0xbf1c0f10, 0x47702068, 0x0001f010, 0x2069bf18,
    0x00004770, 0x40020000, 0x40020004, 0x00000000, 0x00080000, 0x00100000, 0x00200000, 0x00400000,
    0x00800000, 0x01000000, 0x02000000, 0x00000000,
                                ],
    'pc_init' : 0x20000021,
    'pc_unInit': 0x20000049,
    'pc_program_page': 0x2000009F,
    'pc_erase_sector': 0x20000071,
    'pc_eraseAll' : 0x2000004D,
    'static_base' : 0x20000000 + 0x00000020 + 0x0000046c,
    'begin_stack' : 0x20000000 + 0x00000800,
    'begin_data' : 0x20000000 + 0x00000A00,
    'analyzer_supported' : True,
    'analyzer_address' : 0x1ffff000,  # Analyzer 0x1ffff000..0x1ffff600
    'page_buffers' : [0x20003000, 0x20004000],   # Enable double buffering
    'min_program_length' : 8,
  }

class K66F18(Kinetis):

    MEMORY_MAP = MemoryMap(
        FlashRegion(    start=0,           length=0x200000,     blocksize=0x1000, is_boot_memory=True,
            algo=FLASH_ALGO, flash_class=Flash_Kinetis),
        RamRegion(      start=0x1fff0000,  length=0x40000),
        RamRegion(      start=0x14000000,  length=0x1000)
        )

    def __init__(self, session):
        super(K66F18, self).__init__(session, self.MEMORY_MAP)
        self._svd_location = SVDFile.from_builtin("MK66F18.svd")

