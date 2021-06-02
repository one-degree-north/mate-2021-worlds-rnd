# packets.py
# a helper file containing all the packets used by mcu.py.


import time


AXES = ("X", "Y", "Z")


# ReturnPacket is never publicly accessible in mcu.py
class ReturnPacket:
    def __init__(self, packet_data):
        self.timestamp = time.time()
        self.og_cmd = packet_data[0]
        self.og_param = packet_data[1]
        self.cmd = packet_data[2]
        self.param = packet_data[3]
        self.data = packet_data[4:8]

    def __str__(self):
        return f"[{self.timestamp}] og_cmd={self.og_cmd}, og_param={self.og_param}, cmd=" \
               f"{self.cmd}, param={self.param}, data: {self.data}"


class TestPacket:
    """
    TestPacket - Class for representing returned packets with cmd 0x00

    Attributes:
        timestamp: float - unix time representation of when the packet was received.
        valid: bool - whether the test packet is valid.
        version: int - the version number returned.
        contents: str - the contents of the packet.
    """
    def __init__(self, valid: bool, version: int, contents: str, timestamp: float):
        self.timestamp = timestamp
        self.valid = valid
        self.version = version
        self.contents = contents

    def __str__(self):
        is_valid = "Valid" if self.valid else "Invalid"
        return f"[{self.timestamp}] {is_valid} TestPacket: version={self.version}, contents='{self.contents}'"


class OKPacket:
    """
    OKPacket - Class for representing returned packets with cmd 0x0A

    Attributes:
        timestamp: float - unix time representation of when the packet was received.
        original_command: int - value of original command
        original_param: int - value of original parameter
        success: boolean - whether the original command succeeded.
    """
    def __init__(self, og_cmd: int, og_param: int, success: bool, timestamp: float):
        self.timestamp = timestamp
        self.original_command = og_cmd
        self.original_param = og_param
        self.success = success

    def __str__(self):
        is_success = "OK" if self.success else "Fail"
        return f"[{self.timestamp}] {is_success} from cmd {self.original_command} with param {self.original_param}"


class AccelPacket:
    """
    AccelPacket - Class for representing returned packets with cmd 0x3A.
    Represents a single direction of acceleration.

    Attributes:
        timestamp: float - unix time representation of when the packet was received.
        axis: int - axis of the measurement. 0=X, 1=Y, 2=Z
        value: float - value of the measurement.
    """
    def __init__(self, axis: int, value: float, timestamp: float):
        self.timestamp = timestamp
        self.axis = axis
        self.value = value

    def __str__(self):
        return f"[{self.timestamp}] Accelerometer {AXES[self.axis]}: {self.value}"


class GyroPacket:
    """
    GyroPacket - Class for representing returned packets with cmd 0x3C.
    Represents a single direction of angular velocity.

    Attributes:
        timestamp: float - unix time representation of when the packet was received.
        axis: int - axis of the measurement. 0=X, 1=Y, 2=Z
        value: float - value of the measurement.
    """
    def __init__(self, axis: int, value: float, timestamp: float):
        self.timestamp = timestamp
        self.axis = axis
        self.value = value

    def __str__(self):
        return f"[{self.timestamp}] Gyroscope {AXES[self.axis]}: {self.value}"


class VoltageTemperaturePacket:
    """
    GyroPacket - Class for representing returned packets with cmd 0x3C.

    Attributes:
        timestamp: float - unix time representation of when the packet was received.
        voltage: float - measured voltage.
        temperature: float - measured temperature.
    """
    def __init__(self, voltage: float, temperature: float, timestamp: float):
        self.timestamp = timestamp
        self.voltage = voltage
        self.temperature = temperature

    def __str__(self):
        return f"[{self.timestamp}] Voltage: {self.voltage}, Temperature: {self.temperature}"