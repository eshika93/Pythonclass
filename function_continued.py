# def func (*args):
#     print(args)
# func(1, 2, 3, "python")

# def func(**kwargs):
#     print(kwargs)
# func(1, 2, 3, name = "ram", contact = "1234", add = "ktm")    

# def func(*args,**kwargs):
#     print(args, kwargs)
# func(1, 2, 3, 4, "python", /n , name = "ram", contact = "1234", add = "ktm")    

# def weolcome():
#     print("welcome ram")
# w = weolcome
# w()

# def welcome(name):
#     print(f"welcome{name}")

# def greet(f):
#     f("ram")
# greet(welcome)

# def welcome(name):
#     print(f"welcome {name}")
# def namaste(name):
#     print(f"namaste {name}")
# def greet(f,name):
#     f(name)
# greet(welcome, "haarry")
# greet(namaste, "ram")



# def main():
#     def inner func():
#         print("i am inner function")
#     inner_func()
# main()

# def main():
#     def inner_func():
#         print("i am inner function")
#     return inner_func
# f = main()
# f()
# f()

# def main(n):
#     def addition(a, b):
#         return a + b
#     def subtraction(a, b):
#         return a - b
#     if n == 1:
#         return addition
#     elif n == 2:
#         return subtraction
# add = main(1)
# print(add(10,9))

# sub = main(2)
# print(sub(10,9))

# num = 10  # immutable object
# def func():
#     global num
#     num = num + 1
#     print(num)
# func()

# alist = [1, 2, 3, 4]
# def func():
#     alist.append(89)
# print(alist)
# func()
# print(alist)

# def main():
#     num = 10
#     def inner_func():
#         nonlocal num
#         num = num + 1
#         print(num)
#     inner_func()
# main()