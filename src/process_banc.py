import re
from typing import List, Dict

from src.generators import description


def filter_bank_transaction(transactions: List[Dict], search_term: str) -> List[Dict]:
    """
        Фильтрует список словарей с информацией о банковских операциях на основе поисковой строки,
        используя регулярные выражения для поиска совпадений в описании каждой операции.

        Аргументы:
            transactions: Список словарей, где каждый словарь представляет банковскую операцию.
                          Ожидается, что каждый словарь имеет ключ 'description' со строковым значением.
            search_term: Строка, которая будет использоваться для поиска в описаниях банковских операций.
                        Регулярное выражение составляется из этой строки.

        Возвращает:
            Список словарей, представляющих банковские операции, в описании которых найдено совпадение
            с поисковой строкой (с учетом регистра). Возвращается новый список, исходный не изменяется.
        """
    filter_transactions: List[Dict] = []
      # Создаем объект регулярного выражения, игнорируя регистр
    regex = re.compile(search_term, re.IGNORECASE)


    for transaction in transactions:
        # Получаем описание, или пустую строку, если нет его
        description: str = transaction.get('description', '')
        # Проверяем, что описание строка и содержит поисковую строку
        if isinstance(description, str) and regex.search(description):
            # Добавляем копию словаря, чтобы не изменять исходный список
            filter_transactions.append(transaction.copy())

    return filter_transactions
    