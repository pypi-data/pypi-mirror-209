from setuptools import find_packages, setup

setup(
    name="u8488a",
    packages=find_packages(),
    version="0.1.1",
    description="Keysight U8488A Powermeter Driver for USRP Power Calibration",
    long_description="This is a simple driver for Keysight U8488A power meter. There are 2 classes in this package. You can use this package individually or for USRP calibration.",
    author="Anıl Gürses",
    author_email="agurses@ncsu.edu",
    url="https://github.com/anilgurses/U8488A_USRP_Calibration.git",
    license="MIT",
    install_requires=[],
    setup_requires=["pyvisa", "pyvisa-py", "pyusb", "pyserial"],
)
