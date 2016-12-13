# BluenoStereo
The skeleton of a smarter car stereo for Raspbery Pi enthusiasts such as yourself.
## Hardware
- Raspberry Pi 3 with latest Raspbian Jesse (as of December 2016)
- [Sleepy Pi 2](http://spellfoundry.com/products/sleepy-pi-2/) power management and RTC hat
- USB webcam with microphone (e.g. PlayStation Eye)
- Breadboard with simple LED circuit
- Bluetooth OBDII connector

## Current Features
- Smart power management:
  - The Sleepy Pi 2 hat manages power, such as high voltage from the car's stereo harness
  - Arduino signals Pi over GPIO when loss of power (such as accessory voltage dropping when the vehicle is turned off)
  - Direct connection to battery power lets Arduino wait while Pi shuts down cleanly
- Error LEDs:
  - Two error LEDs wired directly to GPIO are made available over localhost through a UDP server
  - Allows non-sudo applications to activate/deactivate LEDs
  - Scripting facilitates the sending of blink patterns
- Security system using webcam:
  - Takes picture when car is turned on
  - Attempts to identify if face is present in image
    - If not, blinks an error code
  - Either way, saves file
- OBD-II Logging
  - SQLite database creation and editing works
  - Most recent data available over Flask API

## In Progress
- Voice control
  - Failed to install Jasper, the "open source platform for developing always-on, voice-controlled applications"
  - In the process butchered all audio settings such that backup plan, Snowboy Hotword Detection, cannot connect to microphone
  - Likely requires fresh Raspbian install to rectify
  - However, all code written with this in mind -> modularity will make it easy to add functionality
- Facial recognition
  - Initial intent was to identify the driver of the car
  - OpenCV 3 made this very hard to do in python
  - Requires downgrading to OpenCV 2 (which is a very time-consuming build) or switch to C++ (which I know nothing of)
- Bluetooth Interface with OBD-II
  - $11 Amazon unit appears to no longer be working (cannot connect from Android app either)
  - Telemetry code needs to be updated to include the actual interaction with a replacement module
