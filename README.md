# BluenoStereo
The skeleton of a smarter car stereo for Raspbery Pi enthusiasts such as yourself.

## History
In the summer of 2016 I spent half my summer earnings on my first car.  However, my "new" '04 Subaru Impreza Outback Sport came with the stock radio, an unfortunate relic from the awkward transtitional years between cassette decks and aux cords.  Rather than do the sensible and economic thing and buy a $40 off-the-shelf radio, I decided to build my own.  Eventually, I hope for this project to include:
- Analog audio circuits, including an old-fashioned graphic equalizer
- Built-in preamp for an electric guitar 
- Data logging from OBD-II port (or possibly directly tapping CAN-BUS lines)
- Operation as bluetooth audio device
- Voice control for querying CAN data, media playback, and other fun stuff
- Apollo mission aesthetics
- Facial recognition to associate data with the current driver, and possibly to alert me if someone other than a specified set of individuals is driving my car

## Versions
### 0.0.1
Initial development of BluenoStereo as my final project for a class at Brown University.  This release contains several low-level utilities to implement some barebones functionality, namely power management, basic I/O, and basic face detection and image capture.

## Hardware
- Raspberry Pi 3 with latest Raspbian Jesse (as of December 2016)
- [Sleepy Pi 2](http://spellfoundry.com/products/sleepy-pi-2/) power management and RTC hat
- USB webcam with microphone (e.g. PlayStation Eye)
- Breadboard with simple LED circuit
- Bluetooth OBD-II connector

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
  - SQLite database creation and editing works, but has no data interface at the moment
  - This component was essentially abandoned when it became clear that the bluetooth OBD-II module had fried

## In Progress
- Voice control
  - Failed to install [Jasper](http://jasperproject.github.io/), the "open source platform for developing always-on, voice-controlled applications"
  - In the process butchered all audio settings such that backup plan, [Snowboy Hotword Detection](https://snowboy.kitt.ai/), cannot connect to microphone
  - Likely requires fresh Raspbian install to rectify
  - However, all code written with this in mind -> modularity will make it easy to add functionality
- Facial recognition
  - Initial intent was to identify the driver of the car
  - OpenCV 3.0 made this very hard to do in python
  - Requires downgrading to OpenCV 2.4 (which is a very time-consuming build) or switching to a programming language with better bindings
- Bluetooth Interface with OBD-II
  - $11 Amazon unit appears to no longer be working (cannot connect from Android app or laptop either)
  - Telemetry code needs to be updated to include the actual interaction with a replacement module
  - Eventually want to make this data queriable by voice commands