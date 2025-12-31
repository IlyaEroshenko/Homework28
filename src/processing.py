from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа "state".

    Args:
        data (list[dict]): Список словарей, содержащий данные о банковских операциях.
        state (str, optional): Статус операции, по которому фильтруются данные. По умолчанию "EXECUTED".

    Returns:
        list[dict]: Новый список, содержащий только те словари, у которых ключ "state" соответствует значению.
    """

    # Создаём новый список для отфильтрованных элементов
    filtered_data = []

    # Перебераем все данные
    for item in data:
        state_value = item.get("state", "")
        if isinstance(state_value, str) and state_value.upper() == state.upper():
            filtered_data.append(item)

    return filtered_data


def sort_by_date(transactions_list: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу "date".

    Args:
        transactions_list (list[dict]): Список словарей для сортировки.
        descending (bool, optional): Порядок сортировки. Если True, сортировка будет по убыванию. По умолчанию True.

    Returns:
        list[dict]: Новый список, отсортированный по дате.
    """

    def get_date_or_none(transaction):
        try:
            return datetime.fromisoformat(transaction["date"])
        except ValueError as e:
            print(f"Ошибка формата даты в: {transaction['date']}", e)
            return None

    # Сортируем, игнорируя элементы с некорректной датой
    return sorted(transactions_list, key=get_date_or_none, reverse=descending)


def filter_bank_transaction(transactions, search_term):
    search_term = search_term.lower()
    result = []
    for transaction in transactions:
        if search_term in transaction['description'].lower():
            result.append(transaction)
    return result
