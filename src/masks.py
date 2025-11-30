import logging
import os
from datetime import datetime

print("Текущая рабочая директория:", os.getcwd())

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'C:\Users\ilyer\OneDrive\Homework\logs\masks.log', 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер и название карты и возвращаем маску номера."""
    logger.info(f'Начало маскировки номера карты: {card_number}')
    parts = card_number.split()  # Делим входящюю информацию на части
    name_card = " ".join(parts[:-1])
    number_card = parts[-1]
    if len(number_card) == 16:  # Проверяем количество цифр в номере
        masked_number = f"{name_card} {number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
        logger.info(f"Номер карты успешно замаскирован. Результат: {masked_number}")
        return masked_number
    else:
        logger.warning(f"Некорректный номер карты: {card_number}")
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.info(f"Начало маскировки номера счета: {account_number}")
    masked_account = f"{'Счёт '}**{account_number[-4:]}"
    logger.info(f"Номер счета успешно замаскирован. Результат: {masked_account}")
    return masked_account


# print() используется в данном коде только для вызова функции, при дальнейшей работе он будет удалён.
print(get_mask_card_number("Visa Platinum 8990922113665229"))

print(get_mask_account("Счет 73654108430135874305"))
