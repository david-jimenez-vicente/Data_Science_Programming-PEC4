"""
Módulo para el ejercicio 4
"""

import re #Para usar expresiones regulares
import pandas as pd

def clean_club(club_name):
    """
    Limpia el nombre del club siguiendo las reglas especificadas
    Args:
        club_name (str): Nombre original del club
    Returns:
        str: Nombre del club limpio
    """
    # Manejamos casos de Nans y strings vacíos
    if pd.isna(club_name) or str(club_name).strip() == '':
        return "INDEPENDIENTE"

    # Convertir a mayúsculas
    club = str(club_name).upper()

    # Lista de prefijos a eliminar completamente
    prefixes = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ',
        'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
        'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
        'CLUB CICLISTA ', 'CLUB '
    ]

    # Lista de prefijos con punto que deben estar al inicio
    prefix_patterns = [
        r'^(C\.C\. |C\.C |CC |C\.D\. |C\.D |CD |A\.C\. |A\.C |AC |'
        r'A\.D\. |A\.D |AD |A\.E\. |A\.E |AE |E\.C\. |E\.C |EC |'
        r'S\.C\. |S\.C |SC |S\.D\. |S\.D |SD )'
    ]

    # Lista de sufijos con punto que deben estar al final
    suffix_patterns = [
        r'( T\.T\.| T\.T| TT| T\.E\.| T\.E| TE| C\.C\.| C\.C| CC|'
        r' C\.D\.| C\.D| CD| A\.D\.| A\.D| AD| A\.C\.| A\.C| AC)$'
    ]

    # Eliminamos prefijos completos
    for prefix in prefixes:
        club = club.replace(prefix, '')

    # Eliminamos prefijos con punto al inicio
    for pattern in prefix_patterns:
        club = re.sub(pattern, '', club)

    # Eliminamos sufijos con punto al final
    for pattern in suffix_patterns:
        club = re.sub(pattern, '', club)

    # Eliminamos espacios en blanco al inicio y final
    club = club.strip()

    # Si después de todas las limpiezas queda vacío, devolver INDEPENDIENTE
    return "INDEPENDIENTE" if club == '' else club

def analyze_clubs(df4):
    """
    Analiza los clubs y crea un nuevo dataframe con el conteo de ciclistas por club
    Args:
        df4 (pandas.DataFrame): DataFrame con los datos
    Returns:
        pandas.DataFrame: DataFrame con el análisis de clubs
    """
    df4 = df4.copy()
    # Creamos una columna con clubs limpios
    df4['club_clean'] = df4['club'].apply(clean_club)

    # Agrupamos por club y contamos los ciclistas
    clubs_df4 = df4.groupby('club_clean').size().reset_index(name='participants')
    clubs_df4 = clubs_df4.sort_values('participants', ascending=False)

    return df4, clubs_df4

def run():
    """Ejecuta el análisis del ejercicio 4"""

    # Obtenemos el DataFrame del ejercicio anterior
    df4 = pd.read_csv("./dataframes/dataframe3.csv")

    # Analizamos los clubs
    df4_with_clean_clubs, clubs_analysis = analyze_clubs(df4)

    print("15 primeros registros con clubs limpios:")
    print(df4_with_clean_clubs[['biker', 'club', 'club_clean', 'time_grouped']].head(15))
    print("\nClubs ordenados por número de participantes:")
    print(clubs_analysis)

    df4_with_clean_clubs.to_csv("./dataframes/dataframe4.csv", index=False)

    return df4_with_clean_clubs, clubs_analysis
