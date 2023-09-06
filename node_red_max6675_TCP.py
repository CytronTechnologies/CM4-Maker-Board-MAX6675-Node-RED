# This code will send thermocouples data to the Node Red using TCP connection
import time
from ReadMAX6675 import Thermocouple
import socket
import sys
import struct

IP_ADDRESS = 'localhost'
PORT = 1234

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server
# given by the caller
server_address = (IP_ADDRESS, PORT)
print('Connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# set the pin for communicate with MAX6675
# GPIO Num
cs_1 = 12
sck_1 = 5
so_1 = 6

cs_2 = 13
sck_2 = 23
so_2 = 24

try:
    # max6675.set_pin(CS, SCK, SO, unit) [unit : 0 - raw, 1 - Celsius, 2 - Fahrenheit]
    thermo1 = Thermocouple(cs_1, sck_1, so_1, 1)
    thermo2 = Thermocouple(cs_2, sck_2, so_2, 1)


    while True:
        # read temperature 
        temp1 = thermo1.read_temp()
        temp2 = thermo2.read_temp()
        
        # print temperature
        print ("Thermocouple 1: {} , Thermocouple 2: {}".format(temp1,temp2))
        temp_bytes = bytes(str(temp1)+','+str(temp2), 'ascii')

        sock.sendall(temp_bytes)

        time.sleep(5)
        
finally:
    sock.close()