import unittest
from unittest.mock import patch
from typing import List, Dict
import re
from src.process_banc import filter_bank_transaction

class TestFilterBankTransaction(unittest.TestCase):

    def test_empty_transactions(self):
        """Тест с пустым списком транзакций."""
        transactions: List[Dict] = []
        search_term: str = "test"
        expected_result: List[Dict] = []
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

    def test_no_matches(self):
        """Тест, когда поисковая строка не соответствует ни одной транзакции."""
        transactions: List[Dict] = [{"description": "Transaction 1"}, {"description": "Transaction 2"}]
        search_term: str = "test"
        expected_result: List[Dict] = []
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

    def test_single_match(self):
        """Тест с одной транзакцией, соответствующей поисковой строке."""
        transactions: List[Dict] = [{"description": "Test transaction"}]
        search_term: str = "test"
        expected_result: List[Dict] = [{"description": "Test transaction"}]
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

    def test_multiple_matches(self):
        """Тест с несколькими транзакциями, соответствующими поисковой строке. """
        transactions: List[Dict] = [{"description": "Test transaction"}, {"description": "Another Test transaction"}, {"description": "Not a match"}]
        search_term: str = "test"
        expected_result: List[Dict] = [{"description": "Test transaction"}, {"description": "Another Test transaction"}]
        self.assertEqual(filter_bank_transaction(transactions, search_term), [t.copy() for t in expected_result])

    def test_case_insensitive(self):
        """Тест, проверяющий регистронезависимый поиск."""
        transactions: List[Dict] = [{"description": "tEsT transaction"}]
        search_term: str = "test"
        expected_result: List[Dict] = [{"description": "tEsT transaction"}]
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

    def test_description_missing(self):
        """Тест, когда поле 'description' отсутствует в транзакции."""
        transactions: List[Dict] = [{}]
        search_term: str = "test"
        expected_result: List[Dict] = []
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

    def test_search_term_is_regex(self):
        """Тест, проверяющий корректную обработку, когда search_term является регулярным выражением."""
        transactions: List[Dict] = [{"description": "Transaction with number 123"}]
        search_term: str = r"\d+"  # Ищем одну или более цифр
        expected_result: List[Dict] = [{"description": "Transaction with number 123"}]
        self.assertEqual(filter_bank_transaction(transactions, search_term), expected_result)

if __name__ == '__main__':
    unittest.main()