import customtkinter
from src.model.product import Product
from typing import List

class Console(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.console_row = ConsoleRow(
            master=self,
            text="[OK] log salvo com sucesso",
            width=400,
            height=20,
            corner_radius=0,
            fg_color="transparent")
        self.console_row.grid(row=0, column=0, padx=15, pady=0, sticky="ne")



class ConsoleRow(customtkinter.CTkFrame):
    def __init__(self, master, text :str|None, **kwargs):
        super().__init__(master, **kwargs)

        self.td_1 = customtkinter.CTkLabel(
            self,
            text=f"{text}",
            font=("Inter", 14, "bold"),
            height=10,
            text_color="#000"
        )
        self.td_1.grid(row=0, column=0, padx=(2, 40), pady=(0, 0), sticky="n")
