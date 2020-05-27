#This is the side that will run on the pi. It should send data (lets have it send random data once a second)

import socket
import sys
import time
import pickle
import random #for testing

host = '192.168.1.5'
port = 50000

s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port)) #remote server must already be running

except socket.error as message:
    if s:
        s.close()
    print ("Unable to open the socket: " + str(message))
    sys.exit(1)

sensor = "CH0"
value = 13
sensor_time = 1039234.323

data_dict = {"sensor": sensor, "value": value, "time": sensor_time}
serialized_data = pickle.dumps(data_dict)

while True:
    #todo set the above sensor, dict, serialized_data, etc here
    value = random.randrange(-20, 20)
    data_dict = {"sensor": sensor, "value": value, "time": sensor_time}
    serialized_data = pickle.dumps(data_dict)
    print("Sending...")
    s.send(serialized_data)
    time.sleep(1)

s.close()
