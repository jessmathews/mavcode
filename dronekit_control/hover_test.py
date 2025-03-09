from dronekit import connect, VehicleMode
import time

# Connect to the vehicle

print("Connecting to the vehicle...")
print("This may take some time sometimes....")
connection_string = "/dev/ttyAMC0"  # for usb
vehicle = connect(connection_string, wait_ready=True,baud=57600)

targAlt = int(input("Enter your target altitude(in m):"))
def arm_and_takeoff(targetAltitude):
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
        
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(targetAltitude)  # Take off to target altitude

    # Check that vehicle has reached takeoff altitude
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95: 
            print("Reached target altitude")
            break
        time.sleep(1)

# takeoff to 5 meters
arm_and_takeoff(5)

print("Take off complete")

# Hover for 10 seconds
time.sleep(15)

print("Starting Landing...")
vehicle.mode = VehicleMode("LAND")

# Close vehicle object
vehicle.close()