print("----CALCULATOR----")
num1 = int(input("Enter first number: "))       #Input first number
num2 = int(input("Enter second number: "))      #Input second number
print("--Operations--")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power")
choice = int(input("Enter your choice as mentioned above(1 - 5): "))   #choose operation 
if (choice == 1):                                    # If choice is 1 → Addition
    print(num1, "+", num2, "=", num1 + num2)
elif (choice == 2):                                  # If choice is 2 → Subtraction
    print(num1, "-", num2, "=", num1 - num2)
elif (choice == 3):                                  # If choice is 3 → Multiplication
    print(num1, "*", num2, "=", num1 * num2)
elif (choice == 4):                                  # If choice is 4 → Division
    print(num1, "/", num2, "=", num1 / num2)
elif (choice == 5):                                  # If choice is 5 → Power (num1 raised to num2)
    print(num1, "^", num2, "=", num1 ** num2)
else:                                                # If user enters an invalid choice
    print("Invalid choice. Enter number from 1 to 5 as per your choice.")
