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


def pedir_numero(mensaje):
    return float(input(mensaje))


def pedir_dos_numeros():
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    return a, b


def main():
    mostrar_menu()
    opcion = input("Elige una opción: ")

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
            texto = input("Números separados por espacios: ")
            numeros = [float(x) for x in texto.split()]
            print("Resultado:", promedio(numeros))
        elif opcion == "12":
            numero = pedir_numero("Número: ")
            decimales = pedir_numero("Cantidad de decimales: ")
            print("Resultado:", redondear(numero, decimales))
        elif opcion == "0":
            print("Hasta luego")
        else:
            print("Opción no válida")
    except ValueError as error:
        print("Error:", error)


main()