# Hand Gesture-Based Screen Brightness Control

This project uses a webcam to capture hand gestures and adjusts the screen brightness based on the detected gestures. It utilizes OpenCV, MediaPipe, and the Screen Brightness Control (SBC) library to achieve this functionality.

## Features
- Detects hand gestures using the webcam.
- Recognizes two main gestures:
  - **Pointing Up**: Increases screen brightness.
  - **Pointing Down**: Decreases screen brightness.
- Automatically adjusts the screen brightness across all displays.
- Runs in real-time and stops when the user presses the `q` key or closes the display window.

## Prerequisites
Before running the code, ensure you have the following installed:

1. **Python** (version 3.7 or higher recommended)
2. Required Python libraries:
   - OpenCV
   - MediaPipe
   - Screen Brightness Control


## How It Works
1. **Hand Detection**: MediaPipe detects hand landmarks using the webcam feed.
2. **Gesture Recognition**: The program compares the y-coordinates of the index finger tip and thumb tip to determine the gesture.
   - If the index finger is above the thumb, the gesture is classified as "pointing up."
   - If the index finger is below the thumb, the gesture is classified as "pointing down."
3. **Brightness Adjustment**:
   - If the gesture is "pointing up," brightness is increased by 10%, up to a maximum of 100%.
   - If the gesture is "pointing down," brightness is decreased by 10%, down to a minimum of 0%.
4. **Real-Time Processing**: The program updates the brightness dynamically as gestures are detected.


## License
This project is licensed under the MIT License.

---

## CONTACT
Kushal Gowda G
kushalgowda126@gmail.com


