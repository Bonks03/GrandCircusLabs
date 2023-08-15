# Declaring variables
appleCount = 0
grapeCount = 0
orangeCount = 0

# Customer greeting
customerName = input(f"Welcome to the GC Fruit Market!\nWhat is your Name?\n> ")

# Loop to query customer until they stop
while True:
    print(f"Welcome {customerName}. Which fruit would you like to buy?")
    print("1. Apple $2 \n2. Grape $1 \n3. Orange $3")
    fruitChoice = input("> ")
    if fruitChoice == '1' or fruitChoice.lower() == 'apple':
        print("You bought an apple at $2")
        appleCount += 1
    elif fruitChoice == '2' or fruitChoice.lower() == 'grape':
        print("You bought a grape at $1")
        grapeCount += 1
    elif fruitChoice == '3' or fruitChoice.lower() == 'orange':
        print("You bought an orange at $3")
        orangeCount += 1
    else:
        print("Sorry, I don't understand your request. Please try again.")
    # A good programmer would add a "fool-proofing" statement to the following if statement
    if input(f"Would you like to buy another piece of fruit? y/n ") == 'n':
        break

# Printing Receipt
print(f"Order for {customerName} \n{appleCount} apple(s) at $2 apiece"
      f"\n{grapeCount} grape(s) at $1 apiece"
      f"\n{orangeCount} orange(s) at $3 apiece")

subtotal = (appleCount * 2)+(grapeCount * 1)+(orangeCount * 3)
tax = subtotal * 0.05

# [<variable>:.2f] formats to 2 decimals no matter what. Makes more sense for money
print(f"Sub Total: ${subtotal} \n5% Tax: ${tax:.2f}"
      f"\nTotal: ${subtotal + tax:.2f}")
