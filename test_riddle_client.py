######################################
#   This is a simple test file to ensure the 
#   RiddleClient works properly. 
#
#   Add in your old tests to be confident 
#   each of your RiddleClient methods work
######################################

from riddle_client import RiddleClient

riddle_client = RiddleClient()

print("--- TEST ALL RIDDLES ---")

riddle_list = riddle_client.all_riddles()

for riddle in riddle_list:
    print(riddle)

print()

#############

print("--- TEST GUESS RIDDLES ---")

id = 17
guess = "to get to the other side"
guess_riddle_message = riddle_client.guess_riddle(id,guess)


print(guess_riddle_message)

print()