print('Learn your squares and cubes!')
# Main loop
while True:
    user_num = int(input('Enter an integer: '))
    print('Number\t\tSquared\t\tCubed')
    print('======\t\t=======\t\t=====')
    for i in range(user_num):
        number = i + 1
        print(f'{number}\t\t\t{number ** 2}\t\t\t{number ** 3}')
    times_table = input(f'Would you like to see a multiplication table for this? (y/n): ')
    if times_table.lower() == 'y' or times_table.lower() == 'yes':
        # Found on stack overflow, adjusted to my needs. I think I understand how it works.
        # I think formatting like this is easier on c++. We did stuff like this for a month straight.
        small_space = '  '
        big_space = '   '
        count = 0
        for i in range(1, user_num + 1):

            # This if/else statement guarantees correct spacing between single and double digits.
            if i > 9:
                small_space = small_space + str(i) + '   '
                big_space = big_space + str(i) + '|'
            else:
                small_space = small_space + str(i) + '    '
                big_space = big_space + str(i) + ' |'

            for a in range(1, user_num + 1):
                product = str(a * i)
                for letter in product:
                    count += 1
                big_space = big_space + product + ' ' * (5 - count)
                count = 0
            big_space = big_space + '\n   '

        print('\t' + small_space)  # Top number formatting
        print(' ' * 6 + ('-' + '    ') * user_num)
        print(big_space)
    loop = input('Continue? (y/n): ')
    if loop.lower() == 'n' or loop.lower() == 'no':
        break
print('I hope this helped you learn your squares and cubes, thanks for playing!')
