import numpy as np

# Metodo trdraddicional
my_list = list(range(0, 1))


# generador de elemnetos
my_list_2 = np.arange(0, 10, 2, dtype=np.float64)
print(my_list_2)



# Funcion de NumPy mas usada en el mundo de data scienece

my_list_3 = np.zeros((10, 10)) # creamos la cantidad X de filas y columnas, con valor cero por defecto
print(my_list_3)



# creamos la cantidad X de filas y columnas, con valor 1 por defecto
my_list_4 = np.ones((10, 5))
print(my_list_4)




my_list_5 = np.linspace(0, 10, 50) # Inicio: Fin : Cantidad
print(my_list_5)



# funcion que nos ayuda permite encontrar funcion lineal (algebra)
my_list_6 = np.eye(8) 
print(my_list_6)


my_list_7 = np.random.rand(2,2) # Datos totalmente aleatorios
my_list_7 = np.random.randint(1, 15) # Entero aleatorio
my_list_7 = np.random.randint(1, 15, (10,5)) # Entero aleatorio, con una extructura
print(my_list_7)


