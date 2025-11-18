import functools
import logging


def log(filename: object = None) -> object:
    """
        Декоратор для логирования начала и конца выполнения функции,
        а также ее результатов или возникших ошибок.

        Args:
            filename (str, optional): Имя файла для записи логов.
                Если не указано, логи выводятся в консоль.
        """
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)  # это код для получения объекта логгера из стандартной библиотеки Python,
            # который будет иметь имя, соответствующее имени функции func.
            logger.setLevel(logging.INFO)
            if filename:  # Определяем, куда писать логи: в файл или в консоль.
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            logger.info(f'Вызов функции {func.__name__} с аргументами: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)
                logger.info(f'Функция {func.__name__} успешно выполнена. Результат: {result}')
                return result
            except Exception as e:
                logger.error(f'Ошибка в функции {func.__name__}. Тип ошибки: {type(e).__name__}, Аргументы: {args}, {kwargs}')
                raise e
            finally:
                logger.removeHandler(handler)
        return wrapper
    return decorator_log

  # Пример использования
if __name__ == '__main__':
    @log(filename='example.log')  # Логирование в файл example.log
    def add(x, y):
        return x + y

@log()  # Логирование в консоль
def divide(x, y):
    return x / y
    add(5, 3)
try:
    divide(10, 0)
except ZeroDivisionError:
    print("Деление на ноль!")