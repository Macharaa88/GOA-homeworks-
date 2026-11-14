# 1)
positive = 0
negative = 0
even = 0
odd = 0
n1 = int(input("Enter first number: "))

if n1 > 0:
    positive += 1
elif n1 < 0:
    negative += 1
else:
    positive += 0

if n1 % 2 == 0:
    even += 1
else:
    odd += 1
n2 = int(input("Enter second number: "))

if n2 > 0:
    positive += 1
elif n2 < 0:
    negative += 1
else:
    positive += 0

if n2 % 2 == 0:
    even += 1
else:
    odd += 1
n3 = int(input("Enter third number: "))

if n3 > 0:
    positive += 1
elif n3 < 0:
    negative += 1
else:
    positive += 0

if n3 % 2 == 0:
    even += 1
else:
    odd += 1
n4 = int(input("Enter fourth number: "))

if n4 > 0:
    positive += 1
elif n4 < 0:
    negative += 1
else:
    positive += 0

if n4 % 2 == 0:
    even += 1
else:
    odd += 1
n5 = int(input("Enter fifth number: "))

if n5 > 0:
    positive += 1
elif n5 < 0:
    negative += 1
else:
    positive += 0

if n5 % 2 == 0:
    even += 1
else:
    odd += 1
n6 = int(input("Enter sixth number: "))

if n6 > 0:
    positive += 1
elif n6 < 0:
    negative += 1
else:
    positive += 0

if n6 % 2 == 0:
    even += 1
else:
    odd += 1
n7 = int(input("Enter seventh number: "))

if n7 > 0:
    positive += 1
elif n7 < 0:
    negative += 1
else:
    positive += 0

if n7 % 2 == 0:
    even += 1
else:
    odd += 1
n8 = int(input("Enter eighth number: "))

if n8 > 0:
    positive += 1
elif n8 < 0:
    negative += 1
else:
    positive += 0

if n8 % 2 == 0:
    even += 1
else:
    odd += 1
n9 = int(input("Enter ninth number: "))

if n9 > 0:
    positive += 1
elif n9 < 0:
    negative += 1
else:
    positive += 0

if n9 % 2 == 0:
    even += 1
else:
    odd += 1
n10 = int(input("Enter tenth number: "))

if n10 > 0:
    positive += 1
elif n10 < 0:
    negative += 1
else:
    positive += 0

if n10 % 2 == 0:
    even += 1
else:
    odd += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Even numbers:", even)
print("Odd numbers:", odd)


# 2)
n = int(input("შეიყვანე პროდუქტების რაოდენობა: "))
sum = 0

for i in range(n):
    price = float(input("შეიყვანე პროდუქტის ფასი: "))
    sum += price

if sum >= 200:
    sum = sum * 0.85
elif sum >= 100:
    sum = sum * 0.90
else:
    sum = sum

print("გადასახდელი თანხა:", sum)


# 3)
n = 42
number = int(input("შეიყვანე რიცხვი: "))
ცდა = 0

while number != n:
    if number < n:
        print("თქვენი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე")
        ცდა += 1
        number = int(input("შეიყვანე რიცხვი: "))
    elif number > n:
        print("თქვენი რიცხვი მეტია ჩაფიქრებულ რიცხვზე")
        ცდა += 1
        number = int(input("შეიყვანე რიცხვი: "))
else:
    ცდა += 1
    print("თქვენ წარმატებით გამოიცანით რიცხვი")
    print("მცდელობა", ცდა)


# 4)
name1 = input("შეიყვანე პირველი სახელი: ")
point1 = int(input("შეიყვანე პირველი სახელის ქულა: "))

name2 = input("შეიყვანე მეორე სახელი: ")
point2 = int(input("შეიყვანე მეორე სახელის ქულა: "))

name3 = input("შეიყვანე მესამე სახელი: ")
point3 = int(input("შეიყვანე მესამე სახელის ქულა: "))

name4 = input("შეიყვანე მეოთხე სახელი: ")
point4 = int(input("შეიყვანე მეოთხე სახელის ქულა: "))

name5 = input("შეიყვანე მეხუთე სახელი: ")
point5 = int(input("შეიყვანე მეხუთე სახელის ქულა: "))

if point1 >= 90:
    print(name1, "შესანიშნავი")
elif point1 >= 70:
    print(name1, "კარგი")
elif point1 >= 50:
    print(name1, "დამაკმაყოფილებელი")
else:
    print(name1, "ჩაჭრილი")

if point2 >= 90:
    print(name2, "შესანიშნავი")
elif point2 >= 70:
    print(name2, "კარგი")
elif point2 >= 50:
    print(name2, "დამაკმაყოფილებელი")
else:
    print(name2, "ჩაჭრილი")

if point3 >= 90:
    print(name3, "შესანიშნავი")
elif point3 >= 70:
    print(name3, "კარგი")
elif point3 >= 50:
    print(name3, "დამაკმაყოფილებელი")
else:
    print(name3, "ჩაჭრილი")

if point4 >= 90:
    print(name4, "შესანიშნავი")
elif point4 >= 70:
    print(name4, "კარგი")
elif point4 >= 50:
    print(name4, "დამაკმაყოფილებელი")
else:
    print(name4, "ჩაჭრილი")

if point5 >= 90:
    print(name5, "შესანიშნავი")
elif point5 >= 70:
    print(name5, "კარგი")
elif point5 >= 50:
    print(name5, "დამაკმაყოფილებელი")
else:
    print(name5, "ჩაჭრილი")


# 5)
n = int(input("შეიყვანე რიცხვი: "))
count = 0
total = 0
positive = 0

while n != 0:
    if n > 0:
        print("რიცხვი დადებითია")
        positive += 1
    else:
        print("რიცხვი უარყოფითია")
    if n % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")
    total += n
    count += 1
    n = int(input("შეიყვანე რიცხვი: "))

print("შეიყვანილი რიცხვების ჯამი:", total)
print("შეიყვანილი რიცხვების რაოდენობა:", count)
print("შეიყვანილი დადებითი რიცხვების რაოდენობა:", positive)