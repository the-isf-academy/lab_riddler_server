from tkinter import font
import customtkinter
from api_client import RiddlerInterface
from template_gui import GUI

class RiddlerGUI(GUI):
    def __init__(self):
        super().__init__()
        self.riddler_interface = RiddlerInterface()
        
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
            'guess_submit': self.guess_riddle_submit,
            'view_one_submit': self.view_one_riddle_submit,
            'new_submit': self.new_riddle_submit
        }

        # map each menu button to its entry_widgets and submit button
        self.menu_dictionary = {
            'view all': self.view_all_riddles,
            'guess': lambda: self.config_entry_widget(['id_widget','guess_widget'],'guess_submit'),
            'one': lambda: self.config_entry_widget(['id_widget'],'view_one_submit'),
            'new': lambda: self.config_entry_widget(['question_widget','answer_widget'],'new_submit'),
            'clear': self.clear,
        }

    def view_all_riddles(self):
        '''Controls how the user views all riddles'''

        self.clear()

        all_riddles_json = self.riddler_interface.all_riddles()
        
        # loops through each riddle
        for riddle_dict in all_riddles_json:
            # adds riddle id and question to the text box
            self.text_box.insert('end', f"{riddle_dict['id']}# {riddle_dict['question']}")
            self.text_box.insert('end', f"\n\n")

        self.display_text_box(row_num=1, height=500)
    
    def guess_riddle_submit(self):
        '''Controls when the user clicks submit 
        for guess a riddle'''

        self.reset_textbox()

        guess_riddle_json = self.riddler_interface.guess_riddle(
            self.entry_widgets['id_widget'].get(), 
            self.entry_widgets['guess_widget'].get())

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

        one_riddle_json = self.riddler_interface.one_riddle(self.entry_widgets['id_widget'].get())

        self.text_box.insert('end',f"{one_riddle_json}")    

        self.display_text_box(row_num=4, height=200)

    def new_riddle_submit(self):
        '''Controls when the user clicks submit 
        for guess a riddle'''

        self.reset_textbox()

        new_riddle_json = self.riddler_interface.new_riddle(
            self.entry_widgets['question_widget'].get(), 
            self.entry_widgets['answer_widget'].get())

        if 'correct' in new_riddle_json:
            if new_riddle_json['correct'] == True:
                message = 'Correct!!'
            else:
                message = 'Incorrect'
        else:
            message = new_riddle_json

        self.text_box.insert('end',f"{message}")    # adds message to text box
        
        self.display_text_box(row_num=4, height=50)
   
gui = RiddlerGUI()
gui.run()