#Importamos las librerias (serial hay que descargarla)
import serial 
import time

#Usando py abrimos el txt que se encuentra en esa carpeta y le damos us parametro de entrada
archivo = open('C:\\Users\\Alex Carri\\Documents\\Programas\\serialdatos.txt' , 'w')

#Declaramos el puerto serial 
serialArduino = serial.Serial("COM4" , 9600)
time.sleep(1) #Para no copiar toda la informacion pusimos un time step de 1

while True:
    #Dentro del ciclo while agregamos la lectura y la decodificacion de arduino
    cad = serialArduino.readline().decode('ascii')
    print(cad) #imprimimos cad para ver que funcione 
    archivo.write(cad) #Escribimos en el txt y se reinicia el loop 