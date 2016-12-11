import socket
import smbus
import time
from gpiozero import LED

led = LED(17)
led2 = LED(18)

steerA = LED(27)
steerB = LED(22)

UDP_IP = "172.24.1.103"
UDP_PORT = 55056

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setblocking(0)
sock.bind((UDP_IP, UDP_PORT))

bus = smbus.SMBus(1)
address = 0x16

cars = {}
phones = {}
phoneData = {}

analogSingle = 330

led.off()
led2.off()

steerA.off()
steerB.off()

def left():
    if(analogSingle > 480):
        steerA.on()
        steerB.off()
    else:
        steerA.off()
        steerB.off()

def right():
    if(analogSingle < 750):
        steerA.off()
        steerB.on()
    else:
        steerA.off()
        steerB.off()

def noSteer():
    if(analogSingle > 620):
        steerA.on()
        steerB.off()
    elif(analogSingle < 460):
        steerA.off()
        steerB.on()
    else:
        steerA.off()
        steerB.off()
    

def forward():
    led.on()
    led2.off()

def reverse():
    led.off()
    led2.on()

def noDrive():
    led.off()
    led2.off()

while True:
    try:
        data, addr = sock.recvfrom(1024)

        if data == 'car':
            print('add')
            cars[addr[0]] = time.time()
        elif data == 'phone':
            phones[addr[0]] = time.time()
        else:
            #print(data)
            phoneData[addr[0]] = data
    except:
        pass

    for k, v in cars.items():
        if v < time.time() - 0.016:
            print('remove')
            cars.pop(k)

    for k, v in phones.items():
        if v < time.time() - 0.016:
            phones.pop(k)
            continue
        #other stuff if valid phone

    analog = bus.read_i2c_block_data(address, 0, 2)
    analogSingle = ((analog[1] << 8) | analog[0])

    #print(analogSingle)

    #555 left
    #316 center
    #78 right


    for k, v in phoneData.items():
        if v == 'f\x00r\x00':
            print('f')
            forward()
            right()
        elif v == 'f\x00l\x00':
            forward()
            left()
        elif v == 'f\x00n\x00':
            forward()
            noSteer()
        elif v == 'b\x00r\x00':
            reverse()
            right()
        elif v == 'b\x00l\x00':
            reverse()
            left()
        elif v == 'b\x00n\x00':
            reverse()
            noSteer()
        elif v == 'n\x00r\x00':
            noDrive()
            right()
        elif v == 'n\x00l\x00':
            noDrive()
            left()
        else:
            noDrive()
            noSteer()
        #print(k)
        v = {}



    #print(cars, phones, phoneData)
    #time.sleep(0.016)