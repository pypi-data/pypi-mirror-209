# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp384

i2c = board.I2C()
bmp = bmp384.BMP384(i2c)

bmp.pressure_oversample = bmp384.OVERSAMPLE_X4

while True:
    for pressure_oversample in bmp384.pressure_oversample_values:
        print("Current Pressure oversample setting: ", bmp.pressure_oversample)
        for _ in range(10):
            press = bmp.pressure
            print("pressure:{:.2f}hPa".format(press))
            time.sleep(0.5)
        bmp.pressure_oversample = pressure_oversample
