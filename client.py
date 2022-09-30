import requests
from simple_term_menu import TerminalMenu


class RiddleClient():

    def __init__(self, server_address):
        self.riddle_server = server_address

        self.menu_options = [
                'View All Riddles',
                'View One Riddle',
                'Quit']
    
    def menu(self,options):
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

            elif user_choice == 'View One Riddle':
                print('[View One Riddle]')

                user_chosen_id = int(input('Enter Riddle ID: '))

                self.view_one_riddle(user_chosen_id)

            elif user_choice == 'Quit':
                client_running = False

                print("="*75)


            print()

    

    def view_all_riddles(self):
        '''This functions sends a GET request to riddles/all.
        It gets all of the riddles and nicely formats them into a bulletted list.'''

        all_riddles_address = self.riddle_server + 'riddles/all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            
            for riddle in all_riddles_json['riddles']:
                print("  • {} (#{})".format(riddle['question'], riddle['id']))
        else:
            print('Server {} Error. Try again...'.format(response.status_code))

    def view_one_riddle(self, user_chosen_id):
        '''This function sends a GET request to riddles/one.
        It gets a single riddle with a specific ID and then formats it in a nice list.'''

        one_riddles_address = self.riddle_server + 'riddles/one'

        one_riddle_payload = {
            'id': user_chosen_id
        }

        response = requests.get(one_riddles_address, json=one_riddle_payload)

        if response.status_code == 200:
            one_riddle_json = response.json()

            for key, value in one_riddle_json.items():
                print("  • {}: {}".format(key,value))

        else:
            print('Server {} Error. Try again...'.format(response.status_code))

       



if __name__ == "__main__":
    network_server= "http://riddles.student.isf.edu.hk/"

    client = RiddleClient(network_server)

    client.start()







