# child class " IS A" parent class


# class Person:
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact

#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):
#     def __init__(self, name, contact):
#         super().__init__(name, contact)

# class Teacher(Person):
#     def __init__(self, name, contact):
#         super().__init__(name, contact)

# st = Student("ram", "12345")
# st.walk()
# t = Teacher("shyam", "543245")
# t.walk()

class Bird:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print(f"{self.name} is flying.")

class Pigeon(Bird):
    def __init__(self, name):
        super().__init__(name)

class Osctich(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} could not fly.")

class Hummingbird(Bird):
    def __init__(self, name):
        super().__init__(name)
    
    def fly(self):
        super().fly()
        print(f"{self.name} can also fly backward.")

P = Pigeon("sabin")
p.fly()

o = Osctich("monstor")
o.fly()

h = Hummingbird("sujan")
h.fly()
    