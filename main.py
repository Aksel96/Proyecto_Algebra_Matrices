# Funcion principal que resuelve la matriz por eliminacion de gauss

import numpy as np

def solEcNv(Matriz, ResulMatriz):
    n = len(Matriz)

    # Pivoteo parcial
    for p in range(n):
        max_index = np.argmax(np.abs(Matriz[p:, p])) + p
        Matriz[[p, max_index]] = Matriz[[max_index, p]]
        ResulMatriz[p], ResulMatriz[max_index] = ResulMatriz[max_index], ResulMatriz[p]

        # Verificar si la matriz es singular
        if Matriz[p][p] == 0:
            raise ValueError("La matriz es singular.")

        # Eliminación Gaussiana
        for j in range(p + 1, n):
            valor = -Matriz[j][p] / Matriz[p][p]
            for i in range(p, n):
                Matriz[j][i] = valor * Matriz[p][i] + Matriz[j][i]
            ResulMatriz[j] = valor * ResulMatriz[p] + ResulMatriz[j]

    x = np.zeros(n)

    # Sustitución hacia atrás
    for i in range(n - 1, -1, -1):
        suma = np.dot(Matriz[i][i+1:], x[i+1:])
        x[i] = (ResulMatriz[i] - suma) / Matriz[i][i]

    return list(x)


# Inicio programa
Matriz = []  # Lista que almacenara los valores de antes del igual de la ecuacion
ResulMatriz = []  # Lista que almacenara la parde despues del igual de la ecuacion
valoresApoyo = []  # Lista de apoyo para castear de string a entero los valores

print("-----PROGRAMA QUE RESUELVE ECUACIONES DE N INCOGNITAS-----")
print("---- Introduce los valores separados por un espacio ----")
print("--- Ej: si la ecuacion es 3x + 3y = 2, deberas colocar: \" 3 3 2 \" ")
numIncognitas = int(input("Numero de incongnitas: "))
for j in range(numIncognitas):
    valoresEcuacion = []
    if j < numIncognitas - 1:
        valoresApoyo = input("Valores de la ecuacion {}: ".format(j + 1))
        valores = valoresApoyo.split(" ")  # Aqui hacemos split a los elementos
        for i in range(len(valores)):
            valoresEcuacion.append(int(valores[i]))  # agregamos y Casteamos de string a entero los valores
    else:
        valoresEcuacion = list(map(int, input("Valores de la ecuacion {}: ".format(j + 1)).split()))
    print(valoresEcuacion)
    Matriz.append(valoresEcuacion[0:-1])  # agregamos los valores de los coeficientes
    ResulMatriz.append(valoresEcuacion[-1]) # agregamos los valores del vector de resultados

resultado = solEcNv(Matriz, ResulMatriz)
print("Valor de las incognitas: {} ".format(resultado))
