from riddle_client import RiddleClient
from gui_template import GUI
import customtkinter

class RiddleGUI(GUI):
    def __init__(self):
        # inherit all the properties and methods from the parent class
        super().__init__(app_title="Riddler",width=800, height=600)

        # create the riddle client object
        self.riddle_client = RiddleClient()
        

        # maps each menu button to the method it triggers
        self.menu_dictionary = {
            '👀 View All': lambda: self.view_all_riddles(),
            '¿ Guess ?': lambda: self.config_entry_widget(['id_widget','guess_widget'],'guess_submit'),
            '␡ Clear': lambda: self.clear()
        }

        # maps each entry_widget to its placeholder text
        self.entry_dictionary = {
            'id_widget': "Riddle ID",
            'guess_widget': "Guess",
        }

        # map each label_widget to its label
        self.label_dictionary = {
            'id_widget': "Enter Riddle ID",
            'guess_widget': "Enter Riddle Guess",
        }

        # maps each submit button with the method it triggers
        self.submit_button_dictionary = {
            'guess_submit': lambda: self.guess_riddle_submit(),
        }

        # creates a text box widget
        self.text_box = customtkinter.CTkTextbox(
            self.app,
            font=customtkinter.CTkFont(size=16),
            text_color="black",  
            corner_radius=10, 
        )

    def view_all_riddles(self):
        '''Controls when the user hits the 'views all' menu button'''

        self.clear()

        # uses the client to make HTTP get request to /all
        riddle_list = self.riddle_client.all_riddles()
        
        # loops through each riddle and adds to textbox
        for riddle in riddle_list:
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

        # uses the client to make HTTP post request to /guess
        guess_riddle_message = self.riddle_client.guess_riddle(id,guess) 

        # adds message to text box
        self.text_box.insert('end',f"{guess_riddle_message}")    
        
        self.display_text_box(row_num=4, height=50)