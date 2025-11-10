import pytest

from src.generators import filter_by_currency


@pytest.fixture
def sample_transactions():  # Fixture для создания тестовых транзакций.
    return [
        {"operationAmount": {"currency": {"code": "RUB"}}},
        {"operationAmount": {"currency": {"code": "EUR"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}}
    ]

def test_filter_usd(sample_transactions):  # Тест для фильтрации транзакций в RUB.
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 2
    assert rub_transactions[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_empty_list():  # Тест с пустым списком транзакций.
    transactions = []
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 0


def test_key_error_handling():  # Тест обработки KeyError.
    transactions = [{"operationAmount": {"code": "RUB"}}]
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 0