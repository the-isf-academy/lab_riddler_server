# riddle_client.py - controls HTTP requests to Riddle API 

import requests

class RiddleClient():

    def __init__(self):
        self.riddle_server = 'http://sycs.student.isf.edu.hk/riddle/'

    def all_riddles(self):
        '''This functions sends a GET request to riddles/all.'''

        # stores the full address for /all
        all_riddles_address = self.riddle_server + 'all'

        # makes HTTP GET request 
        response = requests.get(all_riddles_address)

        # checks if request is successful
        if response.status_code == 200:

            # stores the response JSON
            all_riddles_json = response.json()

            parsed_riddle_list = []

            for riddle_dict in all_riddles_json['riddles']:
                parsed_riddle_list.append(f"{riddle_dict['id']}# {riddle_dict['question']}")

            # returns the list of riddles 
            return parsed_riddle_list

        else:     
            # returns HTTP error code, if request is unsuccessful
            return f"HTTP error {response.status_code}"


    def guess_riddle(self, user_chosen_id, user_guess):
        '''This function sends a POST request to riddles/guess.'''

        # stores the full address for /guess
        guess_riddles_address = self.riddle_server + 'guess'

        # stores the payload in a dictionary
        payload = {
            'id': user_chosen_id,
            'guess': user_guess
        }

        # makes HTTP POST request with the payload
        response = requests.post(guess_riddles_address, json=payload)


        if response.status_code == 200:
            guess_riddle_json = response.json()

            # parse response JSON
            if 'riddle' in guess_riddle_json:
                parsed_messaged = ""

                if guess_riddle_json['riddle']['correct'] == True:
                    parsed_messaged = 'Correct!!!'

                else:
                    parsed_messaged = 'Incorrect ;('
                
                return parsed_messaged

            else:
                return guess_riddle_json['error']

        else:
            return f"HTTP error {response.status_code}"
        