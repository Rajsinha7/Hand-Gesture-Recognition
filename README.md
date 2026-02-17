# Hand-Gesture-Recognition
The Hand Gesture Recognition System is a real-time computer vision project developed using Python, OpenCV, and MediaPipe Hands.
The system captures webcam video input, detects hand landmarks, and classifies simple finger gestures such as:
- Thumbs Up

- Index Finger Up
- Middle Finger Up
- Ring Finger Up
- Pinky Finger Up

This project serves as a foundation for gesture-controlled interactive applications.
--> Features
- Real-time hand detection using webcam
- Hand landmark detection with MediaPipe Hands
- Gesture classification based on finger positions
- Live visualization of landmarks and gesture labels
- Fast and lightweight processing
--> Tech Stack
Programming Language: Python
Libraries:
OpenCV – video processing & visualization
MediaPipe – hand landmark detection
NumPy – numerical computations

--> Project Structure
Hand-Gesture-Recognition/
│
├── hand_gesture_recognition.py
├── requirements.txt
└── README.md

--> How to Run the Project
1️. Prerequisites
Python 3.x installed
A working webcam
2️. Install Dependencies
pip install opencv-python mediapipe numpy
3️. Clone the Repository
git clone https://github.com/Rajsinha7/Hand-Gesture-Recognition.git
cd Hand-Gesture-Recognition

4️. Run the Application
python hand_gesture_recognition.py

5️. Output
Webcam window opens
Hand landmarks detected in real time
Recognized gesture displayed on screen
Press q to exit the program
--> How It Works
Webcam captures live video frames
MediaPipe Hands detects hand landmarks

Finger positions are analyzed

Gestures are classified based on raised fingers
