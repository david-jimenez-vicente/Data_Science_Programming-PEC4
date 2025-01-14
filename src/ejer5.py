"""
Módulo para el ejercicio 5
"""

import pandas as pd

def get_ucsc_cyclists(df5):
    """
    Obtiene los ciclistas de la UCSC

    Args:
        df5 (pandas.DataFrame): DataFrame con los datos y clubs limpios

    Returns:
        pandas.DataFrame: DataFrame con los ciclistas de la UCSC
    """
    return df5[df5['club_clean'] == 'UCSC'].copy()

def get_best_ucsc_cyclist(df5):
    """
    Obtiene el mejor ciclista de la UCSC y su posición en la clasificación general
    Args:
        df5 (pandas.DataFrame): DataFrame con los datos
    Returns:
        tuple: (pandas.Series, int, float) - Mejor ciclista, posición y porcentaje
    """
    # Obtenemos solo los ciclistas de la UCSC
    ucsc_cyclists = df5[df5['club_clean'] == 'UCSC']

    # Ordenamos por tiempo
    df5_sorted = df5.sort_values('time_grouped')

    # Obtenemos el mejor de la UCSC
    best_ucsc = ucsc_cyclists.sort_values('time_grouped').iloc[0]

    # Calculamos su posición en la general
    position = df5_sorted.index.get_loc(best_ucsc.name) + 1

    # Calculamos el porcentaje
    percentage = (position / len(df5)) * 100

    return best_ucsc, int(position), percentage  # Convertimos position a int

def run():
    """Ejecuta el análisis del ejercicio 5"""

    # Obtenemos el DataFrame del ejercicio anterior
    df5 = pd.read_csv("./dataframes/dataframe4.csv")

    # Obtenemos los ciclistas de UCSC
    ucsc_cyclists = get_ucsc_cyclists(df5).reset_index()
    print("Ciclistas de la UCSC:")
    print(ucsc_cyclists[['biker', 'time_grouped', 'dorsal']])
    print()

    # Obtenemos el mejor ciclista de UCSC
    best_cyclist, position, percentage = get_best_ucsc_cyclist(df5)
    print("Mejor ciclista de la UCSC:")
    print(best_cyclist)
    print(f"\nPosición en la clasificación general: {position}")
    print(f"Porcentaje sobre el total: {percentage:.2f}%")

    return ucsc_cyclists, best_cyclist, position, percentage
