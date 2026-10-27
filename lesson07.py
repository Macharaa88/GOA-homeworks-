#2)
user_number = int(input("Please enter your number: "))

for number in range(1, user_number + 1):
    print(number)

number=1
while number <= user_number:
    print(number)
    number += 1


#3)
user_number = int(input("Please enter your number: "))

count = 0

for number in range(3, user_number + 1, 3):
    count += 1

print(count)

number=3
count=0
while number <= user_number:
    count += 1
    number += 3
print(count)


#4)
user_number = int(input("Please enter your number: "))

sum_numbers = 0

for number in range(0, user_number + 1, 2):
    sum_numbers += number

print(sum_numbers)

number = 0
sum_numbers = 0
while number <= user_number:
    sum_numbers += number
    number += 2
print(sum_numbers)


#5)
user_number = int(input("Please enter your number: "))

for number in range(1, user_number + 1, 2):
    print(number)

number = 1
while number <= user_number:
    print(number)
    number += 2


#6)
user_number = (input("Please enter your number: "))

numbers_sum = 0

for number in user_number:
    numbers_sum += int(number)

print(numbers_sum)

user_number = int(user_number)
numbers_sum = 0
while user_number > 0:
    numbers_sum += user_number % 10
    user_number //= 10
print(numbers_sum)


#7)
user_number = int(input("Please enter your number: "))

count = 0

for i in range(0, user_number + 1, 2):
    count += 1

print(count)

count = 0
i = 0
while i <= user_number:
    i += 2
    count +=1
print(count)


#8)
user_number = int(input("Please enter your number: "))

for number in range(0, user_number + 1, 5):
    print(number)

number = 0
while number <= user_number:
    print(number)
    number += 5