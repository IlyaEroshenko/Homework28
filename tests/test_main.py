import unittest
from unittest.mock import patch
import io
from datetime import datetime
from contextlib import redirect_stdout
from src.main import main  # Замените your_module на имя файла, где main находится

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет', 'нет'])
    def test_basic_flow(self, mock_input):
      """Тест, проверяет базовый сценарий выполнения программы."""
      with redirect_stdout(io.StringIO()) as captured_output:
        main()
        self.assertIn("Привет! Добро пожаловать в программу", captured_output.getvalue())
        self.assertIn("Всего банковских операций в выборке:", captured_output.getvalue())

    @patch('builtins.input', side_effect=['1', 'INVALID', 'EXECUTED', 'да', 'возрастанию', 'да', 'слово', 'да'])
    def test_filter_by_all_options(self, mock_input):
      """Проверка фильтрации по всем возможным параметрам."""
      with redirect_stdout(io.StringIO()) as captured_output:
          main()
          output = captured_output.getvalue()
          self.assertIn("Всего банковских операций в выборке:", output )
          self.assertNotIn('USD', output)

    @patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет', 'нет', 'нет'])
    def test_no_transactions_found(self, mock_input):
        """Тест проверяет сценарий, когда не найдено ни одной транзакции."""
        with patch('sys.stdout', new_callable=io.StringIO) as stdout:
            main()
            self.assertIn("Всего банковских операций в выборке: 4", stdout.getvalue())

if __name__ == '__main__':
    unittest.main()