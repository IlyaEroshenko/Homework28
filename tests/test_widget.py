import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),  #Проверяем маскировку карты
        ("Mastercard 9876543210987654", "Mastercard 9876 54** **** 7654"),
        ("Счет 1234567890", "Счет **7890"),  #Проверяем маскировку счёта
        ("Visa Electron 1111222233334444", "Visa Electron 1111 22** **** 4444"),
        ("Счет 5555666677", "Счет **6677"),
    ],
)
def test_mask_account_card(account_info, expected):
    """Тестирует функцию mask_account_card с различными входными данными."""
    assert mask_account_card(account_info) == expected


@pytest.mark.parametrize(
    "date_string, date_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "%Y-%m-%dT%H:%M:%S.%f", "11.03.2024"),  # Стандартный формат
        ("2023-12-25", "%Y-%m-%d", "25.12.2023"),  # Формат без времени
        ("01.01.2025", "%d.%m.%Y", "01.01.2025"),  # Другой формат даты
        ("2024/05/10", "%Y/%m/%d", "10.05.2024"),  #Формат с разделителем /
        ("invalid_date", "%Y-%m-%dT%H:%M:%S.%f", "Ошибка"),  # Неверный формат даты
    ],
)
def test_get_date(date_string, date_format, expected, capsys):
    """Тестируем функцию get_date с различными входными данными."""
    result = get_date(date_string, date_format)
    assert result == expected

    # Проверяем, выводится ли сообщение об ошибке, если ожидаем "Ошибка"
    if expected == "Ошибка":
      captured = capsys.readouterr()
      assert "Ошибка:" in captured.out