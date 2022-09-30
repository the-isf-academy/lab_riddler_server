import requests
from simple_term_menu import TerminalMenu



class RiddleClient():

    def __init__(self, server_address):
        self.riddle_server = server_address

        self.menu_options = [
                'View All Riddles',
                'View One Riddle',
                'Guess a Riddle',
                'New Riddle',
                'Play Game',
                'Quit']
    
    def menu(options):
        '''This function creates an interactive Terminal menu.'''

        terminal_menu = TerminalMenu(options) #Creates the Terminal Menu
        option_num = terminal_menu.show() #Get user selected Option

        return options[option_num]

    def start(self):
        '''This function runs the client.'''

        print("-"*35)
        print("---- Welcome to the Riddler ----")
        print("-"*35,"\n")

        client_running = True

        while client_running == True:
            user_choice = self.menu(self.menu_options)

            if user_choice == 'View All Riddles':
                print('[View All Riddles]')

                self.view_all_riddles()

            elif user_choice == 'Guess a Riddle':
                print('[Guess a Riddle]')

                user_id = int(input('Enter Riddle ID: '))
                user_guess = input('Enter your guess: ')

                self.guess_riddle(user_id, user_guess)

            elif user_choice == 'Quit':
                client_running = False
                print("="*75)

            print()


    def view_all_riddles(self):
        '''This function is responsible for hitting the riddles/all endpoint. 
        It gets all of the riddles and nicely formats them into a bulletted list '''

        all_riddles_address = self.riddle_server + 'riddles/all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            
            for riddle in all_riddles_json['riddles']:
                print("  • {}".format(riddle['question']))
        else:
            print('Server {} Error. Try again...'.format(response.status_code))


    def guess_riddle(self, user_id, user_guess):
        guess_riddle_address = self.riddle_server + 'riddles/guess'

        guess_riddle_payload = {
            'id': user_id,
            'guess': user_guess
        }

        response = requests.post(guess_riddle_address, json=guess_riddle_payload)

        if response.status_code == 200:
            guess_riddle_response_json = response.json()

            if guess_riddle_response_json['correct'] == True:
                print('Correct!')
            else:
                print('Incorrect!')

        else:
            print('Server {} Error. Try again...'.format(response.status_code))
       



if __name__ == "__main__":
    network_server= "http://riddles.student.isf.edu.hk/"

    client = RiddleClient(network_server)

    client.start()







