import torch
import cv2
import numpy as np
import time
import os
from picamera2 import Picamera2
from pyzbar.pyzbar import decode

# Load YOLOv5 model from local directory
#model = torch.hub.load("yolov5", "custom", path="best.pt", source="local")  
#model.eval()

# Create output directory
output_dir = 'detected_images'
os.makedirs(output_dir, exist_ok=True)

# Initialize the camera
picam2 = Picamera2()

config = picam2.create_preview_configuration()
config['controls']['FrameRate'] = 10

picam2.configure(config)
picam2.start()
time.sleep(2)  # Allow camera to initialize

refresh_rate = float(1/15)  # Adjustable refresh rate

try:
    while True:
        # Capture frame
        frame = picam2.capture_array()
        image_path = "streamer/static/output.jpg"
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        cv2.imwrite(image_path, frame)

        frame = cv2.resize(frame, (640, 640))  # Resize for YOLO model

        # Run inference directly using the model
        """
        results = model(frame)

        # Extract detections (xyxy format: x_min, y_min, x_max, y_max, confidence, class)
        detections = results.pandas().xyxy[0]  # Convert results to pandas DataFrame
        i=1
        for _, row in detections.iterrows():
            conf = row['confidence']
            if conf > 0.9:  # Confidence threshold
                detected_img_name = f"{output_dir}/image_{i}.jpg"
                cv2.imwrite(detected_img_name, frame)
                print(f"Image saved: {detected_img_name}")
                qr_codes = decode(frame)
                for qr in qr_codes:
                    qr_data= qr.data.decode('utf-8')
                    print(qr_data)
                i+=1
        """
        qr_codes = decode(frame)
        for qr in qr_codes:
            qr_data = qr.data.decode('utf-8')
            print(qr_data)
            time.sleep(10)
        time.sleep(refresh_rate)

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    picam2.stop()
