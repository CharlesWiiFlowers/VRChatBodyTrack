import cv2

class Utils():

    # How much do you like to move?
    SENSITIVY:int = 15

    def getCameraList():
        """TODO"""

    def normalizer(number):
        """Change an interval of [0,1] to [-1,1]"""
        return (number * 2) - 1

    def getYaw(track:dict) -> int:
        """Get Yaw"""
        
        center = track["Nose"][1][0]
        point2X = track["Left eye"][1][0]
        point5X = track["Right eye"][1][0]

        yaw = ((point2X - center) - (center - point5X)) * Utils.SENSITIVY

        return yaw
    
    def getPitch(track:dict) -> int:
        """Get the Pitch rotation"""

        center = track["Nose"][1][1]
        point7Y = track["Left ear"][1][1]
        point8Y = track["Right ear"][1][1]

        media = (point7Y + point8Y) / 2
        pitch = (media - center) * Utils.SENSITIVY

        return pitch

    def getSlope(track:dict) -> int:
        """Get the slope rotation"""

        point2X = track["Left eye"][1][0]
        point5X = track["Right eye"][1][0]
        point2Y = track["Left eye"][1][1]
        point5Y = track["Right eye"][1][1]

        slope = (point5Y - point2Y) / (point5X - point2X) * (Utils.SENSITIVY / 10)

        print(slope)
        return slope