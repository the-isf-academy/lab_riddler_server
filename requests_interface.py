# requests_interface.py - controls HTTP requests to Riddle API 

import requests
from view import View

class RequestsInterface():

    def __init__(self):
        self.riddle_server = 'http://sycs.student.isf.edu.hk/riddles/'
        self.view = View()

    def all_riddles(self):
        '''This functions sends a GET request to riddles/all.'''

        all_riddles_address = self.riddle_server + 'all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            self.view.all_riddles(all_riddles_json['riddles'])

        else:       
            self.error(response)


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

            if 'error' not in guess_riddle_json:
                self.view.guess_riddle(guess_riddle_json['riddle'])

            else:
                self.error_json(guess_riddle_json)

        else:
            self.error_no_json(response)



    def error_json(self, response_json):
        error_message = response_json['error']
        self.view.error_json(error_message)

    def error_no_json(self,response):
        self.view.error_no_json(response.status_code)