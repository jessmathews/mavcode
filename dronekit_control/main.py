from dronekit import connect, VehicleMode, LocationGlobalRelative
from time import sleep

# Connect to the vehicle

print("Connecting to the vehicle...")
print("This may take some time sometimes....")
connection_string = "/dev/ttyACM0"  # for usb
vehicle = connect(connection_string, wait_ready=True,baud=57600)

def arm_and_takeoff(target_altitude):
    """
    Arms the drone and takes off to the specified altitude.
    """
    
    print("Basic pre-arm checks")
    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        sleep(1)

    print("Taking off...")
    vehicle.simple_takeoff(target_altitude)
    while True:
        print(f"Altitude: {vehicle.location.global_relative_frame.alt}")
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Target altitude reached!")
            break
        sleep(1)

def navigate_to_gps(target_lat, target_lon, target_alt):
    """
    Navigates the drone to a specific GPS coordinate.
    """
    print(f"Navigating to {target_lat}, {target_lon} at {target_alt}m altitude...")
    target_location = LocationGlobalRelative(target_lat, target_lon, target_alt)
    vehicle.simple_goto(target_location)

    while True:
        current_location = vehicle.location.global_relative_frame
        print(f"Current Location: {current_location.lat}, {current_location.lon}")
        if abs(current_location.lat - target_lat) < 0.0001 and abs(current_location.lon - target_lon) < 0.0001:
            print("Reached target location!")
            break
        sleep(3)

def scan_qr_code():
    """
    captures image and scans for a QR code.
    """
    print("Scanning QR Code...")
    # Add QR code detection logic here
    qr_data = "Sample QR Data"
    print(f"QR Code Data: {qr_data}")
    return qr_data

def drop_payload():
    """
    Activates the payload release mechanism.
    """
    # Payload release mechanism
    print("Landing for payload drop")
    vehicle.mode = VehicleMode("LAND")
    
    from servo_control import open_box,close
    print("Opening payload box")
    open_box()
    
    print("Payload dropped!")

def return_to_launch(arm_location,alt):
    """
    Returns the drone to the arm position.
    """
    print("Returning to the armed location...")
    navigate_to_gps(arm_location.lat,arm_location.lon,alt)
    vehicle.mode = VehicleMode("LAND")

if __name__ == "__main__":
    try:
        print("Requesting Mission Parameters...")
        string = input("Enter latitude,longitude,altitude:")
        string = string.split(",")
        latit = float(string[0].strip())
        longit = float(string[1].strip())
        altit = float(string[2].strip())
        print(f"latitude:{latit} longitude:{longit} altitude:{altit}")
        arm_location = vehicle.location.global_relative_frame
        print(f"Arming at {arm_location.lat},{arm_location.lon}")

        c=input("confirm?")
        
        arm_and_takeoff(altit)
        
        navigate_to_gps(latit,longit, altit)
        
        qr_data = scan_qr_code()
        print(qr_data)
        
        prompt= input("Drop payload?[y/n]:")
        if prompt.strip().lower() == 'y':
            drop_payload()
        else:
            print("Delivery cancelled!")
        print(f"Returning to launch position at {arm_location.lat}, {arm_location.lon} at 5m altitude")
        input("confirm?")
        return_to_launch(arm_location,5)
        #print("Landing...")
        #vehicle.mode = VehicleMode("LAND")

    except Exception as e:
        if e==KeyboardInterrupt:
            c = input("RTL?[y/n]:")
            if c.lower() == 'y':
                vehicle.mode = VehicleMode("RTL")
        else:
            print(f"Error:{e}")

    finally:
        print("Closing vehicle connection...")
        vehicle.close()
        print("Byeee...")