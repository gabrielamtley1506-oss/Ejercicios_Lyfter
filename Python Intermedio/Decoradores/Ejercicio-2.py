class Numbers:
    def __init__(self):
        pass

    @staticmethod
    def number_only(func):
        def wrapper(*args, **kwargs):
            for arg in args[1:]:
                if not isinstance(arg, (int, float)):
                    raise ValueError(f"Error: '{arg}' this is not a number")
                
            for key, val in kwargs.items():
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Error: '{key}={val}' is not a number")
                
            return func(*args, **kwargs)
        return wrapper

    @number_only
    def calculate(self, *args):
        print(f"Thanks for enter the numbers: {args}")


num1 = Numbers()


num1.calculate(10, 5, 6, 8)



num1.calculate(10, "hola", 6)