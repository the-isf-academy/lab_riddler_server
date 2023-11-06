# client.py - controls user interaction logic

from requests_interface import RequestsInterface
from view import View

client_running = True
requests_interface = RequestsInterface()
view = View()

view.welcome()

while client_running == True:

    user_choice = view.menu(
        prompt = "Menu:",
        options = [
                'View All Riddles',
                'Guess Riddle',
                'Quit']
                )

    if user_choice == 'View All Riddles':
        requests_interface.all_riddles()

    elif user_choice == 'Guess Riddle':
        user_chosen_id =  view.get_input('Enter Riddle ID')
        user_guess=  view.get_input('Enter guess')

        requests_interface.guess_riddle(user_chosen_id, user_guess)


    elif user_choice == 'Quit':
        client_running = False
        view.quit()
  
