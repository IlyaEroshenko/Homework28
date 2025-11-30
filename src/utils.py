import json
import os
import logging
from _datetime import datetime

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'C:\Users\ilyer\OneDrive\Homework\logs\utils.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions_from_json(filepath):
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Args:
    filepath (str): Путь к JSON-файлу.
    Returns:
    list: Список словарей с данными о транзакциях. Возвращает пустой список,
    если файл не найден, пуст или содержит данные не в формате списка.
    """
    logger.info(f"Начало загрузки данных из файла: {filepath}")
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(filepath):
            logger.warning(f"Файл {filepath} не найден.")
            return []

        with open(filepath, "r", encoding="utf-8") as f:
            logger.info(f"Файл {filepath} открыт для чтения.")
            try:
                data = json.load(f)
                logger.debug(f"Данные успешно прочитаны из файла: {data}")
                if isinstance(data, list):  # Проверяем, является ли загруженные данные списком
                    logger.info("Данные имеют формат списка.")
                    return data
                else:
                    logger.warning("Данные не в формате списка.")
                    return []  # Возвращаем пустой список, если данные не в формате списка
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования JSON в файле {filepath}.")
                return []  # Возвращаем пустой список, если файл пустой или содержит некорректный JSON
    except FileNotFoundError:
        logger.error(f"Файл {filepath} не найден. (FileNotFoundError)")
        return []
    finally:
        logger.info(f"Загрузка данных из файла {filepath} завершена.")


if __name__ == "__main__":
    # Пример использования функции
    filepath = os.path.join("data", "operations.json")  # Путь к файлу
    transactions = load_transactions_from_json(filepath)
    print(transactions)
