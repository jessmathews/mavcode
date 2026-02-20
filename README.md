# Autonomous Quadcopter missions using Dronekit
# NOTE: This repo was deprecated in favour of a more reliable and hardware tested ROS2 implementation. Check it out here: https://github.com/jessmathews/ros2_autonomous_drone
## This Repo Contains:
- Testing Scripts for Dronekit (takeoff, hover, servo_control)
- Camera initialization scripts
- Streaming camera feed to webpage
- Mission Script
## Prerequisites
- Python3
- A stable calibrated Quadcopter with camera and GPS
## Mission Code Workflow
```mermaid
flowchart TD

A[Start] --> B[Connect to Vehicle]
B --> C[Input Lat, Lon, Alt]
C --> D[Store Arm Location]
D --> E[User Confirmation]

E --> F[Arm and Takeoff]
F --> G[Navigate to Target GPS]
G --> H[Scan QR Code]

H --> I{Drop Payload?}

I -->|Yes| J[LAND]
J --> K[Open Payload Box]
K --> L[Payload Dropped]

I -->|No| M[Skip Drop]

L --> N[Return to Launch at 5m]
M --> N

N --> O[LAND]
O --> P[Close Vehicle]
P --> Q[End]
```


## Setup 
Clone the repo 
```sh
git clone https://github.com/jessmathews/mavcode
cd mavcode
```
NOTE: Create a virtual environment for easy dependency management.
```sh
python3 -m venv env
source env/bin/activate
```
Install requirements
```sh
pip install -r requirements.txt
pip install -r dronekit_control/requirements.txt
```
Run the code
```sh
cd dronekit_control
python3 main.py
```
### Created with ❤️ and Python
