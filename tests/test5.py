"""
Test del ejercicio 5
"""
import pytest
import pandas as pd
from src.ejer5 import get_ucsc_cyclists, get_best_ucsc_cyclist, run

@pytest.fixture
def sample_df():
    '''Creación del dataframe de prueba'''
    data = {
        'dorsal': [1, 2, 3, 4, 5, 6],
        'biker': [f'Biker{i}' for i in range(1, 7)],
        'club_clean': ['UCSC', 'TEST', 'UCSC', 'TEST', 'UCSC', 'EXAMPLE'],
        'time_grouped': ['1:23:45', '1:20:00', '1:30:00', '1:40:00', '1:25:00', '1:35:00']
    }
    return pd.DataFrame(data)

def test_get_ucsc_cyclists(sample_df):
    '''Prueba del test de UCSC'''
    ucsc_df = get_ucsc_cyclists(sample_df)

    # Verificar que solo hay ciclistas de UCSC
    assert len(ucsc_df) == 3
    assert all(ucsc_df['club_clean'] == 'UCSC')

    # Verificar que están todos los datos
    assert set(ucsc_df['dorsal']) == {1, 3, 5}
    assert set(ucsc_df['time_grouped']) == {'1:23:45', '1:30:00', '1:25:00'}

    # Test con DataFrame sin ciclistas UCSC
    df_no_ucsc = sample_df.replace('UCSC', 'OTHER')
    assert len(get_ucsc_cyclists(df_no_ucsc)) == 0

def test_get_best_ucsc_cyclist(sample_df):
    '''Prueba del mejor del club'''
    best_cyclist, position, percentage = get_best_ucsc_cyclist(sample_df)

    # Verificar mejor ciclista
    assert best_cyclist['dorsal'] == 1
    assert best_cyclist['time_grouped'] == '1:23:45'

    # Verificar posición
    assert position == 2  # Segundo en la general

    # Verificar porcentaje
    expected_percentage = (2 / len(sample_df)) * 100
    assert percentage == expected_percentage

    # Test con diferentes ordenaciones
    df_modified = sample_df.copy()
    df_modified.loc[df_modified['dorsal'] == 1, 'time_grouped'] = '0:59:59'
    best_cyclist_mod, position_mod, percentage_mod = get_best_ucsc_cyclist(df_modified)
    assert position_mod == 1  # Ahora es primero
    assert percentage_mod == (1 / len(df_modified)) * 100

def test_run(capsys):
    '''Test del proceso principal'''
    ucsc_cyclists, best_cyclist, position, percentage = run()

    assert isinstance(ucsc_cyclists, pd.DataFrame)
    assert isinstance(best_cyclist, pd.Series)
    assert isinstance(position, int)
    assert isinstance(percentage, float)

    captured = capsys.readouterr()
    assert "Mejor ciclista de la UCSC" in captured.out
    assert "Posición en la clasificación general" in captured.out
