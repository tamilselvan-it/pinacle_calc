def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("\n🧮 Welcome to the Python Calculator!")
    print("--------------------------------------")
    
    while True:
        print("\nChoose an operation:")
        print("  1 ➕ Add")
        print("  2 ➖ Subtract")
        print("  3 ✖️ Multiply")
        print("  4 ➗ Divide")
        print("  5 ❌ Exit")
        
        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("👋 Exiting... Have a nice day!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("⚠️ Invalid choice. Please choose a number from 1 to 5.")
            continue

        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            op = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            op = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            op = "*"
        elif choice == '4':
            result = divide(num1, num2)
            op = "/"

        print(f"\n✅ Result: {num1} {op} {num2} = {result}")

calculator()
