import time
import pythonosc
import pythonosc.udp_client

class VarClass():
    def __init__(self):
        self._client = pythonosc.udp_client.SimpleUDPClient("127.0.0.1", 9000)

class Message(VarClass):
    def __init__(self):
        super().__init__()

    def sendMessage(self, track:dict):
        """Send message using OSC"""
        self._client.send_message("/input/LookHorizontal", track["Nose"][1][0])
        time.sleep(0.1)