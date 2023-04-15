import math
#1) Escribe un programa muestre por pantalla “Hello World”
print('hola bruno')
print ('Vamos para adelante')

#2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
print(3+5)
#3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
#nombre = input("Ingrese su nombre: ")
#print('Hola', nombre)


#4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
#num1 = float(input("ingrese un numero: "))
#num2 = float(input("ingrese un numero: "))
#print(num1 +num2)

#5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
#num1 = float(input("ingrese un numero: "))
#num2 = float(input("ingrese un numero: "))
'''
if num1 > num2:
    print(num1)
else:
    print(num2)    

'''
#6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# num3 = int(input("Ingrese el tercer numero: "))

# if num1 > num2 and num1 > num3:
#     print('el mayor es ', num1)
# elif num2 > num1 and num2 > num3:
#     print('el mayor es ', num2)
# else:
#     print('el mayor es ', num3)
#7) Escribe un programa que pida un número y diga si es divisible por 2
# num1 = int(input("Ingrese el numero: "))
# if num1 % 2 == 0:
#     print('El numero: ', num1, ' es divisible por 2')
# else:
#     print('El numero ', num1, ' no es divisible por 2')
#8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)

#9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
#10) Escribir un programa que escriba en pantalla los divisores de un número dado
# num = int(input('ingrese un numero:'))
# for i in range (1, num):
#     if num % i == 0:
#         print('el numero ', num, ' es divisible por ', i)

#11) Escribir un programa que nos diga si un número dado es primo (no es divisible
#por ninguno otro número que no sea él mismo o la unidad)
num = int(input('ingrese un numero:'))
if num <= 0:
    print('debe ingresar un numero mayor a cero')
for i in range(2, num // 2):
    if num % i == 0:
        print('el numero no es primo')
    else:
        print('el numero es primo')

  