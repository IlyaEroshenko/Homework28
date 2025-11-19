

import os

import pytest

from src.decorators import log


# Фикстура для очистки лог-файла перед и после каждого теста
@pytest.fixture
def log_file_cleaner():
    log_file = "test.log"
    if os.path.exists(log_file):
        os.remove(log_file)
    yield log_file  # Полезно для получения имени файла в тестах
    if os.path.exists(log_file):
        os.remove(log_file)


def test_log_to_console(capsys):
    @log()
    def my_function(x):
        return x * 2
        result = my_function(5)
        captured = capsys.readouterr()
        assert "my_function" in captured.out
        assert "10" in captured.out
        assert result == 10


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test.log"
    @log(filename=log_file)
    def another_function(x, y):
        return x - y
    another_function(10, 3)
    with open(log_file, "r") as f:
        log_contents = f.read()
        assert "another_function" in log_contents
        assert "7" in log_contents


def test_log_exception(capfd):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capfd.readouterr()
    assert "Ошибка в функции divide" in captured.err
    assert "Тип ошибки: ZeroDivisionError" in captured.err