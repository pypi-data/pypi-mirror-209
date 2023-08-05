from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="u8488a",
    packages=find_packages(),
    version="0.1.2",
    description="Keysight U8488A Powermeter Driver for USRP Power Calibration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anıl Gürses",
    author_email="agurses@ncsu.edu",
    url="https://github.com/anilgurses/U8488A_USRP_Calibration.git",
    license="MIT",
    install_requires=[],
    setup_requires=["pyvisa", "pyvisa-py", "pyusb", "pyserial"],
)
