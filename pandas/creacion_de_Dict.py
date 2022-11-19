import pandas as pd


# genera lista con keys: 'A', 'B', 'C', 'D'

keys = list('ABCD')  

# values será un list comprehension que contendrá una lista de listas:
# ['A0', 'A1', ..., 'A3'], ['B0', 'B1', ..., 'B3'], ...
# es un list comprehension anidado

values = [ 
            # list comprehension anidado
            # crea una lista del tipo: ['A0', 'A1', ..., 'A3']
            
            [f'{letter}{number}' for number in range(4)] 
                            # para las letras A, B, C, D, E, F
                                                         for letter in list('ABCDEF')
         
         
         ]

df3 = pd.DataFrame(
    # dictionary comprehension:
    # uso zip para crear tuplas de dos elementos que suministren
    # pares de valores k:v al diccionario
    {k:v for k,v  in zip(keys, values)}
)

#print([values[0]])