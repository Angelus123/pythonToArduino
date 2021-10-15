# import serial
# import time

# arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
# time.sleep(2)

# print("Presione 1 para Encender y 0 para Apagar el LED:  ")
# print (f'{arduino.readline()}')                            #read the serial data and print it as line 
# print ("You have new message from Arduino")

# while 1:

#     datousuario = input()

#     if datousuario == '1':
#         arduino.write(b'1')
#         print("LED Encendido")
#     elif datousuario == '0':
#         arduino.write(b'0')
#         print("LED Apagado")
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
