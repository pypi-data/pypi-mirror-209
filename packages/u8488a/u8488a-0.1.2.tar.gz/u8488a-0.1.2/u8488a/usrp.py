from uhd.usrp.cal.visa import VISADevice
from time import sleep


class U8488ADriverUSRP(VISADevice):
    """
    Keysight U8488A VISA Driver for USRP
    """

    def __init__(self, resource):
        self.power_offset = 0
        self.dev = resource
        self.dev.timeout = 25000
        self.dev.write("SYST:PRES DEF")
        self.dev.write("CAL:ZERO:AUTO ONCE")
        sleep(2)
        self.dev.query("*OPC?")
        print("DEVICE SELF CALIBRATED -> STARTING MEASUREMENTS")

    def init_power_meter(self):
        """
        Initialize this device to measure power.
        """
        self.dev.write("INIT:CONT ON")

    def init_signal_generator(self):
        """
        Initialize this device to generate signals.
        """
        raise NotImplementedError()

    def set_frequency(self, freq):
        """
        Set frequency
        """
        print("Frequency is set to {} Hz".format(freq))
        self.dev.write("FREQ {}Hz".format(freq))
        sleep(5.0)
        self.dev.write("INIT:CONT ON")
        self.dev.query("FETC?")

    def get_power_dbm(self):
        """
        Return the received/measured power in dBm (power meter) or return  the
        output power it's currently set to (signal generator).
        """
        # self.dev.write("INIT:CONT ON")
        sleep(0.01)
        return float(self.dev.query("FETC?")) + self.power_offset
