import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam & hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)  # List of 5 elements [thumb, index, middle, ring, pinky]
        finger_count = fingers.count(1)

        cv2.putText(img, f'Fingers: {finger_count}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

