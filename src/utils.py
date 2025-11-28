import json
import os


def load_transactions_from_json(filepath):
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Args:
    filepath (str): Путь к JSON-файлу.
    Returns:
    list: Список словарей с данными о транзакциях. Возвращает пустой список,
    если файл не найден, пуст или содержит данные не в формате списка.
    """
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(filepath):
            return []

        with open(filepath, "r", encoding="utf-8") as f:

            try:
                data = json.load(f)
                if isinstance(data, list):  # Проверяем, является ли загруженные данные списком
                    return data
                else:
                    return []  # Возвращаем пустой список, если данные не в формате списка
            except json.JSONDecodeError:
                return []  # Возвращаем пустой список, если файл пустой или содержит некорректный JSON
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    # Пример использования функции
    filepath = os.path.join("data", "operations.json")  # Путь к файлу
    transactions = load_transactions_from_json(filepath)
    print(transactions)
