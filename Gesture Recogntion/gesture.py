
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands API
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def classify_gesture(hand_landmarks):
    # Get y-coordinates of fingertip landmarks
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    # Find the lowest (highest on screen) finger tip
    fingers = {
        "Thumbs Up": thumb_tip,
        "Index Finger Up": index_tip,
        "Middle Finger Up": middle_tip,
        "Ring Finger Up": ring_tip,
        "Pinky Finger Up": pinky_tip
    }

    # We consider a finger "up" if its tip is significantly above the other fingers
    # Using a threshold difference to avoid noise
    threshold = 0.03  # tweak this value if needed

    # Sort fingers by y-coordinate (lower y means finger is raised)
    sorted_fingers = sorted(fingers.items(), key=lambda x: x[1])

    # Check if the top finger is sufficiently above the second finger
    top_finger, top_y = sorted_fingers[0]
    second_y = sorted_fingers[1][1]

    if (second_y - top_y) > threshold:
        return top_finger
    else:
        return "Unknown"

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hands API
    results = hands.process(image)

    # Draw hand landmarks on the image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Classify the gesture
            gesture = classify_gesture(hand_landmarks)
            cv2.putText(image, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image
    cv2.imshow('Hand Gesture Recognition', image)

    # Exit on ESC key press
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
