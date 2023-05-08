#   AKSEL VILLELA ANDRADE
#   FES ARAGON
#   ICO
#   ALGEBRA LINEAL
#   PROYECTO FINAL
#   MAYO 2023
def producto_matriz(matrizUno, matrizDos):
    pass


def resta_matriz(matrizUno, MatrizDos):
    pass


def suma_matriz(matrizUno, MatrizDos):
    pass


def determinante_matriz(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for j in range(n):
            signo = (-1) ** j
            submatriz = [[matriz[i][k] for k in range(n) if k != j] for i in range(1, n)]
            det += signo * matriz[0][j] * determinante_matriz(submatriz)
        return det


def sistema_N_Dimensiones(matrizNDim, vectorResultados):
    n = len(matrizNDim)
    for p in range(n - 1):
        for j in range(p + 1, n):
            valor = -matrizNDim[j][p] / matrizNDim[p][p]
            for i in range(n):
                matrizNDim[j][i] = valor * matrizNDim[p][i] + matrizNDim[j][i]
            vectorResultados[j] = valor * vectorResultados[p] + vectorResultados[j]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(matrizNDim[i][j] * x[j] for j in range(i, n))
        x[i] = (vectorResultados[i] - suma) / matrizNDim[i][i]

    return list(x)


def llenado_matriz(opcion, numFil=0):
    matriz = []
    matrizNDim = []
    vectorResultados = []
    for i in range(numFil):
        valMatriz = []
        if i == 0:
            print("----    Introduce los valores separados por un espacio")
            print("----    Ej: \" 3 3 2 \"")
        if opcion == "E" and i == 0:
            print("----    Ej: Si la ecuacion es 3x + 1y - 4z = 7, deberas colocar: \" 3 1 -4 7 \"")
        valUsuario = input("Valores de la fila {}: ".format(i + 1))
        valFila = valUsuario.split(" ")
        for j in range(len(valFila)):
            valMatriz.append(int(valFila[j]))
        matriz.append(valMatriz)
        if opcion == "E":
            matrizNDim.append(valMatriz[0:-1])
            vectorResultados.append(valMatriz[-1])
    if opcion == "E":
        return matrizNDim, vectorResultados
    else:
        return matriz


def menu():
    print("-------------------------------------------------------")
    print("PROGRAMA GENERAL DE OPERACIONES CON MATRICES")
    print("-------------------------------------------------------")
    print("Menu de opciones:")
    print("\tA) PRODUCTO de Dos Matrices")
    print("\tB) RESTA de Dos Matrices")
    print("\tC) SUMA de Dos Matrices")
    print("\tD) DETERMINATE de una Matriz")
    print("\tE) Solucion de Sistema de Ecuaciones de N Dimensiones")
    print("\tS) SALIR")
    print("-------------------------------------------------------")


def opcion_menu(opcion):
    match opcion:
        case "A":
            print("A")
        case "B":
            print("B")
        case "C":
            pass
        case "D":
            print("Obtencion del Determinante de una matriz")
            numFilas = int(input("Introduce el numero de filas que tiene la Matriz: "))
            matriz = llenado_matriz("D", numFilas)
            determinante = determinante_matriz(matriz)
            print("El determinante de la matriz {} es: {}".format(matriz, determinante))

        case "E":
            print("Solucion de un sistema de ecuaciones de N dimensiones")
            numFilas = int(input("Introduce el numero de filas que tiene la Matriz: "))
            matriz, vector_resultados = llenado_matriz("E", numFilas)
            print("Matriz: {}".format(matriz))
            print("Vector: {}".format(vector_resultados))
            resultado = sistema_N_Dimensiones(matriz, vector_resultados)
            print("El valor de las incognitas en orden es el siguiente: {}".format(resultado))

        case "S":
            print("Adios...")
        case other:
            print("Opcion no valida :/")


def main():
    menu()
    opcion = input("Introduce la opcion: ")
    opcion_menu(opcion.upper())


if __name__ == '__main__':
    main()
