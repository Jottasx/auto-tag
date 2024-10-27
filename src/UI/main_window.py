import customtkinter
from PIL import Image
from src.UI.table import Table

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")

        # Configurações da janela
        self.geometry("1000x811")
        self.title("Auto Tag")
        self.resizable(False, False)

        # Widgets -----------------------------------------------------------
        # "Logo"
        self.h1_title = customtkinter.CTkLabel(
                self,
                text="AUTO TAG",
                font=("Inter", 26, "bold"),
                fg_color="transparent",
                text_color="#000",
                width=36,
            )
        self.h1_title.grid(row=0, column=0, padx=(50, 0), pady=(30, 0), sticky="nw")

        # Tabela de produtos

        # Título da tabela
        self.table_title = customtkinter.CTkLabel(
            self,
            text="Lista de produtos:",
            font=("Inter", 14, "bold"),
            fg_color="transparent",
            text_color="#000"
        )
        self.table_title.grid(row=1, column=0, padx=(50, 0), pady=(50, 0), sticky="w")

        # Tabela
        self.table = Table(master=self, width=650, height=450, corner_radius=0, fg_color="#DDD")
        self.table.grid(row=3, column=0, padx=(50, 0), pady=(1, 1), sticky="nsew")


        # Botões lado direito -----------------------------------------------------------
        
        # SMGOI13
        self.btn_smgoi13_upper_text = customtkinter.CTkLabel(
            self,
            text="Data SMG13 [27/10]",
            text_color="#000",
            font=("Inter", 12, "bold"),
        )
        self.btn_smgoi13_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(1, 1), sticky="ne")

        img_excel = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/excel_icon.png"),
            size=(29, 29)
        )

        self.btn_smgoi13 = customtkinter.CTkButton(
            self,
            text="SMGOI13",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_excel,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_smgoi13.grid(row=3, column=2, padx=(80, 0), pady=(25, 1), sticky="ne")

        # Produtos
        self.btn_products_upper_text = customtkinter.CTkLabel(
            self,
            text="Carregar produtos",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_products_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(75, 1), sticky="ne")

        self.btn_products = customtkinter.CTkButton(
            self,
            text="Produtos",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_excel,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_products.grid(row=3, column=2, padx=(80, 0), pady=(100, 1), sticky="ne")


        # SASOI006
        img_sasoi006 = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/sasoi006_icon.png"),
            size=(26, 26)
        )

        self.btn_sasoi006_upper_text = customtkinter.CTkLabel(
            self,
            text="Enviar para SASOI006",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_sasoi006_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(150, 1), sticky="ne")

        self.btn_sasoi006 = customtkinter.CTkButton(
            self,
            text="SASOI006",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_sasoi006,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_sasoi006.grid(row=3, column=2, padx=(80, 0), pady=(175, 1), sticky="ne")



        # TAGSELL
        img_tagsell = customtkinter.CTkImage(
            light_image=Image.open("./src/assets/img/tagsell_icon.png"),
            size=(27, 27)
        )

        self.btn_tagsell_upper_text = customtkinter.CTkLabel(
            self,
            text="Enviar para o TagSell",
            text_color="#000",
            fg_color="transparent",
            font=("Inter", 10, "bold"),
        )
        self.btn_tagsell_upper_text.grid(row=3, column=2, padx=(80, 0), pady=(225, 1), sticky="ne")

        self.btn_tagsell = customtkinter.CTkButton(
            self,
            text="TAGSELL",
            text_color="#000",
            font=("Inter", 12, "bold"),
            fg_color="#B2B2B2",
            image=img_tagsell,
            width=140,
            height=45,
            corner_radius=0
        )
        self.btn_tagsell.grid(row=3, column=2, padx=(80, 0), pady=(250, 1), sticky="ne")