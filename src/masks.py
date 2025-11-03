def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер и название карты.
        Оставляет видимыми только первые 6 и последние 4 цифры
    Args:
        card_number: Строка, содержащая название карты и номер (например, "Visa 1234567890123456").

    Returns:
        Отформатированная строка с маскированным номером карты или сообщение об ошибке.
    """
    parts = card_number.split()  # Делим входящюю информацию на части по пробелам
    name_card = " ".join(parts[:-1])
    number_card = parts[-1]


    if len(number_card) == 16:  # Проверяем количество цифр в номере
        return f"{name_card} {number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    elif len(number_card) < 2:
        return "Отсутствует номер карты."
    else:
        return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"{'Счёт '}**{account_number[-4:]}"


# print() используется в данном коде только для вызова функции, при дальнейшей работе он будет удалён.
print(get_mask_card_number("Visa Platinum 8990922113665229"))

print(get_mask_account("Счет 73654108430135874305"))
