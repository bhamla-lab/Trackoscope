# Trackoscope

## Programs

### TrackoscopeComm.py (MAIN PROGRAM)
This program is to be run on a laptop. It has the full organism-tracking capability and has a user-friendly GUI. Once "Start Tracking" has been clicked, the user can then select the organism that they wish to track and hit the "Enter" key on their keyboard to start the track. As the organism starts moving, the actuator moves to keep it in frame.
<img width="463" alt="image" src="https://github.com/bhamla-lab/Trackoscope/assets/30093976/86f3ee81-4869-4006-9269-dee48f4e4056">

### Grapher.py
Taking CSV data and converting to meaningful graphs that display speed and position over the track duration.

### ArduinoMovPlat.ino
This program is to be uploaded to the Arduino Uno and enables the python code to control Trackoscope. This code also allows for pure joystick control.

## Getting Started
This project uses python virtual environments

Open a command prompt and then install the dependencies to get it working.

    pip install -r requirements.txt
    
    
### Materials
* Arduino Uno
* CNC Shield
* 2 NEMA 17 Stepper Motors
* Webcam/USB Camera
* Arduino Joystick Module

## The Paper

