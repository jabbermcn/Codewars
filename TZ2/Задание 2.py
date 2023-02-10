# Задание 2
# Все хэндлеры в списке handlers будут вызваны с аргументом 4,
# т.к. значение переменной step в цикле for успевает достичь 5,
# а затем будет использоваться во всех хэндлерах.

def create_handlers(callback: callable) -> list:
    handlers: list = []
    for step in range(5):
        handlers.append(lambda x=step: callback(x))
    return handlers


def execute_handlers(handlers: list):
    for handler in handlers:
        handler()


def callback(step: int):
    print(f'Step {step} is executed')


handlers = create_handlers(callback)
execute_handlers(handlers)
