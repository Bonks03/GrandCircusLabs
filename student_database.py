name_list = ('Sophia Petrillo', 'Rose Nylund', 'Blanche Devereaux', 'Nathan Bonkowski')
hometown_list = ('Sicily', 'Chicago', 'Atlanta', 'Wyandotte')
fav_food_list = ('pasta', 'cupcakes', 'barbecue', 'pizza')
user_name = input('Welcome! What is your name?\n>')

# Main loop
while True:
    student_choice = int(input(f'Hello {user_name.capitalize()}, which student would you like to learn more about? '
                               f'Enter a number 1-{len(name_list)} or 0 to see list:\n>'))
    # Display all names
    if student_choice == 0:
        for name in name_list:
            print(name)
        student_choice = int(input(f'Which student would you like to learn more about?\n>'))
    # Validate user number
    if student_choice > 4 or student_choice < 0:
        print(f'That is an invalid input, please try again.')
    # Continue if input is valid
    else:
        index = int(student_choice) - 1
        print(f'Student {student_choice} is {name_list[index]}. What would you like to know?')
        # Loop to validate category
        while True:
            info_choice = input(f'Enter "hometown" or "favorite food"\n>')
            if info_choice.lower() == 'hometown' or info_choice.lower() == 'home town':
                print(f"{name_list[index]} is from {hometown_list[index]}")
                break
            elif info_choice.lower() == 'favorite food' or info_choice.lower() == 'food':
                print(f"{name_list[index]}'s favorite food is {fav_food_list[index]}.")
                break
            else:
                print(f'"{info_choice}" is not a valid category, please try again.')
    # Ask user if they would like to repeat
    loop = input(f'Would you like to learn about another student? Enter "y" or "n"\n>')
    if loop.lower() == 'n' or loop.lower() == 'no':
        break
print(f'Thank you for playing, {user_name}!')
