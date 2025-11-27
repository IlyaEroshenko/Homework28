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
        return data['rates']['RUB']
    else:
        print(f"Ошибка при получении курса валюты: {response.status_code}")
        return None


def calculate_rub_amount(transaction):
    """
    Вычисляет сумму транзакции в рублях.
    """
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)
    elif currency in ('USD', 'EUR'):
        rate = get_exchange_rate(currency)
        if rate:
            return float(amount * rate)
        else:
            return None  # Возвращаем None, если не удалось получить курс
    else:
        print(f"Неподдерживаемая валюта: {currency}")
        return None

# Пример использования
transaction1 = {'amount': 100, 'currency': 'USD'}
transaction2 = {'amount': 5000, 'currency': 'RUB'}

rub_amount1 = calculate_rub_amount(transaction1)
rub_amount2 = calculate_rub_amount(transaction2)

print(f"Сумма в рублях (USD): {rub_amount1}")
print(f"Сумма в рублях (RUB): {rub_amount2}")
