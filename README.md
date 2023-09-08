# CM4-Maker-Board-MAX6675-Node-RED

If you want to test displaying sensor data on Node-RED using CM4 Maker Board, you are in the right place! Here you will find all the information you need to set up your hardware and software.

You can visit [Node-RED on CM4 Maker Board: Displaying Thermocouple Sensor Data](https://cytron.io/tutorial/node-red-on-cm4-maker-board-displaying-thermocouple-sensor-data) to learn more about it.  

## Requirements  
To get started, you will need the following hardware and software:  

**Hardware:**  
* [CM4 Maker Board](https://cytron.io/p-cm4-maker-board-and-kits)  
* [Rapberry Pi CM4 Lite](https://cytron.io/p-raspberry-pi-cm4-wireless-4gb-ram-lite-no-emmc-and-kits) or [Rapberry Pi CM4 with eMMC](https://cytron.io/p-raspberry-pi-cm4-wireless-8gb-ram-8gb-emmc-and-kits)  
* [MAX6675 K-Thermocouple](https://cytron.io/p-max6675-k-thermocouple-to-digital-converter-module)  


**Software:**  
Raspberry Pi OS with installed Python. If you want to know how to install the Raspberry Pi OS on the CM4 Maker Board, you can visit this tutorial on [Boot up Raspberry Pi CM4 on CM4 Maker Board](https://cytron.io/tutorial/boot-up-raspberry-pi-cm4-on-cm4-maker-board).  

## Installation  
To begin, connect the MAX6675 thermocouples to the Grove port on the CM4 Maker Board. In this example, we will use two thermocouples.

<img src="https://github.com/CytronTechnologies/CM4-Maker-Board-MAX6675-Google-Sheets/blob/main/Pictures/2_thermocouple_connection_to_cm4_maker_board.jpg" width="600"> 

Install Node-RED on Raspberry Pi CM4.
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
Download the code from Github to your home directory.
```
git clone https://github.com/CytronTechnologies/CM4-Maker-Board-MAX6675-Node-RED
```
This repository contains two examples of sending sensor data to Node-RED through TCP/IP and MQTT connections.  

**Local TCP/IP Connection to Node-RED**  
1. Import the JSON file 'node_red_max6675_TCP.json' into your Node-RED.
2. Click the "Deploy" button on the top right of the Node-RED interface.
3. Open the Python code 'node_red_max6675_TCP.py' and run it.

**Making Your Node-Red Dashboard Online with MQTT**  
1. Import the JSON file 'node_red_max6675_TCP.json' into your Node-RED.
2. Add the Cluster URL, Port number, and Access Credentials (Username and Password) of your MQTT Broker.
3. Click the "Deploy" button on the top right of the Node-RED interface.
4. Open the Python code 'node_red_max6675_MQTT.py' and edit the the USERNAME, PASSWORD, CLUSTER_URL, and PORT.
   
```python
# Your HiveMQ Access Credentials Username
USERNAME = "Username"
# Your HiveMQ Access Credentials Password
PASSWORD = "Password"
# The Cluster URL
CLUSTER_URL = "HiveMq_Cluster_URL"
# The Cluster Connection Port
PORT = 8883
```
Run your code, and you can access the Node-RED dashboard.  

## Resources    
For more information on the CM4 Maker Board, check out the resources here:  
* [CM4 Maker Board Resources](https://my.cytron.io/p-cm4-maker-board-and-kits#tab-resource)  

## Support  
You can visit [Log Thermocouple Sensor Data to Google Sheets using CM4 Maker Board](https://cytron.io/tutorial/log-thermocouple-sensor-data-to-google-sheets-using-cm4-maker-board) to learn more about it. 

If you need further assistance, we welcome you to our [technical forum](http://forum.cytron.io) or you can contact us through email support@cytron.io where our team will be happy to assist you. 

Let's start building with CM4 Maker Board!
