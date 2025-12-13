from typing import List, Dict
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
