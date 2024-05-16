# Trackoscope

## Programs

### TrackoscopeComm.py (MAIN PROGRAM)
This program is to be run on a laptop. It has the full organism-tracking capability and has a user-friendly GUI. Once "Start Tracking" has been clicked, the user can then select the organism that they wish to track and hit the "Enter" key on their keyboard to start the track. As the organism starts moving, the actuator moves to keep it in frame.

<img width="463" alt="image" src="https://github.com/bhamla-lab/Trackoscope/assets/30093976/86f3ee81-4869-4006-9269-dee48f4e4056">

### Grapher.py
Taking CSV data and converting to meaningful graphs that display speed and position over the track duration.

### ArduinoMovPlat.ino
This program is to be uploaded to the Arduino Uno and enables the python code to control Trackoscope. This code also allows for pure joystick control.

### Getting Started
This project uses python virtual environments. We suggest using software such as Visual Studio Code or JetBrains Pycharm to run the code.

Open a command prompt and then install the dependencies to get it working.

    pip install -r requirements.txt

## Trackoscope Build Instructions

### Assembly
#### Document/Files
Trackoscope Assembly Instructions.PDF contains the step by step instructions on how to build a Trackoscope. All files can be found in the MakerFiles folder in the repository.

#### Additional Tools/Materials
* M5 Allen Key
* M4 Allen Key
* M3 Allen Key
* M2 Allen Key
* Flush Cutters
* Hot Glue/Super Glue

### 3D Printing
All STL files can be fit on any standard 3D printer (ender 3, prusa mini, ultimaker 3). They can be sliced with Ultimaker Cura, a free slicing software.

<img width="842" alt="image" src="https://github.com/bhamla-lab/Trackoscope/assets/30093976/11eabce7-4d9b-4f47-a9cb-2a900a5f5267">

#### Print Settings/Layout
* 0.2 mm layer height
* 30% infill density (gyroid or tri-hexagonal pattern)
* Supports: Yes (tree)
* Adhesion: Yes (7mm  brim)

### Laser Cutting
DXF files provided are in the inches unit. They can be preppped for laser cutting using a vector modifying software such as Inkscape or Adobe Illustrator. These files are meant for 1/4" material thickness. Files that end in "TAP" have smaller hole sizes for tapping instead of clearance holes to be used with nuts and bolts. The files ending in "Spacer" are optional and can be cut if extra height is needed. There are two motor mount files. Depending on your application, the tall mount can be used.

## The Paper
Link: doi.org/10.1101/2024.02.06.579130

Supplementary Files can be found at figshare.com/account/home#/projects/200934
