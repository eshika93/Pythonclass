# def decorate_function(func):
#     def wrapper():
#         print(f"func:{func}")
#         print("nice to see u ")
#         func()
#         print("welcome again")
#     return wrapper
# @decorate_function
# def greet():
#     print("welcome home")
# greet()
# print(f"greet:{greet}")


def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return ("could not divide by zero")
        else:
            return func(a, b)
    return wrapper
@smart_division

def division(num1, num2):
    return num1 / num2
print(division(10, 10))
print(division(10, 0))