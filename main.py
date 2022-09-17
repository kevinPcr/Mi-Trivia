import random
import time

print("\033[35m           TRIVIA  \033[39m             ")
print("")
nombre=str(input("\n \033[33m Hola, me podrias brindar tu nombre: \n")) .lower()
correcta=0
incorrecta=0

correcta=random.randint(0,10) 
print("")
print("\033[33m Hola",nombre,"pon a prueba tus conocimientos sobre la cultura peruana \033[39m")
print("")

#########
print("\033[34m 1.- ¿Quién fue el primer Inca? \033[39m")
print("")
print("\033[36m a) Pachacutec \033[39m")
print("\033[36m b) Inca Yupanqui \033[39m")
print("\033[36m c) Manco Cápac \033[39m") #correcta
print("\033[36m d) Sinchi Roca \033[39m")
respuesta1=str(input("\033[33m Su respuesta es: \033[39m")) .lower()
print("")
while respuesta1 not in ("a","b","c","d"):
 respuesta1 = str(input("\n \033[31m Solo debes ingresar a,b,c o d. Vuelve a intentarlo: \033[39m \n")) .lower()

if respuesta1=="c":
  correcta=correcta+1 
  print("\033[32m Muy bien",nombre,"Respuesta correcta \033[39m")
else:
   print("\033[31m Respuesta incorrecta \033[39m")
   incorrecta+=1 
print("")
print("\033[35m Esperando la siguiente pregunta.... \033[39m")
time.sleep(2)
print("")
 ######################
print("\033[34m 2.- ¿Cuál es la ‘capital histórica’ de Perú? \033[39m")
print("")
print("\033[36m a) Lima \033[39m")
print("\033[36m b) Cuzco \033[39m") #correcta
print("\033[36m c) Jauja\033[39m")
print("\033[36m d) N.A \033[39m")
respuesta2=str(input("\033[33m Su respuesta es: \033[39m")) .lower()
print("")
while respuesta2 not in ("a","b","c","d"):
 respuesta2 = str(input("\n \033[31m Solo debes ingresar a,b,c o d. Vuelve a intentarlo: \033[39m \n")) .lower()

if respuesta2=="b":
  correcta=correcta+1 
  print("\033[32m Muy bien",nombre,"Respuesta correcta \033[39m")
else:
   print("\033[31m Respuesta incorrecta \033[39m")
   incorrecta+=1 
print("")
print("\033[35m Esperando la siguiente pregunta....\033[39m")
time.sleep(2)
print("")
#############
print("\033[34m 3.- ¿Cuántos años duró la guerra entre Perú y Chile? \033[39m")
print("")
print("\033[36m a) 10 años \033[39m")
print("\033[36m b) 8 años \033[39m")
print("\033[36m c) 6 años \033[39m")
print("\033[36m d) 4 años \033[39m")#correcta
respuesta3=str(input("\033[33m \n Su respuesta es: \033[33m")) .lower()
print("")
while respuesta3 not in ("a","b","c","d"):
 respuesta3 = str(input(" \n \033[31m Solo debes ingresar a,b,c o d. Vuelve a intentarlo: \033[39m \n")) .lower()

if respuesta3=="d":
  correcta=correcta+1 
  print("\033[32m Muy bien",nombre,"Respuesta correcta \033[39m")
else:
   print("\033[31m Respuesta incorrecta \033[39m")
   incorrecta+=1 
print("")
print("\033[35m Esperando tu puntaje.... \033[39m")
time.sleep(2)
print("")
print("\033[33m    RESULTADOS     \033[39m")
print("\033[33m Su puntaje es=  \033[39m",correcta)
print("\033[33m Respuestas incorrectas= \033[39m",incorrecta)

input("\033[35m \n Presiona Enter para continuar \n \033[39m")

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
clearConsole()

while 1:
    os.system("python main.py")
    exit()