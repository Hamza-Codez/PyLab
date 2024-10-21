# print('I love to eat Pizza!')
# print('Hello World!')

# full_Name = "Hamza Ahmad"
# print(f"Hello Friends This is {full_Name}")
# age = 23
# gpa = 3.3
# is_Student = False
# if is_Student:
#   print("I am a Student")
# else:
#   print("I am Not a student")

# print(f"My age is {age}")
# print(f"My Final result displays the gpa of {gpa}")


# num = 2
# num = num + 2
# num += 3
# print(num)
# num -= 2
# print(num)
# num *= 9
# print(num)
 

# friends = 9
# friends = friends // 4
# print(f"Friends: {friends}")
# teacher = 10
# teacher = teacher / 2
# print(f"Teacher: {teacher}")


name = input("Enter Your Name : ")
# print(type(name))

# age = int(input("Enter Your Age : "))
# # age = int(age)
# # age = age + 23
# print(f'Hi {name}!')
# if age > 18:
#   print(f"Welcome {name}, your age is {age} and you are eligible for playing this game.")
# elif age < 19:
#   print(f"{name} Please visit us when you will be 19")
# elif age >= 50:
#   print(f"{name} you are too Old for Playing this game")
# else:
#    print(f"{name} You are not eligible")


name = input("Enter Your Name: ")

age = int(input("Enter Your Age: "))
print(f'Hi {name}!')

if age >= 50:
    print(f"{name}, you are too old for playing this game.")
elif age >= 19:
    print(f"Welcome {name}, your age is {age} and you are eligible for playing this game.")
else:
    print(f"{name}, please visit us when you turn 19.")