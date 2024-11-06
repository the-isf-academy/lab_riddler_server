# riddle_client.py - controls HTTP requests to Riddle API 

import requests

class RiddleClient():

    def __init__(self):
        self.riddle_server = 'http://sycs.student.isf.edu.hk/riddle/'

    def all_riddles(self):
        '''This functions sends a GET request to riddles/all.'''

        all_riddles_address = self.riddle_server + 'all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            return all_riddles_json['riddles']

        else:     
            return f"HTTP error {response.status_code}"


    def guess_riddle(self, user_chosen_id, user_guess):
        '''This function sends a POST request to riddles/guess.'''

        guess_riddles_address = self.riddle_server + 'guess'

        payload = {
            'id': user_chosen_id,
            'guess': user_guess
        }

        response = requests.post(guess_riddles_address, json=payload)

        if response.status_code == 200:
            guess_riddle_json = response.json()

            if 'riddle' in guess_riddle_json:
                return guess_riddle_json['riddle']

            else:
                return guess_riddle_json

        else:
            return f"HTTP error {response.status_code}"
        