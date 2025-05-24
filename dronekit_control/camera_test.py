import cv2

def list_available_cameras(max_cameras=10):
    available_cameras = []
    
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()  # Release the camera after checking
        else:
            print(f"Camera index {i} is not available.")
    
    return available_cameras

if __name__ == "__main__":
    cameras = list_available_cameras()
    
    if cameras:
        print("Available camera indices:")
        for cam in cameras:
            print(f"Camera index: {cam}")
    else:
        print("No cameras found.")