import math, numpy, random, time, getpass # normal python stuff

from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, S, T, X, CNOT, Entangle, get_inverse, Measure  # import the operations we want to perform

import projectq.setups.ibm
from projectq.backends import IBMBackend

eng = MainEngine(IBMBackend(use_hardware=True, num_runs=1024, verbose=False, user=None, password=None))

print("\n\n\n\n===== Welcome to Quantum Battleships! =====\n\n")
print("  ~~ A game by the Decodoku project ~~ ")
print("\n\n")
print("When in doubt, press any key to continue!")
raw_input()
print("This is a game for two players.")
raw_input()
print("Player 1 will choose the position of a Battleship.")
raw_input()
print("Player 2 will try to bomb it.")
raw_input()

# get player 1 to position boat
print("We start with Player 1.")
print("Look away Player 2!")
raw_input()
print("The lines in the bowtie shape below are the places you can place your ship.\n")
print("|\     /|")
print("| d   b |")
print("|  \ /  |")
print("f   X   a")
print("|  / \  |")
print("| e   c |")
print("|/     \|\n")
# note: at time of release, ProjectQ does not actually put the qubits in the places you'd expect on the IBM chip
raw_input()

chosen = 0
while (chosen==0):
	ship = getpass.getpass("Choose a line for your ship. (a, b, c, d, e or f)\n")
	if ship in ["a","b","c","d","e","f"]:
		chosen = 1
	else:
		print("u wot m8? Try that again.")

# get player 2 to position three bombs
time.sleep(1)
print("\nPlayer 2: You're up!")
raw_input()
print("The numbers below mark places you can bomb.\n")
print("4       0")
print("|\     /|")
print("| \   / |")
print("|  \ /  |")
print("|   2   |")
print("|  / \  |")
print("| /   \ |")
print("|/     \|")
print("3       1\n")
raw_input()

chosen = 0
while (chosen==0):
    bomb1 = int(raw_input("Choose a position for your first bomb. (0, 1, 2, 3 or 4)\n"))
    if ( (bomb1 >= 0) & (bomb1 < 5) ):
        chosen = 1
    else:
        print("u wot m8? Try that again.")

chosen = 0
while (chosen==0):
    bomb2 = int(raw_input("\nChoose a position for your second bomb. (0, 1, 2, 3 or 4)\n"))
    if ( (bomb1 >= 0) & (bomb1 < 5) ):
        if (bomb2 != bomb1):
            chosen = 1
        else:
            print("That's already been bombed. Choose again.")
    else:
        print("u wot m8? Try that again.")

chosen = 0
while (chosen==0):
    bomb3 = int(raw_input("\nChoose a position for your third and final bomb. (0, 1, 2, 3 or 4)\n"))
    if ( (bomb1 >= 0) & (bomb1 < 5) ):
        if bomb3 not in [bomb1,bomb2]:
            chosen = 1
        else:
            print("That's already been bombed. Choose again.")
    else:
        print("u wot m8? Try that again.")

# now all that's left is to run the scenario on the qubits and see what happens
print("\nWe'll now run this scenario on IBM's qubits and see what happens.")
raw_input()
print("But first you'll have to sign in...\n")


# prepare qubits
qubits = eng.allocate_qureg(5)

# make the ship: an entangled pairs prepared for a CHSH experiment
# first we make a Bell pair with H and CNOT
# then use an X to anticocorrelate Z basis (measurements will be made in x-y plane)
# then do a T on any Bobs (higher numbered qubit)
bobs = [0]*5 
if (ship == "a"): # a means 0 and 1
	H | qubits[0]
	CNOT | (qubits[0], qubits[1])
	X | qubits[0]
	bobs[0] = 1
	T | qubits[0]
if (ship == "b"): # b means 0 and 2
	H | qubits[0]
	CNOT | (qubits[0], qubits[2])
	X | qubits[0]
	bobs[0] = 1
	T | qubits[0]
