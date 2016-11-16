import socket
import struct
import serial
import time

UDP_IP = "192.168.100.1"
UDP_PORT = 55056

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
time.sleep(5)

print('ready')

while True:
    data, addr = sock.recvfrom(1024)

    x = struct.unpack('d', bytes(data[0:8]))[0]
    y = struct.unpack('d', bytes(data[8:16]))[0]
    #z = struct.unpack('d', bytes(data[16:24]))[0]

    if(x < 6):
        if(y < -3 ):
            ser.write('a')
            print('a')
        elif(y > 3):
            ser.write('b')
            print('b')
        else:
            ser.write('f')
            print('f')
    elif(x > 9):
        if(y < -3 ):
            ser.write('c')
            print('c')
        elif(y > 3):
            ser.write('d')
            print('d')
        else:
            ser.write('z')
            print('z')
    else:
        if(y < -3 ):
            ser.write('l')
            print('l')
        elif(y > 3):
            ser.write('r')
            print('r')
        else:
            ser.write('n')
            print('n')
    
    time.sleep(0.016)
