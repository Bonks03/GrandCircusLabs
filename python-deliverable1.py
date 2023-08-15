# Declaring Variables
# Starting currentHole at 1 so the while loop later looks nicer. Several ways to accomplish same result.
currentHole = 1
holeScore = 0
totalScore = 0
par = 0

playerName = input("Welcome to GC mini golf! What is your name? ")

# Struggled a lot with trying to incorporate the conditions into the While line, so a compromise was made.

while True:
    NumHoles = int(input(f"Hi, {playerName}! Would you like to play 3 or 6 holes today? "))
    if NumHoles == 3 or NumHoles == 6:
        break

while currentHole <= int(NumHoles):
    holeScore = int(input(f"How many putts for hole {currentHole}? (Par is 3) "))
    while holeScore < 1:    # Cannot have a score of 0
        holeScore = int(input(f"How many putts for hole {currentHole}? (Par is 3) "))
    currentHole +=1
    par +=3
    totalScore = holeScore + totalScore
if totalScore > par:
    print(f"Nice try, {playerName}... Your total score was: {totalScore - par}.")
elif totalScore < par:
    print(f"Great job, {playerName}! Your total score was: {totalScore - par}.")
else:
    print(f"Good game, {playerName}. Your total score was: 0.")