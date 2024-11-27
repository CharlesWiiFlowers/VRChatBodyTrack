from modules.posemark import PoseDetector as pose
import cv2

class main():
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

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()