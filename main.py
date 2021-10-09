import datetime

def logger(old_function):

        def new_function(*args):
            start_date = datetime.datetime.now().strftime("%d-%m-%y")
            start_time = datetime.datetime.now().strftime("%H:%M:%S")
            result = old_function(*args)
            with open('data_file.txt', 'a', encoding='utf-8') as f:
                line = f'Функция "{old_function.__name__}" с аргументами {args} вызвана {start_date} в {start_time}.\n' \
                       f'Полученный результат: {result}.\n'
                f.write(line)
            return result
        return new_function


def logger2(log_file):
    def _logger2(old_function):
        def new_function(*args):
            start_date = datetime.datetime.now().strftime("%d-%m-%y")
            start_time = datetime.datetime.now().strftime("%H:%M:%S")
            result = old_function(*args)
            with open(log_file, 'a', encoding='utf-8') as f:
                line = f'Функция "{old_function.__name__}" с аргументами {args} вызвана {start_date} в {start_time}.\n' \
                       f'Полученный результат: {result}.\n'
                f.write(line)
            return result
        return new_function
    return _logger2

# @logger
@logger2('data_file.txt')
def sum_function(a, b):
    result = a + b
    return result


sum_function(4, 6)
sum_function(5, 5)
sum_function(3, 1)
sum_function(0, 7)

