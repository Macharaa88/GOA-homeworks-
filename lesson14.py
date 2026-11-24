# 2)
def greet(name):
    print("hello", name)

greet("David")
greet("Gio")
greet("Nika")


# 3)
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
operator = input("Enter operator: +,-,*,/ : ")
if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    print(n1 / n2)
else:
    operator = input("Enter operator: +,-,*,/ ")

# 4)
def chek_even(num):
    if num % 2 == 0:
        print("ლუწი რიცხვია")
    else:
        print("კენტი რიცხვია")

chek_even(8)


# 5)
def print_numbers(n):
    for i in range(1,n+1):
        print(i)

print_numbers(8)