import unittest
from unittest.mock import patch, mock_open
import json
import os
from src.utils import load_transactions_from_json

class TestLoadTransactionsFromJson(unittest.TestCase):

    @patch("os.path.exists")
    def test_file_not_found(self, mock_exists):
        """Тест: Файл не существует."""
        mock_exists.return_value = False
        result = load_transactions_from_json("nonexistent_file.json")
        self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_empty_file(self, mock_file, mock_exists):
        """Тест: Файл существует, но пустой."""
        mock_exists.return_value = True
        result = load_transactions_from_json("empty_file.json")
        self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_invalid_json_data(self, mock_file, mock_exists):
        """Тест: Файл содержит некорректный JSON."""
        mock_exists.return_value = True
        result = load_transactions_from_json("invalid_json.json")
        self.assertEqual(result, [])

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_valid_json_data(self, mock_file, mock_exists):
        """Тест: Файл содержит валидный JSON."""
        mock_exists.return_value = True
        expected_data = [{"amount": 100, "currency": "USD"}]
        result = load_transactions_from_json("valid_json.json")
        self.assertEqual(result, expected_data)

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"not": "list"}')
    def test_not_a_list(self, mock_file, mock_exists):
        """Тест: Не список"""
        mock_exists.return_value = True
        result = load_transactions_from_json("not_list.json")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()