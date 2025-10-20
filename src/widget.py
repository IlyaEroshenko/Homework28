def mask_account_card(account_info):
    """Маскирует номер карты или счета, представленного в виде строки."""


    parts = account_info.split() # Делим входящюю информацию на части
    account_type = ' '.join(parts[:-1])  # Объединяем все слова, кроме последнего
    account_number = parts[-1]
    visible_digits = 4
    masked_number = account_number[:visible_digits] + '*' * (len(account_number) - 2 * visible_digits) + account_number[-visible_digits:]

    return f"{account_type} {masked_number}"

print(mask_account_card("Maestro 7000792289606361"))  # print() используется в данном коде только для вызова функции