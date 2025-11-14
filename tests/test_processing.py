import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions_data() -> None:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_by_state_executed() -> None:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(transactions) == expected


def test_filter_by_state_canceled() -> None:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    assert filter_by_state(transactions, "CANCELED") == expected


def test_filter_by_state_no_matching_state() -> None:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result = filter_by_state(transactions, "PENDING")  # Запрашиваем статус "PENDING"
    assert result == [], "Функция должна возвращать пустой список, если нет совпадений."


@pytest.fixture
def transaction_data() -> None:
    """Фикстура для подготовки тестовых данных (список словарей)."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 4, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]


def test_sort_by_date_descending(transaction_data) -> None:  # Проверяем сортировку по убыванию
    sorted_transactions = sort_by_date(transaction_data)
    assert sorted_transactions[0]["id"] == 1  # Самая поздняя дата должна быть первой
    assert sorted_transactions[1]["id"] == 3
    assert sorted_transactions[2]["id"] == 2
    assert sorted_transactions[3]["id"] == 4


def test_sort_by_date_growing(transaction_data) -> None:  # Проверяем сортировку по возрастанию
    sorted_transactions = sort_by_date(transaction_data, descending=False)
    assert sorted_transactions[0]["id"] == 4  # Самая ранняя дата должна быть первой
    assert sorted_transactions[1]["id"] == 2
    assert sorted_transactions[2]["id"] == 3
    assert sorted_transactions[3]["id"] == 1


def test_sort_by_date_empty_list() -> None:  # Проверяем на работу с пустым списком
    assert sort_by_date([]) == []