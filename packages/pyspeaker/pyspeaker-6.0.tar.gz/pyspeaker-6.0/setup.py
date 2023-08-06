from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
    name = "pyspeaker",
    author = "Akshat Sabharwal",
    version = "6.0",
    package_dir={"": "app"},
    package=find_packages(where = "app"),
    author_email = "akshatsabharwal35@gmail.com",
    description = """A module for controlling the Speakers of the device
    \bMethods\b

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
