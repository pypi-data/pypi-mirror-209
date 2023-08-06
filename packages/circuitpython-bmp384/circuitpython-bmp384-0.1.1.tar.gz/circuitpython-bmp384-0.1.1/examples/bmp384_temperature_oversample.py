# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp384

i2c = board.I2C()
bmp = bmp384.BMP384(i2c)

bmp.temperature_oversample = bmp384.OVERSAMPLE_X2

while True:
    for temperature_oversample in bmp384.temperature_oversample_values:
        print("Current Temperature oversample setting: ", bmp.temperature_oversample)
        for _ in range(10):
            temp = bmp.temperature
            print("temperature:{:.2f}C".format(temp))
            time.sleep(0.5)
        bmp.temperature_oversample = temperature_oversample
