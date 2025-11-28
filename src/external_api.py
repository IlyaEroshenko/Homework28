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
        return  None
    if "amount" not in transaction or "currency" not in transaction:
        print("Ошибка в transaction отсутствуют ключи 'amount' или 'currency'")
        return None

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)
    elif currency in ("USD", "EUR"):
        rate = get_exchange_rate(currency)
        if rate:
            return float(amount * rate)
        else:
            return None  # Возвращаем None, если не удалось получить курс
    else:
        print(f"Неподдерживаемая валюта: {currency}")
        return None


# Пример использования
transaction1 = {"amount": 100, "currency": "USD"}
transaction2 = {"amount": 5000, "currency": "RUB"}
transaction3 = {"amount": 200} # Отсутствует ключ currency

rub_amount1 = calculate_rub_amount(transaction1)
rub_amount2 = calculate_rub_amount(transaction2)
rub_amount3 = calculate_rub_amount(transaction3)

print(f"Сумма в рублях (USD): {rub_amount1}")
print(f"Сумма в рублях (RUB): {rub_amount2}")
print(f"Сумма в рублях (некорректная транзакция): {rub_amount3}")
