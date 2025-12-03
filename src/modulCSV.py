import pandas as pd

def read_financial_data(filepath):
    """
    Считывает финансовые операции из CSV- или XLSX-файла с использованием pandas.

    Args:
        filepath (str): Путь к файлу.

    Returns:
        pandas.DataFrame: DataFrame с финансовыми данными, или None в случае ошибки.
    """
    try:
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath) # Читаем CSV в DataFrame
        elif filepath.endswith('.xlsx'):
            df = pd.read_excel(filepath) # Читаем XLSX в DataFrame
        else:
            print("Неподдерживаемый формат файла. Поддерживаются только CSV и XLSX.")
            return None

        # Приведем названия столбцов к нижнему регистру и заменим пробелы на подчеркивания
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]


        return df
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None

# Пример использования
file_csv = '../data/transactions.csv'
file_xlsx = '../data/transactions_excel.xlsx'

data_csv = read_financial_data(file_csv)
data_xlsx = read_financial_data(file_xlsx)

if data_csv is not None:
    print("Данные из CSV:")
    print(data_csv.head())

if data_xlsx is not None:
    print("\nДанные из XLSX:")
    print(data_xlsx.head())