import serial
import time

arduino = serial.Serial('COM2', 9600)
time.sleep(2)

print("Enter 1 to turn on and  0 to turn off LED:  ")

while 1:

    x = input()

    if x == '1':
        arduino.write(b'1')
        print("LED is on")
    elif x == '0':
        arduino.write(b'0')
        print("LED is off")