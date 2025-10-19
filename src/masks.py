from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер и название карты и возвращаем маску номера."""
    parts = card_number.split() #Делим входящюю информацию на части
    name_card = ' '.join(parts[:-1])
    number_card = parts[-1]
    if len(number_card) == 16:  # Проверяем количество цифр в номере
        return f"{name_card} {number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    else:
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"{'Счёт '}**{account_number[-4:]}"


def get_date(date_string: str, date_format: str = "%Y-%m-%dT%H:%M:%S.%f") -> str:
    """Получаем и выводим дату в нужном нам формате"""
    try:
        return datetime.strptime(date_string, date_format).strftime("%d-%m-%y T %H:%M:%S.%f")
    except ValueError:
        print(f"Ошибка: Неверный формат даты '{date_string}' для формата '{date_format}'")
        return "Ошибка"

        # print() используется в данном коде только для вызова функции, при дальнейшей работе он будет удалён.


print(get_mask_card_number("Visa Platinum 8990922113665229"))


print(get_mask_account("Счет 73654108430135874305"))


print(get_date("2024-03-11T02:26:18.671407"))
