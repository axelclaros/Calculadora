import math

from operaciones import (
    suma, resta, multiplicacion, division, potencia, modulo,
    raiz_cuadrada, porcentaje, valor_absoluto, factorial,
    promedio, redondear, seno, coseno, tangente, ln, log10,
)

hist = []


def menu():
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
    print("13. Ver historial")
    print("14. Limpiar historial")
    print("15. Seno")
    print("16. Coseno")
    print("17. Tangente")
    print("18. Logaritmo natural")
    print("19. Logaritmo base 10")
    print("0.  Salir")


def conv(t):
    try:
        n = float(t.strip().replace(",", "."))
    except ValueError:
        return None
    if not math.isfinite(n):
        return None
    return n


def pedir(m):
    while True:
        n = conv(input(m))
        if n is not None:
            return n
        print("Entrada no válida: escribe un número (por ejemplo 5 o 3.5)")


def pedir2():
    a = pedir("Primer número: ")
    b = pedir("Segundo número: ")
    return a, b


def pedir_lista(m):
    while True:
        ns = [conv(x) for x in input(m).split()]
        if ns and None not in ns:
            return ns
        print("Entrada no válida: escribe uno o más números separados por espacios")


def reg(d, r):
    print("Resultado:", r)
    hist.append(f"{d} = {r}")


def ver_hist():
    print("===== HISTORIAL =====")
    if len(hist) == 0:
        print("Todavía no hay operaciones en el historial")
    else:
        for i, o in enumerate(hist, start=1):
            print(f"{i}. {o}")


def limpiar_hist():
    if len(hist) == 0:
        print("El historial ya está vacío")
    else:
        hist.clear()
        print("Historial borrado")


def main():
    while True:
        menu()
        op = input("Elige una opción: ")

        if op == "0":
            print("Hasta luego")
            break

        try:
            if op == "1":
                a, b = pedir2()
                reg(f"{a} + {b}", suma(a, b))
            elif op == "2":
                a, b = pedir2()
                reg(f"{a} - {b}", resta(a, b))
            elif op == "3":
                a, b = pedir2()
                reg(f"{a} * {b}", multiplicacion(a, b))
            elif op == "4":
                a, b = pedir2()
                reg(f"{a} / {b}", division(a, b))
            elif op == "5":
                b = pedir("Base: ")
                e = pedir("Exponente: ")
                reg(f"{b} ^ {e}", potencia(b, e))
            elif op == "6":
                a, b = pedir2()
                reg(f"{a} % {b}", modulo(a, b))
            elif op == "7":
                n = pedir("Número: ")
                reg(f"raíz cuadrada de {n}", raiz_cuadrada(n))
            elif op == "8":
                p = pedir("Porcentaje: ")
                c = pedir("Cantidad: ")
                reg(f"{p}% de {c}", porcentaje(p, c))
            elif op == "9":
                n = pedir("Número: ")
                reg(f"valor absoluto de {n}", valor_absoluto(n))
            elif op == "10":
                n = pedir("Número entero: ")
                reg(f"factorial de {n}", factorial(n))
            elif op == "11":
                ns = pedir_lista("Números separados por espacios: ")
                reg(f"promedio de {ns}", promedio(ns))
            elif op == "12":
                n = pedir("Número: ")
                d = pedir("Cantidad de decimales: ")
                reg(f"{n} redondeado a {d} decimales", redondear(n, d))
            elif op == "13":
                ver_hist()
            elif op == "14":
                limpiar_hist()
            elif op == "15":
                g = pedir("Ángulo en grados: ")
                reg(f"seno de {g}°", seno(g))
            elif op == "16":
                g = pedir("Ángulo en grados: ")
                reg(f"coseno de {g}°", coseno(g))
            elif op == "17":
                g = pedir("Ángulo en grados: ")
                reg(f"tangente de {g}°", tangente(g))
            elif op == "18":
                n = pedir("Número: ")
                reg(f"logaritmo natural de {n}", ln(n))
            elif op == "19":
                n = pedir("Número: ")
                reg(f"logaritmo base 10 de {n}", log10(n))
            else:
                print("Opción no válida")
        except (ValueError, ZeroDivisionError, OverflowError) as err:
            print("Error:", err)

        print()


main()