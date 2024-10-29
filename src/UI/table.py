import customtkinter
from src.model.product import Product
from typing import List

class Table(customtkinter.CTkScrollableFrame):
    def __init__(self, master, products: List[Product], **kwargs):
        super().__init__(master, **kwargs)

        # Cabeçalho da tabela (COD, Desc, Emb, Preço, Local, Status)
        self.table_header = TableHead(master=self, width=650, height=30, corner_radius=0, fg_color="#000")
        self.table_header.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        if len(products) > 0:
            for i, product in enumerate(products):
                # Linhas da tabela
                self.table_row = TableRow(
                        master=self,
                        width=650,
                        height=30,
                        corner_radius=0,
                        fg_color="#FFF",
                        code=product.get_code(),
                        desc=product.get_descritpion(),
                        emb=product.get_emb(),
                        price=product.get_price(),
                        status=product.get_status(),
                        local=product.get_local(),
                        row=i,
                        checked=True
                    )
                self.table_row.grid(row=i+1, column=0, padx=0, pady=0, sticky="nsew")

        
class TableHead(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.checkbox = customtkinter.CTkCheckBox(
            self,
            border_color="#FFF",
            border_width=1,
            text=None,
            width=20,
            height=20
        )
        self.checkbox.grid(row=3, column=0, padx=(2, 2), pady=(2, 2), sticky="nsew",)

        self.tr_2 = customtkinter.CTkLabel(
            self,
            text="COD",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_2.grid(row=3, column=1, padx=(2, 40), pady=(2, 2), sticky="nsew")

        self.tr_3 = customtkinter.CTkLabel(
            self,
            text="Desc",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_3.grid(row=3, column=2, padx=(2, 180), pady=(2, 2), sticky="nsew")

        self.tr_4 = customtkinter.CTkLabel(
            self,
            text="Emb",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_4.grid(row=3, column=3, padx=(2, 80), pady=(2, 2), sticky="nsew")

        self.tr_5 = customtkinter.CTkLabel(
            self,
            text="Preço",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_5.grid(row=3, column=4, padx=(2, 50), pady=(2, 2), sticky="nsew")

        self.tr_6 = customtkinter.CTkLabel(
            self,
            text="Local",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_6.grid(row=3, column=5, padx=(2, 50), pady=(2, 2), sticky="nsew")

        self.tr_7 = customtkinter.CTkLabel(
            self,
            text="Status",
            font=("Inter", 12, "bold"),
            text_color="#FFF"
        )
        self.tr_7.grid(row=3, column=6, padx=(2, 50), pady=(2, 2), sticky="nsew")

class TableRow(customtkinter.CTkFrame):
    def __init__(self, master, checked: bool, code: str, desc: str, emb: str, price: str, local: str, status: str, row: int, **kwargs):
        super().__init__(master, **kwargs)

        self.checkbox = customtkinter.CTkCheckBox(
            self,
            border_color="#000",
            border_width=1,
            text=None,
            width=20,
            height=20
        )
        self.checkbox.grid(row=row+4, column=0, padx=(2, 2), pady=(2, 2), sticky="nsew",)

        self.td_2 = customtkinter.CTkLabel(
            self,
            text=f"{code}",
            width=30,
            font=("Inter", 10, "bold"),
            text_color="#000"
        )
        self.td_2.grid(row=row+4, column=1, padx=(2, 10), pady=(2, 2), sticky="nsew")

        self.td_3 = customtkinter.CTkLabel(
            self,
            text=f"{desc[:25]}",
            width=200,
            font=("Inter", 10, "bold"),
            text_color="#000"
        )
        self.td_3.grid(row=row+4, column=2, padx=(2, 10), pady=(2, 2), sticky="nsew")

        self.td_4 = customtkinter.CTkLabel(
            self,
            text=f"{emb}",
            font=("Inter", 10, "bold"),
            width=100,
            text_color="#000"
        )
        self.td_4.grid(row=row+4, column=3, padx=(2, 10), pady=(2, 2), sticky="nsew")

        self.td_5 = customtkinter.CTkLabel(
            self,
            text=f"R$ {price}".replace('.', ','),
            width=80,
            font=("Inter", 10, "bold"),
            text_color="#000"
        )
        self.td_5.grid(row=row+4, column=4, padx=(2, 0), pady=(2, 2), sticky="nsew")

        self.td_6 = customtkinter.CTkLabel(
            self,
            text=f"{local}",
            width=80,
            font=("Inter", 10, "bold"),
            text_color="#000"
        )
        self.td_6.grid(row=row+4, column=5, padx=(2, 2), pady=(2, 2), sticky="nsew")

        self.td_7 = customtkinter.CTkLabel(
            self,
            text=f"{status}",
            width=80,
            font=("Inter", 10, "bold"),
            text_color="#000"
        )
        self.td_7.grid(row=row+4, column=6, padx=(2, 2), pady=(2, 2), sticky="nsew")

