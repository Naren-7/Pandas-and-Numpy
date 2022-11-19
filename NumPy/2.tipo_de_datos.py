import numpy as np

arr = np.array([1, 3, 4, 5, 7])
#arr = np.array(["2", "3", "4", "5"])

# Tipo de datos
print(arr.dtype)



arr = np.array([1, 3, 4, 5, 7], dtype="float64")
#arr = np.array(["2", "3", "4", "5"])

print(arr.dtype)



# ---- cambiando tipo de datos ----------

# booleanos
arr = np.arange(0,10) # crea un rango de numeros
arr = arr.astype(np.bool_)
print(f"{arr} -> booleano\n")


# String
arr = arr.astype(np.string_)
print(f"{arr} -> tip stirng\n")



# Enteros
arr = np.array(['1', '2', '3', '4', '7' ])
arr = arr.astype(np.int64) 
print(f"{arr} -> Enteros\n")





# float 
arr = arr.astype(np.float64)
print(f"{arr} -> float")

