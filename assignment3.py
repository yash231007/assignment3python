#QUESTION-1
num = int(input(" Hey user , Enter a number "))
print(bin(num))

#QUESTION-2
# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")

#QUESTION-3
import math

print("(a) : ", (3*4)*5)
n = float(input("Enter value of n : "))
print("(b) : ", (n*(n-1))/2)
r = float(input("Enter value of r : "))
print("(c) : ", 4* math.pi *(r*r))
r_2 = float(input("Enter value of r : "))
a = float(input("Enter value of a in radians : "))
b = float(input("Enter value of b in radians : "))
print("(d) : ", math.sqrt((r_2*(math.cos(a))*(math.cos(a)))+(r_2*(math.sin(b))*(math.sin(b)))))
y2 = float(input("Enter value of y2 : "))
y1 = float(input("Enter value of y1 : "))
#Don't keep x1=x2 as division by zero is not defined.
x2 = float(input("Enter value of x2 : "))
x1 = float(input("Enter value of x1 : "))
print("(e) : ",(y2-y1)/(x2-x1))

#QUESTION-4
print("First Part")
for i in range(5):
  print(i,"\n",end="")

print("Second Part")
for i in range(3,10):
  print(i,"\n",end="")

print("Third Part")
for i in range(4,13,3):
  print(i,"\n",end="")

print("Fourth Part")
for i in range(15,5,-2):
  print(i,"\n",end="")

print("Fifth Part")
for i in range(5,3):
  print(i,"\n",end="")

#QUESTION-5

H = 1.00794
C = 12.0107
O = 15.9994
x = int(input("Enter the number of Hydrogen atoms"))
y = int(input("Enter the number of Carbon atoms"))
z = int(input("Enter the number of Oxygen atoms"))
weight = x*H + y*C + z*O
print(weight)