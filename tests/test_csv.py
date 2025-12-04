import pandas as pd
import pytest
from src.modulCSV import read_financial_data

def test_read_csv_success(tmp_path):
    # Создаём временный CSV-файл для тестирования
    file_path = tmp_path / "test.csv"
    file_path.write_text("col1,col2\n1,2\n3,4")

    df = read_financial_data(str(file_path))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_read_xlsx_success(tmp_path):
    # Создаём временный XLSX -файл для тестирования
    file_path = tmp_path / "test.xlsx"
    df_test = pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]})
    df_test.to_excel(file_path, index=False)

    df = read_financial_data(str(file_path))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_read_file_not_found():
    df = read_financial_data("nonexistent_file.csv")
    assert df is None

def test_read_unsupported_format(tmp_path):
    # Создаём временный файл с неподдерживаемым форматом
    file_path = tmp_path / "test.txt"
    file_path.write_text("some text")

    df = read_financial_data(str(file_path))
    assert df is None

def test_read_csv_column_names(tmp_path):
    # Проверяем, что названия столбцов приводятся к нижнему регистру и пробелы заменяются
    file_path = tmp_path / "test.csv"
    file_path.write_text("Column One,Column Two\n1,2")

    df = read_financial_data(str(file_path))
    assert 'column_one' in df.columns
    assert 'column_two' in df.columns