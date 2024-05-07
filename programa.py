# 1 Escribe un programa en Python que imprima tu nombre en la pantalla.
def imprimir_nombre(nombre):
        # Aquí se imprime el nombre en la pantalla
        print("Mi nombre es: ",nombre);
    # if __name__ == "__main__":
        imprimir_nombre("Santiago")
    # Se llama a la función imprimir_nombre() para ejecutarla

# 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
        # Se utiliza la función sum() para calcular la suma del rango del 1 al 10
        suma = 0
        for i in range(1, 11):
            suma += i
        return suma 
        total = suma_1_al_10()
        print("Suma total del 1 al 10 es ",total)


# # 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura): 
        print("Hi ",nombre," tienes ",edad,"años y tu estatura es de ",estatura)

imprimir_datos_personales("Santy",30,1.70)

# # 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
# Se verifica si el número es divisible por 2
    # Si es divisible, se devuelve "par"
#     else:
#         # Si no es divisible, se devuelve "impar"

def par_o_impar(numero):
    if numero % 2  == 0:
        print("Par")
    else:
        print("Impar")
num = int(input("Ingrese numero: "))
par_o_impar(num)

    
# if __name__ == "__main__":
#     num = int(input("Ingrese un número: "))  # Se solicita al usuario que ingrese un número
#     print(par_o_impar(num))  # Se imprime si el número ingresado es par o impar

# # 5 Crea una función que calcule el área de un círculo dado su radio.
# import math
import math
def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    # Se devuelve el área calculada
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    # Se imprime el área calculada del círculo


# # 6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(a, b):
# Se devuelve la suma de los dos números recibidos como argumentos
        sum = a 
        print("La suma es:", sum)  # Se imprime la suma de los dos números ingresados

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma(num1,num2)

# # 7 Modifica la función que calcula el área del círculo para que reciba el radio como parámetro.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    # Se devuelve el área calculada

radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
print("El área del círculo es:", area_circulo(radio))  # Se imprime el área calculada del círculo

#  # 8 Diseña un programa que convierta grados Celsius a Fahrenheit y viceversa, utilizando funciones para realizar los cálculos.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Se aplica la fórmula de conversión de Celsius a Fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
    
celsius = float(input("Ingrese la temperatura en grados celsius: "))
print("Temperatura en Fahrenheit: ", celsius_a_fahrenheit(celsius))

fahrenheit = float(input("Ingrese el valor Fahrenheit: "))
print("Temperatura en Celsius:",fahrenheit_a_celsius(fahrenheit) )  
# Se imprime la temperatura convertida a grados Celsius