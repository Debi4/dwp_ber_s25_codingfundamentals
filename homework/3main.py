#Homework:
first_number = 5
second_number = 2
addition = 5 + 2
subtraction = 5 - 2
multiplication = 5 * 2
division = 5 / 2
print("The first number:", first_number)
print("The second number:", second_number)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Assign two variables:")
x = input("5 and 2")
x = input(first_number, second_number)
print("Assign two variables: " + x)
Number = 7
Modulus_operator = 7 % 3
Exponentiation = 7 ** 2
print("The number is:", Number)

Number = 4
if Number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

x = 10
y = 20
x > y
x < y
x == y
print("The first number is:" + x)
print("The second number is:" + y)
print(y > x)

for numbers in range(1, 100):
    print(numbers)

multiply = 3
while multiply <= 30:
    print(multiply)
    multiply = multiply * 1


    if numbers == 3:
        print("fizz")
    elif numbers == 5:
        print("buzz")
    else:
        print(numbers)

def is_leap_year(year):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Year is a leap year.")
    else:
        print("Year is not a leap year.")
year = int(input("Enter a year:"))

