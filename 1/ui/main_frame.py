import customtkinter

from settings import explorer_image


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.file_path_field = customtkinter.CTkTextbox(
            master=self, height=28, corner_radius=6
        )
        self.file_path_field.grid(
            row=0, column=0,
            padx=(10, 10), pady=(10, 10),
            columnspan=1,
            sticky="ew"
        )
        self.file_path_field.configure(state="disabled")

        self.explorer_button = customtkinter.CTkButton(
            self,
            text="",
            height=28,
            width=25,
            image=explorer_image,
            fg_color="gray40",
            command=self.explorer_button_callback,
        )
        self.explorer_button.grid(
            row=0, column=1,
            padx=(0, 10), pady=(10, 10),
            sticky="ew"
        )

        self.edit_box = customtkinter.CTkTextbox(
            master=self, height=700, corner_radius=6
        )
        self.edit_box.grid(
            row=1, column=0,
            padx=(10, 10), pady=(10, 10),
            columnspan=2, sticky="nsew"
        )

    def explorer_button_callback(self):
        file_path = customtkinter.filedialog.askopenfilename(
            filetypes=[
                ("All files", ("*.yaml", "*.ini", "*.xml", "*.json")),
                ("YAML files", "*.yaml"),
                ("INI files", "*.ini"),
                ("XML files", "*.xml"),
                ("JSON files", "*.json"),
            ]
        )

        if file_path:
            self.file_path_field.configure(state="normal")
            self.file_path_field.delete(0.0, "end")
            self.file_path_field.insert(index=0.0, text=file_path)
            self.file_path_field.configure(state="disabled")
            self.master.sidebar_frame.load_button.configure(state="normal")
        else:
            self.master.sidebar_frame.load_button.configure(state="disabled")
