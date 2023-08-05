from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np


class Volume:
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

    def get_volume(self):
        vol = self.volume.GetMasterVolumeLevel()
        return vol

    def set_volume(self, VolumeLevel):
        self.volume.SetMasterVolumeLevel(VolumeLevel, None)

    def rangify(self, x, from_tuple: tuple, to_tuple: tuple):
        vol = np.interp(x, from_tuple, to_tuple)
        return vol
