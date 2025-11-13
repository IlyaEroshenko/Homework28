import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_card_number():
    return "Maestro 7000792289606361"


@pytest.fixture
def valid_card_number():
    return "Visa Classic 1234567890123456"


def test_valid_card_number(valid_card_number):  # правельный ввод с одним словом
    assert get_mask_card_number(valid_card_number) == "Maestro 7000 79** **** 6361"


def test_valid_card_number(valid_card_number):  # правельный ввод с двумя словами
    assert get_mask_card_number(valid_card_number) == "Visa Classic 1234 56** **** 3456"


def test_masking_correct():  # правильная маска
    assert get_mask_card_number("Visa Classic 1234567890123456") == "Visa Classic 1234 56** **** 3456"


def test_card_number_is_missing():
    assert get_mask_card_number("Visa Classic") == "Некорректный номер карты"


@pytest.fixture
def valid_mask_account():
    return "Счет 73654108430135874305"


def test_valid_account_number():  # правельный ввод
    assert get_mask_account("986541084374305") == "Счёт **4305"


def test_masking_correct_account():  # правильная маска
    assert get_mask_account("Счет 73654108430135874305") == "Счёт **4305"


def test_get_mask_account_empty():  # пустой номер
    assert get_mask_account("") == "Счёт **"


def test_get_mask_account_short():  # короткий номер
    assert get_mask_account("123") == "Счёт **123"


def test_get_mask_account_alphanumeric():  # с буквами и цифрами в номере счета
    assert get_mask_account("ABC123XYZ") == "Счёт **3XYZ"
