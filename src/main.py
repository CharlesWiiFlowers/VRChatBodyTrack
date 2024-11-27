from modules.posemark import PoseDetector as pose
from modules.osc_connection import Message as msg
import cv2

class Data():
    def convertLines(result) -> dict:
        
        # "Nose": [0, (0,0,0,0)]
        track:dict = {"Nose": [0, (0,0,0,0)],
                      "Left elbow": [13, (0,0,0,0)]}

        for key, values in track.items():
            # print() # Example: ('Head', [0, (0, 0, 0, 0)])
            point = result.landmark[values[0]]

            values[1] = ((point.x), (point.y), (point.z), (point.visibility))
            
        return track

class Main():
    # init class
    detector = pose()
    msg = msg()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened:
        print("Camera is don't available")
        exit(2)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error ocurred when tried to read the camera's frame")
            break

        processed_frame, pose_landmark = detector.detectPose(frame=frame)

        cv2.imshow('Pose', processed_frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

        msg.sendMessage(Data.convertLines(pose_landmark))

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Main()