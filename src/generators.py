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
