#1# CLASS AND OBJECT ##

# class laptop:

#     def __init__(self, brand, color, ram):
#         self.brand = brand
#         self.color = color
#         self.ram = ram
    
#     def power_on(self):
#         print(f"{self.brand} laptop is starting.")

#     def reboot(self):
#         print("{self.brand} laptop is reboting. ")

# d =  laptop("lenovo", "black", "16GB")
# l = laptop("dell", "silver", "8GB")
# # print(d.__dict__)
# print(l.__dict__)
# d.power_on()
# l.poweron()

# class = Car
# attribute = brand , year , color 
# method = start

# class laptop:
#     def __init__(self, brand, color, ram):
#         self.brand = brand
#         self.color = color 
#         self.ram = ram 
#     def power_on(self):
#         print(f"{self.brand} laptop is starting")
#     def reboot(self):
#         print(f"{self.brand} laptop is reboting")
# d = laptop("hp", "red", "6 GB")
# d.power_on()

# class car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color 

#     def start(self):
#         print(f"{self.brand} is starting.")
# c = car("kia", "1997", "black")
# c.start()







# class calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#         ##instancemethod##
#     def add(self):
#         return self.num1 + self.num2
    
#     def difference(self):
#         return self.num1 - self.num2
    
#     def product(self):
#         return self.num1 * self.num
    
#     @staticmethod
#     def square_root(num):
#         return num ** 2
    


# c = calculator(19, 10)

# print(c.add())
# print(c.difference())
# print(c.product())

# print(c.square_root(100))


# class student:
#     ##class or stattic variable##
#     college_name = "ABC College"

#     def __init__(self, _id, name, contact):
#         ##instance##
#         self._id = _id
#         self.name = name
#         self.contact = contact

# st = student("001", "Ram", "12345")
# std = student("002", "Shyam", "54321")
# print(std.college_name)
# #print(std.__dict__)

# class product:
#     def __init__(self, name, price):
#         self.name = name
#         # _product__price
#         # name managaling _classname__attrname
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price
        
#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price

#     # def get_price(self):
#     #     return self.__price

#     # def set_price(self, price):
#     #     self.__price = price

# pant = product("pant", 1600)
# # print(pant.get_price())
# # pant.set_price(1700)
# print(f"initial value: {pant.price}")
# pant.price = 900
# print(f"final value : {pant.price}")
# print(pant.__dict__)


##OPERATOR OVERLOADING##
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, obj):
        return self.price == obj.price

    def __add__(self, obj):
        return self.price + obj.price

pant = product("pant", 1600)
tshirt = product("tshirt", 1600)
print(pant == tshirt)
print(pant + tshirt)