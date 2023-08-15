import math

print("Hello World!")

# Declaring Variables
my_name = "Nathan Bonkowski"
work_from_home = False
side = 15
radius = 10
square_area = side**2
square_perimeter = side * 4
circle_area = math.pi * radius**2
circle_circumference = math.pi * 2 * radius
travel_options = ["foot", "bike", "car", "airplane"]

# Printing information
print("My name is " + str(my_name))
print("I work from home: " + str(work_from_home))
print("\nThe length of each side of the square is " + str(side))
print("The radius of the circle is " + str(radius))

# Practice using f-string
print(f"The square area is {square_area} and the perimeter is {square_perimeter}")
print(f"The circle area is {circle_area} and the circumference is {circle_circumference}")

# Travel problem
print("\nThe travel options are:", f" \n1) {travel_options[0]}")
print(f"2) {travel_options[1]}")
print(f"3) {travel_options[2]}")
print(f"4) {travel_options[3]}")
distance = 100
time = 0
cost = 0
speed = 0
travel_type = input("How would you like to travel? ")
print(f"Travel type: {travel_type}")
if travel_type == "foot":
    speed = 3
    print(f"Walking is free! Speed is {speed}mph.")
    cost = 0
    time = distance / speed
elif travel_type == "bike":
    speed = 10
    rent_bike = input("Do you need to rent a bike? (yes or no): ")
    if rent_bike == "yes":
        print(f"Bike rental is $45! Speed is {speed}mph")
        cost = 45
    else:
        print(f"Biking is free! Speed is {speed}mph.")
        cost = 0
    time = distance / speed
elif travel_type == "car":
    speed = 60
    print(f"Driving is $0.25/mi. Speed is {speed}mph.")
    cost = 0.25 * distance
    time = distance / speed
elif travel_type == "airplane":
    speed = 400
    print(f"Flying is $0.10/mi per passenger. Speed is {speed}mph.")
    passenger_count = int(input("How many passengers? "))
    cost = .10 * distance * passenger_count
    time = distance / speed
else:
    print(f"Sorry. {travel_type} is an invalid option.")
    exit()

print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")

# Progress Bars
cost_bar = "Cost: "
time_bar = "Time: "
time = math.ceil(time)
cost = math.ceil(cost)
for i in range(cost):
    cost_bar += "$"
for i in range(time):
    time_bar += "/"
print(f"{time_bar} \n{cost_bar}")
