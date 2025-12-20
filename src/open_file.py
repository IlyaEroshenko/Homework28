import json

import pandas as pd


def read_financial_data_csv(filepath):
    """Читает данные из CSV-файла."""
    try:
        df = pd.read_csv(filepath)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return None


def read_financial_data_excel(filepath):
    """Читает данные из XLSX-файла."""
    try:
        df = pd.read_excel(filepath)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return None

def load_transactions_from_json(filepath):
    """Читает данные из JSON-файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filepath}.")
        return None
