user_name = input("Welcome to Number Analyzer! Please enter your first name: ")
while True:
    user_num = int(input(f"Hello {user_name}! Enter a number between 1 and 100: "))
    if user_num % 2 == 1 and user_num < 60:
        print(f"{user_num} is odd and less than 60.")
    elif user_num % 2 == 0 and 2 <= user_num <= 24:
        print(f"{user_num} is even and less than 25.")
    elif user_num % 2 == 0 and 26 <= user_num <= 60:
        print(f"{user_num} is even and between 26 and 60 inclusive.")
    elif user_num % 2 == 1 and user_num > 60:
        print(f"{user_num} is odd and greater than 60.")
    else:
        print("Your input is invalid.")
        # This validation check only works for ints
        # I could add one for strings, but it would be messy
    user_repeat = input(f"Would you like to try again {user_name}? (y/n): ")
    if user_repeat.lower() == "n" or user_repeat.lower() == "no":
        break
print(f"Thank you for playing Number Analyzer, {user_name}!")
