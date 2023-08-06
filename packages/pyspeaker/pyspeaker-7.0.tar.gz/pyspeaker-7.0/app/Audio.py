from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np


class Volume:
    def __init__(self):
        self._devices = AudioUtilities.GetSpeakers()
        self._interface = self._devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self._volume = cast(self._interface, POINTER(IAudioEndpointVolume))

    def get_volume(self):
        """Returns the volume of the device's speakers"""
        vol = self._volume.GetMasterVolumeLevel()
        return vol

    def set_volume(self, VolumeLevel):
        """Sets volume of the device's speakers to the user specified value"""
        self._volume.SetMasterVolumeLevel(VolumeLevel, None)

    def rangify(self, x, from_tuple: tuple, to_tuple: tuple):
        _vol = np.interp(x, from_tuple, to_tuple)
        return _vol
