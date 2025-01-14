"""
Función de test del segundo ejercicio
"""

import pytest
import pandas as pd
from src.ejer2 import name_surname, remove_no_participants, get_participant_by_dorsal, run

@pytest.fixture
def sample_df():
    '''Definición del dataframe de prueba'''
    data = {
        'dorsal': [1, 2, 3, 4, 5],
        'biker': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Day'],
        'club': ['Club A', 'Club B', 'Club C', 'Club D', 'Club E'],
        'time': ['1:23:45', '00:00:00', '3:45:67', '00:00:00', '5:67:89']
    }
    return pd.DataFrame(data)

def test_name_surname(sample_df):
    '''Testeo de anonimización'''
    df_anon = name_surname(sample_df)

    # Verificar que los nombres han cambiado
    assert not any(name in df_anon['biker'].values for name in sample_df['biker'].values)

    # Verificar formato de nombres
    assert all(len(name.split()) >= 2 for name in df_anon['biker'])

    # Verificar que el resto de columnas no han cambiado
    for col in ['dorsal', 'club', 'time']:
        assert all(df_anon[col] == sample_df[col])

def test_remove_no_participants(sample_df):
    '''Test de limpieza de tiempo 0'''
    df_clean = remove_no_participants(sample_df)

    # Verificar que se han eliminado los registros con tiempo 00:00:00
    assert len(df_clean) == 3
    assert not any(df_clean['time'] == '00:00:00')

    # Verificar que se mantienen los datos correctos
    assert all(time != '00:00:00' for time in df_clean['time'])

    # Test con DataFrame sin registros a eliminar
    df_no_zeros = df_clean.copy()
    df_clean_2 = remove_no_participants(df_no_zeros)
    assert len(df_clean_2) == len(df_no_zeros)

def test_get_participant_by_dorsal(sample_df):
    '''Tests de existencia'''
    # Test participante existente
    participant = get_participant_by_dorsal(sample_df, 1)
    assert participant['dorsal'] == 1
    assert participant['biker'] == 'John Doe'
    assert participant['club'] == 'Club A'
    assert participant['time'] == '1:23:45'

    # Test dorsal no existente
    with pytest.raises(IndexError):
        get_participant_by_dorsal(sample_df, 999)

def test_run(capsys):
    '''Test de la función principal'''
    df_clean = run()
    assert isinstance(df_clean, pd.DataFrame)
    assert not any(df_clean['time'] == '00:00:00')
    captured = capsys.readouterr()
