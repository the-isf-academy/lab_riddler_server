######################################
#   This is a simple test file to ensure the 
#   RiddlerClient works properly. 
#
#   Add in your old tests to be confident 
#   each of your RiddlerClient methods work
######################################

from riddle_client import RiddlerClient

riddler_client = RiddlerClient()

print("--- TEST ALL RIDDLES ---")

all_riddles_json = riddler_client.all_riddles()

print(all_riddles_json)
print()

#############

print("--- TEST GUESS RIDDLES ---")

id = 17
guess = "to get to the other side"
guess_riddle_json = riddler_client.guess_riddle(id,guess)


print(guess_riddle_json)
