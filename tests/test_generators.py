import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

@pytest.mark.parametrize(
    "start, end, expected_cards",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (1, 1, ["0000 0000 0000 0001"]),# проверка случая единичного диапазона
    ],
)


def test_card_number_generator_valid_ranges(start: int, end: int, expected_cards: list[str]):
    """
    Тесты для проверки корректной генерации номеров карт при валидных диапазонах.
    Используется параметризация для различных входных данных.
    """
    result = list(card_number_generator(start, end))
    assert result == expected_cards


def test_valid_range():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(generator)


def test_maximum_value():  # Тестовая функция с максимальным значением.
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize(
    "start, end, expected_exception",
    [
        (10, 1, ValueError),
        (0, 1, ValueError),
        (1, 10000000000000000, ValueError),
    ],
)
def test_card_number_generator_invalid_ranges(start: int, end: int, expected_exception: type[Exception]):
    """
    Тесты для проверки генерации исключений при некорректных диапазонах.
    Используется параметризация для различных некорректных входных данных.
    """
    with pytest.raises(expected_exception):
        list(card_number_generator(start, end)) # Преобразуем в список, чтобы сразу выполнить генератор.


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


def test_descriptions_present():
    """Проверяем наличие описаний в списке."""
    transactions = [{'description': 'Зарплата'}, {'description': 'Покупка'}]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ['Зарплата', 'Покупка']


#  Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.

def test_empty_list():
    transactions = []
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == []


def test_non_dict_transaction():
    """Проверяем пропуск не-словаря в списке."""
    transactions = [123, {'description': 'Покупка'}]  # type: ignore
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ['Покупка']