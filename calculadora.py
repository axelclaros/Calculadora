import math

from operaciones import (
    suma, resta, multiplicacion, division, potencia, modulo,
    raiz_cuadrada, porcentaje, valor_absoluto, factorial,
    promedio, redondear,
)


def mostrar_menu():
    print("===== CALCULADORA =====")
    print("1.  Suma")
    print("2.  Resta")
    print("3.  Multiplicación")
    print("4.  División")
    print("5.  Potencia")
    print("6.  Módulo")
    print("7.  Raíz cuadrada")
    print("8.  Porcentaje")
    print("9.  Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    print("0.  Salir")


def convertir_numero(texto):
    try:
        numero = float(texto.strip().replace(",", "."))
    except ValueError:
        return None
    if not math.isfinite(numero):
        return None
    return numero


def pedir_numero(mensaje):
    while True:
        numero = convertir_numero(input(mensaje))
        if numero is not None:
            return numero
        print("Entrada no válida: escribe un número (por ejemplo 5 o 3.5)")


def pedir_dos_numeros():
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    return a, b


def pedir_lista_numeros(mensaje):
    while True:
        numeros = [convertir_numero(x) for x in input(mensaje).split()]
        if numeros and None not in numeros:
            return numeros
        print("Entrada no válida: escribe uno o más números separados por espacios")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Hasta luego")
            break

        try:
            if opcion == "1":
                a, b = pedir_dos_numeros()
                print("Resultado:", suma(a, b))
            elif opcion == "2":
                a, b = pedir_dos_numeros()
                print("Resultado:", resta(a, b))
            elif opcion == "3":
                a, b = pedir_dos_numeros()
                print("Resultado:", multiplicacion(a, b))
            elif opcion == "4":
                a, b = pedir_dos_numeros()
                print("Resultado:", division(a, b))
            elif opcion == "5":
                base = pedir_numero("Base: ")
                exponente = pedir_numero("Exponente: ")
                print("Resultado:", potencia(base, exponente))
            elif opcion == "6":
                a, b = pedir_dos_numeros()
                print("Resultado:", modulo(a, b))
            elif opcion == "7":
                numero = pedir_numero("Número: ")
                print("Resultado:", raiz_cuadrada(numero))
            elif opcion == "8":
                porc = pedir_numero("Porcentaje: ")
                cantidad = pedir_numero("Cantidad: ")
                print("Resultado:", porcentaje(porc, cantidad))
            elif opcion == "9":
                numero = pedir_numero("Número: ")
                print("Resultado:", valor_absoluto(numero))
            elif opcion == "10":
                numero = pedir_numero("Número entero: ")
                print("Resultado:", factorial(numero))
            elif opcion == "11":
                numeros = pedir_lista_numeros("Números separados por espacios: ")
                print("Resultado:", promedio(numeros))
            elif opcion == "12":
                numero = pedir_numero("Número: ")
                decimales = pedir_numero("Cantidad de decimales: ")
                print("Resultado:", redondear(numero, decimales))
            else:
                print("Opción no válida")
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print("Error:", error)

        print()


main()