import cv2
import numpy as np
import mediapipe as mp
from keras.models import model_from_json
import pyttsx3
import os
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Loading our Bhasha Model into Program
json_file = open("Bhasha.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("Bhasha.h5")

# Function to preprocess the frame
def preprocess_frame(frame):
    crop_frame = frame[40:400, 0:300]
    frame = cv2.rectangle(frame, (0, 40), (300, 400), (0, 255, 0), 2)
    return crop_frame, frame

# Function to extract keypoints from our frames
def extract_keypoints(results):
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            rh = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten() if hand_landmarks else np.zeros(21*3)
            return np.concatenate([rh])
    return np.zeros(21*3)

## Todo These is For our Speech
# Function to speak the detected alphabet
def speak_alphabet(alphabet):
    engine = pyttsx3.init()
    engine.say(f"Word {alphabet} is detected.")
    engine.runAndWait()

# Function to check accuracy
def check_accuracy(predictions, threshold=0.7):
    if len(predictions) > 0:
        confidence = np.max(predictions)
        if confidence > threshold:
            return True, confidence
    return False, 0


DATA_PATH = os.path.join('MP_Data')

actions = np.array(['A', 'B', 'C'])

no_sequences = 30
sequence_length = 30
threshold = 0.5
prediction_window = 10

sequence = []
predictions = []
last_detection_time = 0
detection_interval = 2

cap = cv2.VideoCapture(0)

# Initialize detected_alphabet outside the loop
detected_alphabet = ""

with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=1,
        min_tracking_confidence=1) as hands:

    while cap.isOpened():
        ret, frame = cap.read()

        crop_frame, frame = preprocess_frame(frame)

        # Process the frames with using MediaPipe
        results = hands.process(cv2.cvtColor(crop_frame, cv2.COLOR_BGR2RGB))

        # Extracting keypoints
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-sequence_length:]

        try:
            if len(sequence) == sequence_length:
                # Converting our sequence to numpy array
                input_sequence = np.array([sequence])

                # Predicting using Keras model
                res = model.predict(input_sequence)[0]

                # For more accuracy Storing responses
                predictions.append(res)

                # For checking our code better accuracy
                if len(predictions) >= prediction_window:
                    # Algorithm
                    final_prediction = int(np.argmax(np.bincount(np.argmax(predictions[-prediction_window:], axis=1))))


                    accurate, confidence = check_accuracy(predictions[-prediction_window:])


                    if accurate and time.time() - last_detection_time > detection_interval:
                        detected_alphabet = actions[final_prediction]
                        print(f"{detected_alphabet} - Confidence: {confidence}")
                        speak_alphabet(detected_alphabet)
                        last_detection_time = time.time()

        except Exception as e:
            pass

        # Printing our hand-landmarks in realtime
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                print("Hand Landmarks:", hand_landmarks)

        cv2.putText(frame, "Alphabet: " + detected_alphabet, (3, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('OpenCV Feed', frame)

        if cv2.waitKey(10) & 0xFF == ord('Q'):
            break

cap.release()
cv2.destroyAllWindows()

