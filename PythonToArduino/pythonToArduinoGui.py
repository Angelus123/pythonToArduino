import tkinter
import serial
import time

arduino = serial.Serial('COM2', 9600)
time.sleep(2)

def encender():
    arduino.write(b'1')

def apagar():
    arduino.write(b'0')

root = tkinter.Tk()
root.title("Punto 1")
root.geometry("220x80")

boton = tkinter.Button(root, text="ENCENDER LEDS", command=encender)
boton.config(fg = "black", bg = "light blue")
boton.pack()

boton1 = tkinter.Button(root, text="APAGAR LEDS", command=apagar)
boton1.config(fg = "black", bg = "light blue")
boton1.pack()

root.mainloop()