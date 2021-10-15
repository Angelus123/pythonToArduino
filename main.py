# import serial
# import time

# arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
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

# import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()
# serialInst = serial.Serial()
# portList = []
# for onePort in ports:
#     portList.append(str(onePort))
#     print(str(onePort))
# val = input("Select Port: COM: ")
# print(val)
# for x in range(0, len(portList)):
#     if portList[x].startswith("COM"+ str(val)):
#         portVar = "COM" + str(val)
#         print(portVar)
# serialInst.baudrate =9600
# serialInst.port = "COM4"
# serialInst.open()

# while True:
#     if serialInst.in_waiting:
#         packet = serialInst.readLine()
#         print(packet.decode('utf').rstrip('\n'))

import serial
import time
# arduino = serial.Serial("COM4", 9600)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
time.sleep(2)
i=1
while (i>0):
    dato = input("turn on: ")
    time.sleep(1)
    arduino.write(dato.encode())
    print("working")
    if(dato == "x"):
        i=0
arduino.close() 