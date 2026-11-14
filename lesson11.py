# 2)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
index = len(numbers) - 1
count =0
while index >= 0:
    count += (numbers[index])
    index -= 1
print(count)


# 3)
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
for name in names:
    print("Hello", name + "!")


# 4)
mixed_list = ["Saba", "Nika", 10, 20, 20.5, 50.10, True, "Levani", False, 500]

result = []

index = len(mixed_list) - 1

while index >= 0:
    result.append(mixed_list[index])

    index -= 1

print(mixed_list)
print(result)


# 5)
ages = [10, 20, 13, 18, 19, 21, 5, 6, 78, 56]

for age in ages:
    if age >= 18:
        print(age, "User is Adult!")
    else:
        print(age, "User is not Adult!")