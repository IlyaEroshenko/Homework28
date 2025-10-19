from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if len(card_number) == 16:  # Проверяем количество цифр в номере
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"**{account_number[-4:]}"


def get_date(date_string: str, date_format: str="%Y-%m-%dT%H:%M:%S.%f") -> str:
    """Получаем и выводим дату в нужном нам формате"""
    try:
        return datetime.strptime(date_string, date_format).strftime("%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        print(f"Ошибка: Неверный формат даты '{date_string}' для формата '{date_format}'")
        return "Ошибка"


        # print() используется в данном коде только для вызова функции, при дальнейшей работе он будет удалён.
print(get_mask_card_number("7000792289606361"))


print(get_mask_account("73654108430135874305"))


print(get_date("2024-03-11T02:26:18.671407"))
