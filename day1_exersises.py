# Exercise 1: Echo String
text_input = input("Enter some text: ")
print(text_input)

# Exercise 2: Adding a number to an integer
number_input = input("Enter a number: ")
print(int(number_input) + 1)

# Exercise 3: Adding a number to a float
float_input1 = input("Enter a number: ")
print(int(float_input1) + .5)

# Exercise 4: Adding two floats
float_input1 = input("Enter a number: ")
float_input2 = input("Enter another number: ")
print(f"The sum is {float(float_input1) + float(float_input2)}")
# If they do add up to whole numbers there is always a decimal point

# Exercise 5: Multiplying floats
float_input1 = input("Enter a number: ")
float_input2 = input("Enter another number: ")
print(f"The product is {float(float_input1) * float(float_input2)}")
# Output doesn't handle exacts very well. Definitely need to cut off the decimals at some point
# Also, if they do divide into whole numbers there is always a decimal point

# Exercise 6: Dividing integers
int_input1 = input("Enter a number: ")
int_input2 = input("Enter another number: ")
print(f"The result is {int(int_input1) / int(int_input2)}")

# When the inputs don't divide evenly, the output is a float
# When the inputs are a decimal, there is an error because it is expecting an integer
# I presume to fix this error, you would either round or chop the decimal off entirely
