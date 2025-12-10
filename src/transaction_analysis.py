from typing import Dict, List


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
    # Словаpь накаплевания статистики
    category_count: Dict[str, int] = {category: 0 for category in categories}

    for operation in operations:
        # Получаем описание(или пустую строку)
        description: str = operation.get("description", "")

        # проходим по всем категориям
        for category in categories:
            if category in description:  # проверка наличия подстроки категории в описании
                category_count[category] += 1  # добавляем категорию
    return category_count
