# Unofficial driver for Keysight U8488A 

This is a simple driver for Keysight U8488A power meter. There are 2 classes in this package. You can use this package individually or for USRP calibration.

## Install 

```
$ pip install u8488a
```

## Example Usage 

```
from u8488a import base
from time import sleep

dev = base.PowerMeter()
# List available devices
devs = dev.get_device_list()

if len(devs) > 0:
    dev.open_device(devs(0))
else:
    print("No device found!")
    exit(1)

print("Available devices:")
print(devs)

# Setting frequency to 20 GHz
dev.frequency(20e9)

while True:
    # Read power level every second
    print(f"Power: {dev.get_power()} dBm")
    sleep(1)

```

## USRP TX Power Reference Level Calibration

This package includes "custom" driver for USRP calibration. `uhd_power_cal.py` scripts is installed with UHD installation by default. It's located under ```/usr/local/lib64/uhd/utils``.

Note: If you can't find uhd folder, it's probably under this directory ```/usr/local/lib/```

```
$ cd /usr/local/lib64/uhd/utils/
$ uhd_power_cal.py -d tx --meas-dev visa -o import=u8488a
```

Note: This can only be used for TX power calibration

