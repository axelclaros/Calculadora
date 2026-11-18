import math

def suma (a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def potencia(b, e):
    if b == 0 and e < 0:
        raise ValueError("No se puede elevar cero a un exponente negativo")
    if b < 0 and e != int(e):
        raise ValueError("No se puede elevar un número negativo a un exponente decimal")
    return b ** e

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
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
    if n > 1000:
        raise ValueError("El número es demasiado grande (máximo 1000)")
    return math.factorial(int(n))

def promedio(n):
    if len(n) == 0:
        raise ValueError("No se puede calcular el promedio de una lista vacía")
    return sum(n) / len(n)

def redondear(n, d):
    if d < 0 or d != int(d):
        raise ValueError("Los decimales deben ser un entero no negativo")
    return round(n, int(d))

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b