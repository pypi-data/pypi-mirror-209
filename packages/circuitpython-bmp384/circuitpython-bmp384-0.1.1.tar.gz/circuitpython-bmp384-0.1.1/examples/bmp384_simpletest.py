# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp384

i2c = board.I2C()  # uses board.SCL and board.SDA
bmp = bmp384.BMP384(i2c)

while True:
    print("Pressure: {:.2f}hPa".format(bmp.pressure))
    time.sleep(0.5)
