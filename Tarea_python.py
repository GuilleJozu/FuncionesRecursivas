print("Ejercicio 1")
def reverse_string(string):
    return ''.join(reversed(string))

print(reverse_string("Buenas"))

print("Ejercicio 2")
def fibonacci(n):
    x, y = 0,1
    while x < n:
        print(x, end=" ")
        x, y = y, x + y
m = int(input("Ingresa el limite de fibonacci: "))     
fibonacci(m)
print(" ")


print("Ejercicio 3")

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

numero = int(input("Escriba un numero"))
numero_invertido = invertir_numero(numero)
print("El número es: ")
print(numero)
print("El número al invertirse es: ")
print(numero_invertido)


print("Ejercicio 4")
def potencia(numero, exponente):
    numerado = 1
    elevado = 1
    while numerado <= exponente:
        elevado = elevado * numero
        numerado = numerado + 1
    return elevado
a = int(input("escriba la base: "))
b = int(input("escriba la potencia: "))
print(f"El resultado es: {potencia(a, b)}")


print("Ejecicio 5")

suma, numero = 0, 0

serie_de_numeros = int(input("Ingrese una serie de numero: "))

while serie_de_numeros != 0:
    numero = serie_de_numeros % 10
    serie_de_numeros = serie_de_numeros // 10
    suma = suma + numero

print("La suma de la serie es: ")
print("{}".format(suma))

print ("Ejercicio 6")

def palindromo(palabra):
    if len(palabra) < 1:
        return ("Es palindroma")
    else: 
        if palabra[0] == palabra [-1]:
            return palindromo(palabra[1:-1])
        else:
         return ("No es palindroma")
palabra= str (input("ingrese una palabra: "))
print("La palabra es palindroma?", palindromo(palabra))

print("Ejercicio 7")
def sumarNumeros(numeros):
    if len (numeros) == 0:
        return 0 
    else:
        return numeros[0] + sumarNumeros(numeros[1:])
valores=[1,2,3,4,5,6]
resultado = sumarNumeros(valores)
print("El resultado es ", resultado)

print("Ejercicio 8")
def sumarNumeros(numeros):
    if len (numeros) == 0:
        return 0 
    else:
        return numeros[0] + sumarNumeros(numeros[1:])
valores=[2,4,6,8,10]
resultado = sumarNumeros(valores)
print("El resultado es ", resultado)

print("Ejercicio 9")
entrada= input("Ingrese el numero binario: ")
cadena = entrada [::-1]
salida = 0; expon = 0

while expon < len(cadena):
    if int(cadena[expon]) == 1:
        salida += int(cadena[expon]) * 2 ** expon
    expon +=1    
print("el resultado es: ", salida)    

print("Ejercicio 10")

import random as rd
n=rd.randint(1,7)
print(n)