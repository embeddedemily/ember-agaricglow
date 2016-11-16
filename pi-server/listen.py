import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(5)

while 1:
    ser.write('testatestbtestctestd')
    print(ser.read(20).decode('utf-8'))
