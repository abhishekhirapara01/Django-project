def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        func(*args, **kwargs)
        print("After calling the function")
    return wrapper

@my_decorator
def my_function():
    print("This is my function")

my_function()
