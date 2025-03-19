#number1 = 10
#number2 = 5
#print (number1 >= number2)
number3 = 30
number4 = 45
print (number3 == number4)
word1 = True
word2 = False
print (word1 == word2)
pi = 3.14
print (pi == 3.14)

# Lesson 2 
# Introduction to Python: Variables, Data Types & Booleans  
                                                           


## 1. Variables and Basic Data Types
#a. Assign the number 10 to a variable named `my_number`.
my_number = 10
#b. Assign the string "Hello, Python!" to a variable named `my_string`.
my_string = "Hello, Python!"
#c. Assign the float 3.14 to a variable named `my_float`.
my_float = 3.14
#Print each variable: `my_number`, `my_string`, and `my_float`.
print(my_number)
print(my_string)
print(my_float)
print(f"myfloat is {my_float}")

## 2. Working with Different Data Types
#**a. String concatenation**
#- Create two string variables: `first_name` and `last_name`.
first_name = "Deborah"
last_name = "Tomassini"
#- Concatenate them with a space in between to form a full name and assign this to a variable named `full_name`.
full_name = "Deborah + Tomassini"
#- Print the full_name.
print(full_name)

#**b. Arithmetic Operations**
#- Create two integer variables: `a = 5` and `b = 3`.
a = 5
b = 3
#- Perform addition, subtraction, multiplication, and division on these variables, e.g., a+b, a-b, a*b, a/b, and save each result to `add_result`, `sub_result`, `mult_result`, `div_result`
#- Print the results of each operation.
add_result = "a + b"
sub_result = "a - b"
mult_result = "a * b"
div_result = "a / b"
print(a + b)
print(a - b)
print(a * b)
print(a / b)

## 3. Booleans and Comparisons

#**a. Creating booleans**
#- Assign the result of 5 > 3 to a variable named `is_greater`.
is_greater = 5 >= 3
#- Assign the result of 5 == 3 to a variable named `is_equal`.
is_equal = 5 == 3
#- Assign the result of 5 < 3 to a variable named `is_smaller`.
is_smaller = 5 <= 3
#- Print the values of `is_greater`, `is_equal`, and `is_smaller`.
print(is_greater)
print(is_equal)
print(is_smaller)

#**b. Boolean Operations**

#Create two boolean variables: `bool1 = True` and `bool2 = False`.
bool1 = True
bool2 = False
#Perform logical AND, OR, and NOT operations on these variables and print the results.

#**c. Comparison between data types**

#Given three variables:
#```
#pi = 3.14
#pi_pi = '3.14'
#pi_pi_pi = "3.14"
#```
#1. Are `pi` and `pi_pi` equal? If not, why?
print(pi != pi_pi) 
pi = "float" 
pi_pi = "string"
#2. Are `pi_pi` and `pi_pi_pi` equal? If not, why?
print(pi_pi == pi_pi_pi + "because they are both strings")

## 4. Type checking and conversion.
#**a. Type checking**

#For each variable `pi`, `pi_pi`, `pi_pi_pi`, use the type() function to print its data type.

#**b. Type conversion**

#- Create a string variable `my_str = "123"`.
#- Convert it to an integer and store it in a variable named `my_int`.
#- Convert `my_int` to a float and store it in a variable named `my_float_converted`.
#- Print all three variables.

## 5. Challenge

#- Define a variable `celsius` and assign it a temperature value in Celsius.
#- Use the formula (celsius * 9/5) + 32 to convert the temperature to Fahrenheit.
#- Store the result in a variable named `fahrenheit`.
#- Print the original temperature in Celsius and the converted temperature in Fahrenheit.

