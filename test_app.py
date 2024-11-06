from tkinter import font
import customtkinter
from riddle_client import RiddlerInterface

class RiddleGUI:
    def __init__(self):

        self.riddler_interface = RiddlerInterface()

        # Create and Setup the application window 
        self.app = customtkinter.CTk()
        self.app.geometry("600x400")
        self.app.title("Riddler Client")

        # columns use space available
        self.app.grid_columnconfigure((0,1,2), weight=1)

        self.menu_buttons = []
        self.create_menu_buttons()

    def create_menu_buttons(self):
        menu_dictionary = {
            'view all': self.view_all_riddles,
            'clear': self.clear,
        }

        for title, method in menu_dictionary.items():
            print(title)
            button = customtkinter.CTkButton(
                self.app, 
                text = title , 
                command = method,
                font = customtkinter.CTkFont(size=16))

            self.menu_buttons.append(button)

            button.grid(row=0, column=self.menu_buttons.index(button), padx=20, pady=20, sticky="ew")

 
    def view_all_riddles(self):
        print('view')
    
    def clear(self):
        print('clear')


    def run(self):
        self.app.mainloop()
   
gui = RiddleGUI()
gui.run()