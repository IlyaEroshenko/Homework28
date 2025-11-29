import requests


def get_exchange_rate(currency):
    """
    Получает текущий курс валюты по отношению к рублю через Exchange Rates Data API.
    """
    api_key = "3ET53I6akq6Nxgzmt4xOrTWZbKBfcScu"
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "rates" in data and "RUB" in data["rates"]:  # Проверка структуры ответа API
            return data["rates"]["RUB"]
        else:
            print("Некорректный формат ответа API")
            return None
    else:
        print(f"Ошибка при получении курса валюты: {response.status_code}")
        return None


def calculate_rub_amount(transaction):
    """
    Вычисляет сумму транзакции в рублях.
    Проверяем на наличие ключей 'amount' и 'currency' в словаре transaction.
    """
    if not isinstance(transaction, dict):
        print("Ошибка: transaction должна быть словарём")
        return
    if 'operationAmount' in transaction:
        operation = transaction['operationAmount']
        if 'amount' in operation and 'currency' in operation:
            try:
                amount = float(operation['amount'])  # Преобразуем amount в float
            except ValueError:
                print("Некорректный формат суммы")
                return  None
            currency = operation['currency']['code']
        else:
            print("Ошибка: Отсутствуют ключи 'amount' или 'currency' в operationAmount")
            return None
    elif 'amount' in transaction and 'currency' in transaction:
        try:
            amount = float(transaction['amount'])  # Преобразуем amount в float
        except ValueError:
            print("Некорректный формат суммы")
            return None
        currency = transaction['currency']
    else:
        print("Ошибка: Отсутствует 'operationAmount' или ключи 'amount' и 'currency' в transaction")
        return None

    if currency == "RUB":
        return float(amount)
    elif currency in ("USD", "EUR"):
        rate = get_exchange_rate(currency)
        if rate:
            return round(float(amount) * float(rate), 2)
        else:
            return None  # Возвращаем None, если не удалось получить курс
    else:
        print(f"Неподдерживаемая валюта: {currency}")
        return None


# Пример использования
transaction1 = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
transaction2 = {"operationAmount": {"amount": 5000, "currency": {"code": "RUB"}}}
transaction3 = {"operationAmount": {"amount": 200, "currency": {"code": "CNY"}}}  # Пример с неподдерживаемой валютой} # Отсутствует ключ currency

rub_amount1 = calculate_rub_amount(transaction1)
rub_amount2 = calculate_rub_amount(transaction2)
rub_amount3 = calculate_rub_amount(transaction3)

print(f"Сумма в рублях (USD): {rub_amount1}")
print(f"Сумма в рублях (RUB): {rub_amount2}")
print(f"Сумма в рублях (некорректная транзакция): {rub_amount3}")
