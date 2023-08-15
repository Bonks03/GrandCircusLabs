students = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]


def list_names(student_list):
    index = 0
    for name in student_list:
        index += 1
        print(f'{index}. {name}')


def get_new_student():
    new_name = input(f'Please input a name for the new student: \n> ')
    new_town = input(f'Next please input their hometown: \n> ')
    new_food = input(f'Last please input their favorite food: \n> ')
    new_entry = {"name": new_name.capitalize(), "hometown": new_town.capitalize(), "favorite_food": new_food.capitalize()}
    return new_entry


while True:
    student_names = []

    for i in students:
        for j in i:
            if j == 'name':
                student_names.append(i[j])

    action = input(f"Please select which action you'd like to do: add, view, or quit \n> ")
    if action.lower() == 'add':
        new_student = get_new_student()
        students.append(new_student)

    elif action.lower() == "view":
        list_names(student_names)
        choice = int(input(f'Which student would you like to learn more about? '
                           f'Enter a number 1-{len(student_names)}: \n> '))
        if choice > len(student_names):
            choice = int(input(f'That is an invalid number, please try again. \n'
                               f'Enter a number 1-{len(student_names)}: \n>'))
        print(f'Student {choice} is {student_names[(choice - 1)]}. What would you like to know?')
        info_choice = input(f'Enter "hometown" of "favorite food" \n> ')
        while True:
            if info_choice.lower() == 'hometown':
                print(f'{student_names[(choice - 1)]} is from {students[choice - 1]["hometown"]}.')
                break
            elif info_choice.lower() == 'favorite food' or info_choice.lower() == 'food':
                print(f"{student_names[(choice - 1)]}'s favorite food is {students[choice - 1]['favorite_food']}.")
                break
            else:
                print(f'{info_choice} is an invalid input. Please try again.')
                info_choice = input(f'Enter "hometown" of "favorite food" \n> ')

    elif action.lower() == 'quit':
        break

    else:
        print(f'{action} is not a valid input. Please try again.')

print('Good bye!')
