def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Parameters: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return: {result}")
        return result
    return wrapper



@log_function
def sum(a, b):
    return a + b

@log_function
def greeting(name, message="Hii"):
    return f"{message}, {name}!"


sum(3, 5)
greeting("Carlos", message="Good morning")