from transactions_data import transactions


def filter_by_currency(transactions, currency):
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
        try:
            transaction_currency = transaction["operationAmount"]["currency"]["code"]  # Получаем код валюты из вложенного словаря.
            if transaction_currency == currency:
                yield transaction  # Возвращаем транзакцию, если валюта соответствует.
        except (KeyError, TypeError):
            continue  # Если структура словаря не соответствует ожидаемой, игнорируем транзакцию.

rub_transactions = filter_by_currency(transactions, "RUB")
for transaction in rub_transactions:
    print(transaction)


def transaction_descriptions(transactions):
    """
    Генератор, извлекающий описание каждой транзакции из списка словарей.
    Args:
        transactions: Список словарей, где каждый словарь представляет транзакцию
                      и содержит ключ 'description' с описанием операции.
    Yields:
        Описание транзакции (значение ключа 'description').
    """
    for transaction in transactions:
        try:
            description = transaction['description']  # Пытаемся получить описание
            yield description  # Возвращаем описание текушей транзакции.
        except (KeyError, TypeError): # Обрабатываем случаи, если ключа 'description' нет в словаре
            continue

descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)