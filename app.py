import cv2
import time

from utills.hand_tracker import HandTracker
from utills.gesture_detector import GestureDetector
from utills.keyboard_controller  import KeyboardController


def main():

    tracker = HandTracker()
    detector = GestureDetector()
    controller = KeyboardController()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Webcam not found.")
        return

    prev_time = time.time()

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        # Detect hand
        frame, landmarks = tracker.find_hands(frame)

        # Predict gesture
        gesture = detector.detect(landmarks)

        # Execute action
        controller.execute(gesture)

        # FPS
        current_time = time.time()
        fps = int(1 / (current_time - prev_time))
        prev_time = current_time

        # Gesture Text
        cv2.putText(
            frame,
            f"Gesture : {gesture}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # FPS Text
        cv2.putText(
            frame,
            f"FPS : {fps}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.imshow("AI Hand Gesture Controller V2", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()