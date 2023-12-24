import random
import matplotlib.pyplot as plt
import qrandom


def montyHall():
    global winCounter, lossCounter


    # creates 3 "doors" where a door with a value of true is a winning door
    doorZero = False
    doorOne = False
    doorTwo = False

    doors = [doorZero, doorOne, doorTwo]

    ## pseudorandomly assigns a door to be the winning door
    doors[random.randrange(0, 3)] = True

    ## if this is true, the "player" in the simulation will always switch their door
    ## otherwise they keep their initial choice
    switchBool = True

    ## has the "player" select a door (either door 0, 1 or 2)
    doorSelection = random.randrange(0, 3)

    ## eliminates one of the losing (false) doors by setting it to null (or none cause this is python lol)
    for i in range(3):
        if i != doorSelection and doors[i] != True:
            doors[i] = None
            break

    ## if the player is switching, finds the first non-null door (so a door thats not been eliminated)
    ## and makes that the new selection
    if switchBool:
        for i in range(3):
            if doors[i] is not None and i != doorSelection:
                doorSelection = i
                break

    ## increases apropriate counters based on win or loss value
    if doors[doorSelection]:
        winCounter += 1
    else:
        lossCounter += 1



## runs the program n number of times
n = 1000000 # number of trials to run
winCounter = 0
lossCounter = 0
for _ in range(n):
    montyHall()

print("Number of wins: ", winCounter)
print("Number of losses: ", lossCounter)

# Values to plot
values = [winCounter, lossCounter]

# Labels for each bar
labels = ['# Wins', '# Losses']

# Creating the bar chart
plt.bar(labels, values)

# Adding title and labels
plt.title('Chart of # of wins vs losses')
# plt.xlabel('')
# plt.ylabel('')

# Displaying the plot
plt.show()