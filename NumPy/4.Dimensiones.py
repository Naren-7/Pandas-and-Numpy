
import numpy as np

scalar = np.array(65)
print(scalar)

# Numeroos de dimensiones. atributo -> ndim
print(scalar.ndim, "numeor de dimensiones")


# vector
vector = np.array([1, 3, 6, 8])
print(f"{vector.ndim} -> cantidad de dimensiones")


# matriz
matriz = np.array([[1, 3, 6, 8],[5, 4, 98, 87 ]])
print(f"{matriz.ndim} -> cantidad de dimensiones")


# tensor
tensor = np.array([ [ [1, 3, 4, 5], [6, 7, 8, 9 ] ], [ [6, 7, 8, 9 ], [10, 11, 12, 13 ] ]  ])
print(f"{tensor.ndim} -> cantidad de dimensiones")



# ----------- Agregar dimensiones -----------------

vector = np.array([1, 3, 6, 8], ndmin=10)
print(vector)
print(f"{vector.ndim} -> cantidad de dimensiones")




# ---------------Expandir una dimension-------------------------------
expand = np.expand_dims(np.array([1, 3, 6, 8]), axis = 0 )

# axis = 0 -> hace referencia a las filas. ( python and NumPy)

# axis = 1 -> hace referencia a las columnas.

print(expand)
print(f"{expand.ndim} -> cantidad de dimensiones")





# ---------- Eliminando dimensiones -----------

print(vector, vector.ndim)

vector_2 = np.squeeze(vector)

print(vector_2, vector_2.ndim)