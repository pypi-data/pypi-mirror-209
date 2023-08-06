# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`bmp384`
================================================================================

CircuitPython Driver for the Bosch BMP384 Pressure and Temperature sensor


* Author(s): Jose D. Montoya


"""

from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct, Struct
from adafruit_register.i2c_bits import RWBits, ROBits
from adafruit_register.i2c_bit import RWBit

try:
    from busio import I2C
except ImportError:
    pass

__version__ = "0.1.1"
__repo__ = "https://github.com/jposada202020/CircuitPython_BMP384.git"

_REG_WHOAMI = const(0x00)
_PWR_CTRL = const(0x1B)
_OSR_CONFIG = const(0x1C)
_ODR_CONFIG = const(0x1D)
_CONFIG = const(0x1F)
_REGISTER_CAL_DATA = const(0x31)

SLEEP_MODE = const(0b00)
FORCED_MODE = const(0b10)
NORMAL_MODE = const(0b11)
power_mode_values = (SLEEP_MODE, FORCED_MODE, NORMAL_MODE)

PRESS_DISABLE = const(0x00)
PRESS_ENABLE = const(0x01)
pressure_mode_values = (PRESS_DISABLE, PRESS_ENABLE)

# Filter Coefficients
IIR_FILTER_DISABLE = const(0x00)
IIR_FILTER_X2 = const(0x01)
IIR_FILTER_X4 = const(0x02)
IIR_FILTER_X8 = const(0x03)
IIR_FILTER_X16 = const(0x04)
IIR_FILTER_X32 = const(0x05)
IIR_FILTER_X64 = const(0x06)
IIR_FILTER_X128 = const(0x07)
filter_coefficients_values = (
    IIR_FILTER_DISABLE,
    IIR_FILTER_X2,
    IIR_FILTER_X4,
    IIR_FILTER_X8,
    IIR_FILTER_X16,
    IIR_FILTER_X32,
    IIR_FILTER_X64,
    IIR_FILTER_X128,
)

TEMP_DISABLE = const(0x00)
TEMP_ENABLE = const(0x01)
temperature_mode_values = (TEMP_DISABLE, TEMP_ENABLE)

# Oversample
OVERSAMPLE_DISABLE = const(0x00)
OVERSAMPLE_X2 = const(0x01)
OVERSAMPLE_X4 = const(0x02)
OVERSAMPLE_X8 = const(0x03)
OVERSAMPLE_X16 = const(0x04)
OVERSAMPLE_X32 = const(0x05)
pressure_oversample_values = (
    OVERSAMPLE_DISABLE,
    OVERSAMPLE_X2,
    OVERSAMPLE_X4,
    OVERSAMPLE_X8,
    OVERSAMPLE_X16,
    OVERSAMPLE_X32,
)
temperature_oversample_values = (
    OVERSAMPLE_DISABLE,
    OVERSAMPLE_X2,
    OVERSAMPLE_X4,
    OVERSAMPLE_X8,
    OVERSAMPLE_X16,
    OVERSAMPLE_X32,
)


class BMP384:
    """Driver for the BMP384 Sensor connected over I2C.

    :param ~busio.I2C i2c_bus: The I2C bus the BMP384 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x77`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`BMP384` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        import board
        import bmp384

    Once this is done you can define your `board.I2C` object and define your sensor object

    .. code-block:: python

        i2c = board.I2C()  # uses board.SCL and board.SDA
        bmp = bmp384.BMP384(i2c)

    Now you have access to the attributes

    .. code-block:: python

        press = bmp.pressure
        temp = bmp.temperature

    """

    _device_id = ROUnaryStruct(_REG_WHOAMI, "B")
    _operation_mode = RWBits(2, _PWR_CTRL, 4)
    _pressure_mode = RWBit(_PWR_CTRL, 0)
    _temperature_mode = RWBit(_PWR_CTRL, 1)
    _filter_coefficients = RWBits(3, _CONFIG, 1)
    _pressure_oversample = RWBits(3, _OSR_CONFIG, 0)
    _temperature_oversample = RWBits(3, _OSR_CONFIG, 3)
    _output_data_rate = RWBits(5, _ODR_CONFIG, 0)

    _temperature = ROBits(24, 0x07, 0, 3)
    _pressure = ROBits(24, 0x04, 0, 3)
    _coeffs = Struct(_REGISTER_CAL_DATA, "<HHbhhbbHHbbhbb")

    def __init__(self, i2c_bus: I2C, address: int = 0x77) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)

        if self._device_id != 0x50:
            raise RuntimeError("Failed to find BMP384")

        self._pressure_mode = PRESS_ENABLE
        self._temperature_mode = TEMP_ENABLE
        self._operation_mode = NORMAL_MODE
        self._read_coefficients()

    @property
    def power_mode(self) -> str:
        """
        Sensor power_mode

        +--------------------------------+------------------+
        | Mode                           | Value            |
        +================================+==================+
        | :py:const:`bmp384.SLEEP_MODE`  | :py:const:`0b00` |
        +--------------------------------+------------------+
        | :py:const:`bmp384.FORCED_MODE` | :py:const:`0b10` |
        +--------------------------------+------------------+
        | :py:const:`bmp384.NORMAL_MODE` | :py:const:`0b11` |
        +--------------------------------+------------------+
        """
        values = (
            "SLEEP_MODE",
            "FORCED_MODE",
            "NORMAL_MODE",
        )
        return values[self._operation_mode]

    @power_mode.setter
    def power_mode(self, value: int) -> None:
        if value not in power_mode_values:
            raise ValueError("Value must be a valid power_mode setting")
        self._operation_mode = value

    @property
    def temperature_mode(self) -> str:
        """
        Sensor temperature_mode

        +---------------------------------+------------------+
        | Mode                            | Value            |
        +=================================+==================+
        | :py:const:`bmp384.TEMP_DISABLE` | :py:const:`0x00` |
        +---------------------------------+------------------+
        | :py:const:`bmp384.TEMP_ENABLE`  | :py:const:`0x01` |
        +---------------------------------+------------------+
        """
        values = (
            "TEMP_DISABLE",
            "TEMP_ENABLE",
        )
        return values[self._temperature_mode]

    @temperature_mode.setter
    def temperature_mode(self, value: int) -> None:
        if value not in temperature_mode_values:
            raise ValueError("Value must be a valid temperature_mode setting")
        self._temperature_mode = value

    @property
    def pressure_mode(self) -> str:
        """
        Sensor pressure_mode

        +----------------------------------+------------------+
        | Mode                             | Value            |
        +==================================+==================+
        | :py:const:`bmp384.PRESS_DISABLE` | :py:const:`0x00` |
        +----------------------------------+------------------+
        | :py:const:`bmp384.PRESS_ENABLE`  | :py:const:`0x01` |
        +----------------------------------+------------------+
        """
        values = (
            "PRESS_DISABLE",
            "PRESS_ENABLE",
        )
        return values[self._pressure_mode]

    @pressure_mode.setter
    def pressure_mode(self, value: int) -> None:
        if value not in pressure_mode_values:
            raise ValueError("Value must be a valid pressure_mode setting")
        self._pressure_mode = value

    @property
    def filter_coefficients(self) -> str:
        """
        Sensor filter_coefficients

        +---------------------------------------+------------------+
        | Mode                                  | Value            |
        +=======================================+==================+
        | :py:const:`bmp384.IIR_FILTER_DISABLE` | :py:const:`0x00` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X2`      | :py:const:`0x01` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X4`      | :py:const:`0x02` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X8`      | :py:const:`0x03` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X16`     | :py:const:`0x04` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X32`     | :py:const:`0x05` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X64`     | :py:const:`0x06` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.IIR_FILTER_X128`    | :py:const:`0x07` |
        +---------------------------------------+------------------+
        """
        values = (
            "IIR_FILTER_DISABLE",
            "IIR_FILTER_X2",
            "IIR_FILTER_X4",
            "IIR_FILTER_X8",
            "IIR_FILTER_X16",
            "IIR_FILTER_X32",
            "IIR_FILTER_X64",
            "IIR_FILTER_X128",
        )
        return values[self._filter_coefficients]

    @filter_coefficients.setter
    def filter_coefficients(self, value: int) -> None:
        if value not in filter_coefficients_values:
            raise ValueError("Value must be a valid filter_coefficients setting")
        self._filter_coefficients = value

    @property
    def pressure_oversample(self) -> str:
        """
        Sensor pressure_oversample

        +---------------------------------------+------------------+
        | Mode                                  | Value            |
        +=======================================+==================+
        | :py:const:`bmp384.OVERSAMPLE_DISABLE` | :py:const:`0x00` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X2`      | :py:const:`0x01` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X4`      | :py:const:`0x02` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X8`      | :py:const:`0x03` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X16`     | :py:const:`0x04` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X32`     | :py:const:`0x05` |
        +---------------------------------------+------------------+
        """
        values = (
            "OVERSAMPLE_DISABLE",
            "OVERSAMPLE_X2",
            "OVERSAMPLE_X4",
            "OVERSAMPLE_X8",
            "OVERSAMPLE_X16",
            "OVERSAMPLE_X32",
        )
        return values[self._pressure_oversample]

    @pressure_oversample.setter
    def pressure_oversample(self, value: int) -> None:
        if value not in pressure_oversample_values:
            raise ValueError("Value must be a valid pressure_oversample setting")
        self._pressure_oversample = value

    @property
    def temperature_oversample(self) -> str:
        """
        Sensor temperature_oversample

        +---------------------------------------+------------------+
        | Mode                                  | Value            |
        +=======================================+==================+
        | :py:const:`bmp384.OVERSAMPLE_DISABLE` | :py:const:`0x00` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X2`      | :py:const:`0x01` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X4`      | :py:const:`0x02` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X8`      | :py:const:`0x03` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X16`     | :py:const:`0x04` |
        +---------------------------------------+------------------+
        | :py:const:`bmp384.OVERSAMPLE_X32`     | :py:const:`0x05` |
        +---------------------------------------+------------------+
        """
        values = (
            "OVERSAMPLE_DISABLE",
            "OVERSAMPLE_X2",
            "OVERSAMPLE_X4",
            "OVERSAMPLE_X8",
            "OVERSAMPLE_X16",
            "OVERSAMPLE_X32",
        )
        return values[self._temperature_oversample]

    @temperature_oversample.setter
    def temperature_oversample(self, value: int) -> None:
        if value not in temperature_oversample_values:
            raise ValueError("Value must be a valid temperature_oversample setting")
        self._temperature_oversample = value

    @property
    def output_data_rate(self) -> int:
        """
        Sensor output_data_rate. for a complete list of values please see the datasheet

        """

        return self._output_data_rate

    @output_data_rate.setter
    def output_data_rate(self, value: int) -> None:
        if value not in range(0, 18, 1):
            raise ValueError("Value must be a valid output_data_rate setting")
        self._output_data_rate = value

    @property
    def temperature(self) -> float:
        """
        The temperature sensor in C
        :return: Temperature
        """
        # pylint: disable = invalid-name, too-many-locals
        raw_temp = self._temperature

        T1, T2, T3 = self._temp_calib

        pd1 = raw_temp - T1
        pd2 = pd1 * T2

        temperature = pd2 + (pd1 * pd1) * T3

        return temperature

    @property
    def pressure(self) -> float:
        """
        The sensor pressure in hPa
        :return: Pressure in hPa
        """
        # pylint: disable = invalid-name, too-many-locals
        temperature = self.temperature

        raw_pressure = self._pressure

        P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11 = self._pressure_calib

        pd1 = P6 * temperature
        pd2 = P7 * temperature**2.0
        pd3 = P8 * temperature**3.0
        po1 = P5 + pd1 + pd2 + pd3

        pd1 = P2 * temperature
        pd2 = P3 * temperature**2.0
        pd3 = P4 * temperature**3.0
        po2 = raw_pressure * (P1 + pd1 + pd2 + pd3)

        pd1 = raw_pressure**2.0
        pd2 = P9 + P10 * temperature
        pd3 = pd1 * pd2
        pd4 = pd3 + P11 * raw_pressure**3.0

        pressure = po1 + po2 + pd4

        return pressure / 100

    def _read_coefficients(self) -> None:
        """Read & save the calibration coefficients
        This is from adafruit_bmp3xx library"""
        coeff = self._coeffs

        self._temp_calib = (
            coeff[0] / 2**-8.0,
            coeff[1] / 2**30.0,
            coeff[2] / 2**48.0,
        )
        self._pressure_calib = (
            (coeff[3] - 2**14.0) / 2**20.0,
            (coeff[4] - 2**14.0) / 2**29.0,
            coeff[5] / 2**32.0,
            coeff[6] / 2**37.0,
            coeff[7] / 2**-3.0,
            coeff[8] / 2**6.0,
            coeff[9] / 2**8.0,
            coeff[10] / 2**15.0,
            coeff[11] / 2**48.0,
            coeff[12] / 2**48.0,
            coeff[13] / 2**65.0,
        )
