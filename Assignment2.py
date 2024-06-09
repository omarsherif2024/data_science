

# 1.To accept a string value from the user and display the count of each character in that string

string_input = input("Enter a string: ")
char_counts = {}
for char in string_input:
    if char in char_counts:
       char_counts[char] += 1
    else:
        char_counts[char] = 1
print("Character Counts:")
for char, count in char_counts.items():
    print(f"'{char}': {count}")

"""
Enter a string: ameena
Character Counts:
Enter a string: omar
Character Counts:
'o': 1
'm': 1
'a': 1
'r': 1
"""

# 2. Python function to find the maximum of three numbers
def max(a, b, c):
  if (a >= b) and (a >= c):
    largest = a
  elif (b >= a) and (b >= c):
    largest = b
  else:
    largest = c
    return largest
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print(f"The maximum of three numbers is:{max(a, b, c)}")

"""
Enter first number: 2
Enter second number: 4
Enter third number: 8
The maximum of three numbers is: 8.0
"""
#3. Python function called exponent(base,exp) that returns an integer value of base raises to the power of exp
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

"""
Enter base: 3
Enter exponential value: 2
Result: 9
"""
#4.Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
def sum_of_cubes(n):
    if n <= 0:
        raise ValueError("The number must be a positive integer.")
    return sum(i**3 for i in range(1, n))
n=int(input("Enter input: "))
print(f"The sum of cubes is:{sum_of_cubes(n)}")

"""
Enter input: 5
The sum of cubes is:100
"""

#5.program which iterates from 1 to 10. For multiples of 2,
#print “Fizz” instead of the number and for the multiples of 5, print “Buzz”.
#For numbers which are multiples of both 2 and 5, print “FizzBuzz”.
def fizz_buzz():
    for i in range(1, 11):
        if i % 2 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 2 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run the function
fizz_buzz()

"""
1
Fizz
3
Fizz
Buzz
Fizz
7
Fizz
9
FizzBuzz
"""

#6.Python program to find the most frequent item in a list of numbers
from collections import Counter
def most_frequent_item(n):
    if not numbers:
        return None
    counter = Counter(numbers)
    most_common_item, _ = counter.most_common(1)[0]
    return most_common_item
numbers = [6, 3, 3, 3, 0, 1, 2, 7, 3, 3, 5]
print(most_frequent_item(n))

"""
3
"""

#7.program to find the sum of squares of the numbers in a list
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)
numbers = [1, 2, 3, 4, 5, 6]
print("The sum of squares is:", sum_of_squares(numbers))

"""
The sum of squares is: 91
"""

#8.program using for loop that will iterate from 1 to 15. Foreach iteration,
#check if the current number is odd or even, and display the message to the screen as odd or even.
def check_odd_even():
    for i in range(1, 16):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
check_odd_even()

"""
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
11 is odd
12 is even
13 is odd
14 is even
15 is odd
"""

#9.program to convert temperatures to and from Celsius Fahrenheit.
 #[Formula: c/5=f-32/9 where c=temperature in Celsius and f=temperature in Fahrenheit.]
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
celsius_temp=float(input("Enter celsius temperature: "))
fahrenheit_temp=float(input("Enter fahrenheit temperature: "))

converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temp)
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temp)

print(f"{celsius_temp} degrees Celsius is {converted_to_fahrenheit} degrees Fahrenheit")
print(f"{fahrenheit_temp} degrees Fahrenheit is {converted_to_celsius} degrees Celsius")

"""
Enter celsius temperature: 31
Enter fahrenheit temperature: 95
31.0 degrees Celsius is 87.8 degrees Fahrenheit
95.0 degrees Fahrenheit is 35.0 degrees Celsius
"""

#10.function to calculate the factorial of a number
def factorial_recursive(n):
    if n < 0:
        raise ValueError("The number must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
number = 5
print(f"Factorial of {number} is {factorial_recursive(number)}")

"""
Factorial of 6 is 720
"""
