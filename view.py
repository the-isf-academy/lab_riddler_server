from InquirerPy import inquirer, get_style        


class View:

    def menu(self, prompt, options):
            # This function creates an interactive Terminal menu.
            # it returns the selected Node 

            choice = inquirer.select(
                message= f"\n{prompt}",
                choices= options,
                qmark="",
                amark="",
                style= get_style({ 
                    "answer": "#438fa8",
                    "pointer": "#438fa8",
                    "questionmark": "hidden"},

                    ),
                ).execute()

            return choice

    def get_input(self, prompt):
        user_chosen_id = input(f'{prompt}: ')
        return user_chosen_id

    def welcome(self):
        print("-"*35)
        print("---- Welcome to the Riddler ----")
        print("-"*35,"\n")

    def all_riddles(self, all_riddles):
        print('\n[View All Riddles]')

        for riddle in all_riddles:
                print(f"  • {riddle['question']} (#{riddle['id']})")

    def one_riddle(self, one_riddle):
        print('\n[View One Riddle]')

        for key, value in one_riddle.items():
            print(f"  • {key}: {value}")

    def error_json(self, error_message):
        print(f'\n[Error: {error_message}]')

        
    def error_no_json(self, status_code):
        print(f'\n[Error: HTTP {status_code}]')

    def quit(self):
        print("="*50)





