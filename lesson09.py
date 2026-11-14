# 2)
age = int(input("შეიყვანე შენი ასაკი: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Adult")
else:
    print("Minor")


# 3)
number = int(input("შეიყვანე რიცხვი: "))

if 0 < number and number % 2 == 0:
    print("Positive Even")
elif 0 < number and number % 2 != 0:
    print("Positive Odd")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 4)
correct_username = "gio"
correct_password = "12345"
username = input("შეიყვანე მომხმარებლის სახელი: ")
password = input("შეიყვანე პაროლი: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Wrong username or password")


# 5)
n = 8
number = int(input("შეიყვანე რიცხვი: "))

while number != n:
    if number < n:
        print("თქვენი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე")
        number = int(input("შეიყვანე რიცხვი: "))
    elif number > n:
        print("თქვენი რიცხვი მეტია ჩაფიქრებულ რიცხვზე")
        number = int(input("შეიყვანე რიცხვი: "))
else:
    print("თქვენ წარმატებით გამოიცანით რიცხვი")


# 6)
n = int(input("შეიყვანე რიცხვი: "))

for i in range(1, n+1):
    print(i)
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")


# 7)
correct_password = "python123"
password = input("Enter password: ")

while password != correct_password:
    print("Wrong password!")
    password = input("Enter password: ")

print("Access granted!")


# 8)
start = int(input("Enter start: "))
end = int(input("Enter end: "))
n = start

while n <= end:
    print(n)
    if n > 0 and n % 2 == 0:
        print("Positive Even")
        n += 1
    else:
        n += 1


# 9)
age = int(input("Enter your age: "))
point = int(input("Enter your point: "))

if age >= 18 and point >= 70:
    print("you passed!")
elif age < 18 and point >= 70:
    print("Good result, but you are under 18!")
else:
    print("you failed!")


# 10)
n = int(input("Enter a number: "))
i = 0

while i <= n:
    print(i)
    if i % 2 == 0 and i % 3 == 0:
        print("Special number")
        i += 1
    elif i % 2 == 0:
        print("Even")
        i += 1
    elif i % 3 == 0:
        print("Divisible by 3")
        i += 1
    else:
        i += 1