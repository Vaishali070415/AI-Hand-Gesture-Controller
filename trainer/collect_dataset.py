
'''import cv2
import mediapipe as mp
import csv
import os
import time

# ==========================
# Create Dataset Folder
# ==========================

os.makedirs("Dataset", exist_ok=True)

csv_path = "Dataset/gestures.csv"

# ==========================
# Create CSV Header
# ==========================

if not os.path.exists(csv_path):

    with open(csv_path, "w", newline="") as file:

        writer = csv.writer(file)

        header = []

        for i in range(21):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])

        header.append("label")

        writer.writerow(header)

# ==========================
# MediaPipe
# ==========================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ==========================
# Webcam
# ==========================

cap = cv2.VideoCapture(0)

label = "jump"
sample_count = 0

# Auto Capture Settings
auto_capture = True
capture_delay = 0.15
last_capture = time.time()

print("\nControls")
print("-------------------------")
print("J = Jump")
print("S = Slide")
print("R = Run")
print("F = Stop")
print("Q = Quit")
print("Auto Capture = ON\n")

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    row = []

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        for lm in hand.landmark:
            row.extend([lm.x, lm.y, lm.z])

        # ==========================
        # AUTO SAVE
        # ==========================

        if auto_capture and len(row) == 63:

            if time.time() - last_capture > capture_delay:

                with open(csv_path, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(row + [label])

                sample_count += 1
                last_capture = time.time()

                print(f"Saved {sample_count} -> {label}")

    # ==========================
    # Display
    # ==========================

    cv2.putText(
        frame,
        f"Label : {label}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Samples : {sample_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        "Auto : ON",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("Dataset Collector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("j"):
        label = "jump"

    elif key == ord("s"):
        label = "slide"

    elif key == ord("r"):
        label = "run"

    elif key == ord("f"):
        label = "stop"

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
'''

import cv2
import mediapipe as mp
import csv
import os
import time

# ==========================
# Create Dataset Folder
# ==========================

os.makedirs("Dataset", exist_ok=True)

csv_path = "Dataset/gestures.csv"


# ==========================
# Create CSV Header
# ==========================

if not os.path.exists(csv_path):

    with open(csv_path, "w", newline="") as file:

        writer = csv.writer(file)

        header = []

        for i in range(21):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])

        header.append("label")

        writer.writerow(header)

# ==========================
# MediaPipe
# ==========================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ==========================
# Webcam
# ==========================

cap = cv2.VideoCapture(0)

# Default Label
label = "accelerate"

sample_count = 0

# Auto Capture
auto_capture = True
capture_delay = 0.15
last_capture = time.time()

print("\n==============================")
print(" AI Gesture Dataset Collector ")
print("==============================")
print("A = Accelerate (One Finger)")
print("B = Brake (Victory)")
print("Q = Quit")
print("==============================\n")

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    row = []

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        for lm in hand.landmark:

            row.extend([
                lm.x,
                lm.y,
                lm.z
            ])

        # Save Automatically

        if auto_capture and len(row) == 63:

            if time.time() - last_capture > capture_delay:

                with open(csv_path, "a", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerow(row + [label])

                sample_count += 1

                last_capture = time.time()

                print(f"Saved {sample_count} -> {label}")

    # ==========================
    # Display
    # ==========================

    cv2.putText(
        frame,
        f"Label : {label}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Samples : {sample_count}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.putText(
        frame,
        "A = Accelerate",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "B = Brake",
        (20,165),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        "Q = Quit",
        (20,200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,0,255),
        2
    )

    cv2.imshow("Dataset Collector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("a"):

        label = "accelerate"

        print("\nCollecting ACCELERATE samples...\n")

    elif key == ord("b"):

        label = "brake"

        print("\nCollecting BRAKE samples...\n")

    elif key == ord("q"):

        break

cap.release()
cv2.destroyAllWindows()