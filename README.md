# MaisinMatila-Projects
This Metropolia Big-Flash project focuses on advancing Artificial intelligence and Robotics solutions to develop a self-pick-up system, cooperating with Maisin's farm.


# About Project

Maisin Maatila project embraces the above idea to gratify customers and optimize logistics cost for manufacturers. Owning an automated pick-up system can save human resources, increase productivity, make it scaleable, and focus more on management. Our system will essentially permit the entry of drivers via their car plate, compared to its on our database, then send a signal to open the entrance gate. At the existing gate, an ultrasonic distance sensor will be installed in order to recognize outcome cars and send them back to database. Maisin Maatila project ensures bringing convenience, saves time and optimizes supply chain for both customers and the company


# Materials:
* Arduino Portenta H7 - [Portenta H7](https://store.arduino.cc/products/portenta-h7).
* Arduino Vision Shield - [Portenta Vision Shield](https://store-usa.arduino.cc/products/arduino-portenta-vision-shield-ethernet).

Sensors:

* Motion Sensor - [motion sensor HC-SR501](https://ihmevekotin.fi/liikeanturit/246-saeaedettaevae-pir-liiketunnistin-hc-sr501.html).
* Ultrasonic Sensor - [Ultrasonic Distance Sensor](https://www.seeedstudio.com/Grove-Ultrasonic-Distance-Sensor.html).

Actuators:

* H-Bridge - [L298N motor](https://kauppa.sintosen.com/product/605/?gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT-uEALPWoaZPsBYVHWpek2E_FxKFkydzNwFWuVzvWdhOdi_tegsGuwaAlzvEALw_wcB).
* Motor - Electric motor BOSCH 24V, 4300 rpm, 180W 0 130 101 616 - Buy (autodoc.fi)

Others:

* Male-to-Male Jumper Wires - [PRT-12795 SparkFun Electronics](https://www.digikey.fi/fi/products/detail/sparkfun-electronics/PRT-12795/5993860?utm_adgroup=General&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Zombie%20SKU&utm_term=&productid=5993860&gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT_6z0XPvhYTjwCleS3g0Xh_Usa0uzIe1Q2axPjhIuTaXoJU2m1RkqsaArCFEALw_wcB).
* Male-to-Female Jumper Wires - [PRT-12794 SparkFun Electronics](https://www.digikey.fi/fi/products/detail/sparkfun-electronics/PRT-12794/5993859?utm_adgroup=General&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Zombie%20SKU&utm_term=&productid=5993859&gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT-0lPbE2fahL0PdxRHLco8nMrJ4OxuJUvqXU_1ZLl8K7T1X7pWP8lcaAlYPEALw_wcB)
* [Breadboard]( https://www.amazon.com/EL-CP-003-Breadboard-Solderless-Distribution-Connecting/dp/B01EV6LJ7G/ref=as_li_ss_tl?dchild=1&keywords=breadboard&qid=1593801975&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySVJZNFYxM0hRTzEzJmVuY3J5cHRlZElkPUEwODY3OTUzM1M1M0xWR05PVzlNRiZlbmNyeXB0ZWRBZElkPUEwNTI0ODkxMTVLQVI1Vk9QVEE5OCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=&linkCode=sl1&tag=craftcarol-20&linkId=cdf60918bce68814b555d1ee9480beb3&language=en_US).

# Block Diagram
* For Entrance: 

<img width="538" alt="Screenshot 2023-01-16 at 22 08 53" src="https://user-images.githubusercontent.com/83159640/212758986-bead5dd3-9e09-412c-b06b-0c7ea11dae38.png">

* For Exitting:
<img width="458" alt="Screenshot 2023-01-16 at 22 09 04" src="https://user-images.githubusercontent.com/83159640/212759115-99164da4-e7e7-4768-ad5a-c364e5a605ea.png">


# Assamble
1. Motor

<img width="426" alt="Screenshot 2023-01-16 at 22 18 23" src="https://user-images.githubusercontent.com/83159640/212759514-d703976a-7c25-4ec1-82ce-694f803c2548.png">

* Connect RED and Black wires from motor to H-Bridge.
* Connect wires from "IN1" and "IN2" port at H-Bridge to pin "PA9" and pin "PA10" in Arduino
* Connect ground in H-bridge to pin "Ground" in Arduino

2. PIR Motion Sensor

<img width="483" alt="Screenshot 2023-01-16 at 22 25 27" src="https://user-images.githubusercontent.com/83159640/212760434-a53843c0-ad4b-406d-8ac6-1c61873836cc.png">

* Connect wire from power pin to 3.3 pin in Arduino
* Connect wire from ground pin to ground in Arduino
* Connect wire from data pin to pin "PC3" in Arduino

# Final Report

[Report](https://docs.google.com/document/d/10kojgWrZTQAsMv4OUa6YUgATDYE_Qozs/edit)

# Ref
* [Big-flash](https://bigflash.metropolia.fi/)
* [Maisin Maatila](https://www.mattilafarm.com/fi)





