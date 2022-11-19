import numpy as np

lista = [1, 2 , 3, 4, 5, 6, 7, 8, 9]

arr = np.array(lista)
#type(arr)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz de 3 dimenciones
matriz = np.array(matriz)

print(matriz[1,1]) # NumPay: antes de la coma hace referencia a las filas despues columnas

print(matriz[0:2,1:3],) #primero las dos primeras filas con la columna 1 a la 3



