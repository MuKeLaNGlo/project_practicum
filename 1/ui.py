import os

import customtkinter
from PIL import Image

from utils import (
    convert_to_ini, convert_to_json, convert_to_xml, convert_to_yaml,
    parse_ini_to_types, parse_json_to_types, parse_xml_to_types, parse_yaml,
    parse_yaml_to_types, save_content
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
explorer_image = customtkinter.CTkImage(light_image=Image.open(f"{BASE_DIR}/images/explorer.png"), size=(25, 25))


class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, title, values, main_frame):
        self.main_frame = main_frame
        super().__init__(master)
        self.values = ["YAML", "XML", "INI", "JSON"]
        self.variable = customtkinter.StringVar(value="")
        self.radiobuttons = []
        self.load_button = None
        self.save_button = None

        self.configure_layout()
        self.create_widgets()

    def configure_layout(self):
        self.grid_columnconfigure(1, weight=1)

    def create_widgets(self):
        self.label1 = customtkinter.CTkLabel(
            self,
            text="Расширение файла\n\n----",
            font=("Arial", 14),
            text_color="white",
            justify="center",
        )
        self.label1.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="w")

        self.load_button = self.create_button("Load", self.load_button_callback, 2, state="disabled")
        self.save_button = self.create_button("Save", self.save_button_callback, 3)
        self.create_button("Convert", self.convert_button_callback, 4)

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(
                self, text=value, value=value, variable=self.variable
            )
            radiobutton.grid(
                row=i + 5, column=0,
                padx=10, pady=(10, 0),
                sticky="w"
            )
            self.radiobuttons.append(radiobutton)

    def create_button(self, text, command, row, state='normal'):
        button = customtkinter.CTkButton(
            self,
            text=text,
            fg_color="gray40",
            command=command,
            state=state
        )
        button.grid(
            row=row, column=0,
            padx=5, pady=(10, 0),
            sticky="nsew"
        )
        return button

    def load_button_callback(self):
        file_path = self.main_frame.file_path_field.get("1.0", "end-1c")
        try:
            _, extension = os.path.splitext(file_path)
            extension = extension[1:].lower()
            self.label1.configure(text=f"Расширение файла\n\n{extension}")
            if extension == "yaml":
                data = parse_yaml(file_path)
                self.update_edit_box(data)
            elif extension in ["ini", "xml"]:
                with open(file_path, "r") as file:
                    content = file.read()
                self.update_edit_box(content)
            else:
                print(f"Unsupported file extension: {extension}")

        except FileNotFoundError:
            print("File not found.")

    def convert_button_callback(self):
        selected_option = self.variable.get().lower()
        file_path = self.main_frame.file_path_field.get("1.0", "end-1c")

        try:
            _, extension = os.path.splitext(file_path)
            extension = extension[1:].lower()
            data = None

            if extension == "yaml":
                data = parse_yaml_to_types(file_path)
            elif extension in ["ini", "xml", "json"]:
                data = globals()[f"parse_{extension}_to_types"](file_path)

            if data is not None:
                converted_content = globals()[f"convert_to_{selected_option.lower()}"](data)
                self.main_frame.edit_box.delete("1.0", "end-1c")
                self.main_frame.edit_box.insert("1.0", converted_content)

        except Exception as e:
            print(f"Error during conversion: {e}")

    def pick_path(self, file_path_field):
        file_path = customtkinter.filedialog.asksaveasfilename(
            filetypes=[
                ("YAML files", "*.yaml"),
                ("INI files", "*.ini"),
                ("XML files", "*.xml"),
                ("JSON files", "*.json")
            ]
        )

        if file_path:
            file_path_field.configure(state="normal")
            file_path_field.delete(0.0, "end")
            file_path_field.insert(index=0.0, text=file_path)
            file_path_field.configure(state="disabled")

    def save(self, file_path_field):
        file_path = file_path_field.get("1.0", "end-1c").strip()

        if not file_path:
            print("Please provide a valid file path.")
            return

        try:
            with open(file_path, "w") as file:
                content = self.main_frame.edit_box.get("1.0", "end-1c")
                file.write(content)
            print(f"Content saved to: {file_path}")
        except Exception as e:
            print(f"Error saving content: {e}")

    def save_button_callback(self):
        save_window = customtkinter.CTkToplevel()
        save_window.title("Save Window")
        save_window.geometry("700x250")
        save_window.transient(self)
        save_window.columnconfigure(0, weight=1)

        label = customtkinter.CTkLabel(save_window, text="Enter the save details:")
        label.grid(row=0, column=0, pady=10)

        file_path_field = customtkinter.CTkTextbox(
            save_window, width=600, height=28, corner_radius=6,
        )
        file_path_field.configure(state="disabled")
        file_path_field.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        pick_button = customtkinter.CTkButton(save_window, text="", width=28, command=lambda: self.pick_path(file_path_field), image=explorer_image)
        pick_button.grid(row=1, column=2, pady=10, padx=10, sticky="ew")
        save_button = customtkinter.CTkButton(
            save_window,
            text="Save file",
            width=100,
            height=50,
            font=("Arial", 20),
            command=lambda: self.save(file_path_field)
        )
        save_button.grid(row=2, column=0, pady=(30, 0), padx=10, columnspan=3)

    def update_edit_box(self, data):
        self.main_frame.edit_box.delete("1.0", "end-1c")
        self.main_frame.edit_box.insert("1.0", data)
        self.check_save_button_state()


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



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Конвертер")
        self.geometry("900x500")
        self.grid_columnconfigure((1, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = MainFrame(
            self, "Options", values=["option 1", "option 2"]
        )
        self.main_frame.grid(
            row=0, column=1,
            padx=(0, 10), pady=(10, 10),
            sticky="nsew", columnspan=1
        )
        self.sidebar_frame = SideBar(
            self,
            title="Values",
            values=["value 1", "value 2", "value 3"],
            main_frame=self.main_frame,
        )
        self.sidebar_frame.grid(
            row=0, column=0,
            padx=10, pady=(10, 10),
            sticky="nsew", rowspan=1
        )

    def button_callback(self):
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())


app = App()
app.mainloop()
