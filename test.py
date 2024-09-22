import cv2
from ultralytics import YOLO

model = YOLO("E:\Colab Notebooks\Best.pt")

video_source = "0"  # Default webcam source


cap = cv2.VideoCapture(int(video_source) if video_source.isdigit() else video_source)

if not cap.isOpened():
    print("Error: Unable to open video source")
    exit()
class_names = {0: "crop", 1: "weed"}

while True:
    # Read a frame from the video source
    ret, frame = cap.read()


    if not ret:
        break


    results = model.predict(frame)


    for result in results:
        # Check if there are detections
        if result.boxes is not None:
     
            for box, label in zip(result.boxes.xyxy, result.names):
                x1, y1, x2, y2 = map(int, box)
                label_name = class_names[int(label)]  # Map numerical label to class name
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw bounding box
                cv2.putText(frame, label_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Write label

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video source
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()





