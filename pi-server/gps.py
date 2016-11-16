import serial
import time

ser = serial.Serial('/dev/serial0', 9600, timeout=0)
time.sleep(5)

print('ready')

while True:
    print(ser.readline())
    time.sleep(1)
