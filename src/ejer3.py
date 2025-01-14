"""
Módulo para el ejercicio 3
"""
import pandas as pd
import matplotlib.pyplot as plt

def minutes_002040(time_str):
    """
    Agrupa los minutos en franjas de 20 min (00, 20, 40)
    Args:
        time_str (str): Tiempo en formato 'hh:mm:ss'
    Returns:
        str: Tiempo agrupado en formato 'hh:mm'
    """
    hours, minutes, _ = map(int, time_str.split(':'))

    if minutes < 20:
        grouped_minutes = 0
    elif minutes < 40:
        grouped_minutes = 20
    else:
        grouped_minutes = 40

    return f"{hours:02d}:{grouped_minutes:02d}"

def add_time_grouped(df3):
    """
    Añade una columna con los tiempos agrupados
    Args:
        df3 (pandas.DataFrame): DataFrame original
    Returns:
        pandas.DataFrame: DataFrame con la nueva columna time_grouped
    """
    df3 = df3.copy()
    df3['time_grouped'] = df3['time'].apply(minutes_002040)
    return df3

def create_time_histogram(df3):
    """
    Crea el histograma de tiempos agrupados
    Args:
        df3 (pandas.DataFrame): DataFrame con columna time_grouped
    Returns:
        pandas.DataFrame: DataFrame con el conteo por grupos de tiempo
    """
    grouped_df3 = df3.groupby('time_grouped').size().reset_index(name='count')
    grouped_df3 = grouped_df3.sort_values('time_grouped')

    plt.figure(figsize=(15, 6))
    plt.bar(grouped_df3['time_grouped'], grouped_df3['count'])
    plt.xlabel('Tiempo (hh:mm)')
    plt.ylabel('Número de ciclistas')
    plt.title('Distribución de tiempos en la Orbea Monegros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('img/histograma.png')
    plt.close()

    return grouped_df3

def run():
    """Ejecuta el ejercicio 3"""
    print("\n\n\n============= Ejercicio 3: Agrupamiento de minutos e histograma\
     =============\n")

    # Obtenemos DataFrame limpio del ejercicio anterior
    df3 = pd.read_csv("./dataframes/dataframe2.csv")

    # Añadimos la columna de tiempos agrupados
    df3_grouped = add_time_grouped(df3)
    print("15 primeros registros con tiempos agrupados:")
    print(df3_grouped.head(15))
    print()

    # Creamos el histograma y obtenemos datos agrupados
    grouped_data = create_time_histogram(df3_grouped)
    print("Distribución de tiempos agrupados:")
    print(grouped_data)
    print("\nHistograma guardado en img/histograma.png")

    df3_grouped.to_csv("./dataframes/dataframe3.csv", index=False)

    return df3_grouped
