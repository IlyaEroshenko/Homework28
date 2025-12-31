import pandas as pd
import pytest
import os
from unittest.mock import patch, Mock
from unittest.mock import patch
from src.modulCSV import read_financial_data

@pytest.fixture
def test_data():
    data = {'date': ['2025-12-01', '2025-12-02'], 'amount': [100.0, -50.0], 'description': ['Test transaction', 'Another transaction']}
    return pd.DataFrame(data)


@pytest.fixture
def csv_file(test_data):
    filename = 'test_data.csv'
    test_data.to_csv(filename, index=False)
    yield filename
    os.remove(filename)


@pytest.fixture
def xlsx_file(test_data):
    filename = 'test_data.xlsx'
    test_data.to_excel(filename, index=False)
    yield filename
    os.remove(filename)


def test_read_csv_success(csv_file):
    result = read_financial_data(csv_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]['date'] == '2025-12-01'


def test_read_xlsx_success(xlsx_file):
    result = read_financial_data(xlsx_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[1]['amount'] == -50.0


def test_read_unsupported_format(test_data, capsys):
    filename = 'test_data.txt'
    with open(filename, 'w') as f:
        f.write("Some text")
    result = read_financial_data(filename)
    captured = capsys.readouterr()
    assert result is None
    assert "Неподдерживаемый формат файла" in captured.out
    os.remove(filename)


def test_file_not_found(capsys):
    result = read_financial_data('missing_file.csv')
    captured = capsys.readouterr()
    assert result is None
    assert "Файл не найден" in captured.out

@patch('pandas.read_excel')  # Мокаем функцию чтения XLSX
def test_read_xlsx_success(mock_read_excel):
    # Устанавливаем мокаемые данные для теста
    mock_data = pd.DataFrame({
        'Date': ['2025-12-01', '2025-12-02'],
        'Amount': [200.0, -75.0],
        'Description': ['Транзакция A', 'Транзакция B']})
    mock_read_excel.return_value = mock_data  # Возврат заготовленных данных

    result = read_financial_data('test.xlsx')  # Вызываем функцию
    assert isinstance(result, list)  # Проверяем, что результат - список
    assert len(result) == 2  # Проверяем количество записей
    assert result[1]['amount'] == -75.0  # Проверяем содержимое
