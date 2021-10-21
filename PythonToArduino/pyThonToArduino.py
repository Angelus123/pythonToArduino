import serial
import time

arduino = serial.Serial('COM2', 9600)
time.sleep(2)

print("Enter 1 to turn on and  0 to turn off LED:  ")

while 1:

    x = input()

    if x == 'd':
        arduino.write(b'd')
        print("LED is on")
    elif x == 'r':
        arduino.write(b'r')
        print("LED is off")
    elif x == 'c':
        arduino.write(b'c')
        print("LED is off")