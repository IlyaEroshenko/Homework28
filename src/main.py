from datetime import datetime


def main():
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

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:"
            "EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if status in available_statuses:
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower() == "да"

    if sort_by_date:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower()

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет\n").lower() == "да"
    filter_by_description = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower() == "да"
    )
    # Запрашиваем строку для фильтрации, если выбрана фильтрация по описанию
    if filter_by_description:
        search_term = input("Введите строку для поиска в описаниях транзакций: ").lower()

    filtered_transactions = [
        {
            "date": "08.12.2019",
            "description": "Открытие вклада",
            "account": "**4321",
            "amount": "40542 руб.",
            "currency": "RUB",
            "status": "EXECUTED",
        },
        {
            "date": "12.11.2019",
            "description": "Перевод с карты на карту\nMasterCard 7771 27** **** 3727->Visa Platinum 1293 38** **** 9203",
            "account": "",
            "amount": "130",
            "currency": "USD",
            "status": "EXECUTED",
        },
        {
            "date": "18.07.2018",
            "description": "Перевод организации\nVisa Platinum 7492 65** **** 7202 -> Счет **0034",
            "account": "",
            "amount": "8390",
            "currency": "RUB",
            "status": "EXECUTED",
        },
        {
            "date": "03.06.2018",
            "description": "Перевод со счета на счет\nСчет **2935 -> Счет **4321",
            "account": "",
            "amount": "8200",
            "currency": "EUR",
            "status": "EXECUTED",
        },
    ]

    print("Распечатываю итоговый список транзакций...")

    filtered_transactions = [t for t in filtered_transactions if t["status"] == status]

    if ruble_only:
        filtered_transactions = [t for t in filtered_transactions if t["currency"] == "RUB"]
    # Сортируем по фразе
    if filter_by_description:
        filtered_transactions = [t for t in filtered_transactions if search_term in t["description"].lower()]

    # Сортировка по дате
    if sort_by_date:
        reverse = sort_order == "убыванию"  # Определяем порядок сортировки
        filtered_transactions = sorted(
            filtered_transactions, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=reverse
        )  # Указываем порядок сор-ки

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        print(
            f'{transaction["date"]} {transaction["description"]}'
            f'\nСчет {transaction["account"]}\nСумма: {transaction["amount"]} {transaction["currency"]}\n'
        )


if __name__ == "__main__":
    main()
