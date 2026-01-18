print("----CALCULATOR----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("--Operations--")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power")
choice = int(input("Enter your choice as mentioned above(1 - 5): "))
if (choice == 1):
    print(num1, "+", num2, "=", num1 + num2)
elif (choice == 2):
    print(num1, "-", num2, "=", num1 - num2)
elif (choice == 3):
    print(num1, "*", num2, "=", num1 * num2)
elif (choice == 4):
    print(num1, "/", num2, "=", num1 / num2)
elif (choice == 5):
    print(num1, "^", num2, "=", num1 ** num2)
else:
    print("Invalid choice. Enter number from 1 to 5 as per your choice.")