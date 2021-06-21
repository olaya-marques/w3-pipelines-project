def isnull(x):
    """ Esta función muestra la suma de todos los NaNs ordenados de mayor a menor"""
    return x.isnull().sum().sort_values(ascending = False)

def comprobacion_duplicados (x):
     """ Esta función muestra el número de datos repetidos"""
    repetidos = list(unique_everseen(duplicates(x)))
    return len(repetidos)

