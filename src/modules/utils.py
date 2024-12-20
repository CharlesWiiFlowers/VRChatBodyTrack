
class Utils():

    # How much do you like to move?
    SENSITIVY:int = 15
    PI:float = 3.141592653589793

    def getEulerRotation(track:dict):
        """Get the rotation on euler angles"""

        yaw = Utils.getYaw(track) * 90 #* 180 / Utils.PI
        pitch = Utils.getPitch(track) * 90 #* 180 / Utils.PI
        slope = Utils.getSlope(track) * 90 #* 180 / Utils.PI

        return [slope, pitch, yaw]

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

        # This means: m = (Y2 - Y1) / (X2 - X1) -> when 'm' is the slope
        slope = (point5Y - point2Y) / (point5X - point2X) * (Utils.SENSITIVY / 10)

        if slope > 1: slope = 1
        elif slope < -1: slope = -1

        print(slope)
        return slope

