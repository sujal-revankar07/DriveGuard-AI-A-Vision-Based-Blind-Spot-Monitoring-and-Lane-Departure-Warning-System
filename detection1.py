import cv2
from ultralytics import YOLO

# Load YOLOv8 model (use 'yolov8m.pt' for better accuracy)
model = YOLO("yolov8m.pt")

# Function to check if detection box intersects ROI
def is_inside_roi(x1, y1, x2, y2, roi_top_left, roi_bottom_right):
    rx1, ry1 = roi_top_left
    rx2, ry2 = roi_bottom_right
    # Overlap check
    return not (x2 < rx1 or x1 > rx2 or y2 < ry1 or y1 > ry2)

def main(video_path=0):
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        # Define Left, Right, and Front ROIs
        left_roi_top_left = (50, int(h * 0.4))
        left_roi_bottom_right = (int(w * 0.35), int(h * 0.9))

        right_roi_top_left = (int(w * 0.65), int(h * 0.4))
        right_roi_bottom_right = (w - 50, int(h * 0.9))

        front_roi_top_left = (int(w * 0.35), int(h * 0.3))
        front_roi_bottom_right = (int(w * 0.65), int(h * 0.8))

        # Draw ROIs
        cv2.rectangle(frame, left_roi_top_left, left_roi_bottom_right, (0, 255, 0), 2)
        cv2.rectangle(frame, right_roi_top_left, right_roi_bottom_right, (0, 255, 0), 2)
        cv2.rectangle(frame, front_roi_top_left, front_roi_bottom_right, (255, 0, 0), 2)

        # Run YOLO detection with lower confidence threshold
        results = model(frame, conf=0.2)

        for r in results[0].boxes:
            x1, y1, x2, y2 = r.xyxy[0].cpu().numpy().astype(int)
            label = model.names[int(r.cls)]
            conf = float(r.conf[0])

            # Detect only automobiles
            if label in ["car", "truck", "bus", "motorbike", "bicycle"]:
                # Draw detection box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                # Check LEFT ROI
                if is_inside_roi(x1, y1, x2, y2, left_roi_top_left, left_roi_bottom_right):
                    cv2.putText(frame, "⚠ Vehicle on LEFT!", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                    print("Vehicle on LEFT detected!")

                # Check RIGHT ROI
                if is_inside_roi(x1, y1, x2, y2, right_roi_top_left, right_roi_bottom_right):
                    cv2.putText(frame, "⚠ Vehicle on RIGHT!", (w - 350, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                    print("Vehicle on RIGHT detected!")

                # Check FRONT ROI
                if is_inside_roi(x1, y1, x2, y2, front_roi_top_left, front_roi_bottom_right):
                    cv2.putText(frame, "⚠ Vehicle AHEAD!", (int(w/2) - 150, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 3)
                    print("Vehicle in FRONT detected!")

        # ✅ Resize frame before showing (fit into laptop screen)
        frame = cv2.resize(frame, (960, 540))   # you can change width=960, height=540 as needed

        # Show frame
        cv2.imshow("Blind Spot Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Replace 0 with video file path if needed
    main(video_path=r"C:\Users\sujal\OneDrive\Desktop\DriveGuard_AI\video3.mp4")
