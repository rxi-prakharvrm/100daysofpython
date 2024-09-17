a = input("Enter a number: ")

try:
    # Check if input is a number
    if a.isdigit():
        print("You entered a number.")
    # Check for special keywords
    elif a.lower() == 'q' or a.lower() == 'quit' or a.lower() == 'exit':
        print("You entered a special keyword.")
    # If input is neither a number nor a special keyword, raise ValueError
    else:
        raise ValueError("You must enter a number or a special keyword.")
except ValueError as e:
    print(e)
