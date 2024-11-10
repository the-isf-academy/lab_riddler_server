import customtkinter

class GUI:
    def __init__(self, app_title, width, height):

        self.app = customtkinter.CTk()
        self.app.geometry(f"{width}x{height}")
        self.app.title(app_title)
        self.app.grid_columnconfigure((0,1,2,3), weight=1)
        
    def widget_setup(self):
        '''Sets up all widgets'''
        
        # setup menu  buttons
        self.menu_buttons = []
        self.setup_menu_buttons()

        # setup entry widgets
        self.entry_widgets = {}
        self.setup_entry_widgets()

        # setup entry widget labels
        self.labels = {}
        self.setup_labels()

        # setup submit buttons
        self.submit_buttons = {}
        self.setup_submit_buttons()

    def setup_menu_buttons(self):
        '''Creates menu buttons'''

        for title, method in self.menu_dictionary.items():
            button = customtkinter.CTkButton(
                self.app, 
                text = title , 
                command = method,
                font = customtkinter.CTkFont(size=16, family="Georgia"),
                text_color="#363e4f",
                fg_color="#edf3ff",
                hover_color="#c8cedb",
                border_spacing=10)

            self.menu_buttons.append(button)

            button.grid(row=0, column=self.menu_buttons.index(button), padx=20, pady=20, sticky="ew")

    def setup_submit_buttons(self):
        '''Create submit buttons for entry widgets'''

        for title, method in self.submit_button_dictionary.items():
            button = customtkinter.CTkButton(
                self.app, 
                text = 'Submit', 
                command = method,
                font = customtkinter.CTkFont(size=16),
                state='disabled')

            self.submit_buttons[title] = (button)         

    def setup_entry_widgets(self):
        '''Creates entry widgets'''
        
        for label, text in self.entry_dictionary.items():
            self.entry_widgets[label] = customtkinter.CTkEntry(
                self.app,
                placeholder_text = text)

    def setup_labels(self):
        '''Creates labels for entry widgets'''

        for label, text in self.label_dictionary.items():
            self.labels[label] = customtkinter.CTkLabel(
                self.app, 
                text = text, 
                fg_color="transparent")

    
    def display_text_box(self, row_num, height):
        '''Displays text box on the grid'''

        self.text_box.grid(row=row_num, column=0, padx=20, pady=20, sticky="ew", columnspan=5)
        self.text_box.configure(height = height) 
        self.text_box.configure(state='disabled') # sets to read-only

    def reset_textbox(self):
        '''Remove all text from textbox'''
        
        self.text_box.configure(state='normal') # sets to read
        self.text_box.delete('1.0', 'end')      # deletes all text 
        
    def clear(self):
        '''Clear all widgets that are 
        NOT the menu from the grid'''

        self.reset_textbox()
        self.text_box.grid_forget()

        for entry_widget_title, entry_widget in self.entry_widgets.items():
            entry_widget.delete(0,'end')
            entry_widget.grid_forget()

        for label_title, label in self.labels.items():
            label.grid_forget()
        
        for button_title ,button in self.submit_buttons.items():
            button.grid_forget()

    def config_entry_widget(self,widget_list, submit_button):
        '''Sets up entry widgets with appropriate labels 
        and places them on the screen'''

        self.clear()

        # Bind the entry boxes to key entry
        self.setup_entry_bind(widget_list, submit_button)

        row_num = 1
        for widget in widget_list:
            self.labels[widget].grid(row=row_num, column=0, padx=0, pady=0)
            self.entry_widgets[widget].grid(row=row_num, column=1, pady=0, padx=20,sticky="ew", columnspan=2)
            row_num += 1
      
        # Place submit button on grid
        self.submit_buttons[submit_button].grid(row=3, column=1, padx=20, pady=10,sticky="ew")

    def setup_entry_bind(self, widget_list, submit_button):
        '''Binds widgets to typing in the entry box'''

        for widget in widget_list:
            self.entry_widgets[widget].bind(
                '<KeyRelease>', 
                lambda entry: self.enable_submit_guess_button(widget_list, submit_button))

    def enable_submit_guess_button(self, entry_widgets, submit_button):
        '''Only activate submit button if user 
        has entered information into the entry box'''

        num_filled = 0
        
        for widget in entry_widgets:
            if self.entry_widgets[widget].get():
                num_filled += 1
        
        if num_filled == len(entry_widgets):
            self.submit_buttons[submit_button].configure(state="normal")

    def run(self):
        '''Launches the app with the widgets setup'''

        self.widget_setup()
        self.app.mainloop()