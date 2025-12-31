from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счета, представленного в виде строки."""

    if not account_info:
        return "Введите счёт"

    parts = account_info.split()  # Разделяем строку на части по пробелам

    if parts[0].lower() in ("счёт", "счет"):  # Проверяем, начинается ли строка со слова "счет"
        masked_account = get_mask_account(parts[-1])

        if "Некорректный номер счёта" in masked_account:
            return "Некорректный номер счёта"

        return f'{" ".join(parts[:-1])} {masked_account}' # Соединяем части строки с замаскированным номером счета
    else: # Если строка не начинается со слова "счет", предполагаем, что это номер карты
        masked_card = get_mask_card_number(parts[-1])

        if "Некорректный номер карты" in masked_card:
            return "Некорректный номер карты"

        return f'{" ".join(parts[:-1])} {masked_card}' # Соединяем части строки с замаскированным номером карты

def get_date(date_string: str, date_format: str = "%Y-%m-%dT%H:%M:%S.%f") -> str:
    """Получаем и выводим дату в нужном нам формате"""
    try:
        date_obj = datetime.fromisoformat(date_string.split("T")[0])
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        print(f"Ошибка: Неверный формат даты '{date_string}' для формата '{date_format}'")
        return "Ошибка"
