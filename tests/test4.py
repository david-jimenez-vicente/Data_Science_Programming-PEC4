"""
Script de test del ejercicio 4
"""
import pytest
import pandas as pd
from src.ejer4 import clean_club, analyze_clubs, run

def test_clean_club():
    '''Test de limpieza de los clubs'''
    test_cases = [
        ('Club Ciclista Huesca', 'HUESCA'),
        ('C.C. Huesca', 'HUESCA'),
        ('HUESCA C.C.', 'HUESCA'),
        ('Peña Ciclista Test', 'TEST'),
        ('Agrupación Ciclista Example', 'EXAMPLE'),
        ('C.D. Sports A.D.', 'SPORTS'),
        ('S.C. Racing T.T.', 'RACING'),
        (None, 'INDEPENDIENTE'),
        ('', 'INDEPENDIENTE'),
        ('  CLUB TEST  ', 'TEST'),
        ('A.C. TEST C.C.', 'TEST')
    ]

    for input_club, expected_output in test_cases:
        assert clean_club(input_club) == expected_output

@pytest.fixture
def sample_df():
    '''Creación del dataframe de prueba'''
    data = {
        'dorsal': range(1, 8),
        'biker': [f'Biker{i}' for i in range(1, 8)],
        'club': [
            'C.C. Huesca',
            'Club Ciclista Test',
            'Huesca C.C.',
            None,
            'Peña Ciclista Example',
            'C.C. Huesca',
            'Independiente'
        ],
        'time': [f'{i}:00:00' for i in range(1, 8)]
    }
    return pd.DataFrame(data)

def test_analyze_clubs(sample_df):
    '''Verificar la limpieza de clubs'''
    df_clean, clubs_df = analyze_clubs(sample_df)

    # Verificar nueva columna
    assert 'club_clean' in df_clean.columns

    # Verificar limpieza de clubs
    assert list(df_clean['club_clean'].unique()) == ['HUESCA', 'TEST', 'INDEPENDIENTE', 'EXAMPLE']

    # Verificar análisis
    assert len(clubs_df) == 4
    assert clubs_df.iloc[0]['club_clean'] == 'HUESCA'
    assert clubs_df.iloc[0]['participants'] == 3

def test_run(capsys):
    '''Test del proceso principal'''
    df_clean, clubs_df = run()
    assert isinstance(df_clean, pd.DataFrame)
    assert isinstance(clubs_df, pd.DataFrame)
    assert 'club_clean' in df_clean.columns
    captured = capsys.readouterr()
    assert "clubs limpios" in captured.out
