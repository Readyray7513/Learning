import cv2

cap = cv2.VideoCapture(0)  # Initialize webcam

while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        print("Failed to grab frame")
        break
        
    cv2.imshow('Webcam', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()