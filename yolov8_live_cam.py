import cv2
from ultralytics import YOLO
import time

# Load the YOLO model
weights_path = 'C:\\Users\\공용PC\\PycharmProjects\\clothes_classification_real\\runs\\detect\\train30\\weights\\best.pt'
model = YOLO(weights_path)

# Set the confidence threshold (e.g., 0.3)
confidence_threshold = 0.3
model.conf = confidence_threshold  # Update the model's confidence threshold

# Function to draw detections on each frame
def draw_detections(img, detections, class_names):
    for det in detections:
        left, top, right, bottom = map(int, det[:4])
        conf, class_id = det[4], int(det[5])
        label = f"{class_names[class_id]} {conf:.2f}"

        # Configuration for the label text
        font_scale = 1  # Adjust font scale for label text
        thickness = 2  # Adjust thickness for label text
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Calculate text size to adjust the background rectangle size
        text_size = cv2.getTextSize(label, font, font_scale, thickness)[0]
        text_width, text_height = text_size[0], text_size[1]

        # Draw the bounding box
        box_color = (0, 255, 0)  # Green color for bounding box
        cv2.rectangle(img, (left, top), (right, bottom), box_color, 2)

        # Define top left corner for the label text (inside the bounding box)
        label_top_left = (left, top + text_height + 4)  # Adjusted to draw inside the box

        # Draw background for text for better readability
        cv2.rectangle(img, (left, top), (left + text_width, label_top_left[1]), box_color, -1)

        # Draw label text
        text_color = (255, 255, 255)  # White color for text
        cv2.putText(img, label, (left, label_top_left[1]), font, font_scale, text_color, thickness)



# Open a video capture device
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:

        #rotate camera
        frame = cv2.rotate(frame, cv2.ROTATE_180)

        start = time.perf_counter()
        # Perform inference
        results = model.predict(frame)
        result = results[0]

        # Check for detections and annotate the frame
        if len(result.boxes) > 0:
            detections = [[*box.xyxy[0], box.conf[0], box.cls[0]] for box in result.boxes]
            draw_detections(frame, detections, model.names)

        end = time.perf_counter()
        fps = 1 / (end - start)

        # Display FPS on the frame
        # cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Show the annotated frame
        cv2.imshow("YOLOv8 Inference", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()