"""
Función de test del módulo 3
"""

import os
import pytest
import pandas as pd
from src.ejer3 import minutes_002040, add_time_grouped, create_time_histogram, run

@pytest.fixture
def sample_df():
    '''Definición del dataframe de prueba'''
    data = {
        'dorsal': [1, 2, 3, 4, 5],
        'time': ['06:19:40', '06:29:40', '06:59:40', '07:00:00', '07:15:30']
    }
    return pd.DataFrame(data)

def test_minutes_002040():
    '''Test de timing'''
    test_cases = [
        ('06:19:40', '06:00'),
        ('06:29:40', '06:20'),
        ('06:59:40', '06:40'),
        ('07:00:00', '07:00'),
        ('07:15:30', '07:00'),
        ('07:35:00', '07:20'),
        ('07:55:59', '07:40')
    ]

    for input_time, expected_output in test_cases:
        assert minutes_002040(input_time) == expected_output

def test_add_time_grouped(sample_df):
    '''Test para la columna nueva de tiempos'''
    df_grouped = add_time_grouped(sample_df)

    # Verificar que existe la nueva columna
    assert 'time_grouped' in df_grouped.columns

    # Verificar los valores agrupados
    expected_values = ['06:00', '06:20', '06:40', '07:00', '07:00']
    assert df_grouped['time_grouped'].tolist() == expected_values

    # Verificar que el DataFrame original no se ha modificado
    assert 'time_grouped' not in sample_df.columns

def test_create_time_histogram(sample_df):
    '''Verificar el histograma'''
    df_grouped = add_time_grouped(sample_df)
    grouped_data = create_time_histogram(df_grouped)

    # Verificar que se ha creado el archivo
    assert os.path.exists('img/histograma.png')
    assert os.path.getsize('img/histograma.png') > 0

    # Verificar estructura del DataFrame resultante
    assert 'time_grouped' in grouped_data.columns
    assert 'count' in grouped_data.columns

    # Verificar que los conteos son correctos
    assert grouped_data.loc[grouped_data['time_grouped'] == '07:00', 'count'].iloc[0] == 2

def test_run(capsys):
    '''Test de la función principal'''
    df_grouped = run()
    assert isinstance(df_grouped, pd.DataFrame)
    assert 'time_grouped' in df_grouped.columns
    captured = capsys.readouterr()
    assert "Histograma guardado" in captured.out
