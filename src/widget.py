from datetime import datetime


def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счета, представленного в виде строки."""
    parts = account_info.split()  # Делим входящюю информацию на части
    account_type = " ".join(parts[:-1])  # Объединяем все слова, кроме последнего
    account_number = parts[-1]
    if account_info.startswith("Счет"):  # Отдельно для счёта
        return f"Счет **{account_number[-4:]}"
    else:
        masked_number = f"{account_number[:4]} {account_number[4:6]}** **** {account_number[12:]}"
        return f"{account_type} {masked_number}"


def get_date(date_string: str, date_format: str = "%Y-%m-%dT%H:%M:%S.%f") -> str:
    """Получаем и выводим дату в нужном нам формате"""
    try:
        return datetime.strptime(date_string, date_format).strftime("%d.%m.%Y")
    except ValueError:
        print(f"Ошибка: Неверный формат даты '{date_string}' для формата '{date_format}'")
        return "Ошибка"


# print() используется в данном коде только для вызова функции
print(mask_account_card("Счет 73654108430135874305"))

print(get_date("2024-03-11T02:26:18.671407"))
