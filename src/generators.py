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

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "EUR",
                  "code": "EUR"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }, {
          "id": 939719580,
          "state": "EXECUTED",
          "date": "2019-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9829.04",
              "currency": {
                  "name": "RUB",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]
rub_transactions = filter_by_currency(transactions, "RUB")
for transaction in rub_transactions:
    print(transaction)