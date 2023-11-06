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
                'View One Riddle',
                'Guess A Riddle',
                'Quit']
                )

    if user_choice == 'View All Riddles':
        requests_interface.all_riddles()

    elif user_choice == 'View One Riddle':
        user_chosen_id =  view.get_input('Enter Riddle ID')
        requests_interface.one_riddle(user_chosen_id)


    elif user_choice == 'Quit':
        client_running = False
        view.quit()
  
