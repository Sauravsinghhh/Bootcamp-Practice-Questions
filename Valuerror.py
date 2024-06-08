def get_valid_integer():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            user_int = int(user_input)
            print(f"Thank you! You entered the integer: {user_int}")
            break  
        except ValueError:
            print("That's not a valid integer. Please try again.")

get_valid_integer()
