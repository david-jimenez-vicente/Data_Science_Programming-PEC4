
"""
Módulo del ejercicio 1. Incuye la función transversal de carga de datos.
"""
import pandas as pd

def load_dataset():
    """
    Carga el dataset desde el archivo CSV
    Returns:
        pandas.DataFrame: DataFrame con los datos de la carrera
    """
    try:
        df1 = pd.read_csv('data/dataset.csv', sep=';')
        return df1
    except FileNotFoundError as exc:
        raise FileNotFoundError("No se encuentra el archivo dataset.csv en la\
        carpeta data/") from exc

def get_num_bikers(datos):
    """
    Obtiene el número total de participantes
    Args:
        datos (pandas.DataFrame): DataFrame con los datos
    Returns:
        int: Número de participantes
    """
    return len(datos)

def get_columns(datos):
    """
    Obtiene los nombres de las columnas del dataset
    Args:
        datos (pandas.DataFrame): DataFrame con los datos
    Returns:
        list: Lista con los nombres de las columnas
    """
    return datos.columns.tolist()

def run():
    """
    Ejecuta el análisis del ejercicio 1 usando las funciones definidas antes
    """

    # Cargamos el dataset
    df1 = load_dataset()

    # Mostramos los primeros 5 registros
    print("Primeros 5 registros:")
    print(df1.head())
    print()

    # Número de participantes
    n_participants = get_num_bikers(df1)
    print(f"Número de participantes: {n_participants}")
    print()

    # Columnas del dataset
    columns = get_columns(df1)
    print("Columnas del dataset:")
    print(columns)

    return df1
