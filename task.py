# user = int(input("enter a year:"))
# print(user)
# if user == 2020:
#     print("2020 is leapyear")
# else :
#     print("is not leap year")

# while True:
try: 
    number = int(input("Type in a number with four digits: "))
except ValueError:
    print("sorry, i did not understand that! ")
if number > 9999:
    print("The number is to big")
elif number < 0:
    print("No negative numbers please!")
else:
    print("Good! The number you wrote was", number)
