import unittest
from typing import List, Dict
from unittest.mock import patch, Mock
from collections import Counter

def categories_banc_operations(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций в каждой заданной категории.

    Аргументы:
        operations: Список словарей, где каждый словарь представляет банковскую операцию
                    и содержит поле 'description' с описанием операции.
        categories: Список строк, представляющих категории банковских операций.

    Возвращает:
        Словарь, где ключи - названия категорий, а значения - количество операций,
        относящихся к этой категории.
    """
    # Инициализируем Counter для подсчета категорий.
    category_counts = Counter()

    # Проходим по каждой операции.
    for operation in operations:
        # Получаем описание операции (если есть).
        description = operation.get("description", "")

        # Проверяем, соответствует ли описание какой-либо категории.
        for category in categories:
            if category in description:
                category_counts[category] += 1

    # Counter можно преобразовать обратно в обычный словарь, если требуется.
    return dict(category_counts)

class TestCategoriesBancOperations(unittest.TestCase):

    def test_empty_operations(self):
        # Проверяем, что функция корректно обрабатывает пустой список операций.
        operations: List[Dict] = []
        categories: List[str] = ["Food", "Shopping"]
        expected_result: Dict[str, int] = {"Food": 0, "Shopping": 0}  # Или просто {}
        self.assertEqual(categories_banc_operations(operations, categories), {})

    def test_no_description(self):
        # Проверяем операции без описания.
        operations: List[Dict] = [{}]
        categories: List[str] = ["Food"]
        expected_result: Dict[str, int] = {}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_empty_categories(self):
        # Проверяем, что функция корректно обрабатывает пустой список категорий.
        operations: List[Dict] = [{"description": "Food purchase"}, {"description": "Shopping spree"}]
        categories: List[str] = []
        expected_result: Dict[str, int] = {}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_basic_categories(self):
        # Проверяем подсчет для простых категорий.
        operations: List[Dict] = [
            {"description": "Food purchase at Tesco"},
            {"description": "Online Shopping at Amazon"},
            {"description": "Food delivery from Deliveroo"}
        ]
        categories: List[str] = ["Food", "Shopping"]
        expected_result: Dict[str, int] = {"Food": 2, "Shopping": 1}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_case_sensitivity(self):
         # Проверяем, что функция чувствительна к регистру.
        operations: List[Dict] = [{"description": "food Purchase"}]
        categories: List[str] = ["Food"]
        expected_result: Dict[str, int] = {}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

    def test_no_description(self):
        # Проверяем, что операции без описания не вызывают ошибок.
        operations: List[Dict] = [{}]
        categories: List[str] = ["Food"]
        expected_result: Dict[str, int] = {}
        self.assertEqual(categories_banc_operations(operations, categories), expected_result)

if __name__ == '__main__':
    unittest.main()