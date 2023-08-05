from setuptools import find_packages, setup

setup(
name = "PySpeaker",
author = "Akshat Sabharwal",
version = "1.1",
packages=find_packages(),
py_modules=['pyspeaker'],
author_email = "akshatsabharwal35@gmail.com",
description = """A module for controlling the Speakers of the device
Methods

get_volume: Returns the current volume of the device's speakers
set_volume: Sets the volume of the device's speakers to the given volume level.
rangify: Interpolates or maps the given volume range of the speakers to the user-specified range.""",
install_requires = [
    'pycaw',
    'ctypes-callable',
    'comtypes',
    'numpy'
]
)