if (ship == "c"): # c means 1 and 2
	H | qubits[1]
	CNOT | (qubits[1], qubits[2])
	X | qubits[1]
	bobs[1] = 1
	T | qubits[1]
if (ship == "d"): # d means 2 and 4
	H | qubits[4]
	CNOT | (qubits[4], qubits[2])
	X | qubits[4]
	bobs[2] = 1
	T | qubits[2]
if (ship == "e"): # e means 2 and 3
	H | qubits[3]
	CNOT | (qubits[3], qubits[2])
	X | qubits[3]
	bobs[2] = 1
	T | qubits[2]
if (ship == "f"): # f means 3 and 4
	H | qubits[3]
	CNOT | (qubits[3], qubits[4])
	X | qubits[3]
	bobs[3] = 1
	T | qubits[3]

# apply the bombs
# whether or not a bomb is applied corresponds to the two measurment choices for CHSH (in x-y plane)
if (bobs[bomb1]==1):
	get_inverse(S) | qubits[bomb1]
else:
	S | qubits[bomb1]
if (bobs[bomb2]==1):
	get_inverse(S) | qubits[bomb2]
else:
	S | qubits[bomb2]

# measure all in X basis
H | qubits[0]
Measure | qubits[0]
H | qubits[1]
Measure | qubits[1]
H | qubits[2]
Measure | qubits[2]
H | qubits[3]
Measure | qubits[3]
H | qubits[4]
Measure | qubits[4]

eng.flush()  # flush all gates (and execute measurements)

time.sleep(1)
print("\nNow let's see how intact the ship is.")
print("Between 1% and 100% intact means it's still afloat.")
print("Between -1% and -100% intact means it's swimming with the fishes.")
print("0% intact could go either way.")

results = eng.backend.get_probabilities(qubits) # get probabilities
# fill in mising values
for b1 in range(2):
	for b2 in range(2):
		for b3 in range(2):
			for b4 in range(2):
				for b5 in range(2):
					bitString = str(b1) + str(b2) + str(b3) + str(b4) + str(b5)
					if bitString not in results:
						results[bitString] = 0

# determine damage for ship
damage = 0
for b1 in range(2):
	for b2 in range(2):
		for b3 in range(2):

			if (ship == "a"): # a means 0 and 1
				damage = damage + results[ "01" + str(b1) + str(b2) + str(b3) ] + results[ "10" + str(b1) + str(b2) + str(b3) ]
			if (ship == "b"): # b means 0 and 2
				damage = damage + results[ "0" + str(b1) + "1" + str(b2) + str(b3) ] + results[ "1" + str(b1) + "0" + str(b2) + str(b3) ]
			if (ship == "c"): # c means 1 and 2
				damage = damage + results[ str(b1) + "01" + str(b2) + str(b3) ] + results[ str(b1) + "10" + str(b2) + str(b3) ]
			if (ship == "d"): # d means 2 and 4
				damage = damage + results[ str(b1) + str(b2) + "0" + str(b3) + "1" ] + results[ str(b1) + str(b2) + "1" + str(b3) + "0" ]
			if (ship == "e"): # e means 2 and 3
				damage = damage + results[ str(b1) + str(b2) + "01" + str(b3) ] + results[ str(b1) + str(b2) + "10" + str(b3) ]
			if (ship == "f"): # f means 3 and 4
				damage = damage + results[ str(b1) + str(b2) + str(b3) + "01" ] + results[ str(b1) + str(b2) + str(b3) +"10" ]


time.sleep(1)
print("\nThe ship is " + str(int( 100*(1-2*damage) )) + "% intact")
print("(which means " + str(int( -100*(1-2*damage) )) + "% broken).\n")
if (damage>0.5):
	print("It has been destroyed!\nPlayer 2 wins!\n\n")
else:
    print("It's still afloat!\nPlayer 1 wins!\n\n")




