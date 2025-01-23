import Generate  # /Generate.py
import customtkinter  # https://github.com/TomSchimansky/CustomTkinter
import pyperclip  # https://pypi.org/project/pyperclip/

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class BianryUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        '''
        Window functionality
        '''
        # Configure window
        self.title("Bianry - Blueberry Technologies")
        self.geometry(f"{1100}x{580}")

        # State for toggling visibility of text frame
        self.text_frame_visible = True

        # Configure grid layout (4x4)
        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=0)

        '''
        Sidebar functionality
        '''
        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=0)

        # The label on the sidebar "Bianry"
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bianry", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # The label on the sidebar "Blueberry Technologies"
        self.logo_label_company = customtkinter.CTkLabel(self.sidebar_frame, text=" Blueberry Technologies", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label_company.grid(row=1, column=0, padx=20, pady=(20, 10))

        # Set Button Functionality in the sidebar
        self.sidebar_button_txt = customtkinter.CTkButton(self.sidebar_frame, text="Text Format", command=self.debug_widget_hierarchy)
        self.sidebar_button_txt.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_json = customtkinter.CTkButton(self.sidebar_frame, text="Json Format", command=self.hideTextUI)
        self.sidebar_button_json.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_img = customtkinter.CTkButton(self.sidebar_frame, text="Img Format")
        self.sidebar_button_img.grid(row=4, column=0, padx=20, pady=10)

        '''
        Main content for text file functionality
        '''
        self.text_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.text_frame.grid(row=0, column=1, columnspan=4, sticky="nsew")
        self.text_frame.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.text_frame.grid_rowconfigure(0, weight=1)
        self.text_frame.grid_rowconfigure(4, weight=0)

        # Create main entry and button
        self.userEntry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Enter length of password 8-32")
        self.userEntry.grid(row=2, column=1, columnspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")

        self.warning_label_top = customtkinter.CTkLabel(self.text_frame, text="")
        self.warning_label_top.grid(row=5, column=0, padx=(20, 20), pady=(30, 0), sticky="nsew")

        self.warning_label_bottom = customtkinter.CTkLabel(self.text_frame, text="")
        self.warning_label_bottom.grid(row=6, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        self.exclusions = customtkinter.CTkEntry(self.text_frame, placeholder_text="Enter excluded characters")
        self.exclusions.grid(row=2, column=2, columnspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")

        self.passwordEntry = customtkinter.CTkEntry(self.text_frame, placeholder_text="")
        self.passwordEntry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_generate_button = customtkinter.CTkButton(master=self.text_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Generate", command=self.generatePassword)
        self.main_generate_button.grid(row=2, column=3, padx=(20, 0), pady=(10, 10), sticky="nsew")

        self.main_copy_button = customtkinter.CTkButton(master=self.text_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Copy to Clipboard", command=self.copyToClipboard)
        self.main_copy_button.grid(row=3, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

    '''
    Functions
    '''
    # Debugging Widget Hierarchy
    def debug_widget_hierarchy(self):
        print("All widgets in the main window:")
        for widget in self.winfo_children():
            print(widget, "->", widget.winfo_children())

    # Hide Text UI
    def hideTextUI(self):
        print(f"Before toggling: text_frame_visible = {self.text_frame_visible}")

        if self.text_frame_visible:
            # Hide all child widgets of text_frame
            for child in self.text_frame.winfo_children():
                child.grid_forget()

            # Hide the frame itself
            self.text_frame.grid_forget()
            print("Text frame and its children hidden.")
        else:
            # Show the frame and its child widgets
            self.text_frame.grid(row=0, column=1, columnspan=4, sticky="nsew")
            self.text_frame.grid_columnconfigure((1, 2, 3, 4), weight=1)
            self.text_frame.grid_rowconfigure(0, weight=1)
            self.text_frame.grid_rowconfigure(4, weight=0)
            for child in self.text_frame.winfo_children():
                child.grid()

            print("Text frame and its children shown.")

        self.text_frame_visible = not self.text_frame_visible
        print(f"After toggling: text_frame_visible = {self.text_frame_visible}")

    # Password Generation Functions
    def generatePassword(self):
        self.passwordEntry.delete(0, 32)
        try:
            userDefinedLength = int(self.userEntry.get())
            userDefinedExclusion = self.exclusions.get()
            userGeneratedPassword = Generate.getGeneratedPassword(userDefinedLength, userDefinedExclusion)
            if userGeneratedPassword == -1:
                self.warning_label_top.configure(text="Please enter a number")
                self.warning_label_bottom.configure(text="between 8 and 32.")
            else:
                self.warning_label_top.configure(text="")
                self.warning_label_bottom.configure(text="")
                self.passwordEntry.insert(0, userGeneratedPassword)
        except ValueError:
            self.warning_label_top.configure(text="Please enter a number")
            self.warning_label_bottom.configure(text="between 8 and 32.")

    def copyToClipboard(self):
        current_password = self.passwordEntry.get()
        if current_password:
            print("The password is: " + current_password)
            pyperclip.copy(current_password)
        else:
            print("There is nothing to copy")


if __name__ == "__main__":
    app = BianryUI()
    app.mainloop()
