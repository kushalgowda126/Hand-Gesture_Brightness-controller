import cv2
import mediapipe as mp
import screen_brightness_control as sbc

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            if index_finger_y < thumb_y:
                hand_gesture = 'pointing up'
            elif index_finger_y > thumb_y:
                hand_gesture = 'pointing down'
            else:
                hand_gesture = 'other'

            # Adjust brightness based on hand gesture
            current_brightness = sbc.get_brightness(display=None)  # Get brightness for all displays

            if hand_gesture == 'pointing up':
                for i, brightness in enumerate(current_brightness):
                    new_brightness = min(brightness + 10, 100)  # Increase brightness, max 100
                    sbc.set_brightness(new_brightness, display=i)
            elif hand_gesture == 'pointing down':
                for i, brightness in enumerate(current_brightness):
                    new_brightness = max(brightness - 10, 0)  # Decrease brightness, min 0
                    sbc.set_brightness(new_brightness, display=i)

    cv2.imshow('Hand Gesture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Check if the window has been closed
    if cv2.getWindowProperty('Hand Gesture', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()