def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

# Function to display results based on user input
def display_logic_gate():
    print("Choose a logic gate to display:\n1. AND Gate\n2. OR Gate\n3. NOT Gate")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        # AND Gate
        a = int(input("Enter first input (0 or 1): "))
        b = int(input("Enter second input (0 or 1): "))
        result = and_gate(a, b)
        print(f"AND Gate Result: {a} AND {b} = {int(result)}")

    elif choice == '2':
        # OR Gate
        a = int(input("Enter first input (0 or 1): "))
        b = int(input("Enter second input (0 or 1): "))
        result = or_gate(a, b)
        print(f"OR Gate Result: {a} OR {b} = {int(result)}")

    elif choice == '3':
        # NOT Gate
        a = int(input("Enter input (0 or 1): "))
        result = not_gate(a)
        print(f"NOT Gate Result: NOT {a} = {int(result)}")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
display_logic_gate()
