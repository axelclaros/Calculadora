# Calculadora Científica

## Descripción

Calculadora por consola hecha en Python. Permite realizar operaciones matemáticas desde un menú, controla los datos mal escritos para que el programa no falle y guarda un historial de las operaciones mientras está abierto.

Fue desarrollada como proyecto de práctica por estudiantes de la FNI (Ingeniería de Sistemas e Ingeniería Informática) y se fue ampliando con nuevas funcionalidades, incluyendo operaciones científicas como trigonometría y logaritmos.

## Operaciones y estados

### Funcionalidades de la práctica

| N.º | Funcionalidad | Descripción | Estado |
|----|---------------|-------------|--------|
| 1 | Potencia | Base elevada a un exponente | Completada |
| 2 | Módulo | Residuo de una división | Completada |
| 3 | Raíz cuadrada | Raíz de un número (no acepta negativos) | Completada |
| 4 | Porcentaje | Porcentaje de una cantidad | Completada |
| 5 | Valor absoluto | Número sin su signo | Completada |
| 6 | Factorial | Factorial de un entero no negativo | Completada |
| 7 | Promedio | Promedio de varios números | Completada |
| 8 | Redondeo | Redondea a los decimales indicados | Completada |
| 9 | Validación de entradas | Controla datos no numéricos | Completada |
| 10 | División por cero | Evita dividir y calcular módulo con divisor cero | Completada |
| 11 | Mejorar el menú | Menú claro con todas las operaciones | Completada |
| 12 | Repetir operaciones | Varias operaciones sin reiniciar | Completada |
| 13 | Historial de operaciones | Guarda y muestra las operaciones realizadas | Completada |
| 14 | Limpiar historial | Borra el historial | Completada |
| 15 | Mejorar documentación | README con ejemplos de uso | Completada |

### Funciones extra (ampliación propia)

| Funcionalidad | Descripción | Estado |
|---------------|-------------|--------|
| Seno, coseno y tangente | Funciones trigonométricas con el ángulo en grados | Completada |
| Logaritmo | Logaritmo natural y logaritmo en base 10 | Completada |
| MCD y MCM | Máximo común divisor y mínimo común múltiplo | Completada |

Además, el programa incluye suma, resta, multiplicación y división.

## Menú

```
===== CALCULADORA =====
1.  Suma
2.  Resta
3.  Multiplicación
4.  División
5.  Potencia
6.  Módulo
7.  Raíz cuadrada
8.  Porcentaje
9.  Valor absoluto
10. Factorial
11. Promedio
12. Redondeo
13. Ver historial
14. Limpiar historial
15. Seno
16. Coseno
17. Tangente
18. Logaritmo natural
19. Logaritmo base 10
20. MCD
21. MCM
0.  Salir
```

## Ejemplos de uso

**Porcentaje** (15 % de 200):

```
Elige una opción: 8
Porcentaje: 15
Cantidad: 200
Resultado: 30.0
```

**Promedio** de varios números:

```
Elige una opción: 11
Números separados por espacios: 4 8 6
Resultado: 6.0
```

**Seno** de un ángulo en grados:

```
Elige una opción: 15
Ángulo en grados: 30
Resultado: 0.5
```

**Logaritmo base 10:**

```
Elige una opción: 19
Número: 1000
Resultado: 3.0
```

**MCD** de dos números:

```
Elige una opción: 20
Primer número: 12
Segundo número: 18
Resultado: 6
```

**División entre cero** (el programa avisa y no se cierra):

```
Elige una opción: 4
Primer número: 5
Segundo número: 0
Error: No se puede dividir entre cero
```

**Entrada no válida** (vuelve a pedir el dato):

```
Elige una opción: 1
Primer número: abc
Entrada no válida: escribe un número (por ejemplo 5 o 3.5)
Primer número: 5
```

**Historial:**

```
Elige una opción: 13
===== HISTORIAL =====
1. seno de 30.0° = 0.5
2. MCD de 12.0 y 18.0 = 6
```

## Tecnologías

- Python 3
- Git
- GitHub (Issues para organizar las tareas)
- Markdown
- Visual Studio Code
- Git Bash

## Instalación y ejecución

1. Instalar [Python 3](https://www.python.org/downloads/) (marcando la opción **Add python.exe to PATH**).
2. Clonar el repositorio:

```bash
git clone https://github.com/axelclaros/Calculadora.git
```

3. Entrar a la carpeta del proyecto:

```bash
cd Calculadora
```

4. Ejecutar el programa:

```bash
python calculadora.py
```

5. Elegir una opción del menú, escribir los datos que pida y ver el resultado.

## Estructura del proyecto

```
Calculadora/
├── README.md
├── calculadora.py    # menú e interacción con el usuario
└── operaciones.py    # funciones matemáticas
```

## Autor

**Claros Cossio Axel Jair**