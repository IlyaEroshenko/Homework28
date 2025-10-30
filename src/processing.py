def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа "state".

    Args:
        data (list[dict]): Список словарей, содержащий данные о банковских операциях.
        state (str, optional): Статус операции, по которому фильтруются данные. По умолчанию "EXECUTED".

    Returns:
        list[dict]: Новый список, содержащий только те словари, у которых ключ "state" соответствует указанному значению.
    """
    # Сщздаём новый список для отфильтрованых элементов
    filtered_data = []

    # Перебераем все данные
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)

    return filtered_data


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Вывод функции со статусом по умолчанию 'EXECUTED'
result_executed = filter_by_state(transactions)
print(result_executed)

# Вывод функции, если вторым аргументом передано 'CANCELED'
result_canceled = filter_by_state(transactions, "CANCELED")
print(result_canceled)


from datetime import datetime


def sort_by_date(list_of_dicts: list[dict], descending: bool = True) -> list[dict]:
    """"
    Сортирует список словарей по ключу "date".

    Args:
        list_of_dicts (list[dict]): Список словарей для сортировки.
        descending (bool, optional): Порядок сортировки. Если True, сортировка будет по убыванию. По умолчанию True.

    Returns:
        list[dict]: Новый список, отсортированный по дате.
    """

    # преобразуем строку даты в объект datetime
    return sorted(list_of_dicts, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)


# Пример использования:
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sort_result = sort_by_date(data)
print(sort_result)
