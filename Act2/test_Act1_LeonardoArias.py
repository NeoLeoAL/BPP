import pytest
import pandas as pd
import Act1_LeonardoArias as actividad

test_df = pd.read_csv('finanzas2020.csv', sep="\s+")

def test_checkColumnType():
    for colum in test_df.columns[:]:
        if test_df[colum].dtype == object:
            test_df[colum] = pd.to_numeric(test_df[colum], errors='coerce')
        
    assert all(test_df.fillna(0) == actividad.checkColumnType(test_df))
    
def test_countColumn():
    test_columns = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12]
    result = 'OK'
    assert result == actividad.countColumn(test_columns)

def test_readCsv():
    assert all(test_df == actividad.readCsv('finanzas2020.csv'))