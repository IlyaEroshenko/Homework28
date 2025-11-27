import pytest
from unittest.mock import patch
import requests
from src.external_api import get_exchange_rate
from src.external_api import calculate_rub_amount

@pytest.fixture
def sample_transaction_usd():
  return {'amount': 100, 'currency': 'USD'}


@pytest.fixture
def sample_transaction_rub():
  return {'amount': 5000, 'currency': 'RUB'}


@pytest.fixture
def sample_transaction_gbp():
  return {'amount': 100, 'currency': 'GBP'}


@patch("src.external_api.get_exchange_rate")  # сумма в долларах США
def test_calculate_rub_amount_usd_success(mock_get_exchange_rate, sample_transaction_usd):
  mock_get_exchange_rate.return_value = 90.0
  result = calculate_rub_amount(sample_transaction_usd)
  assert result == 9000.0
  mock_get_exchange_rate.assert_called_once_with('USD')


def test_calculate_rub_amount_rub_success(sample_transaction_rub):
  result = calculate_rub_amount(sample_transaction_rub)
  assert result == 5000.0


@patch("src.external_api.get_exchange_rate")  # неподдерживаемая валюта
def test_calculate_rub_amount_unsupported_currency(mock_get_exchange_rate, sample_transaction_gbp):
  result = calculate_rub_amount(sample_transaction_gbp)
  assert result is None
  mock_get_exchange_rate.assert_not_called()


@patch("src.external_api.get_exchange_rate")  # вычисления суммы рубля ошибка API
def test_calculate_rub_amount_api_failure(mock_get_exchange_rate, sample_transaction_usd):
  mock_get_exchange_rate.return_value = None
  result = calculate_rub_amount(sample_transaction_usd)
  assert result is None

