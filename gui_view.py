from riddle_client import RiddleClient
from gui_template import GUI
import customtkinter
from random import shuffle

class RiddlerGUI(GUI):
    def __init__(self):
        # inherit all the properties and methods from the parent class
        super().__init__(app_title="Riddler",width=800, height=600)

        self.app.configure(fg_color="#2e446e")


        # create the riddler client object
        self.riddler_client = RiddleClient()
        
        # maps each entry_widget to its placeholder text
        self.entry_dictionary = {
            'id_widget': "Riddle ID",
            'guess_widget': "Guess",
            'question_widget': "Riddle Question",
            'answer_widget': "Riddle Answer"
        }

        # map each entry_widget to its label
        self.label_dictionary = {
            'id_widget': "Enter Riddle ID",
            'guess_widget': "Enter Riddle Guess",
            'question_widget': "Enter Riddle Question",
            'answer_widget': "Enter Riddle Answer",
        }

        # maps each submit button with the method it triggers
        self.submit_button_dictionary = {
            'guess_submit': lambda: self.guess_riddle_submit(),
            'view_one_submit': lambda: self.view_one_riddle_submit(),
            'new_submit': lambda: self.new_riddle_submit()
        }

        # map each menu button to its entry_widgets and submit button
        self.menu_dictionary = {
            '👀 View All': lambda: self.view_all_riddles(),
            '¿ Guess ?': lambda: self.config_entry_widget(['id_widget','guess_widget'],'guess_submit'),
            '👀 View One': lambda: self.config_entry_widget(['id_widget'],'view_one_submit'),
            '✨ Make New': lambda: self.config_entry_widget(['question_widget','answer_widget'],'new_submit'),
            '⌫ Clear': lambda: self.clear(),
            'game': lambda: self.play_game()
        }

        # creates a text box
        self.text_box = customtkinter.CTkTextbox(
            self.app,
            font=customtkinter.CTkFont(size=16),
            text_color="black",  
            corner_radius=10, 
            border_spacing=20
        )

    def view_all_riddles(self):
        '''Controls how the user views all riddles'''

        self.clear()

        parsed_riddle_list = self.riddler_client.all_riddles()
        
        # loops through each riddle
        for riddle in parsed_riddle_list:
            # adds riddle id and question to the text box
            self.text_box.insert('end', riddle)
            self.text_box.insert('end', f"\n\n")

        self.display_text_box(row_num=1, height=500)
    
    def guess_riddle_submit(self):
        '''Controls when the user clicks submit 
        for guess a riddle'''

        self.reset_textbox()

        # store input from entry widgets in variables
        id = self.entry_widgets['id_widget'].get()
        guess =self.entry_widgets['guess_widget'].get()

        guess_riddle_json = self.riddler_client.guess_riddle(id,guess) 

        if 'correct' in guess_riddle_json:
            if guess_riddle_json['correct'] == True:
                message = 'Correct!!'
            else:
                message = 'Incorrect'
        else:
            message = guess_riddle_json

        self.text_box.insert('end',f"{message}")    # adds message to text box
        
        self.display_text_box(row_num=4, height=50)


    def view_one_riddle_submit(self):
        '''Controls when the user clicks submit 
        for guess a riddle'''

        self.reset_textbox()

        id = self.entry_widgets['id_widget'].get()

        one_riddle_json = self.riddler_client.one_riddle(id)

        self.text_box.insert('end',f"{one_riddle_json}")    

        self.display_text_box(row_num=4, height=200)

    def new_riddle_submit(self):
        '''Controls when the user clicks submit 
        for guess a riddle'''

        self.reset_textbox()

        question = self.entry_widgets['question_widget'].get()
        answer = self.entry_widgets['answer_widget'].get()

        new_riddle_json = self.riddler_client.new_riddle(question, answer)

        if 'correct' in new_riddle_json:
            if new_riddle_json['correct'] == True:
                message = 'Correct!!'
            else:
                message = 'Incorrect'
        else:
            message = new_riddle_json

        self.text_box.insert('end',f"{message}")    # adds message to text box
        
        self.display_text_box(row_num=4, height=50)

    def play_game(self):
        self.clear()

        riddles_list = self.riddler_client.all_riddles()
        shuffle(riddles_list)

        for question in riddles_list:
            question = customtkinter.CTkLabel(
                self.app, 
                text = question, 
                fg_color="transparent")

            question.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=5)
   
gui = RiddlerGUI()
gui.run()