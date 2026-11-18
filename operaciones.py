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

def porcentaje(porcentaje, cantidad):
    return cantidad * porcentaje / 100