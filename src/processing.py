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
    """ "
    Сортирует список словарей по ключу "date".

    Args:
        list_of_dicts (list[dict]): Список словарей для сортировки.
        descending (bool, optional): Порядок сортировки. Если True, сортировка будет по убыванию. По умолчанию True.

    Returns:
        list[dict]: Новый список, отсортированный по дате.
    """

    # преобразуем строку даты в объект datetime
    return sorted(transactions_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)


def filter_bank_transaction(transactions, search_term):
    search_term = search_term.lower()
    result = []
    for transaction in transactions:
        if search_term in transaction['description'].lower():
            result.append(transaction)
    return result