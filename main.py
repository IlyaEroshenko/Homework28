import os
from datetime import datetime

from src.open_file import read_financial_data_csv, read_financial_data_excel
from src.process_banc import filter_bank_transaction
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions_from_json

base_dir = os.path.dirname(__file__)


def main(filtered_transactions=None):
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3]:
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    print(f"Для обработки выбран {'JSON' if choice == 1 else 'CSV' if choice == 2 else 'XLSX'}-файл.")

    if choice == 1:
        transaction_data = load_transactions_from_json(base_dir + "/data/operations.json")
    elif choice == 2:
        transaction_data = read_financial_data_csv(base_dir + "/data/transactions.csv")
    else:
        transaction_data = read_financial_data_excel(base_dir + "/data/transactions_excel.xlsx")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:"
            "EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if status in available_statuses:
            transaction_data = filter_by_state(transaction_data, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_by_date_ans = input("Отсортировать операции по дате? Да/Нет\n").lower() == "да"

    if sort_by_date_ans:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower() == "по возрастанию"
        transaction_data = sort_by_date(transaction_data, sort_order)

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет\n").lower() == "да"

    if ruble_only:
        transaction_data = [t for t in transaction_data if t.get("currency") == "RUB"]
        print(transaction_data)
    filter_by_description = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower() == "да"
    )
    # Запрашиваем строку для фильтрации, если выбрана фильтрация по описанию
    if filter_by_description:
        search_term = input("Введите строку для поиска в описаниях транзакций: ").lower()
        transaction_data = filter_bank_transaction(transaction_data, search_term)

    print("Распечатываю итоговый список транзакций...")

    print(f"Всего банковских операций в выборке: {len(transaction_data)}")

    for transaction in transaction_data:
        print(
            f'{transaction["date"]} {transaction["description"]}'
            f'\nСчет {transaction["from"] if "from" in transaction else transaction["to"]}\n'
        )

    for transaction in transaction_data:
        # Здесь ты уже применил все нужные фильтры и сортировки
        formatted_date = datetime.fromisoformat(transaction['date']).strftime("%d.%m.%Y")
        formatted_output = (
            f"{formatted_date} {transaction['description']}\n"
            f"Счет {transaction['from']} -> Счет {transaction['to']}\n"
        )
        print(formatted_output)


if __name__ == "__main__":
    main()
