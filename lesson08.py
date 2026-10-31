#2)
n = int(input("Enter n: "))
i = 1

while i <= n:
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
    i += 1


#3
n = int(input("Enter n: "))
i = 0

while i <= n:
    if i % 5 == 0:
        print("Divisible by 5")
    else:
        print(i)
    i += 1


#4)
correct_password = "python123"
password = input("Enter password: ")

while password != correct_password:
    if password == correct_password:
        print("Access Granted!")
    else:
        print("Wrong password!")
    password = input("Enter password: ")

print("Access Granted!")


#5)
user_number = int(input("Please enter your number: "))

for number in range(1, user_number + 1):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


#6)
n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
    else:
        print("Not divisible by 3")