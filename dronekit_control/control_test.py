from dronekit import connect, VehicleMode
import time

# Connect to the vehicle

print("Connecting to the vehicle...")
print("This may take some time sometimes....")
connection_string = "/dev/ttyAMC0"  # for usb
vehicle = connect(connection_string, wait_ready=True,baud=57600)

def arm_drone():
    """
    Testing arming of drone
    """
    print("Setting mode to GUIDED...")
    vehicle.mode = VehicleMode("GUIDED")

    # Wait for the mode change
    while not vehicle.mode.name == "GUIDED":
        print("Waiting for GUIDED mode...")
        time.sleep(1)

    print("Arming motors...")
    vehicle.armed = True

    # Wait until the drone is armed
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Drone armed successfully!")

# Call the function
arm_drone()

# Keep script running for a few seconds to observe status
time.sleep(5)

# Close vehicle connection
vehicle.close()
print("Connection closed")
