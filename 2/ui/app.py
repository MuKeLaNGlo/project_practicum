import customtkinter

from ui.main_frame import MainFrame
from ui.sidebar import SideBar


class App(customtkinter.CTk):
    """Класс приложения конвертера файлов.

    Attributes:
        main_frame (MainFrame): Главный фрейм приложения.
        sidebar_frame (SideBar): Боковая панель приложения.

    """

    def __init__(self):
        super().__init__()

        self.title("Конвертер")
        self.geometry("900x500")
        self.grid_columnconfigure((1, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame: MainFrame = MainFrame(
            self, "Options", values=["option 1", "option 2"]
        )
        self.main_frame.grid(
            row=0, column=1,
            padx=(0, 10), pady=(10, 10),
            sticky="nsew", columnspan=1
        )
        self.sidebar_frame: SideBar = SideBar(
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
        """Обработчик нажатия кнопки."""
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())
