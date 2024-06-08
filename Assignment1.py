# 1.Accepts the radius of a circle from the user and compute the area.

import math
from math import pi
r=float(input("Enter the radius of the circle:"))
area=float(pi)*pow(r,2)
print("The area of the circle is"+str(area))

# 2.To accept the details of a student like name, rollnumber and mark and display it.

name = input("Enter the student's name: ")
rollnumber = input("Enter the student's roll number: ")
marks = input("Enter the student's marks: ")
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {rollnumber}")
print(f"Marks: {marks}")

# 3.To get the largest number from a list.
list1 = [20,40,1,34,67,5,43,200]
print("Largest element is:", max(list1))

# 4.To iterate from start number to the end number and print the sum of the current number and previous number.

previous_num = 0
for current_number in range(10):
    sum = previous_num + current_number
    print(f'Current number {current_number} Previous Number {previous_num} is {sum}')
    previous_num = current_number

# 5.To print only those numbers which are divisible of 5.

n=50
for i in range(0,n+1):
  if i%5==0:
    print(i,end=" ")


# 6. Program to check if a number is prime or not

num = int(input("Enter a number: "))
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# 7.To reverse a list using for loop.

myList = [1,2,3,4,5,6,7]
reversedList = []
for i in range(len(myList)) :
    reversedList.append(myList[len(myList) - i - 1])
print(f'Original List : {myList}')
print(f'Reversed List : {reversedList}')


# 8.To print the following pattern.

num_rows = 4
for i in range(1, num_rows + 1):
    print('*' * i)


# 9.To find the maximum of three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
    maximum = num1
elif (num2 >= num1) and (num2 >= num3):
    maximum = num2
else:
    maximum = num3
print(f"The maximum of the three numbers is: {maximum}")


# 10.Print the pattern

num_rows = 5
for i in range(num_rows * 2):
    if i <= num_rows:
        print('*' * i)
    else:
        print('*' * (2 * num_rows - i))
