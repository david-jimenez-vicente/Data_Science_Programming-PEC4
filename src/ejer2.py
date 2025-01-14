"""
Módulo para el ejercicio 2
"""
import pandas as pd
from faker import Faker
from src.ejer1 import load_dataset

def name_surname(df2):
    """
    Anonimiza los nombres de los ciclistas usando Faker
    Args:
        df2 (pandas.DataFrame): DataFrame original
    Returns:
        pandas.DataFrame: DataFrame con nombres anonimizados
    """
    fake = Faker()
    df2 = df2.copy()
    df2['biker'] = [fake.name() for _ in range(len(df2))]
    return df2

def remove_no_participants(df2):
    """
    Elimina los participantes con tiempo 00:00:00
    Args:
        df2 (pandas.DataFrame): DataFrame original
    Returns:
        pandas.DataFrame: DataFrame sin los no participantes
    """
    return df2[df2['time'] != '00:00:00'].copy()

def get_participant_by_dorsal(df2, dorsal):
    """
    Obtiene los datos de un participante por su dorsal
    Args:
        df2 (pandas.DataFrame): DataFrame con los datos
        dorsal (int): Número de dorsal
    Returns:
        pandas.Series: Datos del participante
    """
    return df2[df2['dorsal'] == dorsal].iloc[0]

def run():
    """
    Ejecuación principal del módulo 2
    """
    print("\n=== Ejercicio 2: Anonimización y limpieza ===\n")

    # Cargamos el dataset original
    df2 = load_dataset()

    # Anonimizar nombres
    df2_anon = name_surname(df2)
    print("Primeros 5 registros con nombres anonimizados:")
    print(df2_anon.head())
    print()

    # Eliminamos no participantes
    df2_clean = remove_no_participants(df2_anon)
    print(f"Número de participantes después de limpieza: {len(df2_clean)}")
    print("\nPrimeros 5 registros después de limpieza:")
    print(df2_clean.head())
    print()

    # Sacamos participante con dorsal 1000
    participant_1000 = get_participant_by_dorsal(df2_clean, 1000)
    print("\nDatos del participante con dorsal 1000:")
    print(participant_1000)

    df2_clean.to_csv("./dataframes/dataframe2.csv", index=False)

    return df2_clean
