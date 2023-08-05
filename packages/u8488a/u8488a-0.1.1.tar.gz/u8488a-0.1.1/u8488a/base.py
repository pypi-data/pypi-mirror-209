import pyvisa
import traceback
from time import sleep

MAX_FREQ = 67e9  # 67 GHz
MIN_FREQ = 50e6  # 50 MHz


class PowerMeter(object):
    """
    Base class for U8488A power meter
    """

    def __init__(self):
        self.__rm = pyvisa.ResourceManager()
        self.__dev_list = self.__rm.list_resources()
        self.__dev = None
        self._frequency = 1e9  # 1 GHz

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, freq):
        if MIN_FREQ <= freq <= MAX_FREQ:
            self._frequency = freq
            if not self.__dev:
                self.__dev.write("FREQ {}Hz".format(freq))
                sleep(1)
        else:
            raise ValueError(
                f"Frequency is not in range! // {MIN_FREQ} <= Freq  <= {MAX_FREQ}"
            )

    def get_device_list(self):
        self.__dev_list = self.__rm.list_resources()
        return self.__dev_list

    def __dev_init(self, device):
        try:
            self.__dev = self.__rm.open_resource(device)
            print(f"{device} is opened!")
            self.__calibration()
            self.__dev.query("*OPC?")
            sleep(1)
            self.__dev.write("FREQ {}Hz".format(self._frequency))
            sleep(1)
            self.__dev.write("INIT:CONT ON")
            self.__dev.query("FETC?")
        except Exception:
            traceback.print_exc()

    def __calibration(self):
        self.__dev.write("SYST:PRES DEF")
        self.__dev.write("CAL:ZERO:AUTO ONCE")
        sleep(2)
        print("Device is calibrated")

    def open_device(self, device):
        self.__dev_init(device)

    def get_power(self):
        if not self.__dev:
            r = self.get_device_list()

            if len(r) > 0:
                print("Using the first availabe measurement device")
                self.__dev_init(r[0])
            else:
                print(
                    "No measurement device present. Please check your USB connection! Refer to pyVisa manual."
                )
                raise Exception("No measurement device present!")

        return float(self.__dev.query("FETC?"))
