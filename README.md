# Game Control with Hand Gestures

This project provides a system to control a car in a game using hand gestures. It utilizes a webcam to track hand movements, processes the data using Mediapipe, and sends keyboard inputs to the game based on the detected hand position.

---

## Features

- **Real-time Hand Tracking**: Uses Mediapipe's hand tracking module to detect and process hand landmarks.
- **Keyboard Input Control**: Sends 'A' or 'D' key presses to steer the car left or right.
- **Customizable**: Adjustable parameters for screen resolution, detection sensitivity, and collision detection area.

---

## How It Works

1. **Hand Tracking**: The program captures the video feed from the webcam and uses Mediapipe to detect the hand landmarks.
2. **Collision Detection**: Checks if the hand is within a defined area on the screen to determine the direction of the movement (left or right).
3. **Keyboard Simulation**: Based on the hand's position, simulates the pressing of 'A' or 'D' keys to control the car in the game.
4. **Visualization**: Displays two views:
   - The original feed with hand landmarks drawn.
   - A visualization of the collision area and detected hand position.

---

## Requirements

- Python 3.7+
- Required Libraries:
  - OpenCV
  - Mediapipe
  - Pynput

To install the dependencies, run:

```bash
pip install opencv-python mediapipe pynput
```



## Code Structure
- Hand Detection:
    Uses Mediapipe's Hands module to track hand landmarks.
    Calculates the center position of the detected hand.
- Collision Detection:
    Checks if the hand's center is within a defined area to determine left or right movement.
    Keyboard Control:
    Simulates 'A' or 'D' key presses based on the detected collision direction using the Pynput library.


## Usage

1. **Setup**: Ensure your webcam is connected and operational.
2. **Run the Script**: Execute the following command in your terminal:
   
3. if you not have **mediapipe** and **opencv**  , **pynput** you may run: 
```bash 
pip install -r requirements.txt 
```
- then: 

```bash
   python handgame.py
```


## Parameters to Customize

- **Resolution**:  
  Adjust the webcam resolution to balance between performance and accuracy:  
  ```python
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


-Steering Area:
Define the size and position of the area that triggers left or right steering:

thickness: Width of the steering detection area.
position: Horizontal placement of the steering area (0.5 = center).

```bash
    thickness = 210
    position = 0.5
```


- Typing Delay:
Set the delay between key presses to prevent repeated inputs:

```bash
    typing_delay = 0.1
```
- Detection Confidence:
Adjust the minimum detection and tracking confidence for hand landmarks:

```bash
    hands = mp_hand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

```

