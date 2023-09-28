def sum(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


print("You can perform the following operations:\n"
      "1. Sum\n"
      "2. Subtraction\n"
      "3. Multipliaction\n"
      "4. Division\n"
      )
operation = int(input("What operation do you want to perform (Enter the no. option)?  "))

# The repetition in the if statements is because I didn't find a better way to show the invalid choice without having
# to ask for the numbers first


if operation == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum is: ", sum(num1, num2))


elif operation == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The difference is:", subtract(num1, num2))


elif operation == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The product is: ", multiply(num1, num2))


elif operation == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The quotient is: ", divide(num1, num2))

else:
    print("Invalid no. choice")


