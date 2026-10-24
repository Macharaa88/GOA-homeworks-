#2)
age=int (input ("შეიყვანეთ თქვენი ასაკი: "))
has_ticket = input ("გაქვთ ბილეთი? (True/False): ") == "True"
print (age >= 18 and has_ticket)

#3)
num1=int (input ("შეიყვანეთ პირველი რიცხვი: "))
num2=int (input ("შეიყვანეთ მეორე რიცხვი: "))
print ((num1 == 100 or num2 == 100))

#4)
first_name = input ("შეიყვანეთ თქვენი სახელი: ")
age2 = int (input ("შეიყვანეთ თქვენი ასაკი: "))
is_student = input ("ხართ სტუდენტი? (True/False): ") == "True"
print(first_name, (is_student and age2 >= 18))

#5)
is_sunny = input ("არის ამინდი მზიანი? (True/False): ") == "True"
is_warm = input ("არის ამინდი თბილი? (True/False): ") == "True"
print (is_sunny and not is_warm)
