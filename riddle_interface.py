# requests_interface.py - controls HTTP requests to Riddle API 

import requests

class RiddlerInterface():

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
        
    def one_riddle(self, user_chosen_id):
        '''This function sends a POST request to riddles/one.'''

        one_riddle_address = self.riddle_server + 'one'

        payload = {
            'id': user_chosen_id,
        }

        response = requests.get(one_riddle_address, json=payload)

        if response.status_code == 200:
            one_riddle_json = response.json()

            if 'riddle' in one_riddle_json:
                return one_riddle_json['riddle']

            else:
                return one_riddle_json

        else:
            return f"HTTP error {response.status_code}"
        
    def new_riddle(self, new_question, new_answer):
        '''This function sends a POST request to riddles/guess.'''

        new_riddles_address = self.riddle_server + 'new'

        payload = {
            'question': new_question,
            'answer': new_answer
        }

        response = requests.post(new_riddles_address, json=payload)

        if response.status_code == 200:
            new_riddle_json = response.json()

            if 'riddle' in new_riddle_json:
                return "Successfully added riddle"

            else:
                return "Error adding riddle"

        else:
            return f"HTTP error {response.status_code}"
