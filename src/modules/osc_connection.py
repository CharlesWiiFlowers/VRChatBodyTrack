import time
import pythonosc
import pythonosc.udp_client
from modules.utils import Utils

class VarClass():
    def __init__(self):
        self._client = pythonosc.udp_client.SimpleUDPClient("127.0.0.1", 9000)

class Message(VarClass):
    def __init__(self):
        super().__init__()

    def sendMessage(self, track:dict):
        """Send message using OSC"""
        # track["Nose"][1][0]
        self._client.send_message("/input/LookHorizontal", Utils.getYaw(track))
        time.sleep(0.1)