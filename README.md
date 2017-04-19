# ScanBot3D project

Our goal is to perform 3D reconstruction using mobile embedded systems. The developed solution should be capable to generate the 3D model of indoor spaces. We’ll be using an infrared (IR) sensor embarked on a vehicle in order to do so.

The vehicle should offer several navigation options which are as follows:
- Manual remote control
- GPS-based autonomous navigation outdoors
- Software override using input from external embarked module (autonomous navigation indoors for 3D reconstruction with 3D IR module, autonomous car control module)

Communication should be possible:
- From radio control unit to main navigation board
- Between a computer or a tablet/smartphone and the main navigation board for configuration and telemetry as well as waypoints definition
- Between the main navigation board and embarked modules

The main software stack used for navigation has to be open enough to allow future implementations and aforementioned communication between the main navigation board and external modules.

Find out more about this project here: https://github.com/QBitor/ScanBot_ECS/blob/master/ScanBot3D.pdf

# ScanBot3D ECS software

Embedded control system (ECS) software handles interaction between the different boards and controls
the overall behavior of the vehicle.

The master Raspberry Pi board, known as master board sends data to and receives data from other boards, including:
- Arduino Uno board for turret servo control using Nanpy - USB link
- Navigation Raspberry Pi/Navio2 board running ArduRover using custom server/client library - Ethernet link
- Logger/Minnowboard running custom Logger1 for RGB-D logging - Ethernet link

This led to the following architecture:

![alt text](https://github.com/QBitor/ScanBot_ECS/blob/master/readme_res/ecs.png =800x800 "ScanBot ECS architecture")

In the server/client approach, the navigation board client sends RC input data to the master board server via TCP/IP which uses this data to control the turret in manual mode. These packets consist in a stream of integers.

ECS software is invoked through remote GCS via SSH. On startup, the user has to choose between two capture modes: manual or autonomous. Once done, the user should specify how long capture will last so the logger board can be configured. 

In manual mode, this system is used to retrieve 3 position switch RC input data used to control turret orientation (left, right, center). Navigation is done via RC control. In autonomous mode on the other hand, the vehicle navigates using US sensors and swipes the room in order to get as many points as possible. It then stops when capture duration is reached.

This behavior can be summarized as follows:

## Manual mode
- Write capture duration on logger board
- Start server on master board
- Start client on navigation board
- Write servo position based on client data while running

## Autonomous mode
- Write capture duration on logger board
- Start server on navigation board
- Start client on master board
- Initialize US sensors (via Nanpy)
- Send PWM data from master to navigation board to control vehicle and turret behavior while running

