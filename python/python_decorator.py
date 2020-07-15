def my_decorator(func):
    def inner():
        res = func()
        return res.upper()
    return inner

@my_decorator
def my_fun():
    return "Hello World"

# temp = my_decorator(my_fun)
# print(temp())

print(my_fun())