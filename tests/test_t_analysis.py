import unittest
from unittest.mock import patch
from typing import List, Dict
from src.transaction_analysis import categories_banc_operations
class TestCategoriesBancOperations(unittest.TestCase):

    def test_empty_input(self):
        """Тест с пустыми входными данными."""
        operations: List[Dict] = []
        categories: List[str] = []
        expected_result: Dict[str, int] = {}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_no_matching_categories(self):
        """Тест, когда ни одна операция не соответствует категориям."""
        operations: List[Dict] = [{"description": "unknown operation"}]
        categories: List[str] = ["deposit", "withdrawal"]
        expected_result: Dict[str, int] = {"deposit": 0, "withdrawal": 0}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_single_matching_category(self):
        """Тест с одной операцией, соответствующей одной категории."""
        operations: List[Dict] = [{"description": "ATM deposit"}]
        categories: List[str] = ["deposit", "withdrawal"]
        expected_result: Dict[str, int] = {"deposit": 1, "withdrawal": 0}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_multiple_operations_and_categories(self):
        """Тест с несколькими операциями и категориями, некоторые соответствуют."""
        operations: List[Dict] = [
            {"description": "ATM deposit"},
            {"description": "online withdrawal"},
            {"description": "deposit check"},
            {"description": "fee"}
        ]
        categories: List[str] = ["deposit", "withdrawal", "fee"]
        expected_result: Dict[str, int] = {"deposit": 2, "withdrawal": 1, "fee":1}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_description_missing(self):
        operations: List[Dict] = [{}]
        categories: List[str] = ["deposit"]
        expected_result: Dict[str, int] = {"deposit": 0}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

if __name__ == '__main__':
    unittest.main()