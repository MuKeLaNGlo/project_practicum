import customtkinter
from ui.sidebar import SideBar
from ui.main_frame import MainFrame


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
