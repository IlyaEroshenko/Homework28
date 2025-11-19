from typing import Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций и возвращает транзакции, соответствующие заданной валюте.
    Использует генератор для эффективной обработки данных.
    Args:
        transactions: Список словарей, где каждый словарь представляет транзакцию
                      и содержит ключ 'currency', определяющий валюту операции.
        currency: Валюта, по которой нужно отфильтровать транзакции (строка).
    Yield:
        Словари, представляющие транзакции, у которых валюта (currency) совпадает с заданной.
    """
    for transaction in transactions:
        try:  # Получаем код валюты из вложенного словаря.
            transaction_currency = transaction["operationAmount"]["currency"]["code"]
            if transaction_currency == currency:
                yield transaction  # Возвращаем транзакцию, если валюта соответствует.
        except (KeyError, TypeError):
            continue  # Если структура словаря не соответствует ожидаемой, игнорируем транзакцию.


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


rub_transactions = filter_by_currency(transactions, "RUB")
for transaction in rub_transactions:
    print(transaction)


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Генератор, извлекающий описание каждой транзакции из списка словарей.
    Args:
        transactions: Список словарей, где каждый словарь представляет транзакцию
                      и содержит ключ 'description' с описанием операции.
    Yields:
        Описание транзакции (значение ключа 'description').
    """
    for transaction in transactions:
        try:
            description = transaction["description"]  # Пытаемся получить описание
            yield description  # Возвращаем описание текушей транзакции.
        except (KeyError, TypeError):  # Обрабатываем случаи, если ключа 'description' нет в словаре
            continue


descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    Args:
        start: Начальное значение диапазона (включительно).
        end: Конечное значение диапазона (включительно).
    Yields:
        Строка, представляющая номер карты в формате XXXX XXXX XXXX XXXX.
    """
    if not (0 < start <= 9999999999999999 and 0 < end <= 9999999999999999):
        raise ValueError("Недопустимый диапазон: 1..9999999999999999")
    if start > end:
        # Начальное значение не может быть больше конечного.
        raise ValueError("Недопустимый диапазон: 1..9999999999999999")

    for number in range(start, end + 1):
        formatted_number = f"{number:016}"  # обеспечиваем 16-значное представление числа с ведущими нулями.
        yield " ".join(formatted_number[n : n + 4] for n in range(0, 16, 4))


card_gen = card_number_generator(1, 5)
for card in card_gen:
    print(card)
