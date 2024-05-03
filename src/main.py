from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
yolo_model = YOLO("model\\yolov8n.pt")

# Initialize webcam
cap = cv2.VideoCapture(0) # Comment this line to test on video
# cap = cv2.VideoCapture("test\\test_video_1.mp4") # Uncomment this line to test on video
ret = True  # Flag to check if the video is opened successfully
frame_count = 0  # Initialize frame counter
save_dir = "frames"  # Directory to save the cropped face images
os.makedirs(save_dir, exist_ok = True)  # Create the directory if it doesn't already exist

while ret:
    # Read frame from webcam
    ret, frame = cap.read()
    frame_count += 1  # Increment the frame counter

    if ret:
        # Run inference on the source
        results = yolo_model.track(
            frame,
            classes = [0],  # Track only persons (Comment this line to track every objects)
            persist = True  # Enable object tracking for better stability
        )

        if results is not None and results[0] is not None:  # Check if results are not None and if there are any detections
            for i, det in enumerate(results[0].boxes.xyxy):
                # Extract bounding box coordinates
                x1, y1, x2, y2 = map(int, det[:4])
                crop = frame[y1:y2, x1:x2]  # Crop the detected object

                # Save the cropped image with the desired naming convention
                if results[0].boxes.id is not None:
                    crop_name = f"id_{results[0].boxes.id[i]}_frame_{frame_count}.jpg"  # eg. id_5.0_frame_45.jpg
                    crop_path = os.path.join(save_dir, crop_name)
                    cv2.imwrite(crop_path, crop)

            # Draw bounding boxes and labels on the frame
            frame = results[0].plot()

            # Display the processed frame
            cv2.imshow("YOLOv8 - PersonTracker", frame)

            # Check for "q" key press to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            # If there are no frames left to read, release the capture and exit the loop
            print("No faces were detected in the frame")

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

