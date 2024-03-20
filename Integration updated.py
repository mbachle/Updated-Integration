##Decided to go back and do an update on this project (without the requirments and restrictions)

##String operations
print("Hello, operator!")
print("Whom am I speaking to today?") ## Removed the unnecessary sep parameter

## Input and Output
name = input("Enter your name: ")
print("Hello, ", name + ". What can I assist you with today?")
while True:
    print("Choose an operation: ")
    print("1. Arithmetic Operations")
    print("2. Conditional Operations")
    print("3. Boolean Operations")
    print("4. For Loops")
    print("5. While Loops")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting the program...")
        break
    if choice not in ['1', '2', '3', '4', '5',]:
        print("Invalid choice, Please enter a number between 1 and 6.")

    if choice == '1':
    #Basic arithmetic operations
        a = int(input("Enter a number: "))
        b = int(input("Enter the second number: "))
        print("addition: ", a + b)
        print("Subtraction: ", a - b)
        print("Multiplication: ", a * b)
        print("Division: ", a / b)
        print("Floor Division: ", a // b)
        print("Exponential: ", a ** b)
        print("Modulus: ", a % b)

    elif choice == '2':
    #Standard conditional statements
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            if b > a:
                print("b is greater than a")
            elif a == b:
                print("a and b are equal")
            else:
                print("a is greater than b")
                print("a != b", a != b)
                print("a == b:", a == b)
                print("a >= b:", a >= b)

    elif choice == '3':
    #Boolean operations
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))

        print("a < b and a < c:", a < b and a <c)
        print("a < b or a < c:", a < b or a < c)
        print("not(a < b and a < c):", not(a < b and a < c))

    elif choice == '4':
    #For Loops
        print("Enter a, b, c: ")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        for x in range(a, b, c):
            print(x)
    elif choice == '5':
        #while Loops
        start = int(input("Enter the starting number for the loop: "))
        limit = int(input("Enter a limit for the loop: "))
        increment = int(input("Enter the increment for the loop"))
        count = start
        while count <= limit:
            print(count)
            count += increment

