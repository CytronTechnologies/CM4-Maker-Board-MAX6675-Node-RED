# This code will send thermocouples data to the HiveMQ Broker, then Node Red will 
import time
import paho.mqtt.client as paho
from paho import mqtt
from ReadMAX6675 import Thermocouple

# Your HiveMQ Access Credentials Username
USERNAME = "Username"
# Your HiveMQ Access Credentials Password
PASSWORD = "Password"
# The Cluster URL
CLUSTER_URL = "HiveMq_Cluster_URL"
# The Cluster Connection Port
PORT = 8883

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set(USERNAME, PASSWORD)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(CLUSTER_URL, PORT)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("thermocouple/#", qos=1)



# set the pin for communicate with MAX6675
# GPIO Num
cs_1 = 12
sck_1 = 5
so_1 = 6

cs_2 = 13
sck_2 = 23
so_2 = 24

try:
    # start MQTT client
    client.loop_start()

    # max6675.set_pin(CS, SCK, SO, unit) [unit : 0 - raw, 1 - Celsius, 2 - Fahrenheit]
    thermo1 = Thermocouple(cs_1, sck_1, so_1, 1)
    thermo2 = Thermocouple(cs_2, sck_2, so_2, 1)


    while True:
        # read temperature 
        temp1 = thermo1.read_temp()
        temp2 = thermo2.read_temp()
        
        # print temperature
        print ("Thermocouple 1: {} , Thermocouple 2: {}".format(temp1,temp2))
        client.publish("thermocouple/1", payload=temp1, qos=1)
        client.publish("thermocouple/2", payload=temp2, qos=1)
        
        time.sleep(5)
finally:
    # stop MQTT client
    client.loop_stop()