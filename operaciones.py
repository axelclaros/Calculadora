import math

def suma (a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def potencia(b, e):
    return b ** e

def modulo(a, b):
    return a % b

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(n)

def porcentaje(p, c):
    return c * p / 100

def valor_absoluto(n):
    return abs(n)

def factorial(n):
    if n < 0 or n != int(n):
        raise ValueError("El factorial solo se calcula para enteros no negativos")
    return math.factorial(int(n))