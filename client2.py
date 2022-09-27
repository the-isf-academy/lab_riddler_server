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
    

    def start(self):
        '''This function runs the client.'''

        print("-"*35)
        print("---- Welcome to the Riddler ----")
        print("-"*35,"\n")

        client_running = True

        while client_running == True:
            user_choice = self.menu()

            if user_choice == 'View All Riddles':
                print('[View All Riddles]')
                self.view_all_riddles()

            elif user_choice == 'View One Riddle':
                print('[View One Riddle]')
                self.view_one_riddle()

            elif user_choice == 'Guess a Riddle':
                print('[Guess a Riddle]')
                user_id = int(input('Enter Riddle ID: '))
                user_guess = input('Enter your guess: ')

                self.guess_riddle(user_id, user_guess)

            elif user_choice == 'New Riddle':
                self.new_riddle()

            elif user_choice == 'Play Game':
                self.game()

            elif user_choice == 'Quit':
                client_running = False

                print("="*75)


            print()

    def menu(self):
        '''This function creates an interactive Terminal menu.'''

        terminal_menu = TerminalMenu(self.menu_options) #Creates the Terminal Menu
        option_num = terminal_menu.show() #Get user selected Option

        return self.menu_options[option_num]

    def view_all_riddles(self):
        all_riddles_address = self.riddle_server + 'riddles/all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            
            for riddle in all_riddles_json['riddles']:
                print("  • {}".format(riddle['question']))
        else:
            print('Server {} Error. Try again...'.format(response.status_code))

    def view_one_riddle(self):
        one_riddles_address = self.riddle_server + 'riddles/one'

        user_id = int(input('Enter Riddle ID: '))
        one_riddle_payload = {
            'id': user_id
        }

        response = requests.get(one_riddles_address, json=one_riddle_payload)

        if response.status_code == 200:
            one_riddle_json = response.json()

            for key, value in one_riddle_json.items():
                print("  • {}: {}".format(key,value))

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
       
    def new_riddle(self):
        new_riddle_address = self.riddle_server + 'riddles/new'

        user_question = input('Enter a Riddle question: ')
        user_answer = input('Enter the answer: ')


        new_riddle_payload = {
            'question': user_question,
            'answer': user_answer
        }

        response = requests.post(new_riddle_address, json=new_riddle_payload)

        if response.status_code == 200:
            new_riddle_response_json = response.json()

            print('Riddle Successfully Added!')
            for key, value in new_riddle_response_json.items():
                print("  • {}: {}".format(key,value))

        else:
            print('Server {} Error. Try again...'.format(response.status_code))
       

    def game(self):
        all_riddles_address = self.riddle_server + 'riddles/all'

        response = requests.get(all_riddles_address)

  

        if response.status_code == 200:
            all_riddles_json = response.json()
            
            for riddle in all_riddles_json['riddles']:
                print('Question: {}'.format(riddle['question']))
                user_guess = input('Enter your guess: ')

                self.guess_riddle(riddle['id'], user_guess)

                print()

        else:
            print('Server {} Error. Try again...'.format(response.status_code))

if __name__ == "__main__":
    network_server= "http://riddles.student.isf.edu.hk/"
    local_server = "http://127.0.0.1:5000/"

    client = RiddleClient(local_server)
    client.start()







