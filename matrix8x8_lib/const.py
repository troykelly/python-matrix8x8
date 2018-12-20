"""
@ Author      : Troy Kelly
@ Date        : 23 Sept 2018
@ Description : 8x8 HDMI Matrix Interface
"""

from enum import Enum


class CommandType(Enum):
    """HDMI Command Codes"""
    A_COMMAND = 0
    ANOTHER_COMMAND = 1

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)
