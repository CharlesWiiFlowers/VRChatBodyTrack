import cv2

class Utils():
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

        yaw = ((point2X - center) - (center - point5X)) * 15

        return yaw