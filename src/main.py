from modules.posemark import PoseDetector as pose
import cv2

class Data():
    def convertLines(result) -> dict:
        #"Left elbow": [0, (0,0,0,0)]
        # "Nose": [0, (0,0,0,0)]
        track:dict = {"Nose": [0, (0,0,0,0)], "Left elbow": [13, (0,0,0,0)]}

        for x in track.items():
            # print() # Example: ('Head', [0, (0, 0, 0, 0)])
            
            point = result.landmark[x[1][0]]

            x[1][1] = ((point.x), (point.y), (point.z), (point.visibility))

            return track

class Main():
    # init class
    detector = pose()

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

        Data.convertLines(pose_landmark)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Main()