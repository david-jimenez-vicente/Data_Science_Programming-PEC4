"""
Test para el ejercicio 1
"""
import pytest
import pandas as pd
from src.ejer1 import load_dataset, get_num_bikers, get_columns, run

#Equivalente a @classmethod con setUpClass de unittest:
@pytest.fixture
def sample_df():
    ''' Crea el dataframe de prueba para todo el test '''
    data = {
        'dorsal': [1, 2, 3, 4, 5],
        'biker': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown',
        'Charlie Day'],
        'club': ['Club A', 'Club B', 'Club C', 'Club D', 'Club E'],
        'time': ['1:23:45', '2:34:56', '3:45:67', '4:56:78', '5:67:89']
    }
    return pd.DataFrame(data)

def test_load_dataset():
    '''Carga el dataset de prueba '''
    df = load_dataset()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert all(col in df.columns for col in ['dorsal', 'biker', 'club', 'time'])
    assert df['dorsal'].dtype == 'int64'
    assert df['time'].str.match(r'\d{1,2}:\d{2}:\d{2}').all()

def test_get_num_bikers(sample_df):
    '''Valida el print del head del dataframe'''
    assert get_num_bikers(sample_df) == 5
    empty_df = pd.DataFrame()
    assert get_num_bikers(empty_df) == 0

def test_get_columns(sample_df):
    '''Comprueba que los nombres de las columnas son los que deben'''
    expected_columns = ['dorsal', 'biker', 'club', 'time']
    assert get_columns(sample_df) == expected_columns

    # Test con DataFrame vacío
    empty_df = pd.DataFrame()
    assert get_columns(empty_df) == []

def test_run(capsys):
    '''Valida la salida entregada por la función run()'''
    df = run()
    assert isinstance(df, pd.DataFrame)
    captured = capsys.readouterr()

    # Verificar el contenido real que está produciendo
    expected_content = [
        "Primeros 5 registros:",
        "Número de participantes:",
        "Columnas del dataset:"
    ]
    for content in expected_content:
        assert content in captured.out
