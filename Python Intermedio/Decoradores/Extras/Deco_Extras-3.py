from datetime import datetime
from functools import wraps


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argumento inválido: '{arg}' no es numérico")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(str(a) for a in args)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"func:{func.__name__} - args: {args_str} - [{timestamp}] - Resultado: {result}")
        print(f"Resultado {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    multiply(3, 4)
