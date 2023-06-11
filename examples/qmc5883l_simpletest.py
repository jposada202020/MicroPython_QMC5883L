# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_qmc5883l import qmc5883l

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
qmc = qmc5883l.QMC5883L(i2c)

while True:
    mag_x, mag_y, mag_z = qmc.magnetic
    print("x:{:.2f}Gs, y:{:.2f}Gs, z{:.2f}Gs".format(mag_x, mag_y, mag_z))
    time.sleep(0.3)
