from datetime import datetime


def mask_account_card(account_info):
    """Маскирует номер карты или счета, представленного в виде строки."""


    parts = account_info.split() # Делим входящюю информацию на части
    account_type = ' '.join(parts[:-1])  # Объединяем все слова, кроме последнего
    account_number = parts[-1]
    visible_digits = 4
    masked_number = account_number[:visible_digits] + '*' * (len(account_number) - 2 * visible_digits) + account_number[-visible_digits:]

    return f"{account_type} {masked_number}"


def get_date(date_string: str, date_format: str = "%Y-%m-%dT%H:%M:%S.%f") -> str:
    """Получаем и выводим дату в нужном нам формате"""
    try:
        return datetime.strptime(date_string, date_format).strftime('"ДД.ММ.ГГГГ" ("%d-%m-%Y")')
    except ValueError:
        print(f"Ошибка: Неверный формат даты '{date_string}' для формата '{date_format}'")
        return "Ошибка"

print(mask_account_card("Maestro 7000792289606361"))  # print() используется в данном коде только для вызова функции

print(get_date("2024-03-11T02:26:18.671407"))
