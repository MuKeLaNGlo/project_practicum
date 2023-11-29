import customtkinter
from tkhtmlview import HTMLLabel

from settings import explorer_image


class MainFrame(customtkinter.CTkFrame):
    """Класс главного фрейма приложения.

    Args:
        master: Родительский виджет.
        title: Заголовок фрейма.
        values: Список значений.

    Attributes:
        file_path_field (customtkinter.CTkTextbox): Поле для отображения пути к файлу.
        explorer_button (customtkinter.CTkButton): Кнопка для вызова диалога выбора файла.
        edit_box (customtkinter.CTkTextbox): Поле редактирования для отображения содержимого файла.

    """

    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.file_path_field: customtkinter.CTkTextbox = customtkinter.CTkTextbox(
            master=self, height=28, corner_radius=6
        )
        self.file_path_field.grid(
            row=0, column=0,
            padx=(10, 10), pady=(10, 10),
            columnspan=3,
            sticky="ew"
        )
        self.file_path_field.configure(state="disabled")

        self.explorer_button: customtkinter.CTkButton = customtkinter.CTkButton(
            self,
            text="",
            height=28,
            width=25,
            image=explorer_image,
            fg_color="gray40",
            command=self.explorer_button_callback,
        )
        self.explorer_button.grid(
            row=0, column=3,
            padx=(0, 10), pady=(10, 10),
            sticky="ew"
        )

        self.edit_box: customtkinter.CTkTextbox = customtkinter.CTkTextbox(
            master=self, height=700, corner_radius=6, font=("Consolas", 12)
        )
        self.edit_box.grid(
            row=1, column=0,
            padx=(10, 10), pady=(10, 10),
            columnspan=2, sticky="nsew"
        )


        # Добавляем поле для SVG
        self.svg_canvas = customtkinter.CTkCanvas(self, bg="white", width=300, height=300)
        self.svg_canvas.grid(
            row=1, column=2,
            padx=(10, 10), pady=(10, 10),
            rowspan=2, sticky="nsew"
        )

        # Добавляем поле для HTML
        self.html_text = HTMLLabel(self, wrap=customtkinter.WORD, height=10, width=40)
        self.html_text.grid(
            row=1, column=3,
            padx=(10, 10), pady=(10, 10),
            columnspan=2, sticky="nsew"
        )
        self.svg_canvas.grid_remove()
        self.html_text.grid_remove()

    def explorer_button_callback(self):
        """Обработчик нажатия кнопки Explorer."""
        file_path = customtkinter.filedialog.askopenfilename(
            filetypes=[
                ("All files", ("*.svg", "*.html")),
                ("SVG files", "*.svg"),
                ("HTML files", "*.html"),
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
