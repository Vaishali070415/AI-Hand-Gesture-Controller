import joblib
import numpy as np
from collections import deque, Counter


class GestureDetector:

    def __init__(self):

        # Load trained model
        self.model = joblib.load("models/gesture_model.pkl")

        # Store last 5 predictions
        self.history = deque(maxlen=5)

    def detect(self, landmarks):

        # No hand detected
        if landmarks is None:
            return "NO HAND"

        # Invalid landmark data
        if len(landmarks) != 63:
            return "UNKNOWN"

        # Convert landmarks to NumPy array
        data = np.array(landmarks).reshape(1, -1)

        # Predict gesture
        prediction = self.model.predict(data)[0].upper()

        # Save prediction history
        self.history.append(prediction)

        # Majority voting
        stable_prediction = Counter(self.history).most_common(1)[0][0]

        return stable_prediction 
