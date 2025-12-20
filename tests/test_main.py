import pytest
from unittest.mock import patch
from io import StringIO
import json

# Определите фикстуру с моковыми данными транзакций
@pytest.fixture
def mock_transactions():
    return [
        {"date": "2023-01-01", "description": "Зарплата", "account": "1234", "amount": 50000, "currency": "RUB", "state": "EXECUTED"},
        {"date": "2023-01-05", "description": "Покупка", "account": "5678", "amount": 1000, "currency": "RUB", "state": "EXECUTED"},
        {"date": "2023-01-10", "description": "Перевод", "account": "9012", "amount": 2000, "currency": "USD", "state": "PENDING"},
    ]

# Тест для фильтрации транзакций по статусу
def test_filter_by_state(mock_transactions, your_module=None):
    from main import filter_by_state  # Замените your_module на имя вашего файла
    filtered_transactions = filter_by_state(mock_transactions, "EXECUTED")
    assert len(filtered_transactions) == 2
    assert all(t["state"] == "EXECUTED" for t in filtered_transactions)

# Тест для сортировки транзакций по дате
from main import sort_by_date  # Убедись, что импортируешь функцию правильно

def test_sort_by_date_ascending(mock_transactions):
    sorted_transactions = sort_by_date(mock_transactions, False)  # Сортировка по возрастанию
    assert sorted_transactions[0]["date"] == "2023-01-01"
    assert sorted_transactions[-1]["date"] == "2023-01-10"

#тест для фильтрации транзакций по слову в описании
def test_filter_bank_transaction(mock_transactions):
    from main import filter_bank_transaction
    filtered_transactions = filter_bank_transaction(mock_transactions, "зарплата")
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0]["description"] == "Зарплата"
