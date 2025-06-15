import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Open the webcam.
cap = cv2.VideoCapture(1)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # Convert the image to RGB for processing.
    image.flags.writeable = False
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Convert back to BGR.
    image.flags.writeable = True
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    image_height, image_width, _ = image.shape

    if results.multi_hand_landmarks and results.multi_handedness:
      for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
        # Draw hand landmarks and connections.
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        # Get the handedness label.
        label = handedness.classification[0].label
        # Swap the label for display since we flip the image.
        if label == "Left":
            display_label = "Right"
        elif label == "Right":
            display_label = "Left"
        else:
            display_label = label
        display_label = label

        # Use the wrist landmark as the position for the label.
        wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
        x = int(wrist.x * image_width)
        y = int(wrist.y * image_height)
        # Adjust x coordinate for the flipped (mirrored) view.
        flipped_x = image_width - x
        
        # Draw the label on the image.
        cv2.putText(image, display_label, (flipped_x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Flip the image for selfie-view display.
    flipped_image = cv2.flip(image, 1)
    cv2.imshow('MediaPipe Hands', flipped_image)
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()
cv2.destroyAllWindows()
