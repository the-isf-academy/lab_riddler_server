import requests
from view import View

class RequestsInterface():

    def __init__(self):
        self.riddle_server = 'http://sycs.student.isf.edu.hk/riddles/'
        self.view = View()

    def view_all_riddles(self):
        '''This functions sends a GET request to riddles/all.
        It gets all of the riddles and nicely formats them into a bulleted list.'''


        all_riddles_address = self.riddle_server + 'all'

        response = requests.get(all_riddles_address)

        if response.status_code == 200:
            all_riddles_json = response.json()
            self.view.all_riddles(all_riddles_json['riddles'])

        else:       
            self.error(response)


    def view_one_riddle(self, user_chosen_id):
        '''This function sends a GET request to riddles/one.
        It gets a single riddle with a specific ID and then formats it in a nice list.'''

        one_riddles_address = self.riddle_server + 'one'

        one_riddle_payload = {
            'id': user_chosen_id
        }

        response = requests.get(one_riddles_address, json=one_riddle_payload)

        if response.status_code == 200:
            one_riddle_json = response.json()

            if 'error' not in one_riddle_json:
                self.view.one_riddle(one_riddle_json['riddle'])

            else:
                self.error_json(one_riddle_json)

        else:
            self.error_no_json(response)



    def error_json(self, response_json):
        error_message = response_json['error']
        self.view.error_json(error_message)

    def error_no_json(self,response):
        self.view.error_status_code(response.status_code)