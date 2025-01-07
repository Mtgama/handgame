import cv2
import mediapipe as mp
from pynput.keyboard import Controller
import time



mp_hand = mp.solutions.hands
hands = mp_hand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

#drease resolotion for increase performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#red line
thickness = 210
position = 0.5 #0.5=center

last_key_press_time = time.time()

typing_delay = 0.1
keyboard = Controller()

def calculate_hand_center(hand_landmarks, width, height):
    x_coords = [int(lm.x * width) for lm in hand_landmarks.landmark]
    y_coords = [int(lm.y * height) for lm in hand_landmarks.landmark]
    center_x = sum(x_coords) // len(x_coords)
    center_y = sum(y_coords) // len(y_coords)
    return center_x, center_y

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    height, width, _ = frame.shape
    middle_x = int(width * position)
    
    collision = frame.copy()
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    
    left_collision = False
    right_collision = False
    
      
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

           
            center_x, center_y = calculate_hand_center(hand_landmarks,width,height)
            cv2.circle(frame,(center_x, center_y),10,(0,255,0),-1)

            
            if middle_x - thickness // 2 <= center_x <= middle_x + thickness // 2:
                cv2.circle(collision, (center_x, center_y),20,(0,0,255),-1)
                if center_x < middle_x:  
                    left_collision = True
                elif center_x > middle_x:  
                    right_collision = True

    
    current_time = time.time()
    if left_collision and current_time - last_key_press_time > typing_delay:
        keyboard.press('a')
        time.sleep(typing_delay)
        keyboard.release('a')
        last_key_press_time = current_time
    elif right_collision and current_time - last_key_press_time > typing_delay:
        keyboard.press('d')
        time.sleep(typing_delay)
        keyboard.release('d')
        last_key_press_time = current_time
    
    cv2.rectangle(collision, (middle_x - thickness // 2,0),
                  (middle_x + thickness // 2, height),(0,0,255),2)

    cv2.imshow("Car Steering Control",frame)
    cv2.imshow("View",collision)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
