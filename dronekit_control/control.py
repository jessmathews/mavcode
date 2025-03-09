from dronekit import connect, VehicleMode
import time

# Connect to the vehicle
connection_string = "127.0.0.1:14550"  # Change this based on your setup
vehicle = connect(connection_string, wait_ready=True)

def arm_drone():
    """
    Arms the drone without taking off.
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
